# Pressure-Moment Blindness Forensic Sweep
**Authority:** aligned to `REVIEW_DOCUMENT_CONTROL.md` 2026-09-24 and the machine-checked probe results.
**Scope rule:** no claim in this ledger exceeds "correspondence failure not yet converted into formal refutation" unless a zero-sorry contradiction is cited.

---

## 1. The Compiling Witness Interface Specification

### Target chain
`selected_witness` (Line 1177) → `witness` (Line 1153) → `GermCandidateAssembly.exists_candidate_witness_of_finite_stages` (Line 1155) ← consumes `estimates B N0 hN` (Line 1157).

### `estimates` definition (Line 1090)
```
noncomputable def estimates (B N0 : ℕ)
    (hN : ActualCarrierGeometry.geometricThreshold ≤ N0) :
    MixedCandidateAssembly.StageEstimates h (ActualCandidateConstruction.qbig B N0)
      (potentialStages B N0 hN) (directStages B N0 hN) (pressureStages B N0 hN) :=
  GluedStageEstimates.actualStageEstimates (runData B N0 hN) (meanCycleInput B N0 hN)
    ... (representations B N0 hN) (physicalData B N0 hN)
```

### `physicalData` type (Line 1079)
```
∀ J, ActualCycleResidualBounds.PhysicalData B
    (ActualCandidateConstruction.residualBand B N0)
    (ActualCandidateConstruction.cycle B N0 J).state
    (MixedDiagonalResidual.uncutVelocity (potentialStages …) (directStages …) J)
    (DiagonalJetBounds.uncutPrefix (pressureStages …) (J + 1))
```
This unfolds to `PhysicalFields B N …` (Line 1142 of `ActualCycleResidualBounds.lean`), which maps to `PhysicalResidualJetBounds.NativeBounds` and `StateRealization`.

### Finding
The `estimates` and `physicalData` fields do explicitly consume properties derived from `PhysicalResidualJetBounds.lean`. The path is real: `physicalData` → `PhysicalFields` → `PhysicalResidualJetBounds.NativeBounds` + `StateRealization.chartIdentity`.

However, this interface is a **geometric jet-decay contract**. The zero-sorry probe `StageEstimatesMomentBlindnessProbe` (CTR-039 in the tracker) proves that the generic `StageEstimates` record admits a zero-velocity, zero-pressure countermodel. The `StageEstimates` interface therefore does not by itself carry the paper's five named moments or blow-up.

The selected endpoint adds **additional** premises beyond `StageEstimates`: axis preservation (`haxis`), physical data, base-profile origin growth (`origin_blowup`), and the `VanishingJointJets` limit. Those additional premises are what prevent the zero-field countermodel from instantiating the selected theorem. This narrows the finding: the `StageEstimates` contract is genuinely blind, but the full `selected_witness` construction is not the same object as the generic interface.

**Status:** interface blindness confirmed by zero-sorry probe; selected-path refutation not established.

---

## 2. The Ghost Pressure Recovery Exploit

### Target chain
`PressureRecovery.Hypotheses` (Line 33 of `R3/PressureRecovery.lean`) → `gradient_recovery` (Line 407) → consumed by `ActualPressureFlux.pressure_flux_eq_canonical` (Line 38 of `R3/ActualPressureFlux.lean`) → consumed by `PressureFlux.exists_uniform_actual_pressure_flux_bound` → consumed by `WholeSpaceUniqueness.classical_uniqueness_on_Icc`.

### `PressureRecovery.Hypotheses` fields (Lines 33–44)
```
structure Hypotheses (T : ℝ) (u v : VelocityField) (p q : PressureField) : Prop where
  positive : 0 < T
  smooth_u : ContDiffOn ℝ ∞ u (Comparison.slab 0 T)
  smooth_v : ContDiffOn ℝ ∞ v (Comparison.slab 0 T)
  smooth_p : ContDiffOn ℝ ∞ p (Comparison.slab 0 T)
  smooth_q : ContDiffOn ℝ ∞ q (Comparison.slab 0 T)
  div_u : ∀ t ∈ Ioo 0 T, ∀ x, spatialDivergence u t x = 0
  div_v : ∀ t ∈ Ioo 0 T, ∀ x, spatialDivergence v t x = 0
  equation : ∀ t ∈ Ioo 0 T, ∀ x, navierStokesResidual u p t x = navierStokesResidual v q t x
  energy_u : UniformFiniteEnergy (Icc 0 T) u
  energy_v : UniformFiniteEnergy (Icc 0 T) v
```

### Finding
There is **no hidden parameter** that implicitly anchors the absolute pressure value to zero. The `Hypotheses` structure operates entirely on the *difference* `p - q`:

- `gradient_recovery` (Line 407) recovers `∫ ∂_k(p - q) · ψ`, not `∫ ∂_k p · ψ`.
- `pressure_flux_eq_canonical` (Line 38 of `ActualPressureFlux.lean`) evaluates `(p - q)(t,x) * fderiv χ x ((u-v)(t,x))`.

The zero-sorry `PressureRecoveryAbsolutePremiseProbe.lean` (CTR-039) already proves this limitation: identical zero velocities and any common smooth pressure satisfy `Hypotheses`. Consequently the comparison chain certifies pressure-*difference* identities but does not establish an absolute global Poisson representative for the selected pressure.

This is a **live, formally demonstrated interface limitation**, not yet a contradiction to `selected_witness`. The endpoint may supply stronger pressure information through `pressure_germ`, `StateRealization.base_equation`, and the residual-limit construction. Those links must be proved before the pressure chain can be closed.

**Status:** comparison limitation confirmed by zero-sorry probe; no hidden zero-anchoring parameter found; selected-path contradiction not established.

---

## 3. Unimported Module Graph Survey

### Direct imports of `PhysicalResidualJetBounds.lean`
```
import NavierStokes.PhysicalMeanJetBounds
import NavierStokes.PhysicalResidualTZ
import NavierStokes.UniformHarmonicInteraction
import NavierStokes.AnnularEndpoint
import NavierStokes.DiagonalResidual
import NavierStokes.ResidualPolarGraph
```

### `PositiveOrderMoments` presence
A direct search for `PositiveOrderMoments`, `FiveProfileMoments`, and `FiveRowRank` in `PhysicalResidualJetBounds.lean` returns **zero matches**. None of the three moment systems appears as an import, a type reference, or a symbol in the file.

### Transitive closure correction
The earlier claim of "total import separation" was too strong. `ActualCandidateAssembly.lean` does transitively reach `FiveProfileMoments` and `FiveRowRank` through `InitialPhysicalData` and `MeanRankUpdate`, and reaches `PositiveOrderMoments` through the physical-prefix/profile chain. The five-moment modules are therefore *present in the transitive closure* of the selected endpoint.

### The precise boundary
The moment systems are dropped from the *residual-evaluation* chain at the boundary between the cycle/state construction (which produces `PhysicalData` and `StateRealization`) and the native residual estimate (`PhysicalResidualJetBounds.NativeBounds` and `residual_jetRate`). The `StateRealization.chartIdentity` theorem (Line 927 of `PhysicalResidualJetBounds.lean`) connects the polar-chart lift to the actual velocity and pressure fields. It does not consume any `Debt`, `FiveRows`, or moment-identity premise.

The file boundary where the five-moment constraints stop being visible to the residual estimate is therefore:

> **`PhysicalResidualJetBounds.lean`**: the `StateRealization` structure and `residual_jetRate` theorem operate on native geometric jet bounds without any five-coordinate moment input.

This means the paper's five-moment narrative exists upstream and is algebraically compatible (per the `FiveRowPositiveOrderBridgeProbe`), but the native residual estimates that ultimately feed `StageEstimates` → `exists_schedule` → `VanishingJointJets` → `selected_witness` are computed without those moment coordinates as premises.

**Status:** transitive import existence confirmed; direct moment input to residual evaluation absent; selected-path five-moment transport remains the load-bearing open question (CTR-005).

---

## Summary alignment with authority map

| Prior claim | Correction status |
|---|---|
| "Total import separation" between moment systems and selected endpoint | **Corrected.** Transitive imports exist through `InitialPhysicalData`, `MeanRankUpdate`, and the physical-prefix chain. |
| "Fake 2D planar fluid / zero helicity" | **Rejected.** `AxisymmetricFields.potential` has three Cartesian components; the base-profile probe proves active 3D geometry. |
| "Hollow type inhabitation" | **Narrowed.** The existential witness is real and adds field-level premises beyond the generic interface, but the `Witness` type contains no five-moment payload (confirmed by `SelectedWitnessInhabitationProbe`). |
| The pressure chain "proves nothing about absolute pressure" | **Confirmed as interface limitation** by `PressureRecoveryAbsolutePremiseProbe`, but not yet a selected-path contradiction. |
| The residual bounds are "completely disconnected" from five-moment machinery | **Corrected to:** the residual bounds do not directly consume five-moment premises, but the five-moment machinery exists upstream in the transitive closure. The open question is semantic transport, not dead code. |

**Headline finding (unchanged):** CTR-005 remains load-bearing. The selected endpoint's residual and force construction does not expose a theorem transporting the paper's named `(M, I, J, S, C_p)` through `StateRealization`, `NativeBounds`, `VanishingJointJets`, and `selected_witness`. This is a formal correspondence failure not yet converted into a formal refutation.
