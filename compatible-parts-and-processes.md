# Compatible parts and processes

Component correctness does not establish system correctness when the connection supplies an input outside a component's supported conditions. Let component A produce outputs in O_A and component B accept inputs in I_B. Direct composition requires O_A ⊆ I_B for the relevant operating situations. The fact that each set is nonempty, or that they overlap, is insufficient for a guarantee over every permitted output.

If a converter C sits between them, the required condition is C(O_A) ⊆ I_B, together with the converter's own availability and correctness. Naming an interface does not construct C. Unit conversion, synchronization, identifier matching, authority transfer, and physical fit are different conversion problems with different failure conditions.

NASA's product-realization guidance already treats implementation, integration, verification, validation, and transition as distinct work, and explicitly rejects relying on a reused product's previous qualification without checking the new application. Engineerperfect develops particular compositions and their consequences rather than claiming that this systems-engineering distinction is new. [NASA, Product Realization](https://www.nasa.gov/reference/5-0-product-realization/).

## Guaranteed composition preserves the joint conditions

Suppose one component supports output y in [0,10], and another accepts input y in [5,15]. Both can pass their own requirements while an actual y = 2 fails at the connection. The interface specification needs [0,10] ⊆ [5,15], which is false. Restricting A to [5,10], widening B to [0,15], or supplying a valid converter are different possible repairs.

A stronger component is not always the cheapest repair. If the system only needs one value, y = 7, configuring A accordingly can suffice. If all outputs must remain possible, that restriction changes the undertaking. The correct repair depends on the actual service demand and admitted operating conditions.

For interacting components, their errors can be correlated. A guarantee covering every combination of independently admitted parts uses the Cartesian product of their allowed ranges. Matched pairs can use a smaller joint set, but then a replacement part must preserve that matching relation. Qualifying one assembled pair does not establish interchangeability.

The [fit calculation](examples/shaft-and-hole-fit.md) carries this through to actual clearance intervals, revised manufacturing bounds, environmental drift, and measurement uncertainty.

## Timing and support are part of an interface

If A supplies a correct result after B's deadline, the content fits but the delivery does not. If B requires permission that A cannot grant, a correctly formatted instruction does not supply authority. If two components require the same exclusive resource at the same time, each can be individually feasible while their joint schedule is infeasible.

Consider two one-hour tasks, both required during the same one-hour interval and both requiring the same nonshareable machine. Their separate resource claims are valid; their composition requires two machine-hours of concurrent capacity where one exists. Changing the order alone cannot meet that interval. A second resource, a longer interval, a faster process, or a changed requirement is necessary.

This is the organizational form of an engineering interface failure. It is not resolved by clearer descriptions of the two tasks.

The disagreement between the two task descriptions should therefore remain visible until the demand or capacity changes. Making their language consistent cannot make their simultaneous claims jointly feasible. Likewise, competing explanations can be retained for comparison without asserting them together, and different people's valuations can disagree without either person's account of the physical events being false. Integration must preserve the kind of difference it is handling.

## Redundancy inherits common dependencies

Let success through route A require a ∧ c and success through B require b ∧ c. Combined success is (a ∧ c) ∨ (b ∧ c) = c ∧ (a ∨ b). The extra route tolerates failure of a or b individually. It does nothing when c fails.

Two pumps on the same unavailable power supply, two backups behind the same inaccessible account, or two workers blocked by the same missing authorization share this logical shape only when the stated dependency actually holds. Names and physical separation do not determine dependency independence.

No failure probabilities are needed for the Boolean conclusion. A probability estimate would require the appropriate joint distribution; multiplying advertised component reliabilities without that distribution adds an unsupported premise.

The same dependency matters in philosophical justification. Suppose one argument derives conclusion q from p together with a, and another derives q from p together with b. If both routes require p, listing both does not create a justification independent of p. Defeating p defeats these routes without proving q false; another route could establish q. The useful change is to inspect or replace the shared premise instead of counting the two arguments as independent protection. This transfer follows the stated logical dependencies rather than a resemblance between arguments and machines.

## A repair must reestablish the receiving conditions

Replacing a broken component with a working one restores the system only if the replacement meets the actual interface conditions. A revised file can fix its own content while leaving generated views stale. A repaired device can operate while using an incompatible connector. A new operator can possess skill while lacking access to the current records.

The receiving relationship determines which corrections must propagate. It is unnecessary to revalidate unrelated material merely because a change occurred. It is necessary to revisit the arguments that consumed the changed assumption, range, timing, or authority.

This makes organization part of engineering. A dependency record is useful when it identifies actual consumers and the conditions they rely on. A generic graph of related names leaves the propagation judgment unsupplied.
