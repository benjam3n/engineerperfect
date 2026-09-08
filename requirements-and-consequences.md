# Requirements and consequences

An exactly satisfied specification can systematically produce the wrong result. Let W be the concern and R the acceptance rule. If an outcome x satisfies R and violates W, x is a counterexample to the sufficiency of R. The defect survives perfect execution of every operation whose only obligation is R.

Consider a service measured by the fraction of accepted jobs completed. A provider accepts one easy job, finishes it, and refuses nine eligible difficult jobs. Its completion rate is 100%; its coverage is 10%. If the concern is service to all ten eligible requests, the denominator has hidden nine failures. Rewriting the evaluation to preserve both eligibility and acceptance exposes the missing service. It does not itself supply capacity to serve the nine requests.

Two changes are therefore required in different places: preserve the actual demand in the judgment, and alter the service arrangement if more of that demand is to be met. Correct reporting is necessary to diagnose the gap but is not the engineering repair that closes it.

## A requirement can describe an outcome or impose a means

Suppose an inquiry requires a comprehensible account of the relation between two events. An additional rule permits only a fixed paragraph form. If the relationship requires a comparison that the form cannot express, the form has become a barrier to the original task. The additional rule must justify its exclusion of the needed expression.

The physical equivalent is prescribing a particular part when the actual concern is a temperature range. The part may be useful, obligatory for a legitimate reason, or merely inherited. A design using different material, passive geometry, a different location, or a changed operating schedule can serve the concern through a different mechanism.

For a fixed set of legitimate demands R, the feasible design set is the intersection of their satisfying sets. An empty intersection establishes an incompatibility within the admitted design space. It does not identify which demand is mistaken or prove that no wider design space can satisfy them. Those questions concern the basis of the demands and the scope of the space.

The [shaft-and-hole case](examples/shaft-and-hole-fit.md) finishes all of these determinations in its specified model: the nominal design interval is empty; the conflict is between allowable process variation and required clearance; tighter variation creates a precise nonempty interval; changing nominal diameter alone cannot do so.

## A stronger claim requires a different quantifier

| Claim | What it requires in an explicit model |
|---|---|
| There is an acceptable outcome | At least one admitted outcome satisfies the concern |
| This arrangement can succeed | At least one available course leads to an acceptable outcome |
| The controller can guarantee success | A policy succeeds for every disturbance admitted by the guarantee |
| The result is maintained | The requirement holds through the relevant later events, not only at arrival |
| Production is reproducible | The required production instances satisfy the claim under their admitted variation |
| This is the best design | The declared comparison establishes no superior member of the declared alternative set |
| This is completely perfected | Every demand and alternative relevant to that unrestricted claim is covered and satisfied or defeated by a sufficient argument |

Moving from one row to another without supplying its additional argument is unsupported. A successful demonstration proves existence in that demonstration. A finite exhaustive calculation can establish every modeled case. Neither move automatically covers unmodeled conditions.

## Unknown values still permit exact engineering conclusions

For a requirement y ≤ b and a model y = ax + e with a > 0 and e in [e_min,e_max], robustness requires ax + e_max ≤ b. Hence x ≤ (b-e_max)/a. No particular measured e is needed to derive that bound.

If a itself is positive and lies in [a_min,a_max], and x ≥ 0, the bound becomes x ≤ (b-e_max)/a_max. For negative x, the worst coefficient changes to a_min. Ignoring the sign would give the wrong robust design region. Missing numerical measurements leave a conditional region, not an instruction to derive it later.

If b represents an unchosen value judgment, the formula does not choose b. It identifies exactly which decision remains normative and which engineering calculation is complete.

## Narrowing a guarantee can reveal or conceal failure

Suppose a machine was sold for all inputs in E, but testing discovers failures in F ⊂ E. Reporting the guarantee on E minus F accurately states a weaker claim. It does not fulfill the original commitment on E. If there is a repair, its obligation survives the reclassification.

Conversely, excluding inputs that were never part of the actual undertaking is ordinary scope control. The relevant question is what the undertaking required, not whether every exclusion is illegitimate. Engineerperfect preserves the original demand next to the changed claim whenever a restriction matters.

This also applies to perfection itself. Calling a small proof complete can be correct. Calling the entire engineering ambition complete because that proof is complete changes the subject. The current repository supplies constructive results and keeps the remaining empirical and universal determinations explicit.
