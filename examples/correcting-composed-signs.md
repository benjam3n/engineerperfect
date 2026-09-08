# Correcting two composed sign changes

Within the original available operations, two observations jointly enable a cheaper repair even when either observation alone makes the complete route more expensive. Constructing a missing operation then beats that optimized route too. These are different corrections to how the problem is approached.

A producer sends a positive value, here instantiated as 7. A producer flag p and consumer flag c each independently reverse its sign when set to 1. The delivered value is

\[
y=7(-1)^{p+c},\qquad p,c\in\{0,1\}.
\]

The undertaking is to restore the original value. The initial operation inventory permits keeping the delivered sign, reversing it, inspecting either flag, or resetting both flags and recomputing. Keeping works when the flags match; reversing works when they differ. Either final operation costs 1. Inspecting either flag costs 1. Resetting both flags is a common intervention costing 4. These are stipulated work costs. The initial optimality claim is over that declared inventory, including its restricted inquiries.

| Producer flag | Consumer flag | Delivered value | Required one-unit operation |
|---:|---:|---:|---|
| 0 | 0 | 7 | Keep sign |
| 0 | 1 | −7 | Reverse sign |
| 1 | 0 | −7 | Reverse sign |
| 1 | 1 | 7 | Keep sign |

Inspecting either flag alone leaves one matching and one mismatching possibility. Neither one-unit operation is justified across that pair. The only common intervention is still the four-unit reset. Judging a question solely by the intervention available immediately afterward gives cost 1 + 4 = 5, worse than resetting without inquiry.

Both inquiries together determine whether the flags match. Their cost plus the appropriate operation is 1 + 1 + 1 = 3. This is optimal: a plan using the common reset costs at least 4, while a plan avoiding it must distinguish matching from mismatching flags. Neither single available inquiry does so, and two inquiries plus an operation cost at least 3.

The [planner and example runner](../tools/run_contribution_examples.py) construct the conditional route and execute its final operation on the actual delivered value in all four cases. Every execution restores 7 at cost 3.

The useful fact for selecting between keeping and reversing is relational. Knowing either component property in isolation does not determine that choice; their relation does. Two reversals preserve the original sign. Correcting each reversal independently would confuse a component convention with the end-to-end concern.

This also exposes a failure in evaluating inquiry. An intermediate distinction may acquire its usefulness through a later distinction. Requiring each first step to justify itself using only immediately available terminal actions can prevent the cheaper complete result. The [contribution choice](../choosing-the-next-contribution.md) evaluates the continuation that makes the first step worthwhile.

## A new operation makes that diagnosis unnecessary

The sign changes preserve magnitude. For an original x > 0,

\[
\left|x(-1)^{p+c}\right|=x.
\]

Taking the positive magnitude therefore restores the original value without learning either flag. The example implements this operation with `abs`, admits it at a stipulated cost of 1, and recomputes the plan. The planner now selects it immediately. All four executions restore 7 at cost 1.

The earlier diagnostic optimum was 3; the enlarged operation set permits 1. The added operation changes which distinctions the undertaking needs. The original solver could not discover this possibility because its input supplied no such intervention. Its proof of optimality did not establish the completeness of that input.

The condition x > 0 matters. If the required original value is −7 and the delivery is already −7, taking positive magnitude produces +7 and destroys a correct result. That counterexample is executed too. A more broadly admitted signal requires a different intervention or the information needed to preserve its legitimate sign.
