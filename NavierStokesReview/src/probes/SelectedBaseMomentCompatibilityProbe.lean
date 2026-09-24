import NavierStokes.FinalSlowBase
import NavierStokes.GlobalStressSupport
import NavierStokes.PositiveOrderMoments

/-!
# Selected base/profile moment-chain re-audit

This probe records the strongest source fact relevant to CTR-005.  The
five-moment repair is live in the upstream aligned scheme and is used to
derive the finite residual identities and the final slow-base construction.
The probe also keeps the endpoint question separate: the generic selected
candidate transport layer does not expose this five-row equality for its
final mixed sums.
-/

noncomputable section

open Set Filter Function MeasureTheory
open scoped ContDiff Topology BigOperators

namespace NavierStokesReview.SelectedBaseMomentCompatibilityProbe

open NavierStokes
open NavierStokes.GlobalStressSupport
open NavierStokes.PositiveOrderMoments

theorem modulated_scheme_has_five_moment_identity
    {F : OutgoingProfile.Profile} {W : NominalProfile.Witness F}
    (H : NominalConeAssembly.Certificate W)
    {ld : ModulatedProfileAssembly.LoopData W}
    (v : ModulatedProfileAssembly.Witness ld)
    {n : ℕ} (hn : 0 < n)
    {eta : ℝ}
    (heta : eta ∈ v.slowParameters) :
    PositiveOrderMoments.moments n
      (PositiveOrderMoments.slice
        (GlobalStressSupport.axialHistory (EntranceAlignedBase.modulatedScheme H v)) eta)
      (PositiveOrderMoments.slice
        (GlobalStressSupport.angularHistory (EntranceAlignedBase.modulatedScheme H v)) eta)
      (fun R => GlobalStressSupport.previousOmega
        (EntranceAlignedBase.modulatedScheme H v) n (R, eta)) = 0 := by
  exact GlobalStressSupport.moments_zero
    (EntranceAlignedBase.modulatedScheme H v) hn heta

theorem actual_base_exposes_finite_identity_and_blowup (upper : ℝ) (B : ℕ) :
    ∃ (F : OutgoingProfile.Profile) (W : NominalProfile.Witness F)
      (H : NominalConeAssembly.Certificate W)
      (ld : ModulatedProfileAssembly.LoopData W)
      (v : ModulatedProfileAssembly.Witness ld),
      LeadingStressWeights.FullTrueCone v ∧
      BaseResidual.FiniteIdentities F.data.h W.axis.normalization
        (FinalSlowBase.coefficients H v) (FinalSlowBase.profileSequence H v) ∧
      ProblemStatement.SpeedUnboundedAtOne
        (FinalSlowBase.velocity H v upper B) := by
  let D := FinalSlowBase.actualProfile
  exact ⟨D.outgoing, D.nominal, D.certificate, D.loop, D.modulation,
    D.fullTrueCone,
    FinalSlowBase.finiteIdentities D.certificate D.modulation,
    FinalSlowBase.speedUnbounded D.certificate D.modulation upper B⟩

end NavierStokesReview.SelectedBaseMomentCompatibilityProbe
