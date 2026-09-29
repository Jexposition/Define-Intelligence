# R3 analytical-module classification

Date: 2026-09-27
Scope: raw source review of the next 24 reachable modules in the semantic queue.
Register update: these modules are now recorded as `evidence_inspected`.

## Purpose

This tranche checks whether the R3 comparison, Fourier, heat-kernel, radial-kernel,
tensor, and signed-calculus modules contain a hidden theorem transporting the
paper-level five-moment data into `ActualCandidateAssembly.selected_witness`.

The test is deliberately narrow.  A module is not marked negative merely because
its filename is generic.  The conclusion below is limited to the declarations
actually inspected in the source files.

## Source findings

| Module | What the source establishes | Endpoint transport result |
|---|---|---|
| `R3/WholeSpaceUniqueness.lean` | `classical_uniqueness_on_Icc`, `candidate_unique_on_Icc`, and `candidate_global_agrees_before_one` compare solutions under the same force before `t = 1`. | Real endpoint comparison chain; no `barMoment`, `FiveRows`, or five-tuple transport. |
| `R3/HarmonicTestFunctionals.lean` | Harmonic functional representation and vanishing/compact-harmonic uniqueness. | No selected-field moment identity. |
| `R3/HeatKernelCommutator.lean` | Heat/Riesz commutator identities and paired bounds. | No evaluation of the selected Cartesian field. |
| `R3/HeatKernelFourier.lean` | Gaussian inverse-transform and heat-symbol integrability identities. | Analytical comparison layer only. |
| `R3/RadialKernelBounds.lean` | `radialCommutatorKernel`, scale, integrability, and Lp bounds. | Not the selected-field `barMoment` observable. |
| `R3/LocalizedTensorBounds.lean` | Localised tensor-difference and quadratic-cutoff bounds. | No five-moment equality. |
| `R3/WeakFourierUniqueness.lean` | Weak Fourier/test-functional uniqueness. | No selected-field moment transport. |
| `R3/TemporalTestUniqueness.lean` | Temporal uniqueness from test-integral identities. | No selected-field moment transport. |
| `SignedPhysicalSumCalculus.lean` | Finite-sum and real-coordinate identities for signed physical sums. | Algebraic assembly support only. |
| `SignedCrossDefectClass.lean` | Cross/residual defect-family membership and exponent bounds. | Intermediate defect classes, not endpoint observables. |

The remaining files in the tranche provide supporting comparison inequalities,
Schwartz approximation, Fourier weights, Lp tools, Hilbert extensions, heat-kernel
bounds, weighted interpolation, and R3 test infrastructure.  Their declarations
are analytic support results and contain no selected-witness five-moment equality.

## Controlled conclusion

This tranche strengthens the map in two directions:

1. The R3 comparison and uniqueness machinery is substantive.  It must not be
   described as an empty wrapper or as absent from the active endpoint route.
2. These modules do not close CTR-005.  They establish comparison, regularity,
   Fourier, kernel, and energy estimates, but do not prove

   \[
   \operatorname{Moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
   = (M,I,J,S,C_p)
   \]

   after the actual potential sums, curl/localisation, periodisation, and endpoint
   packaging.

This is not a proof that the concrete selected field has a nonzero defect.  It is
an evidence-backed classification of the inspected modules and keeps the remaining
reachable queue visible.

## Register accounting

The authoritative generated register is:

- `NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-27.json`
- `NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-27.md`
- `NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-27.html`

The mapping/control documents remain the human-readable interpretation layer:
`docs/LEAN_MODULE_EXPLANATIONS.md`, `docs/LEAN_DECLARATION_INDEX.md`,
`docs/REPOSITORY_ARCHITECTURE_MAP.md`, `docs/REPOSITORY_MODULE_ATLAS.md`,
`docs/REPOSITORY_ARCHITECTURE_ATLAS.md`, and `docs/SEMANTIC_CORRESPONDENCE_MAP.md`.
