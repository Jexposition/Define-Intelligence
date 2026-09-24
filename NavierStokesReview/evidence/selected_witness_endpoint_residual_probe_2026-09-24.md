# Selected-witness endpoint residual probe

## Result

The new probe compiles with zero errors and contains no `sorry`:

`NavierStokesReview/src/probes/SelectedWitnessEndpointResidualProbe.lean`

It establishes three facts about the actual selected endpoint:

1. `selected_witness` supplies `CandidateProperties u p f` for concrete
   velocity, pressure, and force fields.
2. The selected schedule has an actual origin speed blow-up and its actual
   mixed residual tends to zero at the same origin endpoint.

3. On `0 < t < 1`, any `CandidateProperties` package identifies its
   Navier–Stokes residual with its selected force:

   $$\mathcal R(u,p)(t,x)=f(t,x).$$

4. If there are constants `c > 0` and `B` such that, eventually as
   `t → 1⁻`,

   $$c\lVert u(t,0)\rVert\leq\lVert\mathcal R(u,p)(t,0)\rVert$$

   and

   $$\lVert f(t,0)\rVert\leq B,$$

   then the selected speed blow-up yields `False`.

The fourth result is the force-smoothness counter-strike in its conditional
form. More strongly, the selected-path theorem
`selected_origin_positive_lower_bound_is_impossible` proves that the actual
selected residual tending to zero and the actual selected origin speed
blowing up make every fixed positive velocity-to-residual lower bound
impossible.

## Source trace

- `NavierStokes/ProblemStatement.lean:105-114` defines the candidate force,
  residual identity, smoothness, and speed consequences.
- `NavierStokes/ActualCandidateAssembly.lean:1177` supplies the selected
  witness.
- `NavierStokes/MixedDiagonalResidual.lean:45` identifies the mixed residual
  with the full Navier–Stokes residual of the assembled fields.
- `NavierStokes/CandidateFromLimits.lean:86-111` proves force smoothness only
  from residual-limit and extension premises and gives interior residual
  agreement.
- `NavierStokes/FinalSlowBase.lean:330-356, 542-551` records the construction's
  residual decomposition and flat error/core-stress route.

## Audit conclusion

The force attack has reached a precise boundary. The selected source proves
the cancellation pattern needed for residual flatness while the selected
origin speed diverges. Consequently, the proposed positive lower-bound route
is formally impossible for the selected raw residual. A remaining
unconditional refutation would need a different theorem, such as a proof that
the raw residual is not the same field as the force used by the final
`CandidateProperties`, or a false premise in the residual-flatness transport.
The probe does not itself establish either failure.
