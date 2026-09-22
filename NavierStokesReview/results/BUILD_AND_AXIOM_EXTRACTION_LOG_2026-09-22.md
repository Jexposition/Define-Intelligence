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

## Completed Navier–Stokes headline probe

After the target emitted its interfaces, the independent probe completed with
exit code 0. Its four reports are preserved verbatim in
`NavierStokesReview/results/HEADLINE_AXIOMS_4_34_RC2.txt`. All four report
only `propext`, `Classical.choice`, and `Quot.sound`. This closes the
Navier–Stokes portion of the formal trust gate, subject to the separate CMI
semantic and human-review gates. Euler exports remain to be probed.

## Independent CMI alias probe

The zero-sorry `CMIQuantifierProbe` initially encountered a missing cached
Mathlib interface. Building `Mathlib.Computability.PartrecCode` restored that
interface; a subsequent sandbox-identity change required a local
`GIT_CONFIG_GLOBAL` safe-directory file for the cached package repositories.
The final probe then completed with exit code 0 and displayed both exact
whole-space and periodic CMI-facing proposition shapes. Raw disposition is in
`NavierStokesReview/results/CMI_QUANTIFIER_PROBE_4_34_RC2.txt`.

## Direct Euler closure and headline probe

The ordinary Lake closure for `Euler.Solution` generated approximately 7 GB
of intermediate IR before the volume filled and therefore was not used as the
review method. The intermediate IR was removed only after an absolute-path
check; ignored build outputs and all source files were preserved.

The independent resumable direct Lean closure
`NavierStokesReview/src/audit/direct_lean_closure.ps1` then compiled the
1,829-module project closure using only `.olean`/`.ilean` outputs. It finished
with all modules available, including `Euler.Solution`. This was an interface
precondition, not a mathematical validation criterion.

The zero-sorry `EulerAxiomProbe` then completed with exit code 0. Both Euler
exports report only `propext`, `Classical.choice`, and `Quot.sound`; neither
report contains `sorryAx`, a native-evaluation axiom, or a project-specific
axiom. Raw output is preserved in
`NavierStokesReview/results/EULER_AXIOMS_4_34_RC2.txt`.
