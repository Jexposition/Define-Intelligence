# Priority-69 source review: annular endpoint, axis contraction, copy bounds, flux, reset, cone, and propagator

Date: 2026-09-28
Evidence class: direct source declarations and theorem signatures only.
Scope: nine reachable priority-69 modules in the OpenAI source tree.
Boundary: this report records what these files prove and do not prove. It does not infer a nonzero defect, an impossibility theorem, or `False` from the absence of a searched symbol.

## `NavierStokes/AnnularEndpoint.lean`

The file imports `PhysicalCopyBounds`, `SimilarityApproach`, and `TailGaugePotential` (lines 1-3). It defines the physical radius and shrinking outer support (lines 27-78), then packages support as `ShrinkingSupport` (lines 101-198). Theorems `ShrinkingSupport.tsum` and `ShrinkingSupport.potentialSum` (lines 175-198) establish closure of the support property under the indexed potential sum.

The copy-family support lemmas (lines 232-278) and extension lemmas (lines 294-395) establish common terminal neighbourhoods and one-sided extensions. The spatial-curl section proves that shrinking support is preserved by `SpatialCurl.spatialCurl` (lines 405-435). The diagonal theorem (lines 440-475) proves that the complete potential sum, pressure sum, velocity sum, and every iterated derivative vanish on one common neighbourhood near the terminal point. `diagonal_addition_germs` (lines 491-520) then proves eventual equality of the added potential, its Cartesian curl, pressure, and the concrete Navier--Stokes residual.

This is substantive support, germ, extension, and residual-localisation infrastructure. It does not define `barMoment`, a torus-average operator, a five-observable tuple, or a theorem transporting those observables through the `tsum` and curl construction. The source does not establish a nonzero moment defect either.

## `NavierStokes/AxisContraction.lean`

The module imports axis coefficient/evaluation/operator/resolvent layers and defines the `Controlled` contraction interface (lines 35-227). `NaturalOperators`, `AxisData`, and the natural linear/quadratic/pressure coefficient expressions are defined in lines 287-400. The file proves controlled remainder bounds, Lipschitz bounds, contraction thresholds, unique fixed points, and integrated fixed-point equations (lines 465-644). It closes with angular, axial, and mixed jet-error bounds and the coefficient transport results (lines 668-753).

These are reduced axis coefficient-space results. The declarations do not expose the selected whole-space Cartesian field, `ActualCandidateAssembly.Witness`, `barMoment`, or a field-level equality to `(M, I, J, S, C_p)`. They therefore cannot, by themselves, close the selected-field transport question.

## `NavierStokes/PhysicalCopyBounds.lean`

The file defines `CopyFamily`, its periodised copy and sum (lines 71-90), and the `RegularFamily` and `SupportCells` predicates (lines 92-105). It proves local copy selection and germ identities for periodised sums (lines 116-190), smoothness and local finiteness of the outer sums (lines 193-218), and native support-cell membership (lines 220-229). `LocalStrippedClass` begins the native local data contract (lines 231-240), while later declarations construct native support cells and derive scalar/vector jet bounds (lines 492-681).

This is a real periodisation and jet-control layer. It proves that, under support hypotheses, the periodised sum is locally represented by one copy and has controlled derivatives. It does not evaluate a radial integral, prove a torus-average identity, or state that copy/periodisation/`tsum` preserves the five paper observables.

## `NavierStokes/R3/LocalizedFluxEstimates.lean`

The module imports localized difference energy, weighted Sobolev, and comparison-cutoff layers (lines 1-3). Its declarations bound the nonlinear coupling, pressure, viscous, and cutoff-flux terms used by the whole-space localized comparison energy argument (lines 19 onward). These estimates support comparison/uniqueness analysis. They contain no selected-witness construction and no radial-moment, `barMoment`, or five-row transport statement.

## `NavierStokes/ResetEnergyBounds.lean`

The file imports angular-reset and tail-energy layers (lines 1-2). It defines reset density and reset energy (lines 45-116), proves support, smoothness, continuity, integrability, derivative bounds, and energy bounds (lines 62-268), then proves corrected-energy identities and normalized reset-energy regularity (lines 270-390). The scheduled small-energy existence results are at lines 420-450.

These are substantive intermediate tail/reset estimates. They are not a selected Cartesian field transport theorem. In particular, no theorem here identifies the reset's effect on `(M, I, J, S, C_p)` after global assembly.

## `NavierStokes/ScaledActualParticularControl.lean`

The module imports `ActualParticularControl` and `ActualSignedGeometry` (lines 1-2). It defines target domains, scale intervals, envelopes, frames, neighbourhoods, patches, and the derived scaled control (lines 21-139). It then defines source transport and actual target controls (lines 265-338), proves patch-envelope and coordinate/point-linear transport bounds (lines 364-403), and derives geometry, scale, slot-cost, and physical `Phi`/`Psi` estimates (lines 414-586). The later `actualSlotControl` construction and tangent equality occur at lines 603-650.

The source comment states that the forcing is the current target residual and that no source-naturality or supplied modal-control record is assumed (lines 5-12). This is relevant provenance evidence for the force-construction audit, but it is not by itself a CMI disproof. No selected-field five-moment equality or global radial observable theorem is declared here.

## `NavierStokes/TerminalCone.lean`

The file imports `HeatedOutgoing` and `TerminalEdgeFactor` (lines 1-2). It defines terminal clocks, normalisation, shifts, edge distances, release quantities, and small-tail predicates (lines 21-50), then proves radius, carrier, slope, speed, angular-stress, axial-stress, mass, and cone-margin properties (lines 53-465). The endpoint clock and vanishing axial profile statements occur at lines 477-566.

These are reduced-profile and cone-admissibility theorems. They show genuine profile control but do not establish that the final three-dimensional Cartesian `tsum` field preserves the paper's five cumulative radial quantities.

## `NavierStokes/ViscousPropagator.lean`

The file imports Gaussian-envelope, tangent-ODE, Hilbert-space calculus, and Gronwall layers (lines 1-7). It proves general norm/envelope estimates and a two-mode Euclidean-plane energy estimate (lines 25-353), high-harmonic and homogeneous propagator bounds (lines 353-389), and reference-viscosity/pulse estimates (lines 419-483).

This is analytic coefficient-energy infrastructure. It does not mention `barMoment`, `FiveRows`, `PositiveOrderMoments`, `CandidateProperties`, or `selected_witness`, and it does not provide selected-field moment transport.

## `NavierStokes/VolterraAnalyticBounds.lean`

The file imports complex Cauchy-integral, matrix, infinite-sum, boundedness, and `AnalyticCoefficientBounds` layers (lines 1-12). It defines six-component complex fields and coefficient matrices, radial inverses, matrix actions, Volterra words, derivative-shape/low-zero predicates, and the radial/analytic/matrix bound contracts (lines 23-200). It proves closure of those bounds under matrix action, radial inverse, parameter differentiation, and Volterra words (lines 208-373), then constructs factorial/exponential majorants and summable word layers (lines 384-598). The final theorem gives locally uniform convergence of the word-layer series (lines 587-598).

This is genuine analytic convergence machinery for a reduced slow-axis recursion. It provides series bounds in its own complex coefficient field, not a theorem about the selected three-dimensional Cartesian field, radial observables, torus averaging, or `barMoment`.

## Cross-file audit result

The nine modules are not empty shells. They add genuine support, periodisation, local jet, reduced-axis, tail-energy, cone, and coefficient-propagator mathematics. Their common boundary is also clear:

\[
\text{support/scale/profile/energy control}
\longrightarrow
\text{local germs, jets, and comparison estimates},
\]

not

\[
\text{final Cartesian field}
\longrightarrow
\operatorname{torusAverage}
\longrightarrow
\operatorname{barMoment}
\longrightarrow (M,I,J,S,C_p).
\]

This tranche therefore strengthens the evidence for a load-bearing endpoint correspondence question, but it does not prove that the transported moments are nonzero or impossible. The status remains `CTR-005: not established`, not `FORMALLY REFUTED`.

## Register action

The nine modules are entered as `evidence_inspected` in `semantic_coverage_register_full_2026-09-27.json`. The generated JSON, Markdown, and HTML registers, together with the review plan, workspace goal, architecture map, document control, correspondence map, research paper, and peer-review manuscript, must be regenerated or appended with the new count before this tranche is considered complete.
