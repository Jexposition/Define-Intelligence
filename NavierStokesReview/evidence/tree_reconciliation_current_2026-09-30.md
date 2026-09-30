# Tree reconciliation

The extracted tree is an inventory snapshot. Current checkout paths are authoritative; unique basenames are used only to reconcile inventory entries, never to manufacture a path from an ambiguous name.

## Inputs

- Tree: `D:\Research Lab\Jexposition\Define Intelligence\Define-Intelligence-github\docs\doc_tree.md`
- Tree SHA-256: `1559a9ab7cdf8f498396e69dddee41e0f78e76720f6f80bd62acf5239217fba3`

## Counts

| Quantity | Count |
|---|---:|
| Tree entries | `49` |
| Tree file entries | `47` |
| Current checkout files | `3466` |
| Unique-basename resolutions | `45` |
| Ambiguous basename entries | `2` |
| Missing current basenames | `0` |
| Duplicate current basenames | `15` |

## Interpretation

A resolved entry establishes only that the named file exists at the unique current path. It does not establish import reachability or theorem use. Ambiguous and missing entries are retained as review obligations.

## Ambiguous entries

- line `18` `ARCHIVE_MANIFEST_2026-09-30.md`: `archive/ARCHIVE_MANIFEST_2026-09-30.md, docs/archive/ARCHIVE_MANIFEST_2026-09-30.md, NavierStokesReview/evidence/archive/ARCHIVE_MANIFEST_2026-09-30.md`
- line `40` `deep_semantics_audit.md`: `docs/deep_semantics_audit.md, NavierStokesReview/src/external-semantic/deep_semantics_audit.md`
