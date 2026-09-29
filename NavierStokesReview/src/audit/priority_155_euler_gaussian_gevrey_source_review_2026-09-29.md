# Priority 155 source review: Euler Gaussian and Gevrey support

## Scope

This tranche directly reviews twelve current Lean files in the Euler support tree. It follows the register queue after Priority 154 and is evidence for the repository map, not a claim that the reviewed files are the complete endpoint graph.

## What the files establish

`GaussianHeatTotal.lean` assembles finitely many line-heat operators into a cylinder heat operator. Its results cover contraction, semigroup and translation identities, continuity, commutation, and a one-derivative estimate. `GeneralCylinderAlgebra.lean` and `GeneralRealCylinderAlgebra.lean` provide fixed-order Sobolev multiplication at `q ≥ 6`, including complex, real, and scalar-vector products under smoothness and `MemLp` hypotheses.

The Gevrey files add a substantial auxiliary regularity layer:

| File group | Direct mathematical role | Endpoint relevance in this tranche |
|---|---|---|
| `GevreyBaseTransport.lean` | Expands base derivative words and bounds commutator forcing with the explicit factor `5461` | No selected-field or five-observable equality |
| `GevreyCompactProduct.lean` | Compact-support factorial derivative product bounds | No selected-field equality |
| `GevreyComposition*.lean` | Ordered-partition and Faà di Bruno Gevrey composition bounds, including L² variants | No Cartesian radial-moment transport |
| `GevreyContinuationNorm.lean` | Converts positive-radius Gevrey bounds into finite Sobolev bounds, optionally through coercivity | No CMI endpoint construction |
| `GevreyFamilyCompactness.lean` | Strong lower-order limit for a bounded viscous correction family | Requires explicit correction-family and divergence-free inputs; no selected witness |
| `GevreyFlow*.lean` | First-hitting bootstrap and finite flow-jet estimates under `B*R*T ≤ 1/8` | No Navier–Stokes selected endpoint |

## Important hypotheses

The estimates are not hypothesis-free. They require combinations of smoothness, pointwise factorial jet bounds, `MemLp` derivative bounds, measure preservation, coercivity, bounded coefficient maps, endpoint data, Duhamel equations, divergence-free subspace membership, Cauchy viscosity parameters, and smallness conditions. The source therefore records genuine conditional mathematics rather than treating a theorem name or successful compilation as a physical realization.

## Correspondence check

A targeted declaration and token scan of all twelve files found no occurrence of:

```text
selected_witness
CandidateProperties
barMoment
FiveRowRank
PositiveOrderMoments
NavierStokesR3
NativeBounds
```

The files also contain no direct equality identifying a final selected Cartesian field with `(M, I, J, S, C_p)`. This negative result is bounded to the twelve reviewed files. It neither proves that the entire repository lacks such a theorem nor changes the current classification of CTR-005 without an active-path closure search.

## Source hygiene

The directly reviewed files contain no `sorry`, `admit`, or `axiom` token. This records source text hygiene only; endpoint axiom status remains a separate dependency-closure question.

## Audit classification

The tranche is classified as **positive Euler/Gevrey infrastructure; selected-field transport not evidenced here**. It does not produce `False`, a non-zero cutoff defect, or a proof that any transformation destroys the five observables. The next audit action is to continue through the remaining queue and then test the declarations that actually feed the active endpoint closure.
