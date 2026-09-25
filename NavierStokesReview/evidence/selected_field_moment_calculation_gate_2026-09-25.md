# Selected-field moment calculation gate

## Question

Can the zero rows in `FiveRowRank.FiveRows` be combined with the concrete
field used by `ActualCandidateAssembly.selected_witness` to produce a nonzero
selected-field remainder and hence `False`?

## Source trace

| Layer | Source location | What is actually defined |
|---|---|---|
| Selected histories | `NavierStokes/ActualCandidateAssembly.lean:531-551,1165-1181` | The selected potential, direct, and pressure histories are raw `ℕ → VelocityField`/pressure histories supplied to `GermCandidateAssembly`. |
| Stage fields | `NavierStokes/ActualCandidateConstruction.lean:953-970` | The initial stage is a wave field plus `streamMeanStages`; a positive stage is `particular.field + signed.field + streamMeanStages`. |
| Mean stage family | `NavierStokes/ActualCandidateConstruction.lean:838-869` | `streamMeanStages` is recovered from `DirectAngularDiagonal.angularField` and indexed physical stage data. |
| Angular component | `NavierStokes/DirectAngularDiagonal.lean:65-71,198-214,231-237` | The direct field is a cylindrical angular field with explicit radius factors, smooth cutoff multiplication, and a locally finite `potentialSum`. |
| Cartesian potential | `NavierStokes/ActualMeanPotentialRealization.lean:29-40,300-316` | Meridional profiles are embedded into Cartesian components and passed through the spatial curl. |
| Finite cycle formula | `NavierStokes/ActualMeanPotentialRealization.lean:630-648` | A finite cycle state is seed plus a finite sum of temporal and rank meridional increments. |
| Infinite assembly | `NavierStokes/SolenoidalDiagonal.lean:31-75` | `potentialSum` is a `tsum` of cutoff stages; local positivity gives a finite local prefix. |
| Radial operator | `NavierStokes/DefectIncrementBounds.lean:214-220` | `barMoment` integrates a torus average of a scalar profile against `R^k`. |
| Correction invariant | `NavierStokes/FiveRowRank.lean:241-246`; `NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean:33-41` | The first two rows constrain correction profiles and the selected cycle state carries two local radial invariants. |

## Calculation result

The source gives enough structure to formulate the calculation, but not the
selected-field identity needed to evaluate it. In particular, the inspected
tree contains no theorem of the form

```text
barMoment k (selected Cartesian field) = selected five-moment expression
```

and no theorem transporting the cut-stage Cartesian `tsum` through the curl,
cylindrical projection, torus average, and radial integral. The existing
`barMoment_apply` theorem applies once a scalar `ScalarField (Point P)` is
already supplied; it does not perform that projection.

This matters for the proposed numeric leak. The derivatives of the spatial
cutoffs, axis terms from the cylindrical chart, and outer-support terms must
all be retained. The finite cycle recurrence alone cannot determine the
integral of the final `tsum`. Conversely, the absence of the transport
theorem is not itself a proof that the selected remainder is nonzero.

## Review classification

The active result is an affirmative burden-of-proof failure for the published
five-moment solution narrative: the selected-field composition theorem is not
exposed. It is not yet a kernel-level refutation of the literal C/D
existential. A `False` theorem requires a concrete selected equality together
with a proved nonzero value or an incompatible endpoint premise.

The calculator at
`NavierStokesReview/tools/radial_profile_integrals.py` remains useful for
checking explicit profiles after that transport identity is supplied. It is
not a substitute for the Lean proof.
