# Fresh post-clean build status: 2026-09-27

## Scope

The previous `.olean` cache was removed because it contained incompatible
headers. A clean rebuild was attempted with:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake build NavierStokes NavierStokesReview
```

The aggregate process exceeded the tool's 20-minute execution limit without
emitting a Lean error. A second bounded attempt targeted:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake build NavierStokes.R3.Theorem
```

That process exceeded a 10-minute limit without emitting a Lean error. Both
process trees were then terminated by exact process identifier. No compiler
workers remain.

## Interpretation

These attempts do not establish a successful fresh build, and they do not
establish a Lean failure. The dated compiled-closure metrics in the
2026-09-26 evidence remain the last completed closure export. They must not be
described as regenerated after the cache clean.

The source conclusions in the current cross-examination remain independently
supported by raw declarations:

- `ActualCandidateAssembly.Witness` is a proposition-valued nested
  existential at `NavierStokes/ActualCandidateAssembly.lean:1121-1151`.
- `selected_witness` is the instantiation at `:1177-1181`.
- `FiveRowRank`, `PositiveOrderMoments`, `FiveProfileMoments`,
  `MeanRankUpdate`, `periodicVelocity`, and `barMoment` are present in the
  selected upstream route, but `Witness` has no conjunct identifying the
  final Cartesian field with `(M,I,J,S,C_p)`.

The build status is therefore **incomplete post-clean verification**, not a
mathematical result and not evidence of a source error.

The expected post-build artifact
`.lake/build/lib/lean/NavierStokes/R3/Theorem.olean` is currently missing,
which confirms that the bounded target attempt did not complete.
