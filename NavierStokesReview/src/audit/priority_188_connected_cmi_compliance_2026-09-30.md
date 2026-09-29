# Priority 188: connected CMI compliance versus manuscript fidelity

**Date:** 2026-09-30  
**Status:** source-checked; formal C/D package established on the inspected
comparator path; manuscript five-moment endpoint fidelity remains
`NOT ESTABLISHED (CTR-005)`

## Finding

Fefferman's “may look for spatially periodic solutions” selects a branch. It
does not waive that branch's requirements. “Thus, we assume” binds `(8),(9)`;
“In place of” replaces the whole-space data controls `(4),(5)` with the
periodic data controls; and “We then accept” binds `(10),(11)`. The phrases
“physically reasonable” and “retaining the heart of the problem” carry the
connected global smoothness, decay, force, domain, and energy meaning into C
and D.

The CMI alternatives must therefore be read as:

\[
C = \exists u^\circ,f\,[\mathrm{Data}_{4,5}
\land \neg\exists(p,u)\,\mathrm{Accepted}_{\mathbb R^3}],
\]

\[
D = \exists u^\circ,f\,[\mathrm{Data}_{8,9}
\land \neg\exists(p,u)\,\mathrm{Accepted}_{\mathbb T^3}],
\]

where the accepted predicates include the PDE, incompressibility, initial
condition, global smoothness, and the relevant energy or periodicity
requirements.

## Lean crosswalk

`ComparatorDefinitions.lean` contains the corresponding connected structures:

* `InitialVelocityCondition` and `InitialVelocityConditionDecay`;
* `ForceCondition` and `ForceConditionDecay`;
* `NavierStokesExistenceAndSmoothness`;
* `NavierStokesExistenceAndSmoothnessRn` with integrability and global energy;
* `InitialVelocityConditionPeriodic`, `ForceConditionPeriodic`, and
  `NavierStokesExistenceAndSmoothnessPeriodic` with periodic velocity and
  pressure.

`ComparatorR3Theorem.navier_stokes_breakdown_R3` and the periodic theorem
therefore prove the repository's formal connected forced C/D propositions on
the inspected path. This is not an equation-only shell.

## Remaining adverse finding

The positive C/D result does not establish that the Lean construction is the
complete construction described in OpenAI's manuscript. The manuscript's five
moments remain load-bearing in its profile matching, modulation restoration,
stress propagation, and correction system. The unresolved selected-field
identity is:

\[
J_{\mathrm{flat}}\Rightarrow
\operatorname{PaperMoments}(u_{\mathrm{selected}},p_{\mathrm{selected}})
=(M,I,J,S,C_p),
\]

after selected sums, curl, localisation, periodisation, torus averaging,
radial integration, support, integrability, and axis limits.

The absence of this endpoint theorem is sufficient for the correspondence
finding `CTR-005`, but not for a selected nonzero moment defect, nonsmooth
force, literal C/D failure, impossibility theorem, or `False`. Any of those
stronger conclusions requires a selected failed connected condition, a
value-level mismatch, an impossibility result, or a contradiction.

## Force provenance

Fefferman's “given, externally applied force” is a physical framing term. The
comparator encodes smoothness and decay, but no separate independence predicate.
OpenAI's manuscript explicitly states that a residual force can be defined for
any incompressible flow and pressure, with the challenge being smooth extension
of the total residual. Thus residual design is a provenance question, not by
itself a literal failure of the existential C/D predicate.

## Sources

* `docs/navierstokes.txt:25-81,89-184`
* `docs/navier-stokes openai.txt:31-47,109-124,306-321`
* `NavierStokes/ComparatorDefinitions.lean:124-243`
* `NavierStokes/ComparatorR3Theorem.lean:21-44`
* `docs/CMI_OpenAI_Full_Semantic_Crosswalk.md`, Priority 188
