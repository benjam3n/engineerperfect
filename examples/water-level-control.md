# Keeping water within a useful range

This is a constructed discrete model of a tank. The values are stipulated for exact reasoning; no physical tank, pump, sensor, or field performance was measured.

At each period, level x is an integer. The actuator adds or removes u units, with u in {−3,−2,−1,0,1,2,3}. An unknown withdrawal d in {0,1,2} then occurs. The next level is x' = x + u − d. The initial acceptable levels are 1 through 9. The actuator is immediately available and accurate; there is no delay, energy limit, leak, saturation behavior, or unmodeled demand in this construction. Negative u represents an available discharge action.

## A fixed action cannot cover every acceptable starting level

At level 1, preventing x' < 1 under d = 2 requires u ≥ 2. At level 9, preventing x' > 9 under d = 0 requires u ≤ 0. A single action cannot satisfy both. A controller receiving no distinction between those states therefore cannot preserve the entire range from every admitted initial level.

Even a precomputed sequence cannot preserve the range indefinitely from one known initial level. Compare an all-zero withdrawal history with an all-two history under the same chosen actions. After n periods their levels differ by exactly 2n because the actuator contributions cancel in the difference. Two levels within [1,9] can differ by at most 8. At n = 5 the difference is 10, so at least one history violates the requirement. This proof covers every blind time-varying sequence; it does not merely test one poorly chosen sequence.

## One low/high reading supplies a preserving controller

For low levels 1 through 4, choose u = 2. The possible next levels span 1 through 6, entirely acceptable. For high levels 5 through 9, choose u = 0. The possible next levels span 3 through 9, also acceptable.

Thus the policy

\[
u(x)=\begin{cases}2&x\le4,\\0&x\ge5\end{cases}
\]

preserves the range indefinitely under the stated dynamics. The computation checks all 27 state-withdrawal combinations for this policy. The induction from one-step preservation to continued preservation supplies the infinite-time argument; the finite check by itself is not an infinite trajectory experiment.

The full sets of common preserving actions are {2,3} for the low observation and {−2,−1,0} for the high observation. The code returns those sets. The chosen policy uses the smallest action magnitude within each.

This result changes the design: exact level measurement is unnecessary for the specified wide range. A sufficient observation preserves the action-changing distinction.

## Reaching and preserving a narrower operating band

Now retain the allowed transit levels 1 through 9 but require arrival at levels 4 through 6 followed by continued operation there. Exact current level is available in this second design.

The constructed policy is u = min(3, 6 − x). For x ≥ 3, the next level lies in [4,6]. At x = 2, u = 3 gives next levels {3,4,5}; at x = 1 it gives {2,3,4}. Repeated application reaches the target in at most three periods from any allowed initial state.

| Initial level | Selected action | Minimum worst-case periods to the maintained band |
|---:|---:|---:|
| 1 | 3 | 3 |
| 2 | 3 | 2 |
| 3 | 3 | 1 |
| 4 | 2 | 0 |
| 5 | 1 | 0 |
| 6 | 0 | 0 |
| 7 | −1 | 1 |
| 8 | −2 | 1 |
| 9 | −3 | 1 |

The lower bound at level 1 is attained by withdrawal 2 at every period: the largest available input raises the level by at most one each time. Reaching 4 then requires at least three periods. The upper and lower bounds agree.

At x in {4,5,6}, preserving the target requires x + u − 2 ≥ 4 and x + u ≤ 6, hence u = 6 − x. The preserving actions are respectively 2, 1, and 0. A memoryless observation that merges any two target levels cannot preserve the entire target set. The finer requirement genuinely demands more distinctions.

## What changes when the assumptions change

If withdrawal can exceed 2, the existing guarantee no longer follows. If the command reaches the pump late, the measured x may not be the state to which the action applies. If pumping consumes a finite supply, the supply must enter the state before an indefinite guarantee is valid.

These are concrete transfer limits of the model. They do not erase the demonstrated result: a two-observation preserving policy and an exact-state arrival-and-maintenance policy have been constructed, with exact operating bounds. [Computation](../tools/run_examples.py) · [Recorded results](../evidence/computed-results.json).
