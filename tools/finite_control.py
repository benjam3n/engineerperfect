"""Exact control constructions for explicitly supplied finite transition systems.

Each action maps to a nonempty set of possible successors. The controller chooses
an action before the successor is selected. Missing actions are unavailable;
states outside the declared safe set are failures. No probabilities are assumed.
"""

from collections.abc import Mapping


def _validate(transitions):
    for actions in transitions.values():
        for successors in actions.values():
            if not successors:
                raise ValueError("An available action must have a possible successor")


def safe_actions(transitions, state, destination):
    """Actions whose every possible successor lies in destination."""
    return frozenset(
        action for action, successors in transitions.get(state, {}).items()
        if successors and set(successors) <= destination
    )


def invariant(transitions: Mapping, safe):
    """Greatest subset of safe maintainable forever with full state observation.

    Returns the set, every preserving action at each retained state, and the
    successive removal sets. Exactness assumes finite, fully specified dynamics.
    """
    _validate(transitions)
    current = frozenset(safe)
    removed = []
    while True:
        following = frozenset(s for s in current if safe_actions(transitions, s, current))
        if following == current:
            return current, {s: safe_actions(transitions, s, current) for s in current}, removed
        removed.append(current - following)
        current = following


def reach_and_stay(transitions: Mapping, safe, target):
    """States from which target's invariant subset can be forced in finite time.

    Returns destination, minimum worst-case step ranks, and all actions that
    strictly lower rank (or preserve destination at rank zero).
    """
    _validate(transitions)
    safe = frozenset(safe)
    destination, preserving, _ = invariant(transitions, safe & frozenset(target))
    ranks = {s: 0 for s in destination}
    actions = dict(preserving)
    layer = 0
    while True:
        known = frozenset(ranks)
        added = {s: safe_actions(transitions, s, known) for s in safe - known}
        added = {s: choices for s, choices in added.items() if choices}
        if not added:
            return destination, ranks, actions
        layer += 1
        ranks.update({s: layer for s in added})
        actions.update(added)


def observation_actions(transitions, maintained, observation):
    """Common preserving actions for each observation on a supplied maintained set.

    This checks maintenance of that entire set by a memoryless observation
    policy. It does not solve arbitrary control with hidden state or memory.
    """
    _validate(transitions)
    maintained = frozenset(maintained)
    cells = {}
    for state in maintained:
        cells.setdefault(observation[state], []).append(state)
    result = {}
    for observed, states in cells.items():
        choices = [set(safe_actions(transitions, s, maintained)) for s in states]
        result[observed] = frozenset(set.intersection(*choices))
    return result


def policy_violations(transitions, maintained, policy):
    """Independent one-step witnesses against a claimed invariant policy."""
    maintained = set(maintained)
    errors = []
    for state in maintained:
        if state not in policy:
            errors.append((state, None, "missing policy action"))
            continue
        action = policy[state]
        successors = transitions.get(state, {}).get(action)
        if not successors:
            errors.append((state, action, "unavailable action"))
        else:
            for successor in successors:
                if successor not in maintained:
                    errors.append((state, action, successor))
    return errors
