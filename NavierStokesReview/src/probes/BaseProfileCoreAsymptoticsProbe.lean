import NavierStokes.TailGaugePotential
import NavierStokes.FinalSlowBase
import NavierStokes.GermCandidateAssembly
import NavierStokes.CandidateFromLimits

/-!
# Base-profile and core-asymptotics audit

This file is a zero-sorry source probe.  It records the exact public
interfaces used by the base profile and checks the claims that can be stated
without adding analytic assumptions.
-/

noncomputable section

namespace NavierStokes.BaseProfileCoreAsymptoticsProbe

open ProblemStatement
open scoped ContDiff

#check TailGaugePotential.finalPotential
#check TailGaugePotential.finalPotential_eq_sub_gauge
#check TailGaugePotential.finalPotential_smooth
#check TailGaugePotential.finalPotential_sameCurl
#check TailGaugePotential.radialNormalize_anchor
#check TailGaugePotential.gaugedSwirl
#check AxisymmetricFields.potential
#check AxisymmetricFields.velocity_zero
#check AxisymmetricFields.velocity_one
#check AxisymmetricFields.velocity_two
#check FinalSlowBase.origin
#check FinalSlowBase.axis_tendsto
#check CandidateFromLimits.tracedResidual_smooth
#check CandidateFromLimits.force_smooth

example (K : TailGaugePotential.Point → ℝ) (t z : ℝ) :
    TailGaugePotential.radialNormalize K (t, (1, z)) = 0 := by
  exact TailGaugePotential.radialNormalize_anchor K t z

example (a : ℕ → ℕ) (h C : ℝ) (d : SlowBorelBase.Coefficients) (t z : ℝ) :
    TailGaugePotential.gaugedSwirl a h C d (t, (1, z)) = 0 := by
  unfold TailGaugePotential.gaugedSwirl
  exact TailGaugePotential.radialNormalize_anchor _ t z

example {F : OutgoingProfile.Profile} {W : NominalProfile.Witness F}
    (H : NominalConeAssembly.Certificate W)
    {ld : ModulatedProfileAssembly.LoopData W}
    (v : ModulatedProfileAssembly.Witness ld) (upper : ℝ) (B : ℕ)
    (w : SpaceTime) :
    TailGaugePotential.finalPotential H v upper B w =
      FinalSlowBase.vectorPotential H v upper B w -
        SlowBorelBase.swirlPotential (FinalSlowBase.scales H v upper B)
          F.data.h W.axis.normalization (FinalSlowBase.coefficients H v)
          (w.1, (1, w.2 2)) • coordinateVector 2 := by
  exact TailGaugePotential.finalPotential_eq_sub_gauge H v upper B w

example {F : OutgoingProfile.Profile} {W : NominalProfile.Witness F}
    (H : NominalConeAssembly.Certificate W)
    {ld : ModulatedProfileAssembly.LoopData W}
    (v : ModulatedProfileAssembly.Witness ld) (upper : ℝ) (B : ℕ) :
    ContDiffOn ℝ ∞ (TailGaugePotential.finalPotential H v upper B)
      BaseResidual.past := by
  exact TailGaugePotential.finalPotential_smooth H v upper B

example {F : OutgoingProfile.Profile} {W : NominalProfile.Witness F}
    (H : NominalConeAssembly.Certificate W)
    {ld : ModulatedProfileAssembly.LoopData W}
    (v : ModulatedProfileAssembly.Witness ld) (upper : ℝ) (B : ℕ)
    {w : SpaceTime} (ht : w.1 < 1) :
    SpatialCurl.spatialCurl (TailGaugePotential.finalPotential H v upper B) w =
      FinalSlowBase.velocity H v upper B w := by
  exact TailGaugePotential.finalPotential_sameCurl H v upper B ht

end NavierStokes.BaseProfileCoreAsymptoticsProbe
