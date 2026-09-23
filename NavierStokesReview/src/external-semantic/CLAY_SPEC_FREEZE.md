# ClaySpec freeze record

- Frozen file: `ClaySpec.lean`
- Initial SHA-256:
  `7b87d6cd20756dc80439b942e220ec3d524b952c08c85ae30edf2409d6981579`
- Line count: 227
- Compiler: Lean `4.34.0-rc2`, commit
  `6a10ac8c22beadecabdbb0919c2b50214762f91d`
- Compile result at freeze: exit code 0, no diagnostics
- Direct import: `Mathlib` only

This hash was recorded before opening `NavierStokes/ComparatorDefinitions.lean`
for the clause-by-clause comparison requested by the audit. From this point,
`ClaySpec.lean` is normative for the semantic comparison. It must not be changed
merely to make a bridge from the Comparator statement provable. Corrections are
allowed only for an independently identified transcription or Lean-definition
bug and must preserve this original hash and explain the correction explicitly.

## Independently required correction after freeze

The first bridge type-check exposed that writing `⊤` without opening Mathlib's
`ContDiff` notation had selected the outer `ω`/analytic differentiability order,
not ordinary `C∞`. The Clay PDF requires `C∞`, not analyticity. Accordingly the
three occurrences were corrected to `∞` after adding `open ContDiff`. This is a
source-faithfulness correction, not a weakening made to accommodate Comparator.
The corrected file recompiles with exit code 0 and has SHA-256
`bab3663c559a10f93e7a0b122622b320bac36c1f6dd5b0261ce59beaebf342ed`.
