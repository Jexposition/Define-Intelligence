# Final peer-review verdict: OpenAI Navier–Stokes claim

Date: 2026-09-22  
Audited public source commit: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`  
Review branch: `review/cmi-first-navier-stokes-2026-09-22`

## Verdict

**YES for the forced CMI Alternative C/D theorem actually exported by Lean.**

**NO for the unforced A/B Navier–Stokes problem.**

The decisive binary record is now in
`NavierStokesReview/results/FINAL_BINARY_VERDICT_2026-09-23.md`.

### Required claim split

This headline “no” must not be read as saying that the Lean theorem fails.
The audited source does formally prove the forced CMI Alternative C/D-shaped
theorem. The direct binary classification is:

- **Yes**, for the forced CMI alternative actually exported by Lean: a smooth
  positive-time force and zero initial datum are constructed and every global
  smooth finite-energy solution with that same force is excluded.
- **No**, for the unforced claim that arbitrary three-dimensional Navier–Stokes
  data develop a singularity or that the unforced Millennium problem is solved.
- **Not yet certified**, for a complete human line-by-line verification of all
  analytic lemmas in the paper.

The force being defined from a residual is not itself a CMI failure. CMI
Alternatives C and D explicitly permit smooth external forcing.

The precise finding is:

> **Forced C/D theorem: proved. Unforced A/B theorem: not proved.**

The remaining burden is independent analytic and procedural replication, not a
discovered counterexample to the theorem. The audited source contains a
substantial formal construction and a kernel-checked theorem. Kernel acceptance
establishes that Lean checked the supplied formal premises and derivation; it
does not by itself settle CMI's publication and community-acceptance process.

## What is positively established

1. The audited Navier–Stokes and Euler headline declarations report only `propext`, `Classical.choice`, and `Quot.sound` under Lean 4.34.0-rc2. No `sorryAx`, native-evaluation axiom, or project-specific axiom was found in those reports.
2. The whole-space route elaborates with the CMI Alternative C existential and same-force negated-global-solution shape. The periodic route separately elaborates with the Alternative D periodic data, forcing, velocity, pressure, and energy structure.
3. The CMI statement explicitly permits smooth external forcing in Alternatives C and D. Therefore the fact that the construction defines a force from a residual is not, by itself, a CMI refutation.
4. The inspected bridge lanes contain explicit pressure recovery, pressure-flux comparison, viscosity scaling, compact-force decay, and the candidate-to-comparator map. No concrete type-level CMI mismatch was found there.
5. An independent Clay specification, Comparator-to-Clay bridge, and final
   adapter were compiled against the current source closure. The resulting C
   and D declarations report only `propext`, `Classical.choice`, and
   `Quot.sound`.

## Remaining peer-review work

The proof obligation is not merely to compile or to expose standard kernel axioms. The load-bearing analytic construction must be independently checked against the classical PDE claim. The following gates remain unclosed:

1. **Construction premise provenance:** every finite-stage estimate and certificate premise must be verified as a genuine analytic estimate, rather than accepted only through its Lean interface.
2. **Common domains:** every inverse, differentiated inverse, correction, and limiting operation must have a common nonempty domain that survives into the selected final witness. The generic `JetRate` API permits vacuous bottom-filter proofs; the selected endpoint is nontrivial, but every derived filter still requires its own proof.
3. **Residual closure:** the final force must be shown term-by-term to be the smooth, globally admissible residual of the classical Navier–Stokes equation, including nonlinear, pressure, support, mean, normalisation, and endpoint-extension terms.
4. **Whole-space comparison:** the pressure recovery, pressure-flux estimates, cutoffs, and energy/uniqueness closure must be independently verified with the exact regularity and integrability hypotheses used by the final contradiction.
5. **CMI convention:** the relative `ContDiffOn` and within-derivative convention on the nonnegative-time half-space must be proved equivalent to the CMI classical-solution convention, including the endpoint and `t = 0` clauses.

Until these gates are discharged, the repository is evidence of a kernel-checked formalisation, not an independently verified solution of the CMI problem.

## What would change the verdict

The five gates above remain useful for independent replication and paper review,
but they are no longer flip conditions for the theorem-level forced C/D
classification. A future discovery that a bottom or unverified derived filter
reaches the selected residual closure would provide a proof-relevant formal
defect.

The present audit found no such confirmed fatal counterexample. Accordingly,
the forced formal CMI-alternative interpretation is **proved at the Lean
theorem level**, while the unforced interpretation is **not proved**. CMI
procedural acceptance remains a separate institutional question.

For the unforced interpretation, this is the final no. For the forced formal
CMI-alternative interpretation, see
`NavierStokesReview/results/FINAL_CLAIM_CLASSIFICATION_2026-09-22.md`.

## Evidence

- Formal-trust and source-completion record: `NavierStokesReview/results/COMPLETION_AUDIT_2026-09-22.md`.
- CMI requirement matrix: `NavierStokesReview/results/CMI_SEMANTIC_MATRIX_2026-09-22.md`.
- Load-bearing semantic interfaces: `NavierStokesReview/results/SEMANTIC_LOAD_BEARING_AUDIT_2026-09-22.md`.
- Filter specification finding: `NavierStokesReview/results/DERIVED_FILTER_AUDIT_2026-09-22.md`.
- Kernel reports: `NavierStokesReview/results/HEADLINE_AXIOMS_4_34_RC2.txt` and `EULER_AXIOMS_4_34_RC2.txt`.
- Independent current-source semantic transcript:
  `NavierStokesReview/results/INDEPENDENT_CLAY_BRIDGE_CURRENT_2026-09-23.txt`.

The external target is Fefferman's official [Clay Mathematics Institute problem statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf). The claimed result and source are the [OpenAI announcement](https://openai.com/index/navier-stokes-solution/) and the [OpenAI repository](https://github.com/openai/NavierStokesAndEuler).
