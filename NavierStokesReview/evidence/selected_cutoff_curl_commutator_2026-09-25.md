# Selected cutoff--curl commutator

## Result

`NavierStokesReview/src/completions/SelectedCutoffCurlCommutator.lean`
compiles without `sorry`, custom `axiom`, or `unsafe` declarations in the
review library. Its theorem
`curl_smul_eq_smul_curl_add_commutator` proves, for differentiable scalar
cutoff `χ` and potential `A`,

$$
\operatorname{curl}(\chi A)(x)
=\chi(x)\operatorname{curl}(A)(x)
+\operatorname{curlLinear}\!\left((D\chi(x)).\operatorname{smulRight}(A(x))\right).
$$

The final summand is the exact cutoff-gradient commutator. It is not set to
zero by the product rule.

## Source anchors

| Item | Location | Meaning |
|---|---|---|
| `curlLinear` | `NavierStokes/SpatialCurl.lean:30-34` | Linear map implementing the three-dimensional curl. |
| `curl` | `NavierStokes/SpatialCurl.lean:48` | Applies `curlLinear` to the Frechet derivative. |
| `cutStage` | `NavierStokes/SolenoidalDiagonal.lean:32-33` | Multiplies each potential stage by `SmoothCutoffs.scaledCutoff`. |
| `potentialSum` | `NavierStokes/SolenoidalDiagonal.lean:37` | Takes the natural-indexed sum of cut stages. |
| `velocitySum` | `NavierStokes/SolenoidalDiagonal.lean:188-190` | Applies spatial curl to the potential sum. |
| cutoff regularity | `NavierStokes/SmoothCutoffs.lean:134-155` | Gives smoothness and compact support of the scaled cutoff. |
| review theorem | `NavierStokesReview/src/completions/SelectedCutoffCurlCommutator.lean:18-26` | Expands the selected calculation's local product rule. |

## What this establishes

The selected construction's order is mathematically material: cutoff first,
sum second, curl third. Any proposed radial-moment calculation must retain the
commutator term on every region where the cutoff varies, then account for the
axis and outer-support boundaries.

## What this does not establish

This theorem does not prove that the commutator has a nonzero radial moment.
The selected potential, torus average, scalar radial projection, integrability,
and boundary evaluation have not yet been identified in one Lean statement.
Accordingly it supplies a concrete calculation gate, not `Delta m ≠ 0` and not
`False`.

## Build record

Command: `lake build NavierStokesReview` under Lean `v4.34.0-rc2`.

Result: `Build completed successfully (3699 jobs).`
