# Designing missing possibilities

Choosing well from the present alternatives and constructing a better alternative are different engineering capabilities. An optimizer over a fixed space can be flawless while its result remains inferior to an arrangement excluded from that space.

Let all paths available from an initial state lie in a reachable set R, and let G be the target. If R ∩ G is empty, no change in selection among those paths can reach G. A successful repair must change the initial conditions, target, or transition possibilities. When the target and initial conditions are justified and fixed, the transition possibilities must change.

That change can be an added operation, a removed interference, a new sequence, a substituted resource, a different interface, or an environment that supplies part of the work. It need not be a more intelligent controller.

This is one way a perspective change becomes consequential: a presumed constant becomes something the undertaking can alter. Merely redescribing the same excluded alternatives leaves the limit unchanged. The construction must expose a different available intervention or establish the exact dependency that would make it available.

The [sign construction](examples/correcting-composed-signs.md) makes this difference executable. With only component inspections, keeping or reversing the delivered sign, and a reset available, the best route costs 3. Since the admitted original signal is positive and the transformations preserve magnitude, taking the delivered magnitude restores it directly. Implementing and admitting that operation yields cost 1. The original optimum did not change through better search; its operation set changed through a derived construction. For a negative original signal, that same operation fails, and the counterexample is retained.

## An apparent trade-off can identify a restricted set of alternatives

The fit undertaking requires clearance to be neither too small nor too large. Under the original production variation, moving nominal diameter to improve one extreme worsens the other, and no nominal choice satisfies both. A compromise within that interval cannot fulfill the demand.

Reducing the combined manufacturing error half-width to at most 0.04 changes the interval itself. With half-widths 0.01 and 0.015, every nominal difference between 0.045 and 0.075 satisfies both limits. This does not prove that tighter production is free or physically available. It determines the exact additional capability and prevents an unsupported conclusion that one clearance requirement must be surrendered.

The general inference is limited but useful. A conflict among current alternatives establishes a conflict within those alternatives. It does not establish that every attainable alternative has that conflict. A new mechanism can improve both properties, introduce a different cost, or fail to be available. The actual alternatives determine which conclusion holds; describing the properties as opposites does not.

## The water requirement exposes different engineering directions

The initial undertaking is to preserve a useful water level despite unknown withdrawal. Candidate constructions differ in what they change:

| Construction | Consequence in the stated model |
|---|---|
| Precompute a fixed sequence of pump actions | Cannot preserve a width-8 range beyond four periods from one known starting level against all withdrawals in {0,1,2} |
| Add a low/high measurement | Supplies a two-action policy that preserves levels 1 through 9 indefinitely |
| Add exact current-level measurement | Supports the constructed controller that reaches levels 4 through 6 in at most three steps and keeps them there |
| Widen the acceptable operating range | Can change the information and actuation needed; it also changes the original requirement |
| Reduce variation at the source | Changes the successor sets and can reduce the information or correction required |
| Change the physical mechanism | Can supply regulation through the plant itself, but requires its own physical model and qualification |

The first three rows are settled in the [water example](examples/water-level-control.md). The latter three identify distinct physical design variables and their exact location in the model. No unbuilt device is credited with an achieved water-control effect.

The comparison prevents two premature commitments: assuming software control is the only solution, and treating a named passive alternative as if its mechanics had already been constructed.

## Changing the system boundary changes what can be designed

In the [fit example](examples/shaft-and-hole-fit.md), a boundary containing only nominal part dimensions makes robust fit impossible. Including the manufacturing process exposes tolerances as changeable variables. Including assembly policy exposes matched pairing, with a separate loss of free interchangeability. Including use conditions exposes environmental drift.

These changes do not merely describe the same option in different words. They admit different causal interventions and impose different costs. The broader boundary is useful when its additional degrees of freedom change the outcome. It is needless expansion when they cannot affect the live judgment.

Similarly, a personal undertaking can be modeled as an isolated intention or as a person with available time, tools, access, surroundings, and other people's contributions. The latter can expose a concrete missing resource. It does not establish that every failure belongs to the environment or that an individual skill cannot be decisive.

For example, suppose an author can complete either of two tasks in the same available hour, and each actually requires that entire exclusive hour. Requiring both by its end exceeds the available time, even if the author understands both perfectly. Moving one deadline to a second available hour makes a sequential route possible. This is an exact consequence of the stipulated timing conditions, not a diagnosis that all personal difficulties are scheduling problems.

## Removal can supply the missing capability

Suppose action a already reaches a useful state, but an unnecessary rule disables a. If removing the rule is authorized and preserves every legitimate constraint, the old mechanism becomes available without adding a new one. The gain comes from removing an exclusion.

Conversely, if a rule blocks an unsafe or unauthorized action, deleting it changes a legitimate condition and cannot be credited as satisfying the same undertaking. The distinction rests on the rule's actual purpose and authority, not a presumption for or against constraints.

A similar result holds for competing processes. If a useful process requires resource r and another process holds r without contributing to any current obligation, ending the latter can enable the former. The operation is resource release. More prompting or more resources may be unnecessary.

## Intermediate capability can be worth a temporary loss

An investment that produces no immediate service can enable cheaper future production. Rejecting every step whose immediate output is lower than the incumbent prevents that investment by construction.

For manual production cost 4n and direct tooling cost 5 + n + 2 floor((n−1)/3), tooling is cheaper for every integer n ≥ 2. The first unit alone favors manual work. An immediate-only comparison therefore chooses correctly for one unit and incorrectly for a known larger undertaking.

When a missing bootstrap part adds cost 4, the decision changes: manual work is cheaper for one or two units, the methods tie at three, and tooling is cheaper from four onward. The [completed calculation](examples/tooling-and-production.md) includes the recurrence and proof, rather than treating “invest in capability” as a universally beneficial instruction.

This is the connection to improvementresearch: the worth of an improvement depends on its actual continuation and accumulation. Engineerperfect supplies the production route and resource consequences needed by that judgment. The repositories can share a result without becoming duplicates.
