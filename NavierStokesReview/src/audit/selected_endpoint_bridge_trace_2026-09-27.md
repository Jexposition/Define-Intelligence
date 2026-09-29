# Selected-endpoint bridge trace

Date: 2026-09-27
Source root: `NavierStokes/` in the current checkout
Instrument: `selected_endpoint_source_census.py`
Status: source trace, not a formal contradiction

## Scope reconciliation

The instruments report different scopes and must not be merged:

| Instrument | Scope | Result |
|---|---|---:|
| Endpoint source census | `NavierStokes/` source root | 817 files, 429,297 lines, 35,430 declarations, 588 reachable modules |
| Repository module atlas | current repository inventory | 2,790 Lean files, 649,366 Lean lines, 50,191 declarations |
| Compiled source-joined map | elaborated selected closure | 572 source-joined modules |

The source census found seven lexical bridge candidates. A lexical hit means
that a declaration contains symbols from moment/profile and endpoint/rate
clusters. It does not mean the declaration transports a value-level observable.

## Candidate-by-candidate classification

| Declaration | Source span | What it actually supplies | Transport status |
|---|---|---|---|
| `ActualPhysicalStageBounds.initialDirect_rate` | `ActualPhysicalStageBounds.lean:595-601` | A `JetRate` estimate for `MB.family.angularField` | Rate estimate; not a five-observable equality |
| `ActualPhysicalStageBounds.background_from_representations` | `ActualPhysicalStageBounds.lean:726-748` and continuation | A finite-background `JetRate` assembled from initial/positive-stage representations | Rate assembly; not a selected radial observable |
| `GermCandidateAssembly.potentialSum_eq_base_germ` | `GermCandidateAssembly.lean:75-81` | Local eventual equality of a potential sum with the base germ under local-zero hypotheses | Germ identity; not a global moment identity |
| `InitializedPhysicalBackground.directIncrement_rate` | `InitializedPhysicalBackground.lean:93-103` | A native angular-field `JetRate` bound | Rate estimate; not total-field transport |
| `MixedAxisPreservation.origin_blowup_global` | `MixedAxisPreservation.lean:470-487` | Axis blow-up transfer from a base curl field to a mixed diagonal field | Blow-up transfer; no five-moment equality |
| `MixedCandidateAssembly.StageEstimates.exists_schedule` | `MixedCandidateAssembly.lean:67-91` | A scale schedule, smooth sums, and `VanishingJointJets` | Schedule/residual-limit construction; no radial moment payload |
| `MixedCandidateWitness.SelectedSchedule` | `MixedCandidateWitness.lean:25-31` | A proposition containing schedule growth, smooth sums, and vanishing residual jets | Witness schedule; no `(M,I,J,S,C_p)` field |

None of these declarations has an output that identifies the final
`ASum`/`BSum`/`PSum`-derived Cartesian field with the paper's five named
observables. This is a negative result for the searched declarations. It is
not an impossibility theorem saying that no such theorem could exist anywhere
outside the searched lexical set.

## Endpoint packaging facts

The current source route is:

```text
ActualCandidateAssembly.selected_witness
  -> ActualCandidateAssembly.witness
  -> GermCandidateAssembly.exists_candidate_witness_of_finite_stages
  -> MixedCandidateWitness.SelectedSchedule
  -> MixedCandidateAssembly.StageEstimates.exists_schedule
  -> smooth sums + VanishingJointJets + CandidateProperties
  -> R3 theorem endpoint
```

The packaging boundary is a proposition-valued definition, not a structure:

```lean
-- ActualCandidateAssembly.lean:1121
def Witness (...) : Prop :=
  ∃ a : ℕ → ℕ, ...
```

The selected endpoint is a theorem, not a definition:

```lean
-- ActualCandidateAssembly.lean:1177
theorem selected_witness : Witness ... := by
  exact witness selectedBudget selectedThreshold ...
```

The exact body contains the selected schedule, potential/direct/pressure
stage sums, away extensions, `CandidateProperties`, smooth forcing,
`CandidateConsequences`, the H3 endpoint limit, force jet decay, and boundary
limits. It contains no named equality of the form

```text
moments(selected Cartesian field) = (M, I, J, S, C_p)
```

and no field requiring `FiveRowRank.FiveRows` for the exported whole-space
candidate.

## Observable type correction

`DefectIncrementBounds.barMoment` is not definitionally the selected R3
velocity observable:

```lean
-- DefectIncrementBounds.lean:214-220
noncomputable def barMoment (k : ℕ)
    (f : ScalarField (Point P)) : ScalarField P :=
  CorrectionState.radialMoment k f

barMoment k f n p = ∫ r, r ^ k *
  PressureStream.torusAverage (f n) (r, p)
```

Here `Point P` is a `PressureStream.Lift`, and the integrand is a scalar
pressure-stream field. The final selected `VelocityField` therefore cannot be
passed to `barMoment` by type alone. A valid selected-field calculation needs
an explicit representation theorem mapping the Cartesian field to this scalar
pressure-stream domain, including the radial measure, auxiliary-torus
average, support, integrability, and axis totalisation.

## Interpretation

The source supports all of the following simultaneously:

1. Upstream moment, debt, rank, curl, localisation, schedule, and energy code
   is real and reachable.
2. The selected endpoint is not a disconnected empty wrapper: it consumes
   concrete stage data and constructs actual sums and candidate properties.
3. The searched endpoint declarations do not expose the required value-level
   transport theorem from the paper's five observables to the selected
   Cartesian field.
4. The absence of that theorem establishes a load-bearing correspondence
   failure, not a kernel-level `False`.
5. The CUDA commutator scan remains a separate profile-level diagnostic until
   the exact selected field and the scalar `barMoment` domain are bound.

The current calibrated status is therefore:

```text
CTR-005: NOT ESTABLISHED as paper-to-endpoint correspondence
Kernel contradiction: NOT PROVED
```

The next decisive operation is not another lexical search. It is a source-bound
finite-prefix evaluation of the actual selected `ASum`/`BSum`/`PSum` route,
followed by a limit theorem or a rigorously reproducible defect calculation.
