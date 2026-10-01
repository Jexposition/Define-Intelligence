# Priority 241: Selected-Route Witness Identity

**Date:** 2026-10-01
**Status:** `SOURCE-TRACE POSITIVE / SEMANTIC BRIDGE STILL OPEN`
**Scope:** current checkout at `review/cmi-first-navier-stokes-reconciled-2026-09-30`, corresponding to the reviewed September 10 source snapshot.

## Finding

The current R3 headline route does not obtain three unrelated existential objects for the candidate velocity, pressure, and force. It obtains one tuple

\[
(u,p,f,K)
\]

from `NavierStokesR3.ActualCandidate.selected_candidate_one_with_initial_rest`, then transports that same tuple through viscosity scaling and the whole-space comparator bridge.

This is positive evidence against the earlier overstatement that the selected endpoint merely assembles unrelated properties. It does **not** close CTR-005: the route still does not expose a theorem identifying the final selected Cartesian/localised/periodised/summed fields with the manuscript observables \((M,I,J,S,C_p)\).

## Exact source chain

1. `ActualCandidateAssembly.selected_witness` (lines 1177–1181) supplies one existential witness containing the common stage schedule, three extensions, one `forcing`, and `CandidateProperties` for the activated velocity and pressure.
2. `R3/ActualCandidate.lean:127–135` consumes that single witness and constructs `selected_candidate_one_with_early_zero` from the same candidate properties and the same activated velocity.
3. `R3/ActualCandidate.lean:143–153` consumes the same selected witness route and returns one tuple \((u,p,f,K)\) together with the common initial-rest property for both \(u\) and \(p\).
4. `R3/Theorem.lean:26–42` takes that one tuple and scales all three fields coherently:

   \[
   (u,p,f)\mapsto
   (\operatorname{scaledVelocity}_\nu u,
    \operatorname{scaledPressure}_\nu p,
    \operatorname{scaledVelocity}_\nu f).
   \]

   The support set is transformed at the same time.
5. `R3/Theorem.lean:46–49` packages the same scaled tuple into `theorem_1_1`; it does not choose a second velocity, pressure, or force for separate clauses.
6. `R3/ComparatorBridge.lean:77–88` receives `CandidateProperties ν u p f K` and the no-global-solution fact for that same `f`, then constructs the comparator force with `toComparator f` and derives the contradiction from `globalSolutionOfComparator`.
7. `PeriodicPaperTheorem.lean:155–162` starts from the same `theorem_1_1_with_initial_rest` tuple, applies compression and parabolic scaling to the candidate, then periodises the resulting fields as one coherent tuple.

## What this establishes

The route-level witness identity is now positively supported:

\[
\exists(u,p,f,K),
  P(u,p,f,K)\land
  \neg\operatorname{GlobalSolution}(f),
\]

and the downstream R3 comparator uses that same `f` rather than silently substituting an independently chosen force. This is a materially stronger finding than “the endpoint contains generic rates only”.

## What remains unresolved

The route-level conjunction is not the manuscript-to-field observable bridge. The inspected path still has no production declaration proving

\[
\operatorname{Moments}(u_{\mathrm{final}},p_{\mathrm{final}},f_{\mathrm{final}})
   =(M,I,J,S,C_p),
\]

nor a theorem proving that the five reduced-profile identities survive the complete selected transformation chain. The correct status is therefore:

- **same selected candidate tuple through the C/D route:** source-trace positive;
- **five-observable transport into the final selected fields:** not located, still open under CTR-005;
- **actual nonzero moment defect:** not proved;
- **literal CMI failure from this omission alone:** not asserted.

This distinction prevents two opposite errors: treating the production route as unrelated scaffolding, and treating coherent witness reuse as proof of the paper's five-moment field identity.

## Next audit edge

The next task is to make the object ledger explicit for the arrows

\[
u_{\mathrm{activated}}
\to u_{\mathrm{R^3}}
\to u_{\mathrm{scaled}}
\to u_{\mathrm{periodised}},
\qquad
f_{\mathrm{selected}}
\to f_{\mathrm{scaled}}
\to f_{\mathrm{periodised}},
\]

and separately test whether any declaration on those arrows consumes or produces the manuscript five-observable payload. This is an arrow audit, not another module-name scan.
