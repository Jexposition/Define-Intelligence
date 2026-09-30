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
| Current checkout files | `3468` |
| Resolved tree entries | `47` |
| Ambiguous tree entries | `0` |
| Missing tree entries | `0` |
| Duplicate current basenames | `15` |

## Interpretation

A resolved entry establishes only that the named file exists at the resolved current path. It does not establish import reachability or theorem use. Explicit tree-relative paths are preferred; basename fallback remains conservative. Ambiguous and missing entries are retained as review obligations.
