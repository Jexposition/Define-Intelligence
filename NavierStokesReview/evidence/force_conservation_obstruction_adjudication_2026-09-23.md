# Force-conservation obstruction: adjudication

## Question

Can the candidate be refuted under the CMI formulation by proving either

\[
\int_{\mathbb R^3} f(x,t)\,dx \ne 0
\quad\text{or}\quad
\nabla\cdot f \ne 0?
\]

## Source result

No. These conditions are not part of the stated forced alternatives. The local
predicate in `NavierStokes/R3/ProblemStatement.lean` requires a globally smooth
force with positive-time compact support and rapid derivative decay. It does
not require the external force itself to be divergence-free or to have zero
spatial integral.

`NavierStokes/R3/PositiveTimeForce.lean` defines

```lean
def force (f : VelocityField) : VelocityField :=
  fun z => timeCutoff z.1 • f z
```

This wrapper contains no pressure-gradient term. The pressure term enters
upstream through `navierStokesResidual` in
`NavierStokes/CandidateFromLimits.lean`, where the force agrees with the
activated residual for `0 ≤ t < 1` and receives a smooth endpoint extension.

## Adjudication

The proposed equal-and-opposite argument is therefore not a counterexample to
the formal C/D statement. An external force may inject net momentum; the
internal action-reaction cancellation applies to internal stresses, not to an
arbitrary prescribed external body force. Likewise, incompressibility requires
the velocity field to be divergence-free. It does not require the body force
to be divergence-free, because pressure can absorb the gradient component.

This does not certify the candidate. The live audit remains whether the actual
selected residual has the endpoint limits needed by `CandidateFromLimits`, and
whether the resulting force satisfies every explicit smoothness, support,
decay, PDE, and energy predicate. A conservation-law result would become
decisive only if the relevant extra identity were proved from the exact CMI
hypotheses or from a separately justified physical admissibility condition.

## Evidence boundary

- Closed: the cutoff is smooth and active at `t = 1`; it is not a step-function loophole.
- Closed: `PositiveTimeForce.force` is not itself the residual formula.
- Open: selected-path residual-limit adequacy and complete paper-to-code moment transport.
- Not a proof: the suggested `sorry` theorem about a force norm tending to `atTop`.

**Classification:** physical-realizability concern and provenance issue; not a
formal CMI refutation.
