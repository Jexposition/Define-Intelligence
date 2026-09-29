# Priority 127: source provenance and environment-closure integrity

## Purpose

This review closes a probe-logic blind spot found in Priority 125-126. A
repository-wide lexical pass can accidentally mix auditor-authored completion
theorems with declarations from OpenAI's `NavierStokes/` source tree. The two
populations must be measured separately before any candidate is discussed as
evidence about OpenAI's endpoint.

## Source-only result

The hardened detector was run against the OpenAI source root alone:

```text
source root: Define-Intelligence-github/NavierStokes
declarations indexed: 31,472
joint candidates: 0
positive manual candidates: 0
selected transport proved: false
selected transport disproved: false
selected Delta m proved: false
kernel False proved: false
absence claim permitted: false
```

The full-repository pass indexed 34,583 declarations and found 11 joint
candidates, but all 11 have origin `review_completion`; all three positive
manual-review candidates are under `NavierStokesReview/src/completions/`.
They are useful auditor-authored completion obligations and finite-prefix
identities. They are not declarations supplied by OpenAI's source tree and
must not be cited as if they were.

This is a provenance result, not an absence theorem. The detector can identify
candidate declarations; it cannot prove that no differently named theorem
exists. The source-only result therefore strengthens the search boundary and
does not by itself establish CTR-005, a nonzero defect, impossibility, or
`False`.

## Environment-closure integrity

The supplied environment snapshot is not a current endpoint closure. It lacks
the configured roots
`NavierStokes.ActualCandidateAssembly.selected_witness` and
`NavierStokesR3.theorem_1_1`. A fresh run of
`NavierStokesReview/src/audit/EnvironmentDependencyExport.lean` was attempted
with Lean `v4.34.0-rc2` and failed before exporting because
`.lake/build/lib/lean/NavierStokes/R3/Theorem.olean` does not exist.

A follow-up `lake build NavierStokes` was then attempted with the same
toolchain. It exceeded the 120-second execution limit, was stopped together
with its child Lean processes, and still left the required `.olean` absent.
This is a build-timeout result, not a successful build and not a proof failure
of the mathematics.

Accordingly, the environment pass is marked unavailable with missing roots;
the source pass is not silently upgraded into environment evidence. Any
endpoint conclusion must wait for a successful build/export or remain labelled
source-level triage.

## Required next gates

1. Build the exact OpenAI endpoint environment and rerun
   `EnvironmentDependencyExport.lean`.
2. Reconcile the exported declaration names with the source definitions before
   reading type-level reachability.
3. Compile the auditor-authored completion probes against that environment,
   keeping their provenance separate from OpenAI source claims.
4. Continue the actual selected-field calculation: finite-prefix to `tsum`,
   direct branch, periodisation, axis/global domain, and the five observables.

No escalation to `False`, `Delta m != 0`, or formal refutation is authorised by
this review.
