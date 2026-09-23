# Goal Description

The objective is to perform a rigorous structural falsification audit of the OpenAI Navier-Stokes Lean 4 proof repository, focusing on load-bearing components rather than exhaustive line-by-line checks. The goal is to identify mathematical flaws, missing correspondences, or false premises that invalidate the main claims.

All original scripts, probes, and findings will be isolated from the user's existing work, utilizing the specified `NavierStokesReview` subdirectories.

## User Review Required

Please review the proposed approach for identifying vulnerabilities and the structure for reporting findings. Let me know if there are specific mathematical areas (e.g., specific stages of the moment matching, specific filters) you want me to prioritize or avoid, given your own ongoing work.

## Open Questions (historical scaffold)

## Current execution contract

> This file is a historical scaffold. The executable plan is
> [`OpenAI_NavierStokes_CMI_First_Review_Plan.md`](OpenAI_NavierStokes_CMI_First_Review_Plan.md),
> and document authority is defined in [`REVIEW_DOCUMENT_CONTROL.md`](REVIEW_DOCUMENT_CONTROL.md).

1. Use the fork as the only active source tree.
2. Preserve source-backed corrections from Agent 2 notes, but do not treat
   those notes as independent evidence.
3. Pursue the selected five-moment transport bridge as the primary open lane.
4. Do not label a claim refuted without a source-level contradiction or a
   zero-sorry Lean countertheorem.

## Historical open questions

> [!WARNING] 
> Are there any specific files in the `NavierStokes` or `Euler` directories that you already know are dead-ends for falsification, so I can save time and avoid duplicating your efforts?

## Proposed Changes

The plan is divided into logical phases, focusing on the most critical structural pillars of the proof.

### Phase 1: Reconnaissance & Target Selection
- **Identify Load-Bearing Modules:** I will use `grep_search` and manual inspection to map out the exact files governing:
  1.  **Moment Repair & Debt Interfaces** (e.g., `FiveRowRank.lean`, `FiveProfileMoments.lean`, `PositiveOrderMoments.lean`).
  2.  **Pressure Recovery & Comparisons** (e.g., `R3PressureFlux.lean`, `WholeSpaceComparisonClosure.lean`).
  3.  **Generic Filters & Vacuity Hazards** (e.g., `JetRate` definitions, `Filter.bot` usage).
  4.  **Empty Branch / Reachability Issues** (e.g., checking if the `ActivePair` branches are provably inhabited).
- **Target Selection:** Select 3-4 highly vulnerable structural joints where a correspondence failure or unprovable premise would cascade into a full refutation.

### Phase 2: Probe Construction
- **Lean Probes (`NavierStokesReview\src\probes\agent_*.lean`):** For each selected target, I will write standalone Lean 4 files that import the relevant OpenAI modules and attempt to:
  - Construct explicit counter-models (e.g., showing a generic condition can be satisfied by a zero-field that breaks the physical equations).
  - Test for isomorphism/correspondence failures between layers (e.g., rank geometry vs. profile moments).
  - Check for `Filter.bot` vacuity.
- **Python Audit Scripts (`NavierStokesReview\src\audit\agent_*.py`):** If large-scale dependency tracking or axiom reporting is needed beyond what Lean can easily output, I will write Python scripts to parse the Lean environment or file structures.

### Phase 3: Execution & Evidence Gathering
- **Compile Probes:** I will use `lake build` specifically targeting the new probe files (to avoid compiling the entire project and crashing the system).
- **Record Evidence (`NavierStokesReview\evidence\agent_evidence_*.md`):** Store raw output from the probes, such as compiler warnings, `#print axioms` outputs, and evaluation results.
- **Synthesize Results (`NavierStokesReview\results\agent_findings.md`):** Compile the raw evidence into a structured findings paper detailing the exact formal weaknesses or contradictions discovered.

## Verification Plan

### Automated Tests
- `lake build NavierStokesReview.src.probes.agent_...` (or equivalent `elan`/`lean` commands) will be run for each probe to ensure it compiles without `sorry` (or explicitly demonstrates where the OpenAI code relies on unproven/false logic).

### Manual Verification
- The final `agent_findings.md` will clearly map any discovered Lean-level failures to the mathematical claims in the CMI problem statement, ensuring the critique remains mathematically grounded.
