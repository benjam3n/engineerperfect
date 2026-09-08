# What the verification establishes

The initial implementation was executed on 2026-09-08 with Python's standard library. The example runner produced the checked-in `computed-results.json`. The four unittest methods passed.

The main verification enumerates all 2,401 transition systems with two safe states, one failure state, two actions per safe state, and every nonempty possible-successor subset. For each system, an independent implementation enumerates all four stationary policies and explores their reachable graphs. It compares the resulting maintainable states with the fixed-point solver.

For each system and each of three targets—empty, one safe state, and both safe states—the independent implementation rejects reachable failure states, exits from a reached target, and reachable cycles outside the target. Otherwise it computes the longest pre-target path. The minimum over valid policies is compared with every rank returned by the arrival-and-maintenance solver. This supplies 7,203 target-system comparisons, including minimum worst-case step counts, rather than comparing the solver with a duplicate of its own recurrence.

Three further checks establish that an available action with an empty successor set is rejected, that a state with no available action is not deemed maintainable, and that pairwise common actions do not imply one action common to an entire observation class.

The water example directly checks every successor under the two-observation preserving policy, checks target preservation under the exact-state policy, and checks strict decrease of arrival rank outside the target. The service computation checks every transition of the selected policies. The fit calculation evaluates the eight independent extreme combinations of revised dimensional errors and environmental drift using exact rational arithmetic. Tooling costs are recomputed for demands 1 through 12; the all-demand threshold proof is in the example text.

These checks support the finite constructions and their implementation. They do not establish that a physical tank follows the stipulated dynamics, that a factory can attain the proposed tolerances, or that a real service has the assumed times and resources. Those empirical premises were not supplied or measured.

The proof of the fixed-point algorithm supplies its finite-model generalization. The enumerated family supplies implementation evidence and counterexamples to specific incorrect alternatives. Neither is a universal judgment of repository quality or a test for every possible placeholder in prose.

The semantic review checked that the central advertised operations have supplied transformations or calculations, that failed designs remain visible, that equations use their stated quantifiers, and that the repository comparison does not turn prior work into claimed novelty. This was an authored review, not an automated certificate of perfection.

## Integrated perspective and mind-change revision

The subsequent 2026-09-08 revision examined four SEBoK pages and one INCOSE-hosted invited presentation. The [source record](source-review.json) preserves page revisions, presentation date, passage locations, and the limits of attribution. The review distinguishes explicit source formulations, acknowledged qualifications, and the further inferences that fail. It does not infer field-wide absence from selected passages or treat an invited presentation as an institutional standard.

The new [perspective analysis](../unoptimized-perspectives.md) and [mind-change analysis](../unoptimized-mind-change-methods.md) use completed counterexamples and identified prior results. The agreement counterexample uses the existing service resource bound. The abstraction analysis preserves the distinction between exact answers and common adequate actions. The alternative-space argument distinguishes conflict within current options from unavoidable conflict. The philosophical dependency example distinguishes defeating two supplied arguments from proving their conclusion false.

The revision changes the working README, purpose, contribution instructions, existing subject arguments, and four example introductions. These are inspectable changes in the current contribution and its retained instructions. Neither their presence nor the source review demonstrates a reader's mind change, faster human performance, durable transfer, or superiority over all existing practice.

The example runner was executed again to check the numerical claims used in the new comparisons. It reproduced the existing computed results without a diff. The solver and its tests were unchanged; the exhaustive verification described above remains the initial implementation evidence. Local Markdown links and JSON syntax were checked, and the patch passed whitespace validation. Cost results are not presented as measurements of elapsed time.
