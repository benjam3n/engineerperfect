"""Recompute the constructed engineering cases; no field data are implied."""

import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

from finite_control import invariant, observation_actions, policy_violations, reach_and_stay


def water_model():
    safe = set(range(1, 10))
    transitions = {
        x: {u: frozenset(x + u - d for d in range(3)) for u in range(-3, 4)}
        for x in safe
    }
    return transitions, safe


def service_model(workers):
    states = set(product(range(3), repeat=2))
    transitions = {}
    for state in states:
        choices = {}
        for active in range(2):
            if state[active] == 2:
                continue
            following = list(state)
            following[active] += 1
            choices[f"serve_{active}"] = frozenset({tuple(following)})
            if workers >= 2:
                following[1 - active] = 0
                choices[f"serve_{active}_repair_{1-active}"] = frozenset({tuple(following)})
        transitions[state] = choices
    return transitions, states


def fmt(value):
    return str(value)


def results():
    water, safe = water_model()
    viable, _, _ = invariant(water, safe)
    destination, ranks, actions = reach_and_stay(water, safe, {4, 5, 6})
    water_policy = {x: min(options, key=lambda u: (abs(u), u)) for x, options in actions.items()}
    binary = observation_actions(water, safe, {x: "low" if x <= 4 else "high" for x in safe})
    blind = observation_actions(water, safe, {x: "same" for x in safe})
    binary_policy = {x: 2 if x <= 4 else 0 for x in safe}
    assert not policy_violations(water, safe, binary_policy)
    assert not policy_violations(water, destination, water_policy)
    for x, rank in ranks.items():
        if rank:
            assert all(ranks[y] < rank for y in water[x][water_policy[x]])
    wrong_policy = {x: 0 for x in safe}
    service = {}
    for workers in [1, 2]:
        model, states = service_model(workers)
        retained, choices, removed = invariant(model, states)
        policy = {s: sorted(choices[s])[0] for s in retained}
        assert not policy_violations(model, retained, policy)
        service[str(workers)] = {
            "maintainable_states": [list(s) for s in sorted(retained)],
            "removed_per_iteration": [[list(s) for s in sorted(group)] for group in removed],
            "policy": {str(s): a for s, a in sorted(policy.items())},
        }
    lower, upper = F(2, 100), F(10, 100)
    old_spread, new_spread = F(9, 100), F(25, 1000)
    old_nominals = [lower + old_spread, upper - old_spread]
    new_nominals = [lower + new_spread, upper - new_spread]
    selected = F(6, 100)
    tolerance = {
        "required_clearance_mm": [fmt(lower), fmt(upper)],
        "old_nominal_constraints_mm": list(map(fmt, old_nominals)),
        "old_design_possible": old_nominals[0] <= old_nominals[1],
        "revised_nominal_interval_mm": list(map(fmt, new_nominals)),
        "chosen_nominal_mm": fmt(selected),
        "revised_actual_clearance_mm": [fmt(selected-new_spread), fmt(selected+new_spread)],
        "nominal_with_extra_drift_mm": fmt(F(55, 1000)),
        "measured_clearance_acceptance_mm": [fmt(F(3, 100)), fmt(F(9, 100))],
    }
    drift_nominal = F(55, 1000)
    extremes = [drift_nominal+dh-dd+drift for dh, dd, drift in product(
        [-F(15, 1000), F(15, 1000)], [-F(1, 100), F(1, 100)], [-F(1, 100), F(2, 100)])]
    assert min(extremes) == lower and max(extremes) == upper
    tooling = []
    for units in range(1, 13):
        upkeep = 2*((units-1)//3)
        manual, direct, bootstrap = 4*units, 5+units+upkeep, 9+units+upkeep
        tooling.append({"units": units, "manual": manual, "direct_tool": direct,
                        "tool_with_bootstrap": bootstrap,
                        "direct_vs_manual": "tool" if direct < manual else "tie" if direct == manual else "manual",
                        "bootstrap_vs_manual": "tool" if bootstrap < manual else "tie" if bootstrap == manual else "manual"})
    return {
        "standing": "Exact results for stipulated finite and interval models; no physical deployment or human trial.",
        "water": {
            "maintainable_states": sorted(viable), "target_maintainable_states": sorted(destination),
            "minimum_worst_case_steps": ranks, "reach_and_stay_policy": water_policy,
            "binary_observation_safe_actions": {k: sorted(v) for k, v in binary.items()},
            "blind_observation_safe_actions": {k: sorted(v) for k, v in blind.items()},
            "binary_policy_preserving_transitions": sum(len(water[x][binary_policy[x]]) for x in safe),
            "zero_action_counterexamples": policy_violations(water, safe, wrong_policy),
        },
        "service": service, "shaft_and_hole": tolerance, "tooling": tooling,
    }


if __name__ == "__main__":
    output = Path(__file__).resolve().parents[1] / "evidence" / "computed-results.json"
    output.write_text(json.dumps(results(), indent=2, sort_keys=True) + "\n")
    print(f"Wrote {output.name}: water control, continuous service, dimensional fit, tooling costs")
