# Pressure-residual non-cancellation audit

`NavierStokes/ProblemStatement.lean:81-85` and
`NavierStokes/R3/ProblemStatement.lean:55-62` define the residual with the
pressure gradient included. The candidate equation is therefore

$$
\mathcal R_\nu(u,p)=f,
$$

not an equation in which a separately specified force must be cancelled by
the pressure.

The zero-sorry probe
`NavierStokesReview/src/probes/PressureResidualNonCancellationProbe.lean`
compiles the exact perturbation identity already established by
`ResidualCalculus.navierStokesResidual_add_sub`:

$$
\mathcal R(u+e,p+q)-\mathcal R(u,p)
=\partial_t e-\Delta e+\nabla q
 +(u\cdot\nabla)e+(e\cdot\nabla)u+(e\cdot\nabla)e.
$$

Its zero-velocity specialisation is

$$
\mathcal R(0,q)-\mathcal R(0,0)=\nabla q.
$$

Thus a nonzero pressure gradient changes the residual. The operator does not
prove an equal-and-opposite cancellation.

`R3/PressureRecovery.lean:31-44` assumes two divergence-free fields with equal
residuals. Its Poisson test is used under those comparison hypotheses, and
`R3/ActualPressureFlux.lean:38-58` transports the result to a pressure-flux
identity. These are genuine comparison results, but they do not impose an
absolute selected-field Poisson representative or `div f = 0`.

For a forced incompressible equation, taking divergence retains the force term:

$$
\Delta p=\nabla\!\cdot f-
\nabla\!\cdot((u\cdot\nabla)u),
$$

when the required derivative commutations are available. Omitting
`\nabla\!\cdot f` silently adds an unproved restriction on the force.

**Disposition:** the selected path still has an absolute pressure-semantics
correspondence gap, but the proposed pressure-annihilation contradiction is
not established.

**Build:** Lean 4.34.0-rc2, zero errors, no `sorry`, no custom axiom.
