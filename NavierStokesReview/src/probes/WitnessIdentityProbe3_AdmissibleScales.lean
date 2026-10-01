import NavierStokes.ConstructedSlowBase
import NavierStokes.EntranceAlignedBase

/-!
# Witness Identity Probe 3: `exists_admissibleScales` selected 3 times

**What it selects:** `Classical.choose (exists_admissibleScales ...)` picks
a sequence `ℕ → ℕ` of scale indices satisfying `AdmissibleScales` — i.e. an
increasing sequence of Fourier truncation levels such that all jet bounds
converge uniformly on a compact set.

**Where it is selected:**
  1. `ConstructedSlowBase.nominalScales`   (L612)  — for the nominal coefficients
  2. `ConstructedSlowBase.modifiedScales`  (L710)  — for the modified coefficients
  3. `EntranceAlignedBase.scales`          (L1019) — for the entrance-aligned base

**Key audit question:** Are these three scale sequences ever compared,
combined, or required to be identical?

**Architecture observation:** Each selection feeds into a DIFFERENT
coefficient bundle:
  - `nominalScales` uses `nominalCoefficients W`
  - `modifiedScales` uses `modifiedCoefficients W Q M`
  - `scales` uses a third, entrance-aligned coefficient bundle

The existence theorem `exists_admissibleScales` is parameterized by the
coefficient bundle (its smoothness, height positivity, and compact box).
Since the three calls pass different coefficient bundles, they are selecting
from *different* existence propositions. This means:

  - The three sequences are NOT expected to be the same.
  - Each sequence is chosen to be admissible for its OWN coefficient bundle.
  - There is no shared identity assumption.

**Deeper check:** Do the three scale sequences ever appear in the same
equation or bound? Examining the downstream consumers:
  - `nominalScales_spec` extracts `AdmissibleScales` for `nominalCoefficients`
  - `modifiedScales_spec` extracts `AdmissibleScales` for `modifiedCoefficients`
  - These never cross-reference each other's scale values.
-/

namespace NavierStokesReview.WitnessIdentityProbe3

-- Verify: the three selections are from different existence propositions
-- because they use different coefficient bundles.

#check @NavierStokes.ConstructedSlowBase.nominalScales
#check @NavierStokes.ConstructedSlowBase.nominalScales_spec
#check @NavierStokes.ConstructedSlowBase.modifiedScales
#check @NavierStokes.ConstructedSlowBase.modifiedScales_spec

/-!
## Cross-contamination check

The critical question: does any theorem use BOTH `nominalScales` and
`modifiedScales` in the same bound? If so, the two sequences must be
compatible (e.g. one dominates the other), and that compatibility would
need to be *proved*, not assumed from identity.

Searching `ConstructedSlowBase.lean`:
- `nominalScales_exterior_residual_zero` uses only `nominalScales`
- `modifiedScales_exterior_residual_zero` uses only `modifiedScales`
- The actual candidiate assembly (`ActualCandidateAssembly.lean`) uses
  `selected_witness` which chooses a specific `ConstructedBase`, and
  that base contains ONE scale sequence, not a mixture of two.

**Verdict:** The three selections from `exists_admissibleScales` are
independent, well-typed, and never cross-referenced. Each satisfies
`AdmissibleScales` for its own coefficient bundle. There is no identity
violation because no theorem assumes two of these sequences are equal.

**Risk level:** LOW — these are genuinely different mathematical objects
(scale sequences for different coefficient bundles), not multiple
selections of the "same" object.
-/

end NavierStokesReview.WitnessIdentityProbe3
