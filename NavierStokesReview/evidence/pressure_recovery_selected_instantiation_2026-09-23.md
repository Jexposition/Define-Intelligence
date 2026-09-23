# Selected pressure-recovery instantiation

Date: 2026-09-23  
Scope: `NavierStokes/R3/WholeSpaceUniqueness.lean` and its imported pressure chain

## Finding

The earlier statement that pressure recovery had not been instantiated for the
selected candidate was too strong. The selected candidate is passed into the
comparison theorem.

`WholeSpaceUniqueness.classical_uniqueness_on_Icc` constructs
`PressureRecovery.Hypotheses` at lines 45–47 from the reference and competitor
fields. It then calls
`PressureFlux.exists_uniform_actual_pressure_flux_bound` at lines 60–61.
`candidate_unique_on_Icc` supplies the selected candidate properties to that
theorem at lines 86–97, and `candidate_global_agrees_before_one` invokes the
same route for the global competitor at lines 104–117.

The pressure chain therefore has this verified source-level shape:

```text
selected CandidateProperties
  -> classical_uniqueness_on_Icc
  -> PressureRecovery.Hypotheses
  -> actual pressure-flux bound
  -> WholeSpaceComparisonClosure
  -> agreement before t = 1
```

## What this does and does not establish

This removes the objection that the pressure-recovery modules are dead or that
the endpoint consumes an unconnected pressure-flux premise. It does not prove
that the analytic lemmas are mathematically sound merely because they compile.
The remaining review task is to inspect the analytic estimates inside
`PressureRecovery`, `PressureFlux`, and `WholeSpaceComparisonClosure`, rather
than to claim that no selected-path pressure use exists.

The compact-support argument remains separate. `CandidateProperties.pressure_support`
is not used to derive pressure recovery, and compact support alone does not imply
that a pressure slice is zero. No pressure trivialisation contradiction was
found.

## Source anchors

- `NavierStokes/R3/WholeSpaceUniqueness.lean:30–68`
- `NavierStokes/R3/WholeSpaceUniqueness.lean:72–100`
- `NavierStokes/R3/WholeSpaceUniqueness.lean:102–117`
- `NavierStokes/R3/PressureRecovery.lean:33–44, 391–438`
- `NavierStokes/R3/PressureFlux.lean:576–599`

Status: correction to the pressure audit; no formal disproof.
