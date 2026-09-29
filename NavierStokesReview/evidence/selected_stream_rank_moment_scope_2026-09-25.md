# Selected stream rank/moment scope

**Source tree:** `Define-Intelligence-github`, working tree based on `cdc97a7`
(`Record pushed review release`).

**Claim class:** selected-path source evidence. It narrows CTR-005; it does
not establish a nonzero remainder or Lean `False`.

## Source trace

1. The selected stream stages are defined in
   `NavierStokes/ActualCandidateConstruction.lean:453-470`.
   `rankNative` is built by `VariableGaugeMean.rankPotential`, and
   `streamNativeStages` adds the temporal and rank potentials before
   `streamMeanStages` maps the scalar to its angular field.

2. For a successor stage,
   `ActualCandidateConstruction.streamMeanStages_succ`
   (`:492-494`) identifies the selected field with
   `initialCycleData.streamFamily j`. The source definition
   `ActualMeanPhysicalData.CycleData.streamFamily` (`:879-880`) is the atlas
   family of the sum of `temporalScalar_overlap j` and
   `rankScalar_overlap j`.

3. The field-level decomposition is explicit in
   `ActualMeanPhysicalData.CycleData.stream_angularField` (`:1098-1100`):

   ```text
   (D.streamFamily j).angularField
     = (D.temporalFamily j).angularField
       + (D.rankFamily j).angularField
   ```

4. The rank correction is not dead code. In
   `NavierStokes/LocalRankDefect.lean:590-604`,
   `desired_mass_zero` proves the order-one radial mass identity for
   `rankDesiredAxial`, and `potential_eq_scaledPrimitive` consumes that
   identity when constructing `rankPotential`. The fixed-stream version at
   `:606-618` consumes the same premise again.

5. The selected combined stream is exported through
   `ActualMeanPhysicalData.CycleData.stream_moving`
   (`NavierStokes/ActualMeanPhysicalData.lean:915-917`). Its output is a
   `GaugeMomentBalances.MovingField`. The structure at
   `NavierStokes/GaugeMomentBalances.lean:460-466` contains only smoothness,
   radial support, and auxiliary-coordinate periodicity.

6. The selected curl transport is independently proved by
   `ActualCandidateConstruction.streamMeanStages_curl_on_chart`
   (`NavierStokes/ActualCandidateConstruction.lean:582-590`) and specialised
   in `src/completions/SelectedStreamCurlChartTransport.lean`.

7. The scalar moment operator remains separate:
   `DefectIncrementBounds.barMoment_apply`
   (`NavierStokes/DefectIncrementBounds.lean:214-220`) applies
   `PressureStream.torusAverage` before the radial integral. No selected
   theorem in this trace identifies the curled Cartesian stream with that
   scalar torus-average input after production assembly.

## Lean completion

`src/completions/SelectedStreamRankScope.lean` composes the successor-stage
decomposition and the `MovingField` result without adding an assumption about
the five moments. The canonical build was:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake build NavierStokesReview
```

Result: `Build completed successfully (3710 jobs).`

The completion contains no `sorry`, custom `axiom`, or `unsafe` declaration.

## Finding

The source supports the precise statement that rank zero-mass data enters the
selected stream construction and survives as regularity/support data into the
curl branch. It does not support the stronger statement that the exported
curl field has the paper's full five cumulative moments. The missing theorem
is a selected field-level transport identity through curl, auxiliary averaging,
radial integration, and the final mixed-field assembly. A nonzero numerical
remainder remains unproved.
