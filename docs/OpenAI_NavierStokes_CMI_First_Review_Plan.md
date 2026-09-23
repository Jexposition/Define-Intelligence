# CMI-First Counter-Paper Review Plan

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

The current evidence supports A and B, rejects the old “periodic toy” objection, and does not establish C or D as a faithful formalisation of the published construction. The zero-sorry moment probes supply a formal obstruction to direct coordinate identification, while the dependency axiom probe finds no custom axiom at the selected witness interfaces. E is outside the literal Newtonian endpoint.

## Falsification lanes

### Lane 1: moment correspondence

Compare the paper's `(M, I, J, S, C_p)` system with both `FiveProfileMoments` and `FiveRowRank`. The former contains matching normalised vectors; the latter is a distinct physical rank interface. Trace `physical_five_rows`, `prescribed_five_rows`, `reserved_five_rows`, the `ModulatedHistories` consumers, and the selected witness. The direct-bridge probe is complete and rules out a row-by-row identification. The remaining decisive test is whether a nontrivial conversion exists and is actually consumed by the selected witness.

### Lane 2: filter non-vacuity

Audit every `JetRate`, frequency-shell, germ, and limit obligation consumed by the selected candidate. Prove `NeBot` for each derived filter or prove that the target statement is independent of that filter. The existing generic `Filter.bot` probe is a warning, not yet a headline refutation.

### Lane 3: force specification

Verify smoothness, compact support, positive-time support, decay, and extension through time one. Separately record that the force is residual-defined and active through collapse. Do not treat force activity alone as a C/D violation.

### Lane 4: whole-space closure

Trace the pressure recovery, pressure flux, uniqueness, energy, and compact-support interfaces into `CandidateBreakdown`. Look for an imported rate bound or other premise that is not derived from the candidate fields.

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

Use “formal disproof” only after a zero-sorry contradiction or a false mandatory premise has been proved. Use “formal correspondence failure” when the code and paper are not connected by a required theorem. Do not escalate a semantic criticism into a theorem-level verdict.
