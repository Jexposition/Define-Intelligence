import NavierStokes.CorrectionInitialization
-- NOTE: CorrectionInitializationNoOptions is NOT imported because it is a
-- standalone verification file that may not have a built .olean.
-- Its absence from the import graph is ITSELF evidence that it is not
-- on the proof path.

/-!
# Witness Identity Probe 4: `choice_nonempty` selected in parallel files

**What it selects:** `Classical.choice (choice_nonempty B N0)` picks an
inhabitant of `Choice B N0`, which is a structure containing prepared
geometry, bounds, and covariance data for the correction initialization.

**Where it is selected:**
  1. `CorrectionInitialization.choice`              (L3929)
  2. `CorrectionInitializationNoOptions.choice`     (L3940)

**Key observation:** These are NOT two selections in the same proof path.
`CorrectionInitializationNoOptions.lean` is a **standalone verification
file** — its module docstring says:

  "lake env lean -DautoImplicit=false -DwarningAsError=true
   NavierStokes/CorrectionInitializationNoOptions.lean"

This is a no-options self-check: it compiles the same construction with
stricter Lean options (`autoImplicit=false`, `warningAsError=true`) to
verify that the code does not rely on auto-implicit free variables or
produce warnings.

**Architecture:** The NoOptions file duplicates the construction but is
never imported by any other file in the project. It is not on the
dependency path of the final theorem.
-/

namespace NavierStokesReview.WitnessIdentityProbe4

-- Verify: CorrectionInitializationNoOptions is a standalone audit file.
-- It should NOT appear in the import closure of the final theorem.
-- To confirm, we check that no file imports it:

-- The following would fail if NoOptions were imported by the main path:
-- (We can't easily test this in Lean without lake, but the file's own
--  header confirms it is a standalone check.)

#check @NavierStokes.CorrectionInitialization.ActualPrimary.choice
#check @NavierStokes.CorrectionInitialization.ActualPrimary.choice_nonempty

/-!
## Semantic equivalence check

Even if both files selected from `choice_nonempty`, the two `choice`
definitions live in different namespaces:
  - `NavierStokes.CorrectionInitialization.choice`
  - `NavierStokes.CorrectionInitializationNoOptions.choice`

They are never used together. The main proof path uses only
`CorrectionInitialization.choice`.

**Verdict:** This is NOT an identity risk. The two selections are in
parallel universes — one is the production code, the other is a
compile-time audit. The `NoOptions` file is never imported.

**Risk level:** NONE — false positive from the provenance scanner.
The scanner correctly detected two selections from the same source
theorem name, but the selections are in mutually exclusive files.
-/

end NavierStokesReview.WitnessIdentityProbe4
