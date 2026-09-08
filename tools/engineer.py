"""Execute the supplied constructions; no unnamed selection operation remains.

The domains and costs are the explicit models in the accompanying derivations.
Signed magnitude consumes the known original sign, never the original magnitude.
"""

from fractions import Fraction
import json

from choose_contribution import Intervention, choose_contribution
from run_contribution_examples import (
    calculation_problem, calculate, execute_plan, inspect_calculation,
    repair_calculation, sign_problem,
)


def signed_magnitude(received, original_sign):
    if original_sign not in (-1, 1):
        raise ValueError("The original sign must be known as -1 or 1")
    return original_sign * abs(received)


def completed_signs():
    cases, original_actions, inquiries = sign_problem()
    actions = dict(original_actions)
    executions = []
    for original in (Fraction(7), Fraction(-7)):
        sign = 1 if original > 0 else -1
        actions["signed_magnitude"] = Intervention(1 if sign > 0 else 2, frozenset(cases))
        plan, blockers = choose_contribution(cases, actions, inquiries)
        if blockers:
            raise AssertionError(blockers)
        for case, (producer, consumer) in cases.items():
            delivered = original * (-1) ** (producer + consumer)
            result = signed_magnitude(delivered, sign)
            executions.append({"original": str(original), "case": case,
                               "received": str(delivered), "restored": str(result),
                               "cost": plan.cost})
    return {"operation": "signed_magnitude", "cost": {"positive": 1, "negative": 2}, "executions": executions}


def completed_calculations():
    fixtures, actions, inquiries = calculation_problem()
    plan, blockers = choose_contribution(fixtures, actions, inquiries)
    if blockers:
        raise AssertionError(blockers)
    runs = {}
    for case, document in fixtures.items():
        runs[case] = execute_plan(
            plan, case, inquiries, actions,
            lambda q, doc=document: inspect_calculation(doc, q),
            lambda a, doc=document: calculate(repair_calculation(doc, a)),
        )
    return {"cost": plan.cost, "executions": runs}


def results():
    return {"signed_magnitude": completed_signs(),
            "calculation_repair": completed_calculations()}


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
