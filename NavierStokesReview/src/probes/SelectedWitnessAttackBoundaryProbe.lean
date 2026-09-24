import NavierStokes.ActualCandidateAssembly
import NavierStokes.PositiveOrderMoments

/-!
# Selected-witness attack boundary

This is an adversarial zero-sorry probe.  It records two limits of the
current falsification programme:

* the exported `Witness` proposition does not entail an arbitrary
  five-coordinate debt certificate;
* velocity blow-up and a residual tending to zero are compatible at the
  level of the exposed scalar interface.  A contradiction therefore needs a
  selected-field PDE lower bound, not the two endpoint predicates alone.

Neither theorem below claims that the selected velocity violates the physical
moment equations.  The first is a specification gap.  The second prevents
the invalid inference that an unbounded velocity norm automatically makes
the residual or every residual derivative unbounded.
-/

noncomputable section

namespace NavierStokesReview.SelectedWitnessAttackBoundaryProbe

open Filter NavierStokes NavierStokes.ActualCandidateAssembly
open NavierStokes.PositiveOrderMoments
open scoped Topology

def nonzeroDebt : Debt := fun _ => 1

theorem selected_witness_does_not_entail_zero_five_debt :
    ¬ (Witness ActualCandidateConstruction.selectedBudget
        ActualCandidateConstruction.selectedThreshold
        ActualCandidateConstruction.selectedThreshold_geometry →
        ∀ d : Debt, d = 0) := by
  intro h
  have hd : nonzeroDebt = 0 := h selected_witness nonzeroDebt
  have hd0 := congrFun hd (0 : Fin 5)
  norm_num [nonzeroDebt] at hd0

theorem scalar_blowup_flat_residual_countermodel :
    Tendsto (fun n : ℕ => (n : ℝ)) atTop atTop ∧
      Tendsto (fun _ : ℕ => (0 : ℝ)) atTop (𝓝 0) := by
  constructor
  · exact tendsto_natCast_atTop_atTop
  · exact tendsto_const_nhds

end NavierStokesReview.SelectedWitnessAttackBoundaryProbe
