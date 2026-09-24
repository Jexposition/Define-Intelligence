# Official claim to Lean endpoint: transport matrix

Date: 2026-09-24  
Repository snapshot: local branch `review/cmi-first-navier-stokes-2026-09-22`  
Reference baseline: upstream review record `700e39d`

## Purpose

This document separates three propositions that have been repeatedly conflated:

1. the literal proposition exported by the Lean endpoint;
2. the mathematical construction described in OpenAI's paper; and
3. the central published claim that the construction has been established as a
   solution of the Clay problem.

The burden of establishing the central solution claim lies with the authors. A missing
transport theorem is therefore sufficient to withhold acceptance of the paper's
description, even when it is not yet a proof of `False` against the literal
Lean endpoint.

## Source anchors

| Source | Relevant statement | Local or published anchor |
| --- | --- | --- |
| Clay, Fefferman | The equations use a given externally applied force and alternatives (C) and (D) concern breakdown under admissible forcing. | `docs/navierstokes.pdf`, pp. 1, 3–4; [Clay PDF](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf) |
| OpenAI paper | Theorem 1.1 claims a smooth compactly supported force, rest initial data, bounded kinetic energy, unbounded velocity, and the C/D consequence. | OpenAI paper, Theorem 1.1, pp. 1–2; [paper PDF](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf) |
| OpenAI paper | The construction defines the force as the momentum residual of a chosen incompressible flow and then proves smooth residual extension. | OpenAI paper, discussion immediately following Theorem 1.1 and proof outline, pp. 3, 8–9 |
| OpenAI announcement | The public announcement describes the result as a resolution of alternatives (C) and (D). | [OpenAI announcement](https://openai.com/index/navier-stokes-solution/) |

## Claim-by-claim result

| Published or implied obligation | Lean location | What is actually established | Review classification |
| --- | --- | --- | --- |
| A selected velocity, pressure, force, and spatial support exist. | `NavierStokes/ActualCandidateAssembly.lean:1121-1151`, `1177-1185` | `Witness` supplies the three stage sums, away extensions, a force, `CandidateProperties`, smooth force, consequences, H3 blow-up, and endpoint force jets. `selected_candidate` exports only the `CandidateProperties` part. | Established for the literal exported proposition. |
| The whole-space candidate is smooth before the singular time. | `NavierStokes/R3/ProblemStatement.lean:92-107`; constructed through `ActualCandidateAssembly.witness`; packaged by `NavierStokes/R3/ActualCandidate.lean` | The endpoint requires `ContDiffOn` for velocity and pressure on the pre-singular domain and the selected construction supplies the required field data. | Established on the inspected selected path, subject to ordinary source review. |
| The force is globally smooth and has the required future-time support. | `NavierStokes/R3/ProblemStatement.lean:101-102`; `ActualCandidateAssembly.lean:1134-1139`; `CandidateFromLimits.lean` | The selected witness requires `ContDiff` of the force and `CompactPositiveTimeSupport`; the residual is used on the interior and extended at the endpoint. | Established as a formal endpoint predicate. It does not prove force independence from the candidate. |
| The initial velocity is zero. | `NavierStokes/R3/ProblemStatement.lean:103`; `ActualCandidateAssembly.selected_candidate` | This is an explicit field of `CandidateProperties`, not merely an informal claim. | Established. |
| The velocity is divergence-free before the singular time. | `NavierStokes/R3/ProblemStatement.lean:104-105`; `CandidateConsequences.mixed_exists_force_with_consequences` | The endpoint requires the divergence predicate. The mixed assembly obtains it from the curl construction plus the stated cut-potential divergence hypothesis. | Established as a formal endpoint predicate; the selected proof’s geometric transport remains a separate analytic reading question. |
| The Navier–Stokes residual equals the force before time one. | `NavierStokes/R3/ProblemStatement.lean:106-107`; `CandidateConsequences.lean:190-207` | `CandidateProperties.navier_stokes` is part of the exported endpoint. The residual is therefore not merely described; it is required by the theorem type. | Established as a formal endpoint predicate. |
| Kinetic energy remains uniformly bounded in the whole-space alternative. | `NavierStokes/R3/ProblemStatement.lean:108`; `NavierStokes/R3/CompactEnergy.lean`; `NavierStokes/R3/ComparatorR3Theorem.lean` | The R³ candidate carries `UniformFiniteEnergy (Ico 0 1)` and the comparator uses the compact candidate closure. | Established for the R³ endpoint as typed. |
| The velocity is unbounded at time one. | `NavierStokes/R3/ProblemStatement.lean:109`; `ActualCandidateAssembly.lean:1142-1144`; `R3/CandidateBreakdown.lean` | The selected witness includes an H³ blow-up limit, and the R³ wrapper supplies the corresponding speed consequence used in the breakdown theorem. | Established as a formal endpoint consequence. |
| No global smooth finite-energy solution exists for the same force and datum. | `NavierStokes/R3/CandidateBreakdown.lean:43-49`; `R3/WholeSpaceUniqueness.lean`; `R3/ComparatorR3Theorem.lean:21-35` | The contradiction is obtained from the candidate’s maximal-lifespan/breakdown theorem after viscosity normalization. | Established for the formal comparator proposition, assuming the inspected source theorems. |
| No global smooth periodic solution exists for the same force and datum. | `NavierStokes/PeriodicPaperTheorem.lean:64-73`; `NavierStokes/ComparatorTheorem.lean:25-51` | The periodic comparator derives option (D) from the periodic candidate and its speed blow-up. | Established for the formal comparator proposition. |
| The force is a “given, externally applied” datum in the causal sense used by the Clay statement. | No corresponding field in `CandidateProperties`, `Witness`, or `selected_candidate`; residual provenance is in `CandidateFromLimits.lean` and `ActualCandidateAssembly.lean` | The code proves existence of a smooth force satisfying the residual identity. It does not formalise independence of force from the selected solution or a forward solution operator. | Not established as part of the published solution claim. This is a provenance/correspondence objection, not a Lean contradiction to C/D. |
| The five published moments `(M, I, J, S, C_p)` are the moments of the selected final velocity/pressure fields. | `PositiveOrderMoments.lean:76-85`; `FiveProfileMoments.lean:473-489`; `ActualCandidateAssembly.lean:1090-1098`, `1121-1151` | The repository contains exact five-moment machinery and substantial upstream profile infrastructure. The exported `Witness` type does not state an equality between `physicalMoments` or `PositiveOrderMoments.moments` and the final mixed sums, residual, or force. | Load-bearing correspondence obligation not established. |
| The three-debt rank interface is the same five-moment system described in the paper. | `FiveRowRank.lean:240-246`; `NavierStokesReview/src/probes/FiveRowPositiveOrderBridgeProbe.lean:22-51` | `FiveRows` has two fixed zero correction rows and three debt coordinates. A zero-padded promotion `(0,0,-P,-Jθ,-Jz)` gives an exact local repair bridge. That bridge is constructive but is not, by itself, a theorem about the selected final field. | Direct identification is false; constrained local bridge is proved; selected-path transport remains open. |
| The exact five-moment identities survive every stage and enter the residual/force endpoint. | `PositiveOrderMoments.lean:251-284`, `913-960`; `ModulatedHistories.lean:941-1018`; `ModulatedCone.lean:1486-1498`; `ActualCandidateAssembly.lean:1090-1098` | Exact repair exists upstream, and repaired axis histories are restored with the physical moment identity. `StageEstimates` and `physicalData` feed the selected assembly, but no inspected theorem has the conclusion that those repaired histories equal the final selected mixed-field quantities used by `CandidateProperties`. | Local transport established; final selected-endpoint transport not established. This is the principal paper-to-code burden gap. |
| The pressure is an absolute global Poisson representative for the selected velocity. | `CandidateProperties` requires a pressure field and residual identity; `PressureRecovery` and `ActualPressureFlux` provide comparison identities under hypotheses. | The inspected chain supports relative pressure recovery and residual compatibility. The exported endpoint does not state an absolute Poisson equation or a selected-field theorem identifying `p` with a globally normalised pressure representative. | Not established as an additional paper-level semantic claim; compact support alone is not a contradiction. |
| The construction is robust under independent perturbation of the force or initial data. | Review-side theorems in `NavierStokesReview/src/extensions/CompactFixedForcePerturbation.lean` and `EndpointContractNonImplication.lean` | A fixed-force perturbation can be shown to create a nonzero residual defect. This demonstrates path dependence of the engineered trajectory. It does not refute an existential statement, which asks for one force and one candidate. | Valid robustness/provenance criticism; not a C/D disproof. |

## Formal review conclusion

The repository’s exported C/D-shaped endpoint is stronger than a mere type
placeholder: it explicitly contains smoothness, support, divergence, residual,
energy, and blow-up predicates. The current evidence therefore does not justify
the sentence “Lean proves `False` from the selected witness.”

The published solution claim nevertheless carries a larger burden than the endpoint
alone. The paper presents the five named moments as the mechanism that makes the
selected construction a physically valid Newtonian flow. The source contains
genuine local repair and axis-history restoration theorems, but the inspected
selected endpoint does not expose the theorem that transports those identities
into the final mixed fields and then into the residual/force theorem. Until that theorem is supplied, the
repository establishes a formal C/D-shaped proposition while leaving the
paper-to-code correspondence for its central five-moment mechanism unproved.

That is a failure to establish the public mathematical solution claim, not a claim that
the literal Lean proposition has already been refuted. The correct burden is on
the authors to provide the missing selected-path transport theorem and its
analytic interpretation. A reviewer need not construct a contradictory force or
prove that every admissible force is regular in order to withhold acceptance of
the published solution claim.

## Required closure theorem

For the paper’s mechanism to be formally established, a theorem should be
provided with the following shape, using the actual selected objects rather than
generic placeholders:

```lean
theorem selected_paper_moments_transport
    : PositiveOrderMoments.moments selectedIndex
        (selectedAxialHistory ...) (selectedAngularHistory ...)
        (selectedPressureProfile ...) =
      paperMomentTuple selectedPotentialStages selectedPressureStages
      ∧ fiveRowDebt_of_selected_state =
        promoted (selectedThreeDebt ...)
      ∧ selected_residual_force =
        navierStokesResidual selectedVelocity selectedPressure := by
  -- Required proof body: derive all three conjuncts from the selected
  -- construction. This specification is not an endpoint theorem.
```

The block is intentionally a specification of the missing obligation, not a
claim that it exists. It must not be added to the trusted endpoint with `sorry`.
