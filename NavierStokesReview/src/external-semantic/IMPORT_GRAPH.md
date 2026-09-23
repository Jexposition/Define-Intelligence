# Audit-file import graph

Direct imports:

```text
Mathlib
└── ClaySpec.lean
    └── Gap.lean
        └── Adapter.lean

NavierStokes/ComparatorDefinitions.lean
└── Gap.lean

NavierStokes/ComparatorSolution.lean
└── Adapter.lean
```

`ComparatorDefinitions.lean` itself imports only `Mathlib`.  Consequently the
transitive non-Mathlib dependency of `Gap.lean` is limited to the independent
Clay specification and the statement-only Comparator definitions.

`Gap.lean` does **not** import `ActualCandidateAssembly`, `ComparatorBridge`,
`ComparatorSolution`, any uniqueness or blow-up module, or any other OpenAI
proof-construction file.  `Adapter.lean` is intentionally separate and is the
only new audit file importing the OpenAI solution.

The umbrella `Mathlib` import is broad but remains within the pinned Mathlib
revision and does not add axioms beyond those reported by `#print axioms`.
