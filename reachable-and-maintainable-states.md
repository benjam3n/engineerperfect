# Reachable and maintainable states

For a continuing purpose, reaching an acceptable state is insufficient if every available continuation destroys it. The engineering problem includes the route to the condition and the ability to remain within the required conditions afterward.

Use a finite set X of modeled states. At state x the controller selects an available action u. A nonempty successor set F(x,u) contains every outcome admitted after that action. Let S ⊆ X be the allowed operating states. An unavailable action has no entry; an available action never has an empty successor set. Otherwise a universal condition over an empty set could falsely certify an impossible action.

Define

\[
\operatorname{Pre}(K)=\{x\in S:\exists u,\ F(x,u)\subseteq K\}.
\]

This is a robust predecessor: the controller chooses u first, and every admitted successor must lie in K. Exchanging the order to “for every successor there is some suitable action” would give the controller information or influence it does not possess.

## Constructing the states that can be maintained

Start with K₀ = S and repeatedly remove states that cannot remain in the current set:

\[
K_{n+1}=K_n\cap\operatorname{Pre}(K_n).
\]

The sets decrease. With finite S, at most |S| strict decreases occur. At the fixed point K*, each retained state has an action whose every successor remains in K*. Selecting such an action at every step proves by induction that the trajectory stays in K* forever, under the modeled disturbances and continued availability of the actions.

Maximality also follows. Every set maintainable under the supplied full-state model is contained in K₀. If it is contained in K_n, its preserving actions keep its states in K_n, so it is contained in K_{n+1}. Thus every maintainable set lies in K*.

This is a construction and proof of the greatest maintainable subset. It is not a statistical estimate or a claim that the physical model is complete. The uncertainty-as-input and worst-case-control framing belongs to established control theory; the repository uses it with explicitly supplied finite dynamics. [MIT, Robust and Stochastic Control](https://underactuated.mit.edu/robust.html).

## Constructing arrival followed by maintenance

Let G ⊆ S be a desired operating region. First compute the greatest maintainable subset H of G. Then set A₀ = H and expand

\[
A_{n+1}=A_n\cup\operatorname{Pre}(A_n).
\]

A state's first inclusion index is its minimum worst-case number of steps to H. An action at a newly included state sends every possible successor to an earlier layer; the layer index strictly decreases until H is reached. Preserving actions then keep the state in H.

For a state outside the final set, every action permits a successor outside it. An adversarial choice can therefore avoid H indefinitely or force departure from S. This establishes the limit of the supplied actions and dynamics. Adding an actuator, altering the plant, changing the disturbance exposure, or changing the legitimate target defines a different problem.

The [implementation](tools/finite_control.py) returns every preserving or rank-decreasing action, not an unexplained “suitable mechanism” field. The [water calculation](examples/water-level-control.md) uses it to produce an explicit controller and a three-step worst-case arrival bound.

## Why maintenance resources belong in the state

If an action consumes a battery, a part, an operator's available time, or a repair allowance, treating that action as permanently available changes the modeled system. The apparent infinite guarantee then depends on an unmodeled replenishment process.

Add the relevant stock to the state. With battery b, action cost c(u), and replenishment r, the transition contains b' = b − c(u) + r and requires enough battery before the action. An invariant set in the augmented state must preserve both the service and sufficient support capacity. It can be empty when the service-only model's invariant set is large.

The [two-station service model](examples/service-during-repair.md) makes the difference explicit: wear accumulates with each job, and restoration requires labor. Without concurrent repair capacity no infinite service policy exists. With it, eight of the nine initial wear configurations support continuous service.

## When this formulation should be changed

A one-time construction may legitimately end on reaching a target. An ongoing operation needs maintenance. A task requiring repeated visits, an average throughput, bounded recovery after faults, or changing goals needs its own trajectory condition. The reach-and-stay routine does not solve those different specifications merely because each involves time.

Likewise, exact state observation is an assumption, not a property created by writing x in an equation. [Information and control](information-and-control.md) derives the additional condition needed when the controller receives only an observation.
