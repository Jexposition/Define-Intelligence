#   Bridge Audit
**Target Modules:** `ActualCandidateAssembly.lean`, `ActualCycleResidualBounds.lean`, `PhysicalResidualJetBounds.lean`

## Verification correction: absence of a direct moment import is not a PDE disproof

The source trace supports a real architectural question: the selected witness
uses native residual-jet bounds, while the public paper foregrounds named
five-moment identities. It does not support the stronger claim that the
residual chain contains no genuine 3D field. `TailGaugePotential` and
`AxisymmetricFields.potential` construct a three-component profile, and the
selected velocity is obtained through the spatial curl. The correct result is
therefore a missing selected-path moment-realisation theorem, not a fake-field
or lower-dimensionality theorem.

## 1.   Compiling Witness Interface Specification
**Target Exact Lines:** 
* `selected_witness` instantiation (`ActualCandidateAssembly.lean`, Line 1177)
* `Witness` type definition (`ActualCandidateAssembly.lean`, Line 1121)
* `estimates` instantiation (`ActualCandidateAssembly.lean`, Line 1090)
* `physicalData` type signature (`ActualCandidateAssembly.lean`, Line 1079)

**Analysis:**
The headline theorem unpacks `selected_witness`, which is instantiated by `witness B N0 hN`. The underlying `Witness` type explicitly consumes properties of `potentialSum`, `directStages`, and abstract `AwayExtensions`. To satisfy the bounds, `witness` passes `estimates`, which consumes `physicalData`. 
The exact type signature consumed is:
`∀ J, ActualCycleResidualBounds.PhysicalData B (ActualCandidateConstruction.residualBand B N0) (ActualCandidateConstruction.cycle B N0 J).state ...`
This unfolds to `PhysicalFields`, mapping straight back to `PhysicalResidualJetBounds.lean` and `CorrectionStep.lean`. The witness directly consumes geometric PDE residual decay bounds (`NativeBounds`). Upstream construction modules also contain moment/rank machinery, but the selected residual interface does not expose a theorem identifying those arrays with `(M, I, J, S, C_p)`.

## 2.   Ghost Moment Drift Severing
**Point of Divergence:** `PhysicalResidualJetBounds.lean` (Line 721 - `def residual`)
**Analysis:**
The PDE correctness is evaluated directly on the physical vector field using `residual u p` in `PhysicalResidualJetBounds.lean`. The compiler bounds the PDE by tracking spatial decay rates (`StateRealization.chartIdentity` and `residual_jetRate`). 
Because neither `FiveRowRank.lean` nor `PositiveOrderMoments.lean` is visibly
imported as a semantic identity by this residual-bounding module, the source
does not display how the paper's five named moments enter the selected bounds.
That supports a missing-transport objection. It does not prove that the
native residual estimates are false or that the moment modules are globally
dead code.

## 3. Human-readable review text
*(To be inserted into `OpenAI_NavierStokes_Peer_Review_v1.md` under 'Technical Discrepancies')*

**The Missing Selected-Endpoint Moment Transport**
The repository achieves a Lean 4 compilation with a boundary between the physical PDE evaluation and the algebraic moment constraints. The foundational modules, including the base profile (`TailGaugePotential`) and the residual bounds (`PhysicalResidualJetBounds`), contain three-component spatial evaluations. The theorem does not rely on the pure-axial or fake-two-dimensional premise; the underlying field construction is genuinely three-component.

However, a critical divergence occurs at the final assembly boundary (`ActualCandidateAssembly.selected_witness`). The proof evaluates PDE correctness through direct geometric jet decay bounds (`NativeBounds`). A closure census rooted at `ActualCandidateAssembly` reaches `FiveProfileMoments`, `FiveRowRank`, and `PositiveOrderMoments` through upstream construction modules, but the residual-realisation chain does not expose those five-coordinate arrays $(M, I, J, S, C_p)$ as semantic premises or prove their identification with the selected residual.

Consequently, while the repository's modules compile, the paper-to-code
correspondence is not established by the selected public interface. The
five-moment machinery exists upstream, but its transport into the final
theorem bounds is not exhibited. The review can require an explicit
moment-realisation theorem and its transport through the residual estimates.
The pressure comparison interface has the same shape limitation: it compares
pressure gradients under hypotheses but does not state an absolute selected
pressure-Poisson representative. Neither gap alone is a formal contradiction
until a selected-path premise is shown false.

The exact closure result is recorded in
`NavierStokesReview/evidence/selected_moment_transport_closure_2026-09-24.md`.

## Selected-cycle invariant refinement

The internal cycle does carry a local two-moment invariant. `Invariant` is a
`CycleAnalyticInvariant` with a `masses` field, and `state_invariant` propagates
it through the actual recurrence. This corrects any suggestion that the
production rank cycle has no mass-preservation theorem. The remaining bridge
question is whether those two radial mean identities are transported into the
mixed sums and identified with the paper's five named moments and the exported
residual/force endpoint.

Evidence: `NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean`.
The broad “orphaned moment specification” wording is withdrawn; the live
finding is a missing theorem at the selected mixed-sum boundary.

## Selected physical-data moment interface

The active bridge has the following source boundary:

| Source | Function in the selected path | Missing export |
|---|---|---|
| `ActualCycleResidualBounds.lean:1015-1037` | `PhysicalFields` record: smoothness, germs, exterior agreement | No five-coordinate debt field |
| `ActualCycleResidualBounds.lean:1142-1173` | `PhysicalData` abbreviation and residual jet-rate construction | No equality to `(M,I,J,S,C_p)` |
| `ActualCandidateAssembly.lean:1079-1098` | Constructs and consumes selected `physicalData` | No field-level moment identity |
| `ActualCandidateAssembly.lean:1121-1151` | Exports `Witness` | No selected mixed-field moment certificate |

`SelectedPhysicalDataMomentInterfaceProbe.lean` compiles a nonzero abstract
debt alongside the actual selected `PhysicalData`. This is a precise proof
that the exported interface does not determine the paper's five-moment
payload. It is not a proof that the concrete selected integrals are false;
that requires a separate identity for those integrals.

## Source-trace correction: active upstream five-moment construction

The closure rooted at `ActualCandidateAssembly` reaches the five-moment
machinery. `PositiveOrderMoments.rowDensity` and `moments`
(`PositiveOrderMoments.lean:76-85`) define the five radial quantities, while
`GlobalSlowProfiles.profiles_moments` (`GlobalSlowProfiles.lean:1043-1055`)
proves their vanishing for the slow-profile sequence. The result is then used
by `AssembledSlowBase.extended_axial_primitive_zero`
(`AssembledSlowBase.lean:592-617`). These are substantive upstream results,
not dead imports.

The unresolved point is the next transport step. The selected mixed fields are
assembled in `ActualCandidateAssembly.lean:515-523`, passed into
`potentialStages` at `531-534`, and exported through `Witness` at `1121-1151`.
No theorem in that selected export identifies the resulting velocity,
pressure, residual, or force with the paper tuple
$$
(M,I,J,S,C_p).
$$
Accordingly, the objection is a missing selected-field realisation theorem,
not a claim that the five upstream formulas do not exist.

Evidence: `NavierStokesReview/evidence/selected_moment_transport_source_trace_2026-09-25.md`.

## Selected-witness export test: 2026-09-25

The review extension
`SelectedEndpointMomentTransportObstruction.lean` now instantiates the actual
`selected_witness`. A nonzero five-coordinate debt can coexist with that
exported witness, and the witness does not entail that every such debt is
zero. This proves an interface non-implication at the final realization
boundary. It does not assert that the selected physical integrals are false.

The surviving bridge obligation is exact: identify the mixed selected fields
with the paper's five moments and transport that identity through the
residual, pressure, and force layers. Until that theorem is exported, the
paper's affirmative solution claim remains **NOT ESTABLISHED**.

Evidence: `NavierStokesReview/evidence/selected_endpoint_moment_transport_obstruction_2026-09-25.md`.

## Profile-tail collision route

The proposed upgrade to a kernel contradiction is now formalised in
`refutations.CTR005ProfileTailCollisionScope`. The source check confirms that
`FiveRows` constrains correction increments, not the total Cartesian endpoint;
`barMoment` is a radial/toroidal profile quantity. A nonzero runtime debt is
compatible with the two zero correction rows, while the selected cycle's local
zero-moment invariant is genuine.

The missing theorem is therefore a real field-level transport map from the
selected Cartesian sums to the radial history/profile inputs. No nonzero
selected remainder has yet been proved. This keeps the counter-paper precise:
CTR-005 is a publication-level failure of selected-field correspondence, not
yet a kernel-level contradiction.

Evidence: `NavierStokesReview/evidence/ctr005_profile_tail_collision_route_2026-09-25.md`.

## Calculation consequence

The bridge is now specified as a field-level calculation rather than an
abstract request. It must carry a selected Cartesian cut-stage `tsum` through
the spatial curl, cylindrical projection, torus average, and radial integral,
with all localisation derivative and boundary terms visible. Until that
theorem exists, the upstream zero-row invariant cannot be used to assert a
nonzero selected remainder or `False`.

## Selected scalar moment transport refinement

The selected cycle does expose more than an abstract invariant: the review
completion proves that the selected scalar mean state has zero `barMoment 2`
angular and zero `barMoment 1` axial values on the carrier at every stage.
Therefore the live bridge is not the existence of local scalar moment
preservation. It is the unproved identification of those scalar profiles with
the final Cartesian field after atlas scaling, angular-frame multiplication,
localisation, curl, torus averaging, and boundary evaluation.

Evidence: `NavierStokesReview/evidence/selected_scalar_barMoment_transport_2026-09-25.md`.

`SelectedRadialSectionComponent.lean` now supplies the positive-radius
coordinate recovery needed by this bridge. Its strict radius hypothesis is
source-mandated by the totalised angular frame; it is not a proof that the
full Cartesian endpoint preserves the scalar moment.

The selected axis branch is now explicit. At the radial axis, the first
component of each selected direct angular stage is zero by the source's
totalised angular frame. The missing bridge must therefore join this value to
the positive-radius identity and then to the full curl/localisation and
`barMoment` composition.

Evidence: `NavierStokesReview/evidence/selected_radial_axis_boundary_2026-09-25.md`.

The production bridge is now ordered explicitly. The selected velocity is the
curl of the cut potential sum plus a separate direct angular sum; periodic
localisation preserves that separation. The missing bridge must transport both
branches before comparing them with `barMoment`.

Evidence: `NavierStokesReview/evidence/selected_mixed_velocity_decomposition_2026-09-25.md`.
