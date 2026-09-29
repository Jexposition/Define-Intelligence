# Direct endpoint-closure validation

**Date:** 2026-09-29
**Target:** `NavierStokes.R3.Theorem`
**Public theorem namespace:** `NavierStokesR3.theorem_1_1`
**Review utility:** `NavierStokesReview/src/audit/direct_lean_closure.py`

## Result

The direct project-import traversal returned **588 Lean project modules**.
The traversal returned **zero `NavierStokesReview` modules**. Its result is
therefore an exact source-import closure for the OpenAI Navier–Stokes R³
theorem module, not a count of review probes or review-side source files.

The regenerated hardened source map and semantic register independently report
the same reachable count: **588**. The repository-wide fork inventory contains
**2,794 Lean modules**, so **2,206** modules lie outside this particular
endpoint closure.

## Reproducible method

From the repository root:

```powershell
& 'D:\Research Lab\V-lab-Equipment\.venv\Scripts\python.exe' `
  -c "import sys; from pathlib import Path; sys.path.insert(0, r'NavierStokesReview/src/audit'); from direct_lean_closure import closure; print(len(closure(Path('.').resolve(), 'NavierStokes.R3.Theorem')))"
```

The traversal follows only project-local `NavierStokes.*` and `Euler.*`
imports. It does not infer theorem use from filenames, declaration names, or
semantic similarity.

## Interpretation boundary

“Reachable” here means **reachable by the specified source import graph**. It
does not mean that every declaration is used by the exported theorem, that
every reachable module has been semantically reviewed, or that the paper's
mathematical identities are transported into the endpoint. Conversely,
“outside this closure” does not mean dead code, invalid code, or code outside
OpenAI's repository. Those modules remain part of the repository-wide audit
inventory and require separate root or source classification.

The closure count therefore validates scope accounting only. It does not alter
the CTR-005 adjudication: the selected-field five-moment correspondence still
requires a value-level source trace through the actual Cartesian construction
and exported witness, and no nonzero defect or impossibility claim is inferred
from the closure count.

## Related records

- `NavierStokesReview/evidence/hardened_source_map_2026-09-29.json`
- `NavierStokesReview/evidence/semantic_coverage_register_full_2026-09-29.md`
- `docs/REVIEW_DOCUMENT_CONTROL.md`
