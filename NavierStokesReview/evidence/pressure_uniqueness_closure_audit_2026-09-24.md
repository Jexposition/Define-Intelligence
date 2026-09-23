# Pressure and whole-space uniqueness closure audit

**Date:** 2026-09-24  
**Branch:** `review/cmi-first-navier-stokes-2026-09-22`  
**Scope:** the selected R³ comparison path, not a re-build of the upstream source

## Result

The proposed compact-pressure trivialisation attack is not established by the
inspected code. `CandidateProperties.pressure_support` gives compact spatial
support to each pre-singular pressure slice, but the whole-space comparison
theorem does not infer zero pressure or zero velocity from that field alone.
The pressure comparison is tested against compact spatial functions and is
recovered from the residual equation and divergence-free hypotheses.

The checked source path is:

1. `R3/PressureRecovery.lean` derives the compact-test differentiated Poisson
   identity and `gradient_recovery` from the two residual equations.
2. `R3/ActualPressureFlux.lean` converts that gradient identity into the
   cutoff pressure-flux pairing.
3. `R3/PressureFlux.lean` constructs one uniform flux constant from the
   pressure-recovery hypotheses and the displayed L²/L³/tensor bounds.
4. `R3/WholeSpaceComparisonClosure.lean` constructs the scalar rate bound
   internally through `ComparisonRateBound.exists_uniform_rate_bound`.
5. `R3/WholeSpaceUniqueness.lean` supplies compact support only for the
   candidate velocity and derives the competitor comparison before time one.

The zero-sorry environment probe
`NavierStokesReview/src/probes/IntermediateAxiomProbe.lean` reports only
`propext`, `Classical.choice`, and `Quot.sound` for the pressure-recovery,
pressure-flux, closure, and uniqueness endpoints. This is dependency evidence,
not a proof that every analytic lemma has the intended mathematical meaning.

## Exact limitation that remains

The pressure chain is an internal proof of the declared comparison interface.
It does not prove the separate paper-to-code correspondence claim that the
selected exported candidate carries the paper's named moment tuple
`(M, I, J, S, C_p)`. That missing transport theorem remains CTR-005. It is a
semantic correspondence objection, not a pressure contradiction or a Lean
kernel inconsistency.

## Disposition

`Compact pressure support implies trivial velocity`: **not demonstrated**.  
`Pressure comparison is an unproved external premise`: **cleared for the
inspected endpoint**.  
`Paper five-moment data are transported into the selected endpoint`: **still
unresolved**.
