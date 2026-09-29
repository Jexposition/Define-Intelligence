# Selected base-profile transport

## Result

The selected base potential is connected to the selected velocity by an
explicit, compiled identity.  In particular,

$$
\operatorname{curl}(A_{\mathrm{selected}})(t,x)
=u_{\mathrm{slow}}(t,x), \qquad t<1,
$$

and the source construction proves

$$
\|u_{\mathrm{slow}}(t,0)\|\longrightarrow\infty
\quad\text{as }t\to1^{-}.
$$

The review completion transports the second statement to the actual selected
potential.  This closes the hypothesis that the base branch is merely an
unconnected potential placeholder.

## Source anchors

- `NavierStokes/TailGaugePotential.lean:464-474` defines
  `constructedPotential` and its curl equality.
- `NavierStokes/TailGaugePotential.lean:467-474` supplies the exact selected
  `EqOn` statement used by the completion.
- `NavierStokes/FinalSlowBase.lean:367-379` proves the selected axis formula and
  `axis_tendsto` for the slow-base velocity.
- `NavierStokesReview/src/completions/SelectedBaseProfileTransport.lean:18-39`
  transports both facts without `sorry`, `axiom`, or `unsafe`.

## Scope

This is positive selected-field evidence.  It does not identify the selected
Cartesian field with the scalar `barMoment` input, does not evaluate a cutoff
commutator, and does not prove `Delta m != 0` or `False`.
