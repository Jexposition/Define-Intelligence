# Build and axiom-extraction log

Date: 2026-09-22  
Repository commit: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`  
Declared toolchain: `leanprover/lean4:v4.34.0-rc2`

## Commands and observations

1. `C:\Users\Admin\.elan\bin\elan.exe run leanprover/lean4:v4.34.0-rc2 lake exe cache get`
   completed successfully. It restored 3,311 already-cached Mathlib files and
   reported no files to download. This changed only ignored `.lake` build/cache
   state.

2. `C:\Users\Admin\.elan\bin\elan.exe run leanprover/lean4:v4.34.0-rc2 lake build NavierStokes.ComparatorSolution`
   was run as a bounded, targeted attempt after cache retrieval. It exceeded
   120 seconds and was stopped with no
   `.lake/build/lib/lean/NavierStokes/ComparatorSolution.olean` emitted. The
   partial build produced project interfaces but did not produce an axiom
   report.

3. The target source contains the requested commands:

   ```lean
   #print axioms NavierStokes.Comparator.navier_stokes_breakdown_R3
   #print axioms NavierStokes.Comparator.navier_stokes_breakdown_periodic
   ```

   They cannot be evaluated independently until the target interface exists.

## Interpretation

This is an environment/build-cost result, not evidence that the theorem fails.
It also is not evidence that the theorem is trusted. The transitive axiom
footprint remains `PENDING` and must be obtained from a completed declared-
toolchain interface or from an independently reproducible equivalent build.

The requested `D:\Research Lab\V-lab-Equipment\.lake\packages-4.32` cache is
not substituted here: the fork declares Lean 4.34.0-rc2 and matching Mathlib
and Comparator revisions. The 4.32 cache remains reserved for isolated
compatibility probes.

## Import-boundary check

The project source imports `ComparatorChallenges` only as its separate default
Lake target. The exported Navier-Stokes solution imports
`NavierStokes.ComparatorR3Theorem` and `NavierStokes.ComparatorTheorem`; the
challenge file's four intentional `sorry` declarations were not found in the
source import scan. This source result still does not replace transitive
kernel output.

## Headline probe retry

The independent probe
`NavierStokesReview/src/probes/HeadlineAxiomProbe.lean` was run with:

```text
C:\Users\Admin\.elan\bin\elan.exe run leanprover/lean4:v4.34.0-rc2 lake env lean NavierStokesReview/src/probes/HeadlineAxiomProbe.lean
```

It failed at import resolution because
`.lake/build/lib/lean/NavierStokes/ComparatorSolution.olean` did not exist.
This is the missing-interface condition, not a theorem failure. A fresh
bounded `lake build NavierStokes.ComparatorSolution` then ran for 60 seconds
and timed out while compiling dependencies. The process inventory showed
dependency workers still active; no headline axiom output is recorded until
the build emits the interface.
