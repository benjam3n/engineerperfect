"""Construct and execute inquiry plans and their actual toy repair operations.

Costs are stipulated work units. No human state, reading time, or field effect
is inferred from the computations. Layout has no operational role in this case.
"""

import json
from dataclasses import asdict
from fractions import Fraction
from itertools import product
from pathlib import Path

from choose_contribution import Inquiry, Intervention, choose_contribution


def calculation_problem(rebuild_cost=4):
    fixtures = {}
    for missing, layout in product(["rule", "input"], ["a", "b", "c", "d"]):
        fixtures[f"{missing}-{layout}"] = {
            "layout": layout,
            "rule": None if missing == "rule" else "hole-minus-shaft",
            "measurements": None if missing == "input" else {"hole": "10.06", "shaft": "10.00"},
        }
    actions = {
        "install_rule": Intervention(1, frozenset(s for s in fixtures if s.startswith("rule-"))),
        "load_input": Intervention(1, frozenset(s for s in fixtures if s.startswith("input-"))),
        "rebuild": Intervention(rebuild_cost, frozenset(fixtures)),
    }
    inquiries = {
        "inspect_missing_part": Inquiry(1, {s: s.split("-")[0] for s in fixtures}),
        "inspect_layout": Inquiry(1, {s: f["layout"] for s, f in fixtures.items()}),
        "identify_everything": Inquiry(3, {s: s for s in fixtures}),
    }
    return fixtures, actions, inquiries


def repair_calculation(document, operation):
    """Supply the named contribution; measurements come from a stipulated fixture."""
    repaired = dict(document)
    if operation in {"install_rule", "supply_both", "rebuild"}:
        repaired["rule"] = "hole-minus-shaft"
    if operation in {"load_input", "supply_both", "rebuild"}:
        repaired["measurements"] = {"hole": "10.06", "shaft": "10.00"}
    if operation not in {"install_rule", "load_input", "supply_both", "rebuild"}:
        raise ValueError("Unknown repair operation")
    return repaired


def calculate(document):
    if document["rule"] != "hole-minus-shaft" or document["measurements"] is None:
        raise ValueError("The calculation still lacks its rule or input")
    data = document["measurements"]
    return Fraction(data["hole"]) - Fraction(data["shaft"])


def inspect_calculation(document, inquiry):
    if inquiry == "inspect_layout":
        return document["layout"]
    if document["rule"] is None and document["measurements"] is not None:
        missing = "rule"
    elif document["rule"] is not None and document["measurements"] is None:
        missing = "input"
    elif document["rule"] is None and document["measurements"] is None:
        missing = "both"
    else:
        raise ValueError("The document has neither modeled omission")
    if inquiry == "inspect_missing_part":
        return missing
    if inquiry == "identify_everything":
        return missing + "-" + document["layout"]
    raise ValueError("Unknown inquiry")


def execute_plan(plan, case, inquiries, actions, observe, apply):
    events, spent = [], 0
    while plan.kind == "inquire":
        inquiry = inquiries[plan.name]
        answer = observe(plan.name)
        assert answer == inquiry.outcomes[case]
        events.append({"inquiry": plan.name, "answer": answer})
        spent += inquiry.cost
        plan = plan.after(answer)
    assert case in actions[plan.name].works_in
    spent += actions[plan.name].cost
    result = apply(plan.name)
    return {"events": events, "intervention": plan.name, "cost": spent, "result": str(result)}


def forced_inquiry_cost(name, cases, actions, inquiries):
    question = inquiries[name]
    branches = []
    for answer in sorted(set(question.outcomes[s] for s in cases)):
        remaining = {s for s in cases if question.outcomes[s] == answer}
        plan, _ = choose_contribution(cases, actions, inquiries, remaining)
        if plan is None:
            return None
        branches.append(plan.cost)
    return question.cost + max(branches)


def sign_problem():
    cases = {f"{producer}{consumer}": (producer, consumer) for producer, consumer in product(range(2), repeat=2)}
    actions = {
        "keep_sign": Intervention(1, frozenset(s for s, (p, c) in cases.items() if p == c)),
        "reverse_sign": Intervention(1, frozenset(s for s, (p, c) in cases.items() if p != c)),
        "reset_both": Intervention(4, frozenset(cases)),
    }
    inquiries = {
        "inspect_producer": Inquiry(1, {s: str(v[0]) for s, v in cases.items()}),
        "inspect_consumer": Inquiry(1, {s: str(v[1]) for s, v in cases.items()}),
    }
    return cases, actions, inquiries


def results():
    fixtures, actions, inquiries = calculation_problem()
    plan, blockers = choose_contribution(fixtures, actions, inquiries)
    assert not blockers and plan.cost == 2 and plan.name == "inspect_missing_part"
    executions = {}
    for case, fixture in fixtures.items():
        try:
            calculate(fixture)
        except ValueError:
            pass
        else:
            raise AssertionError("Fixture must begin with an unusable calculation")
        run = execute_plan(plan, case, inquiries, actions,
                           lambda name: inspect_calculation(fixture, name),
                           lambda name: calculate(repair_calculation(fixture, name)))
        assert run["result"] == "3/50" and run["cost"] == 2
        executions[case] = run

    identified_actions = {s: Intervention(1, frozenset({s})) for s in fixtures}
    identify_plan, _ = choose_contribution(fixtures, identified_actions, inquiries)
    assert identify_plan.cost == 3
    known, _ = choose_contribution(fixtures, actions, inquiries, {s for s in fixtures if s.startswith("rule-")})
    assert known.kind == "intervene" and known.name == "install_rule" and known.cost == 1
    _, cheaper_actions, _ = calculation_problem(rebuild_cost=1)
    common, _ = choose_contribution(fixtures, cheaper_actions, inquiries)
    assert common.kind == "intervene" and common.name == "rebuild" and common.cost == 1

    outside = {"layout": "a", "rule": None, "measurements": None}
    outside_answer = inspect_calculation(outside, plan.name)
    try:
        plan.after(outside_answer)
    except ValueError:
        rejected_unmodeled_answer = True
    else:
        raise AssertionError("The eight-case plan must not guess a repair for an unmodeled answer")
    expanded = {**fixtures, "both-a": outside}
    expanded_actions = {**actions, "rebuild": Intervention(4, frozenset(expanded)),
                        "supply_both": Intervention(2, frozenset({"both-a"}))}
    expanded_inquiries = {q: Inquiry(old.cost, {s: inspect_calculation(f, q) for s, f in expanded.items()})
                          for q, old in inquiries.items()}
    expanded_plan, _ = choose_contribution(expanded, expanded_actions, expanded_inquiries)
    assert expanded_plan.cost == 3
    expanded_runs = {}
    for case, fixture in expanded.items():
        run = execute_plan(expanded_plan, case, expanded_inquiries, expanded_actions,
                           lambda name: inspect_calculation(fixture, name),
                           lambda name: calculate(repair_calculation(fixture, name)))
        assert run["result"] == "3/50" and run["cost"] <= 3
        expanded_runs[case] = run
    assert expanded_runs["both-a"]["intervention"] == "supply_both"

    signs, sign_actions, sign_inquiries = sign_problem()
    sign_plan, _ = choose_contribution(signs, sign_actions, sign_inquiries)
    assert sign_plan.cost == 3
    sign_runs = {}
    for case, (producer, consumer) in signs.items():
        delivered = 7 * (-1) ** (producer + consumer)
        run = execute_plan(sign_plan, case, sign_inquiries, sign_actions,
                           lambda name: str(producer if name == "inspect_producer" else consumer),
                           lambda name: 7 if name == "reset_both" else -delivered if name == "reverse_sign" else delivered)
        assert run["result"] == "7" and run["cost"] == 3
        sign_runs[case] = run
    # Either observation alone still leaves only the cost-4 reset common.
    for inquiry in sign_inquiries.values():
        for answer in {"0", "1"}:
            cell = {s for s in signs if inquiry.outcomes[s] == answer}
            one_step = min(a.cost for a in sign_actions.values() if cell <= a.works_in)
            assert inquiry.cost + one_step == 5

    # Construct a missing operation: rectify the delivered value when the
    # original signal is positive. The original optimum cannot invent it.
    rectified_actions = {**sign_actions, "positive_magnitude": Intervention(1, frozenset(signs))}
    rectified_plan, _ = choose_contribution(signs, rectified_actions, sign_inquiries)
    assert rectified_plan.kind == "intervene" and rectified_plan.name == "positive_magnitude"
    rectified_runs = {}
    for case, (producer, consumer) in signs.items():
        delivered = 7 * (-1) ** (producer + consumer)
        run = execute_plan(rectified_plan, case, sign_inquiries, rectified_actions,
                           lambda name: str(producer if name == "inspect_producer" else consumer),
                           lambda name: abs(delivered))
        assert run["result"] == "7" and run["cost"] == 1
        rectified_runs[case] = run
    negative_source, unchanged_delivery = -7, -7
    assert abs(unchanged_delivery) != negative_source
    before_component_repair = 7 * (-1) ** (1 + 1)
    after_component_repair = 7 * (-1) ** (0 + 1)
    assert before_component_repair == 7 and after_component_repair == -7

    unresolved_cases = ["needs_rule", "needs_input"]
    incompatible = {"rule": Intervention(1, frozenset({"needs_rule"})),
                    "input": Intervention(1, frozenset({"needs_input"}))}
    blind = {"read_status": Inquiry(1, {s: "unusable" for s in unresolved_cases})}
    impossible, obstruction = choose_contribution(unresolved_cases, incompatible, blind)
    assert impossible is None and len(obstruction) == 1 and len(obstruction[0]) == 2

    return {
        "standing": "Exact finite constructions and executed toy repairs. Costs are stipulated work units, not measured human effort or time.",
        "calculation": {
            "plan": asdict(plan), "executed_repairs": executions,
            "cost_after_forcing_first_inquiry": {q: forced_inquiry_cost(q, fixtures, actions, inquiries) for q in inquiries},
            "complete_case_identification_and_repair_cost": identify_plan.cost,
            "already_known_missing_rule": asdict(known), "cheap_common_rebuild": asdict(common),
            "expanded_case_model": {"original_plan_rejected_answer": rejected_unmodeled_answer,
                                    "new_answer": outside_answer, "plan": asdict(expanded_plan),
                                    "executed_repairs": expanded_runs},
        },
        "sign_composition": {"plan": asdict(sign_plan), "executed_repairs": sign_runs,
                             "direct_common_intervention_cost": 4, "one_inquiry_then_common_intervention_cost": 5,
                             "constructed_operation": {"plan": asdict(rectified_plan), "executed_repairs": rectified_runs,
                                                       "scope_failure": {"required": negative_source, "produced": abs(unchanged_delivery)}},
                             "repairing_only_producer": {"before": before_component_repair, "after": after_component_repair}},
        "indistinguishable_incompatible_cases": {"plan": None, "obstruction": obstruction},
    }


if __name__ == "__main__":
    output = Path(__file__).resolve().parents[1] / "evidence" / "contribution-results.json"
    output.write_text(json.dumps(results(), indent=2, sort_keys=True) + "\n")
    print("Wrote contribution-results.json; executed 17 calculation repairs and 8 sign repairs; checked a rectification scope failure.")
