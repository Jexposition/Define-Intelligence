# Priority 241: Selected Object-Identity Ledger

**Date:** 2026-10-01
**Status:** `PARTIAL SOURCE TRACE / ARROW SEMANTICS OPEN`
**Scope:** current September 10 checkout, branch `review/cmi-first-navier-stokes-reconciled-2026-09-30`

## Purpose

This ledger audits the mathematical objects, not merely the files that mention
them. Every arrow must identify the source object, target object, domain,
regularity, support/time scope, and the theorem that transports the property.
The central invariant is the tuple

\[
(u,p,f,K),
\]

with the manuscript observables tracked separately:

\[
\mathcal M(u,p,f)=(M,I,J,S,C_p).
\]

An arrow can be kernel-valid without proving that \(\mathcal M\) is preserved.
`SOURCE-TRACE POSITIVE` therefore means that the stated Lean object relation is
visible in the source. It does not mean that the paper-level physical
correspondence has been independently reconstructed.

## Ledger

| ID | Source object | Target object | Evidence | Scope carried | Current status |
|---|---|---|---|---|---|
| OI-001 | `ActualCandidateAssembly.selected_witness` | one activated velocity, pressure, and forcing witness | `ActualCandidateAssembly.lean:1121–1151,1177–1185` | One schedule, three extensions, one `forcing`, `CandidateProperties` for the activated fields | **SOURCE-TRACE POSITIVE** |
| OI-002 | selected witness tuple | `selected_candidate_one_with_early_zero` | `R3/ActualCandidate.lean:127–135` | Same candidate properties and same activated velocity; early-zero property | **SOURCE-TRACE POSITIVE** |
| OI-003 | selected witness tuple | `selected_candidate_one_with_initial_rest` | `R3/ActualCandidate.lean:143–153` | One tuple \((u,p,f,K)\), with common initial-rest data | **SOURCE-TRACE POSITIVE** |
| OI-004 | \((u,p,f,K)\) from selected candidate | \((\operatorname{scaledVelocity}_\nu u,\operatorname{scaledPressure}_\nu p,\operatorname{scaledVelocity}_\nu f,K_\nu)\) | `R3/Theorem.lean:26–42` | Same three-field tuple is scaled; support set is transformed | **SOURCE-TRACE POSITIVE; scaling identities still require independent review** |
| OI-005 | scaled R³ tuple | `NavierStokesR3.theorem_1_1` / `breakdownStatement` | `R3/Theorem.lean:46–49,62` | Existential packaging of the same scaled candidate route | **SOURCE-TRACE POSITIVE** |
| OI-006 | candidate force `f` | comparator force `toComparator f` | `R3/ComparatorBridge.lean:77–88` | Same force under the explicit representation adapter; no independent force is selected | **SOURCE-TRACE POSITIVE; representation equivalence remains an audit edge** |
| OI-007 | comparator solution `(v,p)` | `GlobalFiniteEnergySolution ν f` | `R3/ComparatorBridge.lean:48–70` | `fromComparator` fields, smoothness, initial data, PDE, `MemLp`, and energy bound | **LEAN INCLUSION PRESENT; Fefferman-class variance still open** |
| OI-008 | R³ candidate tuple | `beforeOne u`, `beforeOne p`, `f` | `PeriodicPaperTheorem.lean:92–100,124–145` | Post-one extensions are discarded before periodisation; equations are used only for `t<1` | **SOURCE-TRACE POSITIVE; endpoint/local-to-global semantics open** |
| OI-009 | compressed candidate | `periodize (beforeOne u)`, `periodize (beforeOne p)`, `periodize f` | `PeriodicPaperTheorem.lean:92–145` | Smoothness, periodicity, support, divergence, PDE, force support, and blow-up are transported by named lemmas | **SOURCE-TRACE POSITIVE; same-observable transport not shown** |
| OI-010 | R³ theorem tuple | periodic corollary tuple | `PeriodicPaperTheorem.lean:155–162` | One tuple is compressed and periodised for D; D does not reuse the C tuple unchanged | **SOURCE-TRACE POSITIVE; D-specific semantic bridge open** |
| OI-011 | upstream physical cycle/profile data | `physicalData` and `estimates` | `ActualCandidateAssembly.lean:1079–1098` | Concrete physical prefix fields feed stage estimates used by the selected witness | **SOURCE-TRACE POSITIVE** |
| OI-012 | upstream repair/moment machinery | final \(\mathcal M(u,p,f)\) | No production declaration located in the selected endpoint trace | Required equality \(\mathcal M(u,p,f)=(M,I,J,S,C_p)\) is not exposed by the inspected endpoint | **NOT LOCATED; CTR-005 remains NOT ESTABLISHED** |

## What the ledger proves

The positive result is stronger than “the repository has unrelated scaffolding”:

\[
\exists(u,p,f,K)\;P(u,p,f,K)
\quad\text{and the same tuple is used by the R³ comparator route.}
\]

The comparator bridge also constructs `toComparator f` from that candidate
force and derives the contradiction through `globalSolutionOfComparator`. This
removes the specific witness-identity objection for the current B route.

The periodic D route is also not a free existential re-selection: it begins
from the R³ tuple, compresses it, discards arbitrary post-one extensions, and
periodises the resulting fields using explicit transport lemmas.

## What the ledger does not prove

The ledger does **not** prove the stronger paper correspondence

\[
\mathcal M(u_{\mathrm{final}},p_{\mathrm{final}},f_{\mathrm{final}})
  =(M,I,J,S,C_p),
\]

nor does it prove that the five reduced-profile identities survive every
selected curl, cutoff, `tsum`, scaling, compression, and periodisation map.
The source contains real repair-engine usage upstream, but the inspected public
endpoint still does not expose the final observable equality. This is a
correspondence finding, not a value-level defect and not a literal CMI
refutation by itself.

## Required arrow checks

1. Prove or refute the exact scaling identities for velocity, pressure, force,
   viscosity, and the transformed support set.
2. Prove the representation equivalence needed by `toComparator` and
   `fromComparator`, rather than treating field-name alignment as identity.
3. Check the required variance direction
   \[
   \text{Fefferman competitor}\Rightarrow\text{Comparator competitor},
   \]
   including finite-energy integral \(\Rightarrow\) `MemLp` and coordinate
   derivative bounds \(\Rightarrow\) Fréchet-derivative norm bounds.
4. Trace `beforeOne` and periodisation at \(t=1\), \(r=0\), and spatial
   boundaries, including pointwise versus eventual/germ equality.
5. For every arrow, record whether \(\mathcal M\) is consumed, produced,
   transported, or absent from the contract.

## Controlled conclusion

The correct current disposition is:

- **B selected tuple identity:** source-trace positive;
- **B comparator same-force route:** source-trace positive;
- **D periodisation tuple route:** source-trace positive, with D-specific
  boundary and scaling checks still open;
- **Fefferman-to-Comparator class inclusion:** not yet independently proved;
- **final five-observable transport:** not located;
- **nonzero defect, impossibility, or kernel contradiction:** not established.

Evidence companion: `priority_241_selected_route_identity_2026-10-01.md`.
