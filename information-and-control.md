# Information and control

The information an engineer needs depends on the interventions available and the condition to be preserved. Exact description of every state is unnecessary when several states admit the same adequate intervention. Conversely, a highly detailed record can omit the one distinction that changes the required action.

This changes what a useful contribution should supply. In the water undertaking, asking for a complete state description adds a prerequisite that the wide-band requirement does not need. The completed selection below identifies the sufficient distinction. In an inquiry whose question or criterion is still forming, discovering that question can be the missing contribution instead; the calculation does not prescribe how every inquiry must begin.

For a candidate maintained set K, let U_K(x) be the actions whose every possible successor remains in K. Suppose the controller receives only observation z = h(x) and chooses its action from z, without additional memory. One policy preserves all of K exactly when

\[
\forall z\in h(K),\quad
\bigcap_{x\in K:h(x)=z}U_K(x)\ne\varnothing.
\]

Necessity: all states producing z receive the same action, which must preserve each of them. Sufficiency: select an action from each nonempty intersection. Every transition stays in K, so the same argument applies indefinitely.

This applies Mind Change Research's existing common-action result to the preserving actions constructed from dynamics. The new step is the dependency on K and its future preservation. A one-step acceptable action can lead to a state that has no acceptable continuation; the maintained-set construction removes that mistake. The result is constructive in the supplied finite model through `observation_actions` in [finite_control.py](tools/finite_control.py).

## Sensing and actuation can substitute for each other within limits

Refining an observation splits an old observation class into smaller classes. If an adequate common action existed before, it still exists within each smaller class. Thus extra information cannot destroy the existence of a preserving memoryless policy when it can be ignored without cost, delay, or other changed conditions.

Adding an available action can also make an empty intersection nonempty. Altering the plant can change all the sets U_K(x). Reducing uncertainty at the source can remove troublesome states or successors. The missing intervention can therefore be supplied by measurement, a different actuator, structural design, or changed exposure.

These are alternatives with different costs. A common preserving action establishes that additional information is unnecessary for the existence of a preserving policy. It does not establish that additional information cannot reduce the cost of a justified intervention. The earlier claim that a cheap common action made more inquiry unjustified confused these two questions.

The [completed contribution choice](choosing-the-next-contribution.md) compares both possibilities. A common rebuild costs 4 in its calculation example, while inspecting the missing part and supplying that part costs 2. Once a common rebuild costing 1 is admitted instead, the planner stops inquiry and selects it directly. The adequacy condition survives; the optimal information choice changes with the available interventions and their costs.

In the [water model](examples/water-level-control.md), a low/high reading is enough to preserve levels 1 through 9. Full state measurement is unnecessary for that requirement. Keeping the narrower region 4 through 6 from any of its initial levels requires three different preserving actions. Under the stated memoryless observation policy, merging any two of those levels loses the guarantee. The same plant therefore needs different distinctions under different operating requirements.

## Information quantity does not determine its contribution

The amount learned also does not determine an observation's contribution. In the [calculation repair](examples/repairing-an-unusable-calculation.md), identifying layout reveals two bits under an explicit uniform comparison but leaves the needed repair unresolved. A one-bit inspection supplies the decisive distinction at the same cost. Conversely, the two observations in [sign composition](examples/correcting-composed-signs.md) each leave the repair unresolved alone but jointly enable it. A distinction's contribution can depend on a later distinction; immediate uncertainty reduction does not supply that dependency analysis.

## An observation is not automatically timely enough

If the controller observes x at time t but its action affects the plant only after delay d, then acting as if x were the current state can select an invalid action. A valid calculation must include every state that can arise during the delay, or include pending actions and observations in an augmented state.

For the water model, a previously measured level 4 followed by one unobserved demand interval can represent levels 2, 3, or 4 when no compensating action occurred. Applying the narrow-band action for level 4, namely +2, then permits level 2 on the next demand of 2. It does not preserve the claimed region 4 through 6. The defect is the use of a stale state at the action's decision time.

This counterexample fixes the inference now: a controller proved for immediate exact observation cannot be transferred to delayed observation unchanged. It does not claim that every delayed controller must fail. A controller using the possible current-state set may succeed, and that is a different synthesis problem.

## Memory can create additional usable distinctions

Two states with the same present observation can sometimes be distinguished by different observation histories. The intersection criterion above is exact for memoryless policies over the entire supplied K. Failure of that criterion does not prove impossibility for controllers that remember history or perform experiments.

A belief state can represent the remaining possible physical states. After action u and observation z', update it to all successors consistent with both. A policy over these sets can use information accumulated through interaction. Its action must work for all states in the current set; a convenient guess does not make the others disappear.

Autophilosophy2 already derives why a representation used through action must preserve distinctions exposed by action sequences. Here the receiving question is narrower and operational: which retained distinctions are sufficient to select actions that preserve the engineering requirement? The implementation currently answers the full-state and memoryless-maintenance cases. It does not advertise a hidden-state controller it has not constructed.
