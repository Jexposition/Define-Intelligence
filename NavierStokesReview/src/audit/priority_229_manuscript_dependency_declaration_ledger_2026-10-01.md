# Priority 229: manuscript-to-Lean declaration dependency ledger

Date: 2026-10-01
Status: source-checked; final selected-field observable edge remains open
Disposition: \`CTR-005: NOT ESTABLISHED\`

## Purpose

This ledger answers a narrower question than a lexical import scan:

> For each load-bearing mechanism in the manuscript, what exact Lean
> declaration consumes it, what hypotheses does that declaration require,
> what object does it return, and what further transformation is still needed
> before the result can be credited to the exported selected endpoint?

The ledger is deliberately directional. A theorem is not treated as an
endpoint bridge merely because its file imports a moment module or because
its output has a similar name.

## Manuscript-to-declaration ledger

| ID | Manuscript role | Exact Lean declaration and source | Required hypotheses/data | Output actually established | Next transformation required | Endpoint status |
|---|---|---|---|---|---|---|
| D1 | Reduced five-moment profile conditions and pressure datum | \`NominalProfile.FiveMomentCertificate\`, \`NominalProfile.Witness.five_moments\`; \`NominalProfile.lean:2079-2111,2536-2576\` | Reduced profile fields \`U\`, \`E\`, profile integrability, five profile integrals, pressure datum | Five identities for the reduced profile variables | Identify those reduced fields with the selected Cartesian cylindrical components and pressure convention | Profile-level only |
| D2 | Five-row correction system | \`FiveRowRank.FiveRows\`, \`FiveRowRank.exists_five_row_repair\`; \`FiveRowRank.lean:241-318\` | Base slices, measured defects, correction rows, compact-support and rank hypotheses | Two zero mass rows plus three defect-cancellation rows for a correction object | Instantiate the rows in the selected cycle and identify them with the manuscript observables | Upstream correction algebra |
| D3 | Actual rank-stage mass preservation and defect cancellation | \`DefectIncrementBounds.fiveRows_preserve_masses\`, \`RankGeometry.solved_rows\`; \`DefectIncrementBounds.lean:635-682,789-823\` | Shell support, slowness, positive operators, smooth base, actual rank increment, row hypotheses | Preservation of two \`barMoment\` masses and equality of three linear rows with negative measured defects | Pass from local \`barMoment\`/debt coordinates to the completed selected physical field | Positively consumed internally |
| D4 | Inductive correction-cycle state | \`CorrectionStep.CycleAnalyticInvariant\`, \`ActualCyclePreservation.state_runInvariant\`; \`CorrectionStep.lean:9408-9448\`, \`ActualCyclePreservation.lean:826-912\` | Actual cycle representations, wave data, correction rows, regularity and state-transition hypotheses | A state invariant carrying masses, debt, residual, representation, and regularity fields | Prove that these fields equal the paper’s named \`(M,I,J,S,C_p)\` after all selected-field transformations | Positively consumed internally; semantic equality open |
| D5 | Physical local field and pressure data | \`ActualCandidateAssembly.physicalData\`; \`ActualCandidateAssembly.lean:1079-1098\` | Geometric threshold, actual cycle state, uncut velocity, uncut pressure prefix, smooth stage data | \`ActualCycleResidualBounds.PhysicalData\` for every cycle index | Use the physical data to derive the residual estimates and then connect its observables to the paper’s definitions | Positively consumed internally |
| D6 | Residual jet-rate mechanism | \`ActualCycleResidualBounds.Invariant.residual_jetRate\`; \`ActualCycleResidualBounds.lean:1158-1173\` | Actual invariant, geometric and stage bounds, base-error equality, \`PhysicalData\`, exterior germs | A \`DiagonalResidual.JetRate\` for the actual residual | Show that this rate theorem is the transported consequence of the manuscript’s five observables, rather than only an invariant/rate contract | Residual consequence proved; paper identity open |
| D7 | All-cycle residual rates used by stage estimates | \`ActualCycleResidualBounds.finite_residual_rates\`; \`ActualCycleResidualBounds.lean:1190-1208\` | Invariant for every cycle, physical data for every cycle, actual velocity and pressure sequences | Residual jet rates for every cycle and derivative order | Identify the entire rate family with the selected manuscript construction after summation and localisation | Positively consumed internally |
| D8 | Selected stage-estimate construction | \`ActualStageEstimates.stageEstimates_of_representations\`; \`GluedStageEstimates.actualStageEstimates\`; \`ActualStageEstimates.lean:350-429\`, \`GluedStageEstimates.lean:684-755\` | Positive scale, residual order, geometry, physical-data family, actual invariant, representation bounds | Concrete \`StageEstimates\`, including finite residual rates and smoothness/loss data | Transport the paper’s named moment identities into the actual sums; generic stage estimates alone do not do this | Concrete, not free-standing; semantic edge open |
| D9 | Locally finite summation, flatness, and smooth-force extension | \`LocalResidualFlatness.exists_schedule_all_jetRates\`; \`MixedPeriodicAssembly.exists_candidate_force\`; \`CandidateFromLimits.force_smooth\`; \`LocalResidualFlatness.lean:88-141\`, \`MixedPeriodicAssembly.lean:330-365\` | Actual stage estimates, away extensions, smooth activated fields, divergence condition, vanishing joint residual jets, axis blow-up | Smooth force, residual boundary jets, candidate consequences, and speed blow-up for the constructed fields | Prove that the input jet-flatness and force extension are exactly the manuscript’s five-moment-corrected field, not merely a separately sufficient construction contract | Endpoint consequences proved; semantic origin open |
| D10 | Public selected endpoint | \`ActualCandidateAssembly.Witness\`, \`selected_witness\`, \`selected_candidate\`; \`ActualCandidateAssembly.lean:1121-1185\` | Selected schedule, actual potential/direct/pressure sums, away extensions, forcing, candidate properties, consequences, decay, boundary limits | Encoded candidate proposition and its CMI comparator projection | Add or derive a production theorem identifying the completed selected fields with the manuscript’s \`(M,I,J,S,C_p)\` observables | No final equality in the inspected production type |

## Missing edge stated precisely

The unclosed edge is not “moment code is absent”. It is the following
composition theorem:

\[
\begin{aligned}
&\operatorname{Moments}_{\mathrm{profile}}(U,E,\Pi)\\
&\qquad\Longrightarrow
\operatorname{Moments}_{\mathrm{paper}}
  \bigl(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}}\bigr)
  =(M,I,J,S,C_p),
\end{aligned}
\]

with the selected \`tsum\`, vector-potential curl, potential cutoffs,
periodisation, torus averaging, radial integration, pressure convention,
residual, and force extension all instantiated. The current production
declarations establish the left-side correction/rate route and the endpoint
consequences, but no inspected consumed declaration establishes this complete
right-side identity.

\`DefectIncrementBounds.barMoment_apply\` is a genuine lower-level weighted
radial integral (\`DefectIncrementBounds.lean:214-220\`). It is not, by itself,
the final selected-field observable theorem. Likewise, the review-side
abstract debt probes show interface non-entailment, not a physical nonzero
debt for the selected field.

## Adjudication

1. **Wholesale bypass:** rejected. D3-D9 positively show actual internal
   consumption of the repair and invariant machinery.
2. **Full manuscript transport:** not established. D1-D4 are not identified
   with the completed selected Cartesian/periodised/summed fields at D10.
3. **Concrete mismatch:** not proved. No value-level \`Delta m != 0\` theorem
   has been derived for the exact selected field.
4. **Kernel failure or compiler trick:** not found. The selected closure
   replay remains standard-axiom and no-sorry; the issue is specification
   correspondence, not kernel soundness.

The controlled conclusion remains:

> The repair engine is partially integrated and load-bearing inside the
> selected construction, but the manuscript-to-selected-endpoint semantic
> bridge for the five observables is not established.

## Source and evidence links

- \`priority_228_coupled_manuscript_lean_dependency_adjudication_2026-10-01.md\`
- \`priority_228_selected_transport_census_2026-10-01.md\`
- \`priority_203_internal_to_endpoint_crossfile_trace_2026-09-30.md\`
- \`priority_211_selected_transport_whole_tree_2026-09-30.md\`
- \`docs/navier-stokes openai.txt:470-735,1426-1588,2190-2347,2379-3065,4622-4915,5521-6240,6655-6990,8091-8530\`

