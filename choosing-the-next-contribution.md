# Choosing the next contribution

An inquiry can remove uncertainty while leaving the useful intervention no closer. It can also look useless in isolation while being indispensable to a cheaper complete route. Counting facts learned or demanding an immediate improvement from every step can therefore select the wrong work.

The construction here chooses among available inquiries and interventions in an explicit finite undertaking. It supplies the actual next operation, conditional continuations, minimum worst-case cost, and a witness when no available inquiry can resolve the obstruction. It finishes a choice that the earlier instruction to supply the missing contribution left open.

| Actual comparison | Determined consequence |
|---|---|
| Investigate a calculation's appearance or the contribution it lacks | [Repairing an unusable calculation](examples/repairing-an-unusable-calculation.md): the useful inquiry and repair cost 2 units; appearance first costs 3, despite revealing more information |
| Diagnose every detail or retain uncertainty that does not affect the repair | Complete case identification plus repair costs 3; a sufficient repair costs 2 and leaves four possible layouts unresolved |
| Investigate before every intervention or use an already justified correction | With the omission already known, the repair costs 1 and no new inquiry is selected; a sufficiently cheap common rebuild also makes inquiry unnecessary |
| Reject a question that does not immediately improve the available intervention or evaluate its continuation | [Correcting composed signs](examples/correcting-composed-signs.md): either observation alone gives a cost-5 route, but the pair enables a cost-3 route instead of a cost-4 reset |
| Accept the optimum of the current operations or construct a missing operation | Taking positive magnitude restores a stipulated positive source signal for cost 1 without either inquiry; the implementation checks its failure for a negative source |
| Treat the original case inventory as complete or let a new answer change it | A document missing both rule and input defeats the original two-defect division; the expanded construction supplies both and executes the repaired plan |

Costs in these examples are stipulated work units. They are not estimates of reading time, human effort, or benefit. The operations inspect and repair actual toy data structures; their outputs are checked against the declared calculations.

## A common adequate action settles feasibility, not the best use of resources

Let B be the nonempty set of cases still possible. Let R(a) contain exactly the admitted cases in which intervention a completes the stated undertaking. The intervention is justified across B when B ⊆ R(a).

That condition permits stopping inquiry. It does not always recommend stopping. A common rebuild can cost 4 while a one-unit inspection selects a one-unit repair. The additional information is unnecessary for the existence of a successful route but necessary for attaining the cheaper route in this example. The distinction corrects an overstatement in the earlier [information analysis](information-and-control.md).

Conversely, uncertainty is not itself a reason to keep investigating. If the missing rule is already known, distinctions among four layouts do not change the appropriate repair. Repeating the diagnosis spends resources without supplying a contribution the current undertaking lacks.

This relation belongs to established work. Mind Change Research already supplies common-action conditions, and Javdani and colleagues' [Near Optimal Bayesian Active Learning for Decision Making](https://proceedings.mlr.press/v33/javdani14.pdf) studies gathering enough information to select a suitable decision among overlapping regions of hypotheses. Its principal objective is expected test cost and it develops an approximation method. Here the implementation performs exact finite search for worst-case total inquiry and intervention cost. The contribution is this completed construction, its cases, and its use in the repository; decision-directed inquiry is not claimed as a new discovery.

## Constructing the complete route

An inquiry q costs c(q) and reports a deterministic answer o without changing the underlying case. Its answer leaves

\[
B_{q,o}=\{x\in B:q(x)=o\}.
\]

Interventions have costs c(a). All costs are nonnegative integers in one declared additive unit. Available operations and their costs do not change during inquiry; there are no hidden deadlines, permissions, side effects, or probabilities in this model. Previously established facts enter through B rather than being requested again.

Let V(B) be the least worst-case total cost of completing the undertaking. Then

\[
V(B)=\min\left\{
\min_{a:B\subseteq R(a)}c(a),\quad
\min_{q\text{ splitting }B}\left[c(q)+\max_{o:B_{q,o}\ne\varnothing}V(B_{q,o})\right]
\right\}.
\]

A minimum over no options is infinite. An inquiry splits B when at least two answers remain possible. A nonsplitting inquiry can be omitted because it adds no distinction and has no other effect under these assumptions. Every retained branch is a proper subset of B.

The equation is both a lower bound and a construction. Any successful plan either intervenes immediately or begins with an inquiry. An immediate intervention must work throughout B. An inquiry must leave a successful continuation for every admitted answer; the most costly branch determines its guarantee. No plan can cost less than the minimum of these alternatives. Selecting a minimizing alternative and recursively supplying its continuations attains the bound. Induction on the size of B establishes the result because every useful inquiry strictly reduces that size on every branch.

[choose_contribution.py](tools/choose_contribution.py) performs these operations, including the comparison with an immediate intervention. It retains a complete plan rather than returning a label that asks the recipient to invent the branches. Equal costs prefer an immediate intervention over further inquiry. Exact search can visit exponentially many subsets; minimal modeled intervention cost does not make the computation itself free.

The minimum is relative to the supplied cost and obligation. Worst-case cost can select a different plan from expected cost. Combining attention, delay, money, and other people's burdens into one number requires a justified conversion; the program does not silently provide one. An undertaking concerned with understanding or discovering a different question can have that as its contribution. There is no requirement that every useful mind change culminate in a physical repair.

## When no amount of available inquiry can resolve the obstruction

Group cases by their entire answer signature: two cases belong together when every available inquiry gives the same answer in both. A guaranteed plan exists exactly when each resulting nonempty group has one intervention that works for every case in that group.

Necessity: cases with the same full signature produce the same history under any adaptive inquiry plan. The plan therefore selects the same final intervention for them. If no intervention covers the whole group, at least one case fails.

Sufficiency: conduct the finite collection of inquiries needed to determine a full signature, then use the group's common intervention. This route may be costly, but it establishes existence. The optimization above removes unnecessary inquiry and selects the least costly complete route.

The code returns the obstructing groups when this condition fails. For example, a status reading that says only that a calculation is unusable cannot distinguish a missing rule from a missing input. If the only repairs each address exactly one omission, the two-case group has no common repair. Repeating the status inquiry cannot solve the problem. A new discriminating inspection, a repair covering both cases, or legitimate revision of the undertaking must change a premise. The calculation example supplies and executes the first two alternatives.

This separates three superficially similar situations: the relevant answer has not yet been obtained; every available answer still leaves incompatible interventions; and a common intervention is already justified. They require different next contributions. More investigation is not a universal remedy.

## A rule that requires immediate progress can prevent progress

In the sign example, either inspected flag alone leaves both preserving and reversing the sign possible. A one-question comparison therefore charges 1 for the question and still requires the 4-unit common reset. It rejects the question in favor of resetting immediately.

The two-question route costs 1 + 1 + 1 = 3 and restores the correct value in all four cases. Either first question becomes useful through what the second can establish. The immediate-progress rule rejects both possible first steps of this cheaper route.

The conclusion is stronger than the advice to be patient: local improvement is not a necessary property of each component of an improving sequence. It follows that a contribution cannot be dismissed solely because it does not yet change the final recommendation. Its relevant continuation can supply the missing connection. This does not vindicate arbitrary delay; the complete route and its advantage are constructed here.

The same case also prevents that conclusion from becoming another restrictive rule. Once taking positive magnitude is constructed and made available, the positive-source undertaking costs only 1 and needs no diagnostic sequence. The initially optimal inquiry was useful relative to the original operations, not a permanent requirement of the subject.

## An optimized plan can still inherit a defective account of the possibilities

The original calculation inventory admitted a missing rule or a missing input, with exactly one missing. A document missing both produces a third answer. The original plan refuses to choose a nonexistent branch. Treating the empty set of matching cases as proof that any repair works would turn model failure into false certainty.

The revision is completed in the example: admit the additional case, supply an intervention that installs the rule and loads the input, and regenerate the plan. The enlarged plan succeeds on all nine admitted documents with worst-case cost 3. The earlier cost-2 result remains correct for its earlier eight-case domain. It cannot establish the adequacy of that domain.

This is why the construction is an available operation within perspective development rather than its governing definition. The formation of the cases, interventions, relevant concern, and costs remains open to correction. The revised [contribution instructions](AGENTS.md), [information analysis](information-and-control.md), [capability analysis](engineering-capability.md), and [method critique](unoptimized-mind-change-methods.md) use these distinctions where the earlier work left the choice unsupplied.
