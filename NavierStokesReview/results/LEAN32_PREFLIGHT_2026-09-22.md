# Lean 4.32 compatibility preflight

Date: 2026-09-22

## Configuration

The isolated harness is
`NavierStokesReview/src/audit/lean32-preflight`. Its `lakefile.toml` points
directly at:

```text
D:/Research Lab/V-lab-Equipment/.lake/packages-4.32/mathlib
```

Its `lean-toolchain` is `leanprover/lean4:v4.32.0`, and Elan is installed at
`C:\Users\Admin\.elan\bin`.

## Commands and result

Initial command:

```text
elan run leanprover/lean4:v4.32.0 lake env lean Main.lean
```

Result: Lake reported that its compiled configuration was invalid and
requested `-R` reconfiguration.

Bounded reconfiguration command:

```text
elan run leanprover/lean4:v4.32.0 lake -R env lean Main.lean
```

Result: the isolated preflight did not return within 60 seconds. No claim
about Mathlib elaboration or the OpenAI repository is inferred from this
timeout. This compatibility lane remains available but is not used as the
repository theorem's toolchain; the public fork declares Lean 4.34.0-rc2.
