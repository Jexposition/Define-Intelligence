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

The next transport identity is now compiled in
`SelectedCylindricalComponentTransport.lean`. On the valid positive-radius
chart, the first Cartesian component is the exact rotated combination of the
first two cylindrical components. This closes a local frame calculation only;
the torus-average, axis/support, and `barMoment` composition remain open.

Evidence: `NavierStokesReview/evidence/selected_cylindrical_component_transport_2026-09-25.md`.

The next source-checked step is the selected direct component formula. It
contains `cos(theta)`, the graph scale, and `swapCylinder`; these factors are
part of the field-level bridge and cannot be dropped when comparing the
Cartesian output with `barMoment`.

Evidence: `NavierStokesReview/evidence/selected_physical_component_transport_2026-09-25.md`.

The selected direct component now reaches the native scalar moment interface
on the positive radial section, and the exact order-two radial integral is
zero.  The remaining bridge is specifically the curled potential summand,
not the direct scalar branch.

Evidence: `NavierStokesReview/evidence/selected_direct_radial_moment_bridge_2026-09-25.md`.

The latest source trace confirms that the rank correction is used upstream in
`rankPotential`; it is not an orphaned module. The unresolved realization
boundary is later: the temporal-plus-rank stream is curled and exported as a
Cartesian field, while `barMoment` consumes a scalar torus average. The
selected equality between those representations is still absent.

Evidence: `NavierStokesReview/evidence/selected_stream_rank_moment_scope_2026-09-25.md`.

The first Cartesian component of the selected cut-stage commutator is
`(D₁χ)A₂ − (D₂χ)A₁`. The global bridge must account for this expression before
identifying the Cartesian field with the scalar radial input.

The production sampling map is now known to miss an explicit point in the
auxiliary square integrated by `torusAverage`. This sharpens the realization
boundary: the raw `ActualMeanPhysicalData.Scalar` family is global, while
`meanField` samples it through `physicalPoint`. A selected equality or selected
difference is still required.

Evidence: `NavierStokesReview/evidence/selected_torus_lift_image_scope_2026-09-25.md`.

The atlas selector adds a second, precise boundary. The completion
`SelectedAtlasPhysicalErasure.lean` proves that `Atlas.physical` depends only
on values at valid chart samples. This is selected interface evidence, not a
claim that the native family is nonunique in the admissible smooth class. The
remaining bridge must relate valid-sample agreement to the full-domain
`barMoment` integral.

## Selected production potential boundary

The selected completion
`NavierStokesReview/src/completions/SelectedPotentialProductionProductRule.lean`
now fixes the production-side input to the bridge. On valid unit-cube points,

$$
V_{\mathrm{prod}}=\chi\,\operatorname{curl}(A)
 +\operatorname{curlLinear}(D\chi\,A).
$$

The derivative-of-cutoff term must be included before any claim about the
radial profile or `barMoment`. The current source does not determine its
selected integral or sign. This record therefore marks the production identity
complete and the scalar transport calculation open.

## Selected positive-radial production component

`SelectedPotentialProductionRadialScalar.lean` now supplies the corresponding
selected potential-side component on the source radial section. Under the
selected physical-domain and unit-cube hypotheses,

$$
V_{\mathrm{prod},1}=\chi(\operatorname{curl}A)_1
 +\bigl(\operatorname{curlLinear}(D\chi\,A)\bigr)_1.
$$

This closes the local component transport and derives its differentiability
from the selected schedule. It does not close the scalar `barMoment` bridge:
the full lifted averaging domain, graph image, axis/support terms, and final
`tsum` remain unresolved. The commutator must therefore remain in the selected
calculation.

Evidence: `NavierStokesReview/evidence/selected_potential_production_radial_scalar_2026-09-25.md`.

## Typed production section for `barMoment`

The potential-production component is now lifted to a genuine scalar family
on `PressureStream.Lift PhysicalGraphBounds.Plane`, the point type accepted by
the source `barMoment`. The section map is explicit and agrees with the
physical point construction on the positive radial section. This closes a
type-level interface question, but not the realization theorem: the final
mixed Cartesian field, auxiliary torus average, boundary terms, and infinite
sum still have to be transported before the five-row invariant can be applied
to the endpoint.

Evidence: `NavierStokesReview/evidence/selected_potential_production_barmoment_section_2026-09-26.md`.

## Finite-prefix production closure

The finite selected potential is now expanded before the infinite limit. The
review-side theorem preserves the exact term

$$
\operatorname{curl}(\chi A_N)=
\chi\operatorname{curl}(A_N)+(\nabla\chi)\times A_N.
$$

It also supplies the scalar `barMoment` representative and its positive-radius
pullback. This advances the selected realization chain, but the weighted
integral and `tsum` passage remain unproved. No `Delta m != 0` or `False` is
inferred.

Evidence: `NavierStokesReview/evidence/selected_potential_production_finite_prefix_2026-09-26.md`.

## Finite-prefix torus-average gate

The finite-prefix scalar now passes through the exact source definitions of
`PressureStream.torusAverage` and `DefectIncrementBounds.barMoment`. The
auxiliary `Plane` coordinate is erased by `pointToCyl`, so both interval
integrals reduce to a single sample and the weighted radial integral is
exposed verbatim. This resolves a local representation question only. The
full mixed Cartesian `tsum`, boundary terms, and selected five-moment equality
remain unproved; no numerical remainder or `False` follows.

Evidence: `NavierStokesReview/evidence/selected_potential_production_torus_average_2026-09-26.md`.

## Finite-prefix endpoint bridge: 2026-09-26

The finite-cutoff endpoint is now transported through the source axis scale:
for every fixed prefix, the cutoffs are eventually one as `t → 1⁻` on the
axis. This sharpens the selected calculation but does not provide the missing
uniform prefix-to-`tsum` theorem, weighted value, or invariant conflict.

Evidence: `NavierStokesReview/evidence/selected_finite_cutoff_endpoint_2026-09-26.md`.

## Mixed field to `barMoment`: 2026-09-26

The actual mixed endpoint, rather than the potential-only surrogate, now has
an exact scalar-family pullback for `barMoment`. The bridge stops at the
weighted radial integral: the direct cut-and-periodised contribution, axis
terms, and endpoint interchange remain to be evaluated.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_barMoment_2026-09-26.md`.

The mixed branch split and exact torus-average reduction now expose the
remaining value-level gate: the cut direct contribution must be integrated.

Evidence: `NavierStokesReview/evidence/selected_mixed_production_torus_average_2026-09-26.md`.

The field-level gate now has a sharper form: the mixed radial pullback is
periodic, whereas bounded radial support would force it to zero. The missing
step is whether the source's radial moment hypotheses can legitimately be
transported to this periodised endpoint.

Evidence: `NavierStokesReview/evidence/selected_mixed_radial_periodicity_2026-09-26.md`.

## R3 packaging boundary: 2026-09-26

The review-side R3 completion proves a non-implication at the exported
candidate boundary: a nonzero `Fin 5 → ℝ` payload can coexist with the R3
`CandidateProperties` witness. The result confirms that the type does not
export the paper's five-moment transport, but it does not evaluate the actual
selected field. The unresolved field-level gate remains the periodic
`barMoment` calculation and its transport through compactification.

Evidence: `NavierStokesReview/evidence/selected_r3_packaging_boundary_2026-09-26.md`.

## Periodised-field support boundary: 2026-09-26

The selected field is not the compact cut field used before periodisation.
`cutPotential` has a compact support theorem, but `periodicVelocity` is a
lattice-periodic assembly. Since `barMoment` integrates over the full real
radial coordinate, the support-to-moment step is not definitional. The
review-side theorem that bounded radial support would force the periodic
pullback to vanish remains conditional on a selected support premise.

## Mapping provenance boundary: 2026-09-26

The current map records 3,021 tree file entries, 3,058 live files, 2,997
unique-basename resolutions, 24 retained ambiguities, and no missing
basenames. Exact compiled-to-source joins improve source navigation only. They
do not supply the field-level equality connecting the selected Cartesian
assembly, periodisation, summation, and `barMoment`.
