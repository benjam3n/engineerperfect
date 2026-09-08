"""Compare synthesis with independent enumeration of every stationary policy.

The exhaustive family has two safe states, one failure state, two available
actions, and every nonempty successor subset: 7**4 = 2,401 transition systems.
"""

import sys
import unittest
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from finite_control import invariant, observation_actions, reach_and_stay


def policy_graph(model, policy, start):
    reached, pending = set(), [start]
    while pending:
        state = pending.pop()
        if state in reached:
            continue
        reached.add(state)
        if state not in policy:
            return None
        pending.extend(model[state][policy[state]])
    return {s: model[s][policy[s]] for s in reached}


def graph_hitting_bound(graph, start, target):
    """Graph path analysis, without predecessor iteration or synthesis helpers."""
    if graph is None:
        return None
    for s in set(graph) & target:
        if not graph[s] <= target:
            return None
    visiting, memo = set(), {}

    def longest(state):
        if state in target:
            return 0
        if state in visiting:
            raise ValueError("Adversary can remain in a cycle outside target")
        if state in memo:
            return memo[state]
        visiting.add(state)
        result = 1 + max(longest(s) for s in graph[state])
        visiting.remove(state)
        memo[state] = result
        return result

    try:
        return longest(start)
    except ValueError:
        return None


class FiniteControlTests(unittest.TestCase):
    def test_all_2401_nondeterministic_systems(self):
        successor_sets = [frozenset(s for s in range(3) if mask & (1 << s)) for mask in range(1, 8)]
        policies = [dict(zip([0, 1], choices)) for choices in product(["a", "b"], repeat=2)]
        count = 0
        for transitions in product(successor_sets, repeat=4):
            model = {0: {"a": transitions[0], "b": transitions[1]},
                     1: {"a": transitions[2], "b": transitions[3]}}
            graphs = {(i, s): policy_graph(model, p, s)
                      for i, p in enumerate(policies) for s in [0, 1]}
            expected_safe = {s for s in [0, 1] if any(graphs[i, s] is not None for i in range(4))}
            actual_safe, _, _ = invariant(model, {0, 1})
            self.assertEqual(actual_safe, expected_safe, model)
            for target in [set(), {0}, {0, 1}]:
                expected = {}
                for s in [0, 1]:
                    bounds = [graph_hitting_bound(graphs[i, s], s, target) for i in range(4)]
                    bounds = [bound for bound in bounds if bound is not None]
                    if bounds:
                        expected[s] = min(bounds)
                _, actual, _ = reach_and_stay(model, {0, 1}, target)
                self.assertEqual(actual, expected, (model, target))
            count += 1
        self.assertEqual(count, 2401)

    def test_empty_successors_are_not_vacuous_success(self):
        with self.assertRaises(ValueError):
            invariant({0: {"wait": set()}}, {0})

    def test_missing_action_is_not_maintenance(self):
        self.assertEqual(invariant({0: {}}, {0})[0], frozenset())

    def test_pairwise_overlap_does_not_supply_one_common_action(self):
        model = {0: {"a": {0}, "b": {0}}, 1: {"b": {1}, "c": {1}},
                 2: {"a": {2}, "c": {2}}}
        observed = observation_actions(model, {0, 1, 2}, {0: "same", 1: "same", 2: "same"})
        self.assertEqual(observed["same"], frozenset())


if __name__ == "__main__":
    unittest.main()
