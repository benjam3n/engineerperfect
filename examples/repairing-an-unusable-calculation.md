# Repairing an unusable calculation

The smallest adequate repair need not identify everything that is wrong or different. In this construction, one inspection and one repair make a calculation usable for 2 work units. Identifying the entire case first costs 3. Inspecting the most informative cheap attribute first also costs 3 while enabling the same repair.

Eight documents combine two omissions with four layouts. A document either lacks the subtraction rule or lacks its input values. It never lacks both in the initial inventory. Layout is a stored label a, b, c, or d and does not affect execution. The intended calculation is hole diameter minus shaft diameter. The stipulated source values are 10.06 and 10.00, so the correct result is exactly 0.06, or 3/50.

These are toy program records. The source values are fixtures, not measured manufacturing data. Work costs are declared integers and do not claim actual human or computer timings.

| Available operation | What it supplies | Cost |
|---|---|---:|
| Inspect the missing part | Distinguishes missing rule from missing input | 1 |
| Inspect layout | Distinguishes a, b, c, and d | 1 |
| Identify everything | Distinguishes all eight original records | 3 |
| Install the rule | Supplies subtraction; finishes only records already containing the input | 1 |
| Load the input | Supplies the available source values; finishes only records already containing the rule | 1 |
| Rebuild | Supplies both rule and input for any admitted record | 4 |

The operations are implemented in [run_contribution_examples.py](../tools/run_contribution_examples.py). Inspections read the record's actual fields. Repairs alter those fields, and the resulting calculation is executed with exact rational arithmetic. A case label alone is not accepted as evidence that its repair succeeded.

## More information selects a worse first inquiry

For the purpose of comparing information counts, suppose the eight original cases have equal probability. Layout has four equiprobable answers and reveals 2 bits. The missing-part inspection has two equiprobable answers and reveals 1 bit. Both cost 1. Maximizing information per unit therefore prefers layout.

After any layout answer, both omissions remain possible. A specific one-part repair is still unjustified. The cheapest continuation inspects the missing part for 1 and repairs it for 1, making total cost 3.

Inspecting the missing part first permits the repair immediately, making total cost 2. The four possible layouts need never be distinguished. Under this undertaking the additional bit supplied by the first method buys no improvement in the result.

Maximizing unadjusted information chooses the full identification, which reveals 3 bits but costs 3 before its one-unit repair. That route costs 4. The counterexample therefore defeats both information count and information per cost as universally sufficient choices for useful contribution. The optimization itself uses worst-case cost and requires no probability distribution; the uniform distribution is used only to evaluate these two information heuristics.

The best route costs exactly 2. Initially no cost-1 repair covers both omissions, and the only common intervention costs 4. Every useful inquiry costs at least 1, and every adequate repair costs at least 1. The missing-part inquiry followed by its appropriate repair attains that lower bound on every branch.

## Complete diagnosis adds an obligation the repair does not need

If the undertaking additionally requires identifying the exact original case, both omission and layout must be known. Neither cheap inquiry supplies both. Asking both costs 2 and repairing costs 1; the full-identification inquiry and repair cost 4. Thus the minimum is 3.

The one-unit difference does not come from concealing a failure. All eight repaired calculations produce exactly the required result under both routes. Complete diagnosis answers an additional question. Its cost is justified only when that question belongs to the undertaking, perhaps because it has another use that the repair criterion alone does not capture.

## Available context and a different intervention reverse the next choice

If the missing rule is already established, the remaining four records all accept the one-unit rule installation. The optimizer chooses it directly. Asking again which part is missing supplies no new distinction, and asking about layout supplies no needed one.

Alternatively, suppose an available rebuild now costs 1 while retaining its ability to supply both rule and input. Rebuilding immediately succeeds for all eight records. Any positive-cost inquiry followed by repair costs more. The correct choice changes from inquiry to intervention even though the uncertainty and inquiry mechanisms are unchanged.

This is a change in what needs to be learned produced by a change in what can be done. The example modifies the actual operation cost in the model and recomputes the plan. It does not infer that real rebuild costs fell merely because that would be convenient.

## A new answer requires changing the case inventory

A ninth record has layout a and lacks both rule and input. The inspection returns a third answer: both. The original plan has no branch for it and raises an explicit model-mismatch error instead of guessing which one-part repair to apply.

The expanded construction admits this record and supplies the combined repair for cost 2. The rebuilt inquiry plan still begins by inspecting the omission. The original branches cost 2 in total; the new branch costs 1 + 2 = 3. A direct common rebuild would cost 4. No cost-1 repair works on the new record, so a route distinguishing it and applying the combined repair cannot cost less than 3. The new plan attains that bound.

All nine calculations are executed after their selected repairs and return 3/50. The old optimum was exact within an inadequate inventory for the expanded undertaking. No increase in search accuracy inside the old inventory could supply its missing branch.

The [stored results](../evidence/contribution-results.json) contain the original plan, forced-first-inquiry comparisons, direct intervention when context already suffices, the cheaper common intervention, rejection of the unmodeled answer, and the executed expanded plan.
