# Priority 134 source review: comparator admissions and Euler proof foundation

**Date:** 2026-09-28
**Scope:** `ComparatorChallenges/NavierStokes.lean`, `ComparatorChallenges/Euler.lean`, and `Euler/EulerProof.lean` in the current `Define-Intelligence-github` source tree.
**Purpose:** Separate repository metadata defects from the active Navier–Stokes endpoint and record what the external Euler foundation actually proves.

## Source identity

| Source | SHA-256 | Source-level anchors |
|---|---|---|
| `ComparatorChallenges/NavierStokes.lean` | `2f81f812237135d56db34771d218cb6e9df37775619f98692608950671e70381` | standalone header: 21–35; admitted bodies: 277, 284 |
| `ComparatorChallenges/Euler.lean` | `fc943d55794962ec2df62fefb316c4e3bf068c175247ef12747a03ee5dc179bb` | standalone header: 21–35; admitted bodies: 88, 184 |
| `Euler/EulerProof.lean` | `984e46e90aa982c4588b14929b0b7da19ca270b33fe6a77ee04ed85aeb29f5ad` | 20,755 lines; 91 imports; 1,202 declaration lines; no `sorry`, `admit`, `axiom`, `opaque`, `unsafe`, or `implemented_by` token match |

## Comparator challenge files

Both comparator files import only `Mathlib`. Their headers explicitly identify them as adapted standalone comparator references and state that their theorem proofs intentionally retain `sorry` challenge placeholders. The Navier–Stokes file defines generalized initial-data, force, smoothness, and breakdown predicates before the two admitted breakdown theorems:

```lean
-- ComparatorChallenges/NavierStokes.lean: 273–284
theorem navier_stokes_breakdown_R3 (nu : ℝ) (hnu : nu > 0) :
    ... := by
  sorry

theorem navier_stokes_breakdown_periodic (nu : ℝ) (hnu : nu > 0) :
    ... := by
  sorry
```

The exact conclusion bodies are intentionally not restated here with ellipses as if they were evidence for the active endpoint. Their significance is the admitted declaration at those source locations, together with the file's own scope statement that the reference is not imported by the proof root or submission.

```lean
-- ComparatorChallenges/NavierStokes.lean: 21–35
Standalone comparator ...
The ... breakdown alternatives (C) and (D)
are retained, including their intentional `sorry` challenge placeholders.
...
Neither the proof root nor the submission imports this reference.
```

The Euler comparator similarly defines unforced Euler smoothness and breakdown predicates, then contains:

```lean
-- ComparatorChallenges/Euler.lean: 85–88
theorem euler_breakdown_R3 :
    ... := by
  sorry
```

and:

```lean
-- ComparatorChallenges/Euler.lean: 170–184
theorem exists_compact_smooth_euler_singularity :
    ... := by
  sorry
```

These four bodies are a repository-scope admission/metadata finding. They do **not**, by themselves, establish contamination of `NavierStokesR3.theorem_1_1`; that requires an active import/dependency edge. The current register records zero missing project import edges for the captured endpoint closure, so the correct classification is:

> **Repository metadata defect; not active-endpoint contamination on the evidence currently captured.**

This is also why the files must not be described as “the whole repository” or as proof of a kernel contradiction in the exported Navier–Stokes endpoint.

## `Euler/EulerProof.lean`: what this tranche establishes

The file is a large, admitted-token-free analytic development. Its namespace and declaration structure includes smooth-limit, Sobolev, pressure, cutoff, cylinder, energy, packet, scale, and breakdown-criterion components. Representative source-level results include:

| Lines | Declaration | Exact scope established |
|---:|---|---|
| 12489–12523 | `EulerBreakdownCriterion.no_escape_near_compact_trajectory` | A compact-trajectory comparison prevents a norm sequence from escaping to infinity under stated convergence hypotheses. |
| 12526–12545 | `EulerBreakdownCriterion.no_gradient_escape_under_C1_comparison` | The preceding comparison is applied to Fréchet derivatives at the origin. |
| 12621 onward | `EulerSobolevBreakdown.no_gradient_escape_from_sobolev_energy` | A stated H³-type energy comparison rules out divergent origin gradients under explicit hypotheses. |
| 18240–18265 | `EulerPacketExistence.exists_solution_on_compact_interval`, `exists_global_solution` | Picard/ODE existence for a jointly continuous, uniformly state-Lipschitz vector field. This is not a three-dimensional Euler PDE theorem. |
| 18420–18473 | `equation30_exists_global`, `equation30_exists_growing_primary`, `equation30_exists_fundamental_system` | Constructed scalar equation-(30) solutions and associated estimates. |
| 18487 onward | `EulerPacketStage.controlled_stage_references` | A parameterised controlled-stage comparison theorem with explicit coefficient and derivative hypotheses. |
| 18934 onward | `EulerPacketTargetCompression.full_target_compression_negative` | A conditional quadratic target-ray compression inequality. |
| 20519–20745 | scale/source/activation theorems | Quantitative scale, summability, source, and activation bounds under their stated parameters. |

The comment at line 18487 says that a controlled scalar comparison solution is “constructed from the axioms rather than supplied as a hypothesis.” This is prose describing construction from preceding definitions and proved results; the file contains no Lean `axiom` declaration under the audited token search. It must not be paraphrased as an admitted axiom without source evidence.

## Boundary and audit classification

This tranche does **not** establish any of the following:

- a completed CMI Euler breakdown theorem;
- a proof that the Euler development is part of the selected Navier–Stokes endpoint;
- a final Cartesian selected-field equality for the five radial observables `(M, I, J, S, Cp)`;
- a non-zero cutoff/curl moment defect `Δm ≠ 0`;
- an impossibility theorem or a derivation of `False`.

It does establish two narrower findings:

1. Four intentional `sorry` bodies exist in standalone comparator files and therefore defeat an unrestricted repository-wide “zero-sorry” statement.
2. `Euler/EulerProof.lean` contains extensive, admitted-token-free Euler analytic and parameterised ODE infrastructure, but the reviewed declarations do not by themselves prove that the published Euler narrative is transported into the selected Navier–Stokes endpoint.

The live verdict therefore remains **correspondence not established**, not “formally refuted”, for this tranche. Further external Euler files require declaration-level review before any repository-wide Euler conclusion is possible.
