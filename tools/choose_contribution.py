"""Exact inquiry/intervention choice for a finite, explicitly supplied problem.

Inquiries report a deterministic fact without changing the case. Interventions
finish the stated undertaking in their declared cases. Costs are nonnegative
integers in one additive unit. The objective is minimum worst-case total cost,
not expected cost, universal benefit, or discovery of the input model.
"""

from collections.abc import Mapping
from dataclasses import dataclass
from functools import lru_cache


@dataclass(frozen=True)
class Intervention:
    cost: int
    works_in: frozenset[str]


@dataclass(frozen=True)
class Inquiry:
    cost: int
    outcomes: Mapping[str, str]


@dataclass(frozen=True)
class Plan:
    kind: str
    name: str
    cost: int
    remaining: tuple[str, ...]
    branches: tuple[tuple[str, "Plan"], ...] = ()

    def after(self, outcome: str) -> "Plan":
        """Follow an admitted answer; never guess a branch for an unknown answer."""
        if self.kind != "inquire":
            raise ValueError("An intervention has no observation branch")
        for label, following in self.branches:
            if outcome == label:
                return following
        raise ValueError("Answer outside the modeled possibilities; revise the model")


def _cost(value):
    if type(value) is not int or value < 0:
        raise ValueError("Costs must be nonnegative integers in one declared unit")


def choose_contribution(cases, interventions, inquiries, remaining=None):
    """Return (minimum-cost Plan, obstruction cells), or (None, obstruction cells).

    Each obstruction is a nonempty set of remaining cases producing identical
    answers to every available inquiry, without one intervention working in all
    of them. Such a cell proves that no inquiry policy can guarantee completion.
    A feasible result has no obstruction cells. Facts already obtained belong
    in `remaining`; an empty or out-of-domain context is rejected.

    Exact search can visit exponentially many case subsets. Inquiries must not
    consume opportunities or change later costs/availability except by adding
    their stated cost. Those effects require a different model.
    """
    case_list = tuple(cases)
    if not case_list or any(not isinstance(s, str) for s in case_list):
        raise ValueError("Supply a nonempty collection of string case identifiers")
    universe = frozenset(case_list)
    if len(universe) != len(case_list):
        raise ValueError("Case identifiers must be unique")
    current = universe if remaining is None else frozenset(remaining)
    if not current or not current <= universe:
        raise ValueError("Remaining cases must be a nonempty subset of the model")

    for collection in (interventions, inquiries):
        if any(not isinstance(name, str) for name in collection):
            raise ValueError("Operation names must be strings")
    actions = {}
    for name, action in interventions.items():
        _cost(action.cost)
        support = frozenset(action.works_in)
        if not support <= universe:
            raise ValueError("An intervention names a case outside the model")
        actions[name] = Intervention(action.cost, support)
    questions = {}
    for name, inquiry in inquiries.items():
        _cost(inquiry.cost)
        outcomes = dict(inquiry.outcomes)
        if set(outcomes) != universe:
            raise ValueError("Each inquiry must specify an answer for every case")
        if any(not isinstance(answer, str) for answer in outcomes.values()):
            raise ValueError("Inquiry answers must be strings")
        questions[name] = Inquiry(inquiry.cost, outcomes)

    # Identical complete answer signatures cannot be separated by adaptation.
    signatures = {}
    for case in sorted(current):
        signature = tuple(questions[q].outcomes[case] for q in sorted(questions))
        signatures.setdefault(signature, set()).add(case)
    blockers = tuple(
        tuple(sorted(cell)) for cell in signatures.values()
        if not any(cell <= action.works_in for action in actions.values())
    )
    if blockers:
        return None, blockers

    @lru_cache(maxsize=None)
    def solve(possible):
        best = None
        for name in sorted(actions):
            action = actions[name]
            if possible <= action.works_in and (best is None or action.cost < best.cost):
                best = Plan("intervene", name, action.cost, tuple(sorted(possible)))
        for name in sorted(questions):
            inquiry = questions[name]
            cells = {}
            for case in possible:
                cells.setdefault(inquiry.outcomes[case], set()).add(case)
            if len(cells) < 2:
                continue  # No new distinction; the inquiry has no other effect.
            branches = tuple(
                (answer, solve(frozenset(cell))) for answer, cell in sorted(cells.items())
            )
            if any(child is None for _, child in branches):
                continue
            cost = inquiry.cost + max(child.cost for _, child in branches)
            if best is None or cost < best.cost:
                best = Plan("inquire", name, cost, tuple(sorted(possible)), branches)
        return best

    plan = solve(current)
    assert plan is not None  # Querying every distinguishing inquiry is feasible.
    return plan, ()
