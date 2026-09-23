# Reproducing the independent semantic-gap check

Baseline:

- OpenAI checkout: `../audit-openai` at
  `8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538`
- Lean: `leanprover/lean4:v4.34.0-rc2`, commit
  `6a10ac8c22beadecabdbb0919c2b50214762f91d`
- Mathlib: `85e3a25e006c35636f0e53b0e9296caca2685bc0`
- Comparator definitions: package commit
  `19e111e2141cf333c7daff0f64c5f24acc91dd2e`

From `../audit-openai`, enter its pinned Lake environment and compile the three
files in order.  The first two files are the independent check; the third is
the deliberately separate end-to-end adapter:

```bash
lake env /bin/bash --noprofile --norc -c '
  set -euo pipefail
  cd ../semantic-gap-audit
  export LEAN_PATH=.:${LEAN_PATH:-}
  lean -o ClaySpec.olean ClaySpec.lean
  lean -o Gap.olean Gap.lean
  lean -o Adapter.olean Adapter.lean
'
```

Expected `#print axioms` output for each gap theorem and each final adapter
theorem is:

```text
[propext, Classical.choice, Quot.sound]
```

The official Comparator and nanoda run is not part of this command.  Its
already completed, independently persisted transcript is
`../audit-artifacts/logs/comparator-systemd.log`.

## Current-source rerun

On 2026-09-23, the same independent files were compiled against the current
public OpenAI source closure at commit
`f9e8bc5b38b6e212696e8a30e3e91517af887bbd`, using the review fork's Lean
build directories on `LEAN_PATH`. The pinned external audit checkout was kept
outside this repository. The reproducible result for that run is recorded in
`NavierStokesReview/results/INDEPENDENT_CLAY_BRIDGE_CURRENT_2026-09-23.txt`.

Generated `.olean` files are intentionally ignored by the review repository;
only the independent source, freeze record, clause comparison, and transcripts
are tracked.
