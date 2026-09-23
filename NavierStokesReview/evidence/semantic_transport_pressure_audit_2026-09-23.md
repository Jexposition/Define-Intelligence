# Semantic transport and pressure-slice audit

Date: 2026-09-23  
Scope: selected OpenAI/Astra source tree in this worktree  
Method: source inspection plus zero-sorry Lean probe

## Executive finding

The current source supports a narrower adverse conclusion than “the proof is
formally contradicted”. The production mean-rank path is a three-coordinate
debt interface whose `FiveRows` statement fixes two correction moments to zero.
The repository also contains a separate exact five-coordinate positive-order
repair. A zero-sorry probe proves that the latter can reproduce the former
after the explicit embedding

```text
(P, Jθ, Jz) ↦ (0, 0, -P, -Jθ, -Jz).
```

What remains unproved is the load-bearing semantic transport: no named theorem
was found that identifies the paper’s `(M, I, J, S, C_p)` with this promoted
vector and then carries that identification into the selected endpoint’s
`StateRealization.chartIdentity` or `CandidateConsequences`. This is a
correspondence objection, not yet a kernel-level contradiction.

The pressure-support attack does not currently produce a trivialisation
theorem. In the R³ statement, `pressure_support` is only a containment of
each spatial slice’s topological support in a compact set. The statement does
not impose a pressure Poisson equation. The comparison pressure-recovery
modules derive gradient pairings from equal-residual hypotheses; they do not
instantiate the selected candidate or prove that compact pressure support
forces zero. The zero-sorry probe below proves the generic implication is
false by exhibiting the nonzero smooth compact cutoff already used by the
repository.

## Action A: debt and moment transport

### Production three-debt path

- `NavierStokes/FiveRowRank.lean:21-22` defines `Debt := Fin 3 → ℝ`, documented
  as `(P, Jθ, Jz)`.
- `NavierStokes/FiveRowRank.lean:241-246` defines `FiveRows`. Its first two
  equations are fixed zero correction moments:

  ```text
  ∫ R, R² * dv R = 0
  ∫ R, R * ga R = 0
  ```

  The final three equations consume all three coordinates of the debt.
- `NavierStokes/CorrectionState.lean:242-244` defines the actual state debt as
  the three defects `(pressureDefect, thetaDefect, axialDefect)`.
- `NavierStokes/CorrectionState.lean:449-458` proves the production rank model
  satisfies `FiveRowRank.FiveRows`; the first two rows are therefore
  constraints on the correction profiles, not two freely solved coordinates.

### Five-coordinate positive-order path

- `NavierStokes/PositiveOrderMoments.lean:21-23` independently defines
  `Debt := Fin 5 → ℝ`.
- `NavierStokes/PositiveOrderMoments.lean:77-85` defines five integrated
  moment densities and moments.
- `NavierStokes/PositiveOrderMoments.lean:192-228` proves exact five-row
  weighted moment identities for its repair profiles.
- `NavierStokes/PositiveOrderMoments.lean:913-956` constructs a parameterised
  exact repair from actual profile integrals.

### Formal probe result

`NavierStokesReview/src/probes/FiveRowPositiveOrderBridgeProbe.lean:22-51`
defines the explicit promotion and proves, with no `sorry`, that the positive
order repairs equal `FiveRowRank.gamma` and `FiveRowRank.deltaV`, with the five
weighted moments equal to the promoted debt. The probe compiles under
`leanprover/lean4:v4.34.0-rc2`.

Therefore the old claim “there is no five-row repair in the repository” is
withdrawn. The stronger remaining objection is:

> The source has an algebraic repair bridge, but the selected endpoint still
> needs a theorem showing that the paper’s named physical moments are exactly
> the promoted quantities used by the production state and that this equality
> survives the residual and endpoint constructions.

### StateRealization and CandidateConsequences

- `NavierStokes/PhysicalResidualJetBounds.lean:885-923` defines
  `StateRealization`. Its fields include operator matching, smoothness, a base
  equation, and velocity/pressure germs. No field is a theorem equating the
  paper’s five named moments with the promoted debt.
- `NavierStokes/PhysicalResidualJetBounds.lean:927-931` states
  `StateRealization.chartIdentity`.
- `NavierStokes/PhysicalResidualJetBounds.lean:932-961` shows the proof uses
  the local graph identity, smoothness, and germs to identify the Cartesian
  residual. It does not visibly invoke `PositiveOrderMoments.moments`.
- `NavierStokes/CandidateConsequences.lean:136-147` defines the downstream
  consequence bundle. It contains maximality, lifespan, Sobolev unboundedness,
  force nonzero, and force-jet decay. It does not contain a moment-realisation
  field.
- `NavierStokes/ActualCandidateAssembly.lean:1123-1144` assembles the selected
  witness through `CandidateProperties` and `CandidateConsequences`, while the
  selected aliases are defined at lines 1164-1175. The endpoint does not expose
  the five-profile moment vector in its public witness type.

### Status

`TRN-01` production three-debt footprint: **proved**.  
`TRN-02` five-coordinate repair exists: **proved**.  
`TRN-03` explicit algebraic promotion: **proved by zero-sorry probe**.  
`TRN-04` paper-moment transport into the selected endpoint: **not located**.  
`TRN-05` formal contradiction that the selected velocity loses 3D stress
coupling: **not proved**.

The admissible counter-paper claim is therefore a missing load-bearing bridge,
not “Lean proves a lower-dimensional fluid” unless a later probe derives that
fact from the selected endpoint’s actual fields.

## Action B: pressure support and recovery

### What `pressure_support` means

- `NavierStokes/R3/ProblemStatement.lean:92-109` defines the R³ candidate
  properties. `pressure_support` says only

  ```text
  ∀ t ∈ Ico 0 1,
    tsupport (fun x => p (t, x)) ⊆ K
  ```

  with `K` separately required compact by `support_compact`.
- This is a whole-space Euclidean formulation. It is not a torus type, and
  `HasCompactSupport` is not a type-level boundary condition forcing a slice
  to vanish.
- `NavierStokes/R3/ActualCandidate.lean:59-65` proves the localised pressure
  support inclusion, and line 108 supplies it to `CandidateProperties`.
- `NavierStokes/SpatialLocalization.lean:149-158` defines `cutPressure` as a
  smooth spatial cutoff multiplied by the pressure. The cutoff is not an
  indicator function.

### Pressure-recovery chain

- `NavierStokes/R3/PressureRecovery.lean:33-44` defines comparison hypotheses:
  smooth fields, divergence-free velocities, equal residuals, and uniform
  finite energy.
- `NavierStokes/R3/PressureRecovery.lean:407-414` proves `gradient_recovery`.
- `NavierStokes/R3/PressureRecovery.lean:419-438` packages the same result as
  `pressure_gradient_recovery`.
- `NavierStokes/R3/ActualPressureFlux.lean:28-45` proves integrability and a
  canonical Riesz-pairing representation for a pressure difference. Its only
  compact-support input is the test/cutoff function.
- `NavierStokes/PhysicalResidualJetBounds.lean:919-923` supplies a local
  `pressure_germ`, and `chartIdentity` uses it as part of a local residual
  reconstruction. This is not a global Poisson recovery theorem for the
  selected pressure slice.

### Trivialisation test

`NavierStokesReview/src/probes/SemanticTransportPressureProbe.lean:37-50`
proves, with no `sorry`, that compact support does not imply a scalar field is
zero. It uses the repository’s own `SpatialLocalization.spatialCutoff`, proves
its compact support, and evaluates it at the origin where it equals one. The
probe compiles under `leanprover/lean4:v4.34.0-rc2`.

Thus the proposed loop

```text
compact pressure support → pressure = 0 → velocity = 0
```

is not derivable from the declarations inspected. A valid adverse pressure
finding would need an additional selected-path theorem imposing the relevant
Poisson equation, pressure normalisation, and enough decay/integrability to
deduce zero. Those premises are not currently present in the candidate
property structure.

### Status

`PRS-03` domain separation R³ versus periodic lift: **proved**.  
`PRS-04` pressure support definition: **proved**.  
`PRS-05` recovery infrastructure: **proved as comparison infrastructure**.  
`PRS-06` selected pressure instantiation into recovery: **located through
`WholeSpaceUniqueness.candidate_unique_on_Icc` and
`classical_uniqueness_on_Icc`**.  
`PRS-07` compact-support trivialisation contradiction: **disproved as a generic
inference; selected-path contradiction remains open**.

## Evidence files

- `NavierStokesReview/src/probes/FiveRowPositiveOrderBridgeProbe.lean`
- `NavierStokesReview/src/probes/SemanticTransportPressureProbe.lean`
- `NavierStokesReview/results/pressure_recovery_infrastructure_probe_2026-09-23.txt`
- `NavierStokesReview/results/pressure_support_scan_2026-09-23.txt`

## Counter-paper wording supported by this audit

The strongest current objection is not that compact pressure support alone
forces a trivial field, nor that a three-coordinate debt is automatically
invalid. It is that the public paper’s five named moment system has not yet
been connected by a selected-path semantic theorem to the production rank debt,
the concrete physical fields, and the final residual endpoint. The repository
contains a real algebraic promotion and a real five-row repair module, but the
load-bearing correspondence remains an obligation to discharge.
