# Trust and CMI completion criteria

Date: 2026-09-22  
Repository snapshot: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`

## Two separate gates

The review uses two gates that must not be conflated:

1. **Formal integrity:** the exported Lean declarations must be replayable
   under the declared toolchain, their transitive axioms must be independently
   captured, and no `sorryAx`, native-evaluation axiom, or unreviewed custom
   axiom may support the result.
2. **CMI mathematical and procedural acceptance:** the proposition proved must
   match one official CMI alternative, the analytic argument must be
   independently understood and accepted by mathematicians, and CMI's
   publication, two-year, and general-acceptance procedure must be satisfied.

Lean evidence can close part of the first gate. It cannot close the second.

## Authoritative CMI obligations

The official Fefferman statement gives the following obligations for the
forced whole-space alternative (C):

| ID | Obligation | Required content |
|---|---|---|
| C1 | Equation | Classical incompressible Navier–Stokes on `R^3 × [0,∞)`, positive viscosity, pressure gradient and spatial Laplacian with the stated signs. |
| C2 | Initial field | Smooth, divergence-free `u⁰`; every spatial derivative decays faster than every polynomial. |
| C3 | Force | Smooth `f(x,t)` on the future half-space; every mixed spatial/time derivative decays faster than every polynomial in `1+|x|+t`. |
| C4 | Nonexistence class | No pair `(p,u)` satisfies the PDE, divergence, initial condition, smoothness, and uniformly bounded kinetic energy on the whole future domain. |
| C5 | Quantifier | The same fixed force and initial field must be used in the negated global-solution statement. |

The periodic alternative (D) changes the domain and replaces C2/C3 decay in
space with spatial periodicity of initial data and force, temporal decay of
all force derivatives, and periodicity of the accepted velocity and pressure.
The erratum explicitly adds pressure periodicity.

## Independent Lean trust obligations

The official Lean documentation defines `#print axioms` as a transitive audit
of all declarations used by a theorem. The following output is required for
each exported result:

```text
#print axioms NavierStokes.Comparator.navier_stokes_breakdown_R3
#print axioms NavierStokes.Comparator.navier_stokes_breakdown_periodic
#print axioms Euler.euler_breakdown_R3
#print axioms Euler.exists_compact_smooth_euler_singularity
```

Acceptable foundational output is limited to Lean's standard
`propext`, `Classical.choice`, and `Quot.sound`. `sorryAx` is disqualifying
for a claimed completed proof. Native-evaluation axioms and project-specific
axioms require separate justification and are not accepted by the default
review rule. The repository's `formalization.yaml` is self-assessed metadata,
not an independent kernel report.

## Current state

| Gate | Status | Evidence |
|---|---|---|
| C1-C5 source predicate mapping | Source-level mapped; final equivalence audit open | `docs/OpenAI_NavierStokes_Peer_Review_v1.md` |
| Periodic D mapping | Source-level mapped; final equivalence audit open | `NavierStokes/PeriodicPaperTheorem.lean`, `PeriodicComparatorSolution.lean` |
| Challenge placeholder isolation | Four lexical `sorry` lines isolated in the separate challenge target; none appears in the audited Navier–Stokes or Euler headline axiom reports | `docs/OpenAI_NavierStokes_Axiom_Ledger.md`; headline reports |
| Transitive kernel axioms | All four Navier–Stokes and both Euler headline declarations report only standard axioms | `HEADLINE_AXIOMS_4_34_RC2.txt`; `PREEXPORT_AXIOMS_4_34_RC2.txt`; `EULER_AXIOMS_4_34_RC2.txt` |
| Human PDE peer review | Not established by Lean or repository metadata | CMI rules and independent literature review |
| CMI procedural acceptance | Not established | Official CMI rules |

## Decision rule

Until every row above is independently evidenced, the review must not label
the claim “CMI-proven”. If a formal mismatch or untrusted dependency is found,
the report may issue a negative finding for the affected route. If all source
and kernel obligations pass, the result remains a formal verification input to
human peer review rather than an automatic CMI resolution.
