# Paper-nuance crosswalk: Fefferman and the OpenAI construction

**Date:** 2026-09-27
**Scope:** checked-in PDFs `docs/navierstokes.pdf`,
`docs/navier-stokes openai.pdf`, and `docs/euler.pdf`, cross-checked against
the current Lean source.

## 1. Fefferman's CMI statement

The official statement defines the force components as a given externally
applied force and specifies smooth, divergence-free initial data. Its whole-
space conditions require rapid spatial decay of the initial data and of every
space/time derivative of the force, together with a globally smooth solution
and bounded energy for all nonnegative time. Alternative (C) is existential:
it asks for smooth data satisfying those hypotheses for which no global
physically reasonable solution exists. The periodic alternative (D) similarly
requires periodic data, time decay of force derivatives, and a global smooth
periodic solution if one exists.

The wording does **not** introduce a formal predicate saying that `f` must be
syntactically independent of the eventual solution `u`. “Given, externally
applied” is a physical/provenance description. It remains relevant to the
interpretation of the construction, but it cannot by itself yield a Lean
contradiction against an existential residual construction.

The statement's errata also matter: pressure periodicity is meant to be
explicit in the periodic data, and the weak formulation has a sign/notation
correction. Any code-to-CMI comparison must check those details rather than
relying on a generic label such as “periodic”.

## 2. OpenAI's Navier--Stokes paper

The paper explicitly adopts the residual-design method. It states that one
may choose an incompressible flow and pressure and define the external force
as the momentum residual; the hard part is arranging cancellation so that the
residual and all derivatives extend smoothly through the singular time. Its
global packaging then localises the velocity and pressure, defines the force
from the residual before the singular time, and extends it smoothly.

This makes the following review claim too strong if stated without an extra
assumption:

> “Because the force is defined from the selected solution, the CMI theorem is
> automatically invalid.”

The defensible claim is narrower and stronger: the Lean endpoint must be shown
to realise the same construction described in the paper. In particular, the
selected Cartesian field must be connected to the paper's five moments,
correction equations, pressure construction, cutoffs, residual cancellation,
and whole-space nonexistence argument. The current source map identifies
those joins as obligations rather than treating the residual method itself as
illegal.

The paper's theorem is also more specific than a generic pre-singular
predicate: it advertises a force in a smooth compact-support class, fields on
the pre-singular interval, and a contradiction with any global smooth
finite-energy continuation having the same datum and force. The Lean endpoint
has a corresponding `CandidateProperties`/`GlobalFiniteEnergySolution`
contract, but the paper-to-selected-field identification remains the active
CTR-005 question.

## 3. OpenAI's Euler paper

The Euler paper describes exact smooth parent/child solutions on nested time
intervals, with stage corrections, a limiting time, and stability estimates.
It does not support an audit claim that a temporal kink or a Zeno collapse
follows merely from the existence of nested intervals. Those are hypotheses
to test against the actual source, not conclusions from the paper's diagram.

The companion audit must therefore ask whether the Lean code proves the
parent-to-child identities, derivative matching, summability, gradient growth,
and stability-to-blow-up passage that the paper uses. It must not infer a
patching contradiction from file names or from a discrete constructor alone.

## 4. Correct burden of proof

The review separates two questions:

1. **Formal endpoint validity:** does Lean prove the exported C/D-shaped
   proposition under its declared predicates?
2. **Paper-to-code correspondence:** does the selected endpoint prove the
   construction and interpretation advertised in the papers and required by
   Fefferman's stated alternatives?

The present evidence supports a live correspondence objection under CTR-005:
the endpoint does not expose a field-level theorem transporting the paper's
five named moments through the selected Cartesian sum, pressure, residual,
and whole-space packaging. It does not support the claim that residual-defined
forcing is automatically disallowed, nor does it support an unconditional
selected-path `False` theorem.

## 5. Source anchors

| Claim | Source anchor |
|---|---|
| Whole-space and periodic CMI alternatives, decay, smoothness, energy | `docs/navierstokes.pdf`, pp. 1--3 and errata |
| Residual-defined force and smooth cancellation | `docs/navier-stokes openai.pdf`, opening sections, residual-construction section, and whole-space packaging section |
| Five cumulative moments and stage correction mechanism | `docs/navier-stokes openai.pdf`, Section 9 and Appendix A |
| Parent/child exact stage construction and limiting argument | `docs/euler.pdf`, abstract, Theorem 1.1, opening construction, and stage/stability sections |
| Active endpoint predicate | `NavierStokes/R3/ProblemStatement.lean:57-109, 138-151` |
| Exported theorem | `NavierStokes/R3/Theorem.lean:46-79` |
| Selected witness junction | `NavierStokes/ActualCandidateAssembly.lean:1121-1185` |
