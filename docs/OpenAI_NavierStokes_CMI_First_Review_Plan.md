# CMI-First Counter-Paper Review Plan

*Research protocol. The tracker records execution; this document defines the method and escalation rules.*

## Objective

Write an evidence-based paper that tests the official OpenAI claim against the mathematical statement it purports to formalise. The goal is an honest disproof where the source permits one, not a compilation report and not a physical objection substituted for a theorem.

## CMI criteria used in this review

The relevant alternatives are the forced whole-space and periodic breakdown alternatives. The review therefore checks:

1. the exact domain, time interval, initial data, force class, decay, and smoothness;
2. the PDE, incompressibility, finite-energy, and blow-up clauses;
3. the comparison statement ruling out a same-force global finite-energy solution;
4. the proof that the constructed fields satisfy the published analytic construction; and
5. whether any required bridge is assumed, vacuous, or weaker than the paper's statement.

The CMI publication and review process is separate from the mathematical audit. This document focuses first on whether the claimed proof proves the claimed proposition.

## Claim hierarchy

| Level | Claim | Required result |
| --- | --- | --- |
| A | Lean accepts a term of the endpoint type. | Compilation and `#print axioms`. |
| B | The endpoint type has the C/D outer shape. | Source-level definition comparison. |
| C | The selected witness satisfies the paper's intermediate construction. | File-by-file dependency and correspondence proof. |
| D | The public paper's direct formal-verification claim is justified. | All load-bearing bridges must be present and valid. |
| E | The result proves spontaneous physical blow-up under altered constitutive laws. | Separate mathematics, not implied by C/D. |

The current evidence supports A and B, rejects the old “periodic toy” objection, and does not establish C or D as a faithful formalisation of the published construction. The zero-sorry moment probes supply a formal obstruction to direct coordinate identification, but `PositiveOrderMoments` supplies a genuine exact five-row repair and prevents the mismatch probe from being treated as a final refutation. The dependency axiom probe finds no custom axiom at the selected witness interfaces. E is outside the literal Newtonian endpoint.

## Falsification lanes

### Lane 1: moment correspondence

Compare the paper's `(M, I, J, S, C_p)` system with `FiveProfileMoments`, `PositiveOrderMoments`, and `FiveRowRank`. The first contains matching normalised vectors; the second proves exact five-coordinate repair in the recursive slow-profile layer; the third is a distinct physical rank interface. Trace `physical_five_rows`, `prescribed_five_rows`, `reserved_five_rows`, `exists_repaired_order`, `profiles_moments`, the `ModulatedHistories` consumers, and the selected witness. The direct-bridge probe rules out only a naïve row-by-row identification. The decisive test is now whether the repository states and proves the staging maps among all three systems.

The probe also rules out a full linear equivalence between the three-coordinate `FiveRowRank.Debt` and the five-coordinate `FiveProfileMoments.Debt`. The next correspondence test must therefore distinguish a constrained embedding or a deliberate stage separation from a claimed identity of the two debt spaces. The positive-order five-coordinate layer must be included before treating this as evidence against the endpoint.

### Lane 2: filter non-vacuity

Audit every `JetRate`, frequency-shell, germ, and limit obligation consumed by the selected candidate. Prove `NeBot` for each derived filter or prove that the target statement is independent of that filter. The existing generic `Filter.bot` probe is a warning, not yet a headline refutation.

### Lane 3: force specification

Verify smoothness, compact support, positive-time support, decay, and extension through time one. Separately record that the force is residual-defined and active through collapse. Do not treat force activity alone as a C/D violation.

### Lane 4: whole-space closure

Trace the pressure recovery, pressure flux, uniqueness, energy, and compact-support interfaces into `CandidateBreakdown`. The imported-rate-bound suspicion has now been checked and withdrawn: `WholeSpaceComparisonClosure` constructs the scalar rate bound internally, while `WholeSpaceUniqueness` constructs the pressure-flux constant from its comparison hypotheses. Continue by testing the mathematical validity and exact hypotheses of those derivations, not by treating the rate bound as an external premise.

### Lane 5: discarded objections

Keep non-Newtonian regularisation, hypo-dissipation, and physical autonomy as robustness questions. They become formal refutations only if the official endpoint claims those stronger properties.

## Lean work rule

Write the smallest zero-sorry probe that tests a load-bearing statement. Do not add code merely to restate a suspicion. Every probe must record its import path, theorem name, exit status, and whether it attacks the endpoint, an interface, or only a semantic interpretation. The completed direct-bridge probe attacks an interface; the selected dependency probe audits kernel assumptions without treating standard axioms as a defect.

## Deliverables

- the coherent paper in `OpenAI_NavierStokes_Research_Paper.md`;
- the adverse referee report in `OpenAI_NavierStokes_Peer_Review_v1.md`;
- the axiom and premise ledger in `OpenAI_NavierStokes_Axiom_Ledger.md`;
- this plan as the review protocol;
- a tracker containing only evidence-backed status changes; and
- independent Lean probes under `NavierStokesReview/src/probes`.

## Escalation rule

The counter-paper may state that OpenAI's stronger claim of faithful formalisation is not established when a required bridge is absent or a selected-path premise is false. It may state “formal disproof” only after a zero-sorry Lean theorem proves the contradiction or a false premise is shown to be mandatory. A physical objection, a missing regularisation, active forcing, or a generic filter hazard must remain in its own category until it reaches the C/D endpoint.

## Current protocol position

The plan now has two live proof-bearing lanes and three closed or bounded lanes.

1. The force lane has a concrete endpoint consequence: every candidate has nonzero force at some `0 < t < 1`. `ForceActivityProbe.lean` now compiles cleanly, and the result is recorded as active forcing rather than autonomous blow-up.
2. The moment lane has a zero-sorry direct-correspondence obstruction, but `PositiveOrderMoments` proves an exact five-coordinate repair internally. The required action is to search for the missing change-of-variables or staging theorem before escalating the finding.
3. The physical-rank predicate was inspected at declaration level. `FiveRowsStructureProbe.lean` confirms three debt coordinates plus two fixed zero rows, so the review must not call it a generic five-by-five inversion. The next test is whether the fixed rows and the three debt rows jointly preserve the paper's five named moments along the selected witness.
4. The periodic-endpoint absence objection is closed because `PeriodicPaperTheorem.lean` exports the D-shaped endpoint.
5. The pressure and energy objection remains an interface audit, not a proved failure. The `Filter.bot` issue remains a generic vacuity hazard until a bottom filter is shown to feed a mandatory endpoint premise.

6. The whole-space provenance objection is closed at source level. `R3/Theorem.lean` extracts the candidate from `ActualCandidateAssembly.selected_witness`, and the R³ localisation, energy, and viscosity-scaling modules carry that witness to the exported endpoint. This removes an attractive but unsupported claim that the endpoint is a disconnected wrapper.

7. The comparison-premise audit corrected the earlier interface criticism. The scalar rate bound is constructed internally by `WholeSpaceComparisonClosure` and recorded by the compiled zero-sorry `R3ComparisonPremiseProbe.lean`; the pressure-flux constant is also derived inside the uniqueness chain. Pressure recovery and localised PDE estimates remain load-bearing analytic targets, but the obsolete “unproved imported rate bound” formulation is closed.

The next falsification threshold is therefore explicit: a selected-path theorem must contradict one required CMI predicate, or the source must expose a mandatory interface whose assumptions cannot be proved. Until then the paper reports a failure of demonstrated correspondence, not a fabricated theorem refutation.

The empty-index branch audit has been added to the reachability lane. `ActualParticularStageControls.raw_jets` uses a valid `Nonempty (ActivePair)` split: the empty branch proves the control patch empty from its own membership predicate, while the nonempty branch uses an explicit countable surjection. The next test is not to label this `False.elim`, but to determine whether the selected endpoint depends on an inhabited active subtype and whether that subtype is proved inhabited. Without that dependency, the branch is not a refutation.

The moment lane now has a source-map test in addition to the type-level probes. `MeanRankUpdate.lean` imports `FiveProfileMoments.lean` but defines its operative interface entirely through `FiveRowRank`; an import-only edge is not a bridge. The next correspondence search must locate a theorem that explicitly transports the five paper moments into the three-debt physical rank update. If no such theorem reaches `selected_witness`, this supports a formal correspondence failure, not merely a stylistic complaint.

Use “formal disproof” only after a zero-sorry contradiction or a false mandatory premise has been proved. Use “formal correspondence failure” when the code and paper are not connected by a required theorem. Do not escalate a semantic criticism into a theorem-level verdict.

### Pressure and uniqueness

The pressure/uniqueness chain has now been inspected beyond its exported theorem names. The temporal recovery theorem uses compact temporal tests and continuity to obtain interior-time equality. The spatial step uses an explicit Fourier Sobolev bound and a weighted `L²` representative to eliminate compactly harmonic functionals. The comparison closure constructs its scalar rate bound internally, while the pressure-flux constant is constructed from the pressure-recovery hypotheses.

This lane does not presently yield a formal disproof. Its status is “analytically load-bearing, no checked contradiction”. The review must not describe the rate bound as an imported premise or describe the pressure route as absent. The decisive remaining routes are the cross-layer moment bridge, a selected-path filter-collapse proof, or a concrete false identity in the pressure/energy estimates.

### Fixed moment rows

The preserved-mass lane was tested against the selected witness and closed as a route to contradiction. The initial state is explicitly tagged with `ActualInitialization.initial_zeroMasses`, and the temporal and rank corrections preserve that invariant. `MomentInitializationProbe.lean` compiles the relevant theorem with no added assumptions.

The next decisive moment test is therefore not whether the fixed rows start at zero. It is whether the source proves a cross-layer map from those rows and the three debt coordinates to the five published quantities `(M, I, J, S, C_p)`, and whether that map is preserved through the selected construction.

### Source-scope correction

The zero-sorry test must be scoped to the exported proof path. Direct compilation of `ComparatorChallenges/NavierStokes.lean` emits two `sorry` warnings, but `NavierStokes/ComparatorSolution.lean` does not import that challenge module. The headline endpoint remains standard-axiom-only in its own dependency report. The review therefore records a repository-level metadata defect without misclassifying it as a contradiction of the selected C/D theorem.

The selected-stage trace is explicit: `ActualCandidateAssembly.selected_witness` feeds `GluedStageEstimates.actualStageEstimates`; the latter consumes `ActualCycleResidualBounds.PhysicalData`; and `ActualPhysicalPrefixFields.physicalFields_all` derives that data from smoothness, local germ identities, pressure-germ identities, and exterior equality. This closes endpoint-disconnection as a route. The live proof-bearing lane remains the cross-layer map among `FiveProfileMoments`, `PositiveOrderMoments`, and `FiveRowRank`.

The latest import-closure census refines that lane. The selected closure contains real `FiveProfileMoments` uses in `NominalProfile`, `ModulatedHistories`, `ModulatedCone`, `ModulatedProfileAssembly`, `MatchingDebtBounds`, `RepairConeBounds`, and `ReservedPatches`. In `ReservedPatches`, the identified cross-use proves support of nominal bump edits and agreement of heated fields with a `FiveRowRank.background`; it does not transport the five nominal moment rows into `FiveRowRank.FiveRows`. The next decisive test is therefore a theorem search for the full row, debt, and coefficient map, not a search for whether the nominal module is imported at all.

### Regularity and row equations

`MovingFieldRowNonImplicationProbe.lean` now supplies a zero-sorry countermodel to the weaker implication that generic moving-field regularity entails the physical row equations. The zero moving field meets `MovingField` for every admissible region and bounds, but a constant nonzero debt makes the third `FiveRows` identity false. This probe is not a selected-endpoint refutation: the actual rank path invokes `LocalRankDefect.RankGeometry.fiveRows`, which derives the rows from a stronger background/rank model.

The plan is therefore updated with a precise obligation. Trace the paper's five quantities into `RankGeometry` and show that the values used by `rank_rows_on_patch` are the same values repaired by the nominal or positive-order layers. A generic regularity theorem cannot discharge that obligation. Escalation to “formal disproof” still requires a contradiction or a false mandatory premise on the selected witness path.
