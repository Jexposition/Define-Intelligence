# Evidence: selected mixed `barMoment` shell gate

This record accompanies
`../src/audit/priority_225_selected_mixed_barmoment_shell_gate_2026-10-01.md`.

## Confirmed by compilation

Six review-side completions compiled with exit code 0 under
`leanprover/lean4:v4.34.0-rc2`: finite-prefix representatives, the mixed
branch split, the exact `barMoment` application formula, conditional
`barMoment` linearity, the native direct-prefix zero moment, and the cutoff
finite-prefix identity.

## What is not proved

The conditional linearity theorem requires `Shell` for both selected branches.
The final mixed Cartesian pullback does not currently export the required
radial-support premise. The native direct-prefix zero moment is before the
final Cartesian cutoff and periodisation, so it cannot be substituted for the
final mixed selected-field moment.

The result is therefore a precise gate, not a numerical moment value and not
a falsification theorem.

## Scientific status

`CTR-005: NOT ESTABLISHED` remains the correct bounded disposition for the
complete manuscript-to-selected-endpoint correspondence. No nonzero selected
defect, force nonsmoothness, literal CMI failure, impossibility theorem, or
kernel-level `False` is established here.
