# Pressure-flux and whole-space uniqueness audit

Snapshot: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`
Date: 2026-09-22

## Question

Does the R3 nonexistence argument assume agreement with the compact candidate,
or does it derive agreement from an independently stated comparison estimate?

## Trace

1. `NavierStokes/R3/WholeSpaceComparisonClosure.lean:32-159` states
   `eq_of_pressure_flux_bound` with an explicit pressure-flux bound as a
   hypothesis. The proof applies the localized energy balance, cutoff Sobolev
   estimates, uniform absorption, Gronwall, and removal of the spatial cutoff.
2. `NavierStokes/R3/PressureRecovery.lean:31-44` defines the comparison
   hypotheses using smoothness, divergence-free equations, equal residuals,
   and uniform finite energy for both fields. The recovery theorem at
   `:391-438` derives the pressure-gradient identity on compact tests from
   those hypotheses; it does not assume a pressure normalization or the final
   flux estimate.
3. `NavierStokes/R3/ActualPressureFlux.lean:47-67` converts the physical
   pressure flux to the canonical Riesz pressure pairing using that recovery
   identity and the divergence equation.
4. `NavierStokes/R3/PressureFlux.lean:496-598` bounds the canonical pairing by
   the difference `L²` bound, the candidate `L³` bound, the tensor `L¹` bound,
   and cutoff/dissipation quantities. The uniform pressure-flux theorem
   supplies one constant for all radii and interior times.
5. `NavierStokes/R3/WholeSpaceUniqueness.lean:30-113` supplies those bounds:
   compact support gives the candidate's finite-energy, `L³`, gradient, and
   cutoff-vanishing estimates; the competitor contributes only smoothness and
   uniform finite energy. It then invokes the closure theorem and obtains
   equality before time one.

## Result

No source-level circularity was found in this route. The final comparison is
not obtained by assuming global agreement, and the pressure estimate is not
introduced as an unproved competitor growth condition. This is a structural
source result, not an independent proof of every imported analytic theorem.

## Remaining checks

- The targeted project interface was not emitted, so the transitive kernel
  axiom set remains pending.
- The analytic lemmas need independent mathematical checking beyond their Lean
  declarations and proof terms, especially pressure recovery and cutoff
  absorption.
- The bridge is specialised to the normalised viscosity-one comparison; the
  separate viscosity scaling remains the correct place to check the general
  `ν > 0` quantifier.

## Classification

`AUD-036`: source-level pressure-flux route is explicit and non-circular;
kernel and analytic validation remain `PENDING`.
