# Priority external tranche: Euler foundation source review

**Date:** 2026-09-28
**Scope:** repository-wide audit, outside the captured `NavierStokesR3.theorem_1_1` closure
**Status:** source-reviewed; not a claim that the whole Euler branch has been audited

## 1. Scope and terminology

The word *external* means only that these modules are outside the currently captured dependency closure rooted at the Navier–Stokes whole-space endpoint. It does **not** mean dead, unused, unreachable from every repository root, or mathematically invalid.

The root file `Euler.lean` contains one import, `Euler.EulerSingularity` (line 1). The inspected Euler modules import other `Euler.*` modules and Mathlib, and the source search found no direct `Euler` import from the inspected `NavierStokes` tree. This is a repository-root separation, not a correctness verdict.

## 2. Files inspected

The following source files were read directly, including their import headers, declarations, and proof/admission tokens:

| File | Lines | Imports | Declarations | `sorry`/`admit`/`axiom` token | Role read from source |
|---|---:|---:|---:|---:|---|
| `Euler.lean` | 1 | 1 | 0 | 0 | Euler entry point; imports `Euler.EulerSingularity`. |
| `Euler/AngleMeanZeroPrimitive.lean` | 101 | 3 | 11 | 0 | Periodic angular primitive, derivative, continuity, zero-mean normalisation, uniqueness. |
| `Euler/AnglePrimitiveBounds.lean` | 42 | 1 | 3 | 0 | Bounds for raw and normalised primitives. |
| `Euler/AnglePrimitiveKernel.lean` | 42 | 1 | 2 | 0 | Translation-kernel representation of the normalised primitive. |
| `Euler/AnglePrimitiveMap.lean` | 25 | 1 | 3 | 0 | Continuous-linear-map compatibility for primitives. |
| `Euler/AnglePrimitiveParity.lean` | 34 | 1 | 3 | 0 | Negation and reflection identities. |
| `Euler/AnglePrimitiveSpatialRegularity.lean` | 69 | 2 | 6 | 0 | Joint continuity and `ContDiff` for parameterised primitives. |
| `Euler/AnglePrimitiveTranslation.lean` | 26 | 1 | 2 | 0 | Translation identity for the primitive. |
| `Euler/AsymmetricTransport.lean` | 73 | 2 | 7 | 0 | Sobolev transport operator, formula, background equality, norm and application bounds. |
| `Euler/BaseEulerDatum.lean` | 103 | 3 | 19 | 0 | Compactly supported vector-potential curl datum, smoothness, support, divergence-free and plateau properties. |
| `Euler/BaseEulerLabelData.lean` | 82 | 2 | 7 | 0 | Label-cost construction and displacement/velocity/acceleration bounds. |
| `Euler/BaseEulerParity.lean` | 23 | 2 | 2 | 0 | Oddness propagation into parent input data. |

The counts above are source counts for this tranche, not repository-wide totals.

## 3. Declaration-level evidence

### 3.1 Angular primitive branch

`AngleMeanZeroPrimitive.lean:22-26` defines the raw integral and mean-subtracted primitive:

```lean
def rawPrimitive (f : ℝ → E) (θ : ℝ) : E := ∫ s in 0..θ, f s

def primitive (P : ℝ) (f : ℝ → E) (θ : ℝ) : E :=
  rawPrimitive f θ - P⁻¹ • (∫ s in 0..P, rawPrimitive f s)
```

The same file proves the derivative and continuity statements (`29-47`), periodicity under a zero-mean forcing hypothesis (`49-65`), exact zero integral over one period (`67-73`), and uniqueness among differentiable primitives with zero mean (`75-101`). These are actual theorem bodies, not comments or interface declarations.

The adjacent files extend that primitive with bounds (`AnglePrimitiveBounds.lean:14-32`), a translation-kernel formula (`AnglePrimitiveKernel.lean:14-25`), continuous-linear-map transport (`AnglePrimitiveMap.lean:14-21`), parity/reflection (`AnglePrimitiveParity.lean:14-31`), joint regularity (`AnglePrimitiveSpatialRegularity.lean:18-65`), and translation (`AnglePrimitiveTranslation.lean:13-23`).

**Audit classification:** genuine Euler angular-primitive infrastructure. No relation to the Navier–Stokes selected `ASum`/`BSum`/`PSum` boundary was found in this tranche.

### 3.2 Asymmetric transport branch

`AsymmetricTransport.lean:20-24` defines a Sobolev operator from an `H^s` and an `H^(s+1)` input. `27-34` expands it into the finite coordinate sum of scalar-times-derivative terms. `36-48` identifies it with the existing transport/background-drift expressions, and `50-68` proves application and operator-norm bounds.

**Audit classification:** genuine bounded transport estimates. The declarations expose Sobolev bounds, not the Navier–Stokes five-radial-moment observables and not a selected-field transport theorem.

### 3.3 Compact Euler datum branch

`BaseEulerDatum.lean:16-27` defines a cut-off linear potential and the velocity as its curl. The file then proves:

- potential smoothness and support (`19-25`);
- velocity smoothness and support (`29-34`);
- compact support (`36-38`);
- divergence-free curl identity (`40-41`);
- oddness (`43-46`);
- a trace-zero plateau identity and derivative identity on the inner ball (`48-64`);
- `SmoothL2Field` packaging and solenoidal membership (`66-77`).

This is direct evidence that the repository contains a real compact, solenoidal Euler datum construction. It does not prove that this datum is part of the Navier–Stokes endpoint, nor does it establish a five-moment equality for that endpoint.

### 3.4 Labels and parity

`BaseEulerLabelData.lean:16-40` defines a nonnegative label cost and proves `1 ≤ labelCost`. Lines `42-66` derive displacement, velocity, and acceleration label bounds from the corresponding field bounds. Lines `68-82` assemble these into `LabelData`.

`BaseEulerParity.lean:15-22` propagates an oddness hypothesis on the input field to the parent displacement data. This is a symmetry transport statement within the Euler parent/packet architecture, not a Navier–Stokes Cartesian-to-radial moment statement.

## 4. Root separation and endpoint relevance

The inspected source gives the following bounded conclusion:

1. `Euler.lean` is an independent repository root for an Euler branch.
2. The inspected Euler files are not evidence that the Navier–Stokes endpoint closure is complete or incomplete.
3. Their presence must be represented as a repository-wide branch, not labelled “dead” because it is outside the captured NS closure.
4. Their theorem content is substantive, but this tranche contains no declaration that transports the Navier–Stokes paper’s five observables `(M, I, J, S, C_p)` into `ActualCandidateAssembly.Witness`.
5. Absence of such a declaration in these 11 files is a local search result only. It is not a repository-wide absence theorem.

## 5. Remaining work for this branch

- Continue the Euler source queue from `Euler.EulerSingularity` and its imported foundations.
- Trace the separate Euler exported theorem(s), if any, and record their own packaging predicates.
- Inspect `ComparatorChallenges/Euler.lean` separately for admitted declarations; those files must not be conflated with the active Euler or Navier–Stokes endpoint.
- Add any Euler endpoint evidence to the repository-wide register only after direct source review.

**Current conclusion:** this tranche is source-reviewed and clean with respect to explicit admission-token search. It neither validates nor refutes the Euler manuscript as a whole and does not alter the current bounded Navier–Stokes finding.
