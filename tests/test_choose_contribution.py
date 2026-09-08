"""Compare optimization with complete syntax-tree enumeration and forward use.

The independent oracle generates every inquiry tree without looking at cases,
then executes those trees in every actual case and checks terminal adequacy.
It does not use possible-case partitions or the optimizer's recurrence.
"""

import sys
import unittest
from functools import lru_cache
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from choose_contribution import Inquiry, Intervention, choose_contribution


@lru_cache(maxsize=None)
def all_trees(available):
    trees = [("act", "a"), ("act", "b")]
    for question in available:
        below = all_trees(tuple(q for q in available if q != question))
        trees.extend(("ask", question, left, right) for left, right in product(below, repeat=2))
    return tuple(trees)


def trace_tree(tree, case, answers):
    counts = [0, 0]
    while tree[0] == "ask":
        question = tree[1]
        counts[question] += 1
        tree = tree[2 + answers[question][case]]
    return tree[1], counts


class ContributionChoiceTests(unittest.TestCase):
    def test_all_8192_costed_problems_against_74_complete_trees(self):
        cases = ("0", "1", "2")
        trees = all_trees((0, 1))
        self.assertEqual(len(trees), 74)
        profiles = [({"a": 0, "b": 3}, (1, 2)), ({"a": 4, "b": 4}, (0, 1))]
        count = 0
        for bits in product(range(2), repeat=6):
            answers = (bits[:3], bits[3:])
            traces = [[trace_tree(tree, case, answers) for case in range(3)] for tree in trees]
            for a_mask, b_mask in product(range(8), repeat=2):
                masks = {"a": a_mask, "b": b_mask}
                valid = [trace for trace in traces
                         if all(masks[action] & (1 << case)
                                for case, (action, _) in enumerate(trace))]
                for action_costs, inquiry_costs in profiles:
                    expected = min((max(action_costs[action] + sum(n * c for n, c in zip(used, inquiry_costs))
                                        for action, used in trace) for trace in valid), default=None)
                    actions = {a: Intervention(action_costs[a], frozenset(s for i, s in enumerate(cases)
                                                                         if masks[a] & (1 << i))) for a in masks}
                    inquiries = {str(q): Inquiry(inquiry_costs[q], {s: str(answers[q][i]) for i, s in enumerate(cases)})
                                 for q in range(2)}
                    plan, blockers = choose_contribution(cases, actions, inquiries)
                    self.assertEqual(None if plan is None else plan.cost, expected,
                                     (bits, masks, action_costs, inquiry_costs))
                    if plan is None:
                        self.assertTrue(blockers)
                        for cell in blockers:
                            self.assertTrue(all(len({q.outcomes[s] for s in cell}) == 1 for q in inquiries.values()))
                            self.assertFalse(any(set(cell) <= a.works_in for a in actions.values()))
                    else:
                        self.assertFalse(blockers)
                        realized = []
                        for case in cases:
                            node, cost, used = plan, 0, set()
                            while node.kind == "inquire":
                                self.assertNotIn(node.name, used)
                                used.add(node.name)
                                question = inquiries[node.name]
                                cost += question.cost
                                node = node.after(question.outcomes[case])
                            self.assertIn(case, actions[node.name].works_in)
                            realized.append(cost + actions[node.name].cost)
                        self.assertEqual(max(realized), plan.cost)
                    count += 1
        self.assertEqual(count, 8192)

    def test_known_context_does_not_require_another_question(self):
        actions = {"a": Intervention(1, frozenset({"0"})), "b": Intervention(1, frozenset({"1"}))}
        queries = {"which": Inquiry(2, {"0": "left", "1": "right"})}
        plan, _ = choose_contribution(["0", "1"], actions, queries, remaining={"0"})
        self.assertEqual((plan.kind, plan.name, plan.cost), ("intervene", "a", 1))
        root, _ = choose_contribution(["0", "1"], actions, queries)
        with self.assertRaises(ValueError):
            root.after("neither")
        with self.assertRaises(ValueError):
            plan.after("left")

    def test_pairwise_repairs_do_not_supply_a_common_repair(self):
        actions = {"a": Intervention(1, frozenset({"0", "1"})),
                   "b": Intervention(1, frozenset({"1", "2"})),
                   "c": Intervention(1, frozenset({"0", "2"}))}
        plan, blockers = choose_contribution(["0", "1", "2"], actions, {})
        self.assertIsNone(plan)
        self.assertEqual(blockers, (("0", "1", "2"),))

    def test_invalid_inputs_do_not_become_a_successful_plan(self):
        cases = ["0"]
        actions = {"a": Intervention(1, frozenset(cases))}
        invalid = [
            ([], {}, {}, None),
            (["0", "0"], actions, {}, None),
            (cases, actions, {}, set()),
            (cases, actions, {}, {"unknown"}),
            (cases, {"a": Intervention(1, frozenset({"unknown"}))}, {}, None),
            (cases, actions, {"q": Inquiry(1, {})}, None),
        ]
        for args in invalid:
            with self.subTest(args=args), self.assertRaises(ValueError):
                choose_contribution(*args)
        for cost in [-1, True, 0.5, float("nan")]:
            with self.subTest(cost=cost), self.assertRaises(ValueError):
                choose_contribution(cases, {"a": Intervention(cost, frozenset(cases))}, {})
            with self.subTest(inquiry_cost=cost), self.assertRaises(ValueError):
                choose_contribution(cases, actions, {"q": Inquiry(cost, {"0": "answer"})})


if __name__ == "__main__":
    unittest.main()
