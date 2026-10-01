# Priority 236: public release provenance delta

## Confirmed repository facts

The source repository contains two relevant public commits:

| commit | date | message | role observed |
|---|---|---|---|
| `8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538` | 2026-09-08 06:57:25 -0400 | `.` | earlier comparator/candidate route |
| `f9e8bc5b38b6e212696e8a30e3e91517af887bbd` | 2026-09-10 07:51:24 -0400 | `.` | later R3/paper-facing route |

The direct Git diff between these objects reports 188 changed files, 25,143
insertions, and 81 deletions. This is the measured checkout result. Earlier
secondary descriptions giving different file and line counts are not used as
evidence until reconciled against the raw Git objects.

## Observed proof-route change

At the earlier commit, the C comparator theorem obtains its selected candidate
from `R3CompactCandidate.selected_compact_candidate` and discharges the
comparator through `option_C_of_compact_candidate`. At the later commit,
`navier_stokes_breakdown_R3` obtains

\[
\langle u,p,f,K,h,h_{\rm global}\rangle
\leftarrow \texttt{NavierStokesR3.theorem\_1\_1}
\]

and calls `NavierStokesR3.comparator_of_breakdown`. The periodic route likewise
changes from `ActualCandidateAssembly.selected_candidate` to
`PeriodicPaper.periodic_corollary`.

These are source-level facts about proof-route provenance. They do not by
themselves show that the earlier route was invalid, that the later route is
valid, or that the added modules merely decorate an unchanged proof.

## Required archaeology

For every changed declaration on a headline path, classify the delta as:

* explanatory or paper-facing wrapper;
* stronger or weaker premise;
* changed witness identity;
* genuine analytic obligation;
* changed domain, boundary, scaling, or convention;
* repaired proof of an obligation previously absent.

The audit must reproduce both commits independently, compute declaration-level
proof-term closures and dominators, and compare the exact hypotheses entering
the C/D comparator theorems. In particular, it must determine whether the R3
energy, pressure, uniqueness, force, and moment modules are in the active proof
term or merely reachable imports.

## Controlled interpretation

The terse commit messages and large delta reduce provenance transparency and
therefore increase audit priority. They are not evidence of concealment or a
mathematical error. The correct inference is:

\[
\text{missing provenance} \Rightarrow
\text{lower evidentiary value and higher reconstruction priority},
\]

not `missing provenance => false proof`.

The scientific disposition remains `CTR-005: NOT ESTABLISHED` for complete
paper-to-endpoint correspondence. This record does not assert a selected
defect, force nonsmoothness, literal CMI failure, or `False`.

Evidence basis: raw Git objects `8937a8f4` and `f9e8bc5` in the checked-out
repository, including `NavierStokes/ComparatorR3Theorem.lean`,
`NavierStokes/ComparatorTheorem.lean`, and `NavierStokes/R3/Theorem.lean`.
