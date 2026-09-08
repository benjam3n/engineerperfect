# Building the tool that makes later production worthwhile

A constructed production task has three stipulated cost components. Manual production costs 4 per finished unit. A tool costs 5 to construct, then 1 per finished unit. After each three units it needs maintenance costing 2 before another unit can be made. Costs share one declared accounting unit; no financing, uncertainty, or calendar constraint is hidden in these numbers.

For a known integer demand n ≥ 1, manual cost is M(n) = 4n. Tooling cost is

\[
T(n)=5+n+2\left\lfloor\frac{n-1}{3}\right\rfloor.
\]

No maintenance is charged after the final unit when the undertaking ends there. An undertaking requiring a ready tool at completion would have a different terminal condition.

## The first unit and the whole undertaking favor different choices

| Units | Manual | Direct tooling | Tooling with the bootstrap described below |
|---:|---:|---:|---:|
| 1 | 4 | 6 | 10 |
| 2 | 8 | 7 | 11 |
| 3 | 12 | 8 | 12 |
| 4 | 16 | 11 | 15 |
| 5 | 20 | 12 | 16 |
| 6 | 24 | 13 | 17 |
| 7 | 28 | 16 | 20 |
| 8 | 32 | 17 | 21 |

Direct tooling is inferior for one unit and cheaper for every n ≥ 2. At n = 2 the saving is 1. Each additional unit increases the saving by 3 except at a maintenance boundary, when it increases by 1. Hence the saving remains positive thereafter. The argument covers all integer n, not only the displayed rows.

An immediate-output rule that refuses to spend time or material on the tool cannot attain these lower future production costs. Conversely, building a tool for a one-unit task is wasteful under the stipulated criteria. General enthusiasm for capability investment cannot replace this comparison.

## A circular prerequisite changes the production route

Now suppose the tool needs a sacrificial calibration part, and the standard production route for that part already assumes the tool exists. Neither is initially available. If these are the only construction rules, neither can ever be produced: no rule is executable initially, and therefore none can create the other's prerequisite.

Allow a manual route that produces the calibration part for 4. The executable sequence is now: make the sacrificial part manually; consume it while constructing the tool for 5; produce the required n finished units with the tool, maintaining it before units 4, 7, 10, and so on.

The total becomes B(n) = 9 + n + 2 floor((n−1)/3). Manual production is cheaper for n = 1 or 2, the methods tie at n = 3, and bootstrapped tooling is cheaper from n = 4 onward. At n = 4 the saving is 1; the same incremental argument makes the saving positive for every larger n.

The missing prerequisite therefore changes the recommendation from tooling at two units to tooling at four. The bootstrap is not a minor documentation detail. It changes both feasibility and comparative cost.

## Constructing more producers has its own requirements

The ability to make finished parts does not imply the ability to make another copy of the tool. A copy can require a different material, accuracy, operator, or machine. Self-reproduction follows only when the actual outputs and available transformations supply every required input, including support and replacement capacity.

If one tool produces q saleable units per period but a new tool consumes q units of the same capacity, creating another producer sacrifices that period's saleable output. Whether the investment helps depends on later demand, remaining life, and the production and support costs of the new tool. Those variables cannot be deleted by calling the result recursive improvement.

The conditional comparison can still be completed. Let K include construction and displaced-output cost, let the new tool become usable after period τ, and let its remaining usable horizon end at H. In each later period t, let unmet demand be d_t, value per additionally delivered unit be v_t, and additional operating and maintenance cost be m_t. Assume the extra tool supplies up to q units independently of existing production and all costs use the same undiscounted criterion. Its net contribution is

\[
\sum_{t=\tau+1}^{H}\left[v_t\min(q,d_t)-m_t\right]-K.
\]

Construction is better than retaining the baseline exactly when this quantity is positive. If H ≤ τ there is no later production in the undertaking and the contribution is −K. If demand is already fully met, the production-value term is zero. These consequences locate the actual dependency on future use without requiring invented demand values.

This connects the repository's literal and broader meanings: engineering a means of further engineering can change what becomes possible, but the initial construction, ongoing support, and later use must all be counted under the actual undertaking.

[Recomputed costs for 1–12 units](../evidence/computed-results.json) · [Calculation](../tools/run_examples.py).
