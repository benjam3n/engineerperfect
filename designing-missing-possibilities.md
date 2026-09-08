# Designing missing possibilities

Choosing well from the present alternatives and constructing a better alternative are different engineering capabilities. An optimizer over a fixed space can be flawless while its result remains inferior to an arrangement excluded from that space.

Let all paths available from an initial state lie in a reachable set R, and let G be the target. If R ∩ G is empty, no change in selection among those paths can reach G. A successful repair must change the initial conditions, target, or transition possibilities. When the target and initial conditions are justified and fixed, the transition possibilities must change.

That change can be an added operation, a removed interference, a new sequence, a substituted resource, a different interface, or an environment that supplies part of the work. It need not be a more intelligent controller.

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

## Removal can supply the missing capability

Suppose action a already reaches a useful state, but an unnecessary rule disables a. If removing the rule is authorized and preserves every legitimate constraint, the old mechanism becomes available without adding a new one. The gain comes from removing an exclusion.

Conversely, if a rule blocks an unsafe or unauthorized action, deleting it changes a legitimate condition and cannot be credited as satisfying the same undertaking. The distinction rests on the rule's actual purpose and authority, not a presumption for or against constraints.

A similar result holds for competing processes. If a useful process requires resource r and another process holds r without contributing to any current obligation, ending the latter can enable the former. The operation is resource release. More prompting or more resources may be unnecessary.

## Intermediate capability can be worth a temporary loss

An investment that produces no immediate service can enable cheaper future production. Rejecting every step whose immediate output is lower than the incumbent prevents that investment by construction.

For manual production cost 4n and direct tooling cost 5 + n + 2 floor((n−1)/3), tooling is cheaper for every integer n ≥ 2. The first unit alone favors manual work. An immediate-only comparison therefore chooses correctly for one unit and incorrectly for a known larger undertaking.

When a missing bootstrap part adds cost 4, the decision changes: manual work is cheaper for one or two units, the methods tie at three, and tooling is cheaper from four onward. The [completed calculation](examples/tooling-and-production.md) includes the recurrence and proof, rather than treating “invest in capability” as a universally beneficial instruction.

This is the connection to improvementresearch: the worth of an improvement depends on its actual continuation and accumulation. Engineerperfect supplies the production route and resource consequences needed by that judgment. The repositories can share a result without becoming duplicates.
