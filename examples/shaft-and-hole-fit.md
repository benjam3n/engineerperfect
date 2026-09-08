# Manufacturing a shaft and hole that always fit

Every nominal design fails under the original stipulated variation. The missing possibility comes from changing the process: a combined error half-width of at most 0.04 millimeters permits a robust nominal design. The calculation changes which variable needs engineering and removes further nominal search as a sufficient repair under the original premises.

The stipulated requirement is clearance between 0.02 and 0.10 millimeters for every admitted shaft-hole combination. Shaft diameter is D + e_D with e_D in [−0.04,0.04]. Hole diameter is H + e_H with e_H in [−0.05,0.05]. All combinations of those errors are admitted. These are invented design values, not a manufacturing standard or measured process capability.

Let Δ = H − D. Actual clearance is c = Δ + e_H − e_D, so its exact range is [Δ − 0.09, Δ + 0.09]. The two requirements imply

\[
\Delta\ge0.11,\qquad\Delta\le0.01.
\]

The interval is empty. Every nominal choice fails. More search over nominal dimensions cannot produce a successful design within these premises.

## Changing the manufacturing process makes the design feasible

For general error half-widths t_D and t_H, robust fit requires

\[
0.02+t_D+t_H\le\Delta\le0.10-t_D-t_H.
\]

A feasible nominal dimension exists exactly when t_D + t_H ≤ 0.04. This is the necessary and sufficient manufacturing-variation condition for the stipulated independent range model.

If a revised process bounds shaft error by ±0.01 and hole error by ±0.015, then Δ can range from 0.045 to 0.075. Choosing Δ = 0.06 gives actual clearance [0.035,0.085]. Every admitted pair satisfies the requirement. The physical ability to hold those tighter tolerances remains unmeasured; the conditional design is exact.

This moves the engineering question from nominal geometry to the process that produces the geometry. It does not merely rename an impossible part design as feasible.

## Environmental drift consumes the remaining margin

Suppose use adds an extra clearance shift δ in [−0.01,0.02]. Combined with the revised manufacturing bounds, clearance lies in [Δ − 0.035, Δ + 0.045]. The robust nominal interval becomes the single point Δ = 0.055, giving the full required range [0.02,0.10].

The eight joint endpoint combinations are evaluated with exact fractions. No sampled interior point can exceed those extremes because clearance is affine in each bounded error. The guarantee has no remaining tolerance margin: further admitted adverse drift would require another design change.

## Measurement does not remove physical variation

Suppose each diameter measurement has error at most ±0.005. Measured clearance c_m differs from true clearance by at most 0.01. A measurement-only acceptance decision guarantees true clearance in [0.02,0.10] exactly when c_m lies in [0.03,0.09], under the independent error bounds.

Accepting the measured interval [0.02,0.10] without this guard band can accept an actual clearance of 0.01 or 0.11. A passed inspection label does not alter the true dimensions. Nor does discarding out-of-range pairs prove that the production process itself produces only acceptable parts.

## Matched pairs change the replacement obligation

Sorting or jointly manufacturing matched pairs could constrain e_H − e_D even when each separate error range is broad. That would use a different admitted joint set. It can make assembled fit possible while failing the original requirement that every permitted shaft fit every permitted hole.

If interchangeability matters for maintenance, the matching information and replacement procedure become additional system requirements. If interchangeability does not matter, preserving it may impose unnecessary manufacturing cost. The calculation identifies the trade-off; it does not silently resolve it by changing the original quantifier.

[Exact calculation](../tools/run_examples.py) · [Recorded bounds](../evidence/computed-results.json).
