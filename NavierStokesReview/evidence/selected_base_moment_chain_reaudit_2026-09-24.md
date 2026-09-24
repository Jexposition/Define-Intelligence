# Selected base moment-chain re-audit

## Question

Is the five-moment repair subsystem actually present in the construction, and
does its presence already prove that the final `selected_witness` realises the
paper's five named moments?

## Machine-checked result

`NavierStokesReview/src/probes/SelectedBaseMomentCompatibilityProbe.lean`
compiles with Lean 4.34.0-rc2 and contains no `sorry`.

It proves the following two facts.

1. For the actual `EntranceAlignedBase.modulatedScheme H v`,
   `GlobalStressSupport.moments_zero` supplies the exact
   `PositiveOrderMoments.moments = 0` identity for all positive orders and
   admissible parameters.
2. The actual profile selected by `FinalSlowBase.actualProfile` simultaneously
   exposes `FinalSlowBase.finiteIdentities` and
   `FinalSlowBase.speedUnbounded` for the constructed base velocity.

This corrects the earlier claim that the five-moment machinery was wholly
dead or disconnected. That claim is false.

## Source ledger

| Source | Live fact |
|---|---|
| `NavierStokes/GlobalStressSupport.lean:144-149` | `moments_zero` identifies the five positive-order rows of `axialHistory`, `angularHistory`, and `previousOmega` with zero. |
| `NavierStokes/GlobalStressSupport.lean:168-180` | `conservative_moments_zero` converts the repaired rows into actual radial stress/pressure-flux identities. |
| `NavierStokes/EntranceAlignedBase.lean:666-671` | `aligned_moments_zero` transports the identity into the aligned scheme. |
| `NavierStokes/EntranceAlignedBase.lean:690-697` | `aligned_finiteIdentities` derives the finite residual identities for the same aligned coefficients. |
| `NavierStokes/EntranceAlignedBase.lean:871-874` | `modulated_finiteIdentities` transports the finite identities through modulation. |
| `NavierStokes/FinalSlowBase.lean:107-109` | `FinalSlowBase.finiteIdentities` exports that result for the final slow profile. |
| `NavierStokes/GlobalSlowProfiles.lean:1043-1051` | The five-row profile identity is established for the infinite profile sequence. |
| `NavierStokes/AssembledSlowBase.lean:592-617` | The repaired rows are used to derive the zero mass primitive. |
| `NavierStokes/FinalSlowBase.lean:356-382` | The same constructed base supplies origin growth and `speedUnbounded`. |

## Remaining load-bearing gap

The live upstream chain proves a base/profile invariant. It does not, in the
inspected endpoint API, expose a theorem identifying the final mixed sums used
by `GermCandidateAssembly.exists_candidate_witness_of_finite_stages` with
`PositiveOrderMoments.moments`, `FiveRowRank.FiveRows`, or the paper's tuple
`(M,I,J,S,C_p)`.

The endpoint consumes generic `StageEstimates`, actual residual-rate data, and
local `PhysicalFields`/germ information. `MixedCandidateAssembly.StageEstimates`
has no moment field. `ActualCycleResidualBounds.PhysicalFields` has local
velocity and pressure germs plus exterior equalities, but no five-row equality.
The selected witness therefore has a real upstream moment construction, but the
source still does not display the required transport theorem from that base
invariant to the final mixed selected velocity, pressure, residual, and force.

This is a material paper-to-endpoint correspondence objection. It is not yet a
zero-sorry proof of `False` from `selected_witness`.

## Disposition

- Reject: “the five-moment branch is entirely dead code”.
- Retain: CTR-005, narrowed to missing selected-mixed-sum transport.
- Retain as open: deriving a concrete field-level moment violation or a
  contradiction with the selected origin residual limits.
