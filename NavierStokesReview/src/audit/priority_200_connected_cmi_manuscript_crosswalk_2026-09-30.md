# Priority 200: connected CMI and manuscript crosswalk

Date: 2026-09-30

Status: source-checked; literal forced endpoint supported; complete manuscript
mechanism correspondence remains `CTR-005: NOT ESTABLISHED`

## Purpose

This tranche checks the complete logical connection instead of isolating
Alternative (C), the force definition, or the five-moment mechanism. It
separates three propositions that earlier discussion repeatedly conflated:

1. Fefferman's literal forced existential target.
2. The Lean proposition exported by the R3 theorem and comparator.
3. OpenAI's stronger claim that the Lean proof is an exact formalisation of
   the manuscript's full construction and explanation.

## Source crosswalk

### Fefferman's CMI specification

The frozen text `docs/navierstokes.txt:25-46` defines a given externally
applied force, imposes the force decay condition (5), and requires a physically
reasonable solution to be globally smooth with bounded energy. The forced
whole-space alternative is stated at `docs/navierstokes.txt:74-81`: for some
smooth admissible initial datum and force, no globally smooth bounded-energy
solution exists.

This language gives the force its forward physical interpretation. It does
not, by itself, add a first-order predicate saying that the force must have
been selected without reference to a constructed trajectory. Therefore the
residual-design route is a causal and modelling objection, not an automatic
logical contradiction of the existential formula.

### OpenAI's manuscript

The manuscript states its theorem at `docs/navier-stokes openai.txt:31-45`.
It claims a smooth compactly supported force, smooth pre-singular velocity and
pressure, the residual equation, incompressibility, zero initial velocity,
compact spatial support, and unbounded velocity as (t\uparrow1), followed by
the no-global-smooth-bounded-energy consequence.

The manuscript also makes the constructional dependencies explicit:

- `docs/navier-stokes openai.txt:109-124` defines the force as the residual
  and says that divergent individual terms require cancellation so the sum
  and all derivatives extend smoothly.
- `docs/navier-stokes openai.txt:307-321` describes the background stress,
  oscillatory pulses, successive corrections, summation, localisation, and
  smooth compactly supported force as one connected construction.
- `docs/navier-stokes openai.txt:695-735` distinguishes four correction
  operations and then solves the five radial moment equations. The moments
  preserve two integrals and cancel three radial-integral defects.
- `docs/navier-stokes openai.txt:746-757` states that cut-off vector
  potentials and pressures are summed, the residual is compared with a finite
  stage, and leading velocity growth is preserved.
- `docs/navier-stokes openai.txt:2145-2244` explicitly computes the
  (O(N^{-1})) moment error after shear modulation and solves the five
  correction equations to restore the moments exactly.

Thus the five-moment repair is not optional exposition in the manuscript. It
is part of the stated construction. The manuscript also contains other
operations, including wave-amplitude equations, covariance corrections,
pressure reconstruction, auxiliary-time inversion, curl/cutoff summation,
and residual estimates. The source does not support the stronger claim that
the five moments are the only cancellation mechanism.

### Lean's whole-space endpoint

`NavierStokes/R3/ProblemStatement.lean:92-109` defines the selected candidate
properties: pre-singular smoothness, compact spatial support, globally smooth
force, compact positive-time force support, zero initial data,
incompressibility, the Navier--Stokes residual equation, energy boundedness on
(0\le t<1), and speed unboundedness at one.

`NavierStokes/R3/ProblemStatement.lean:119-153` defines the competing global
finite-energy solution and the full `breakdownStatement` with the same force
and datum. `NavierStokes/R3/Theorem.lean:26-49` proves the selected fields and
then proves `theorem_1_1 : ProblemStatement.breakdownStatement`.

`NavierStokes/ComparatorR3Theorem.lean:21-35` transfers the compact candidate
to the comparator's whole-space quantifiers, and
`ComparatorR3Theorem.lean:37-44` proves
`navier_stokes_breakdown_R3` from `NavierStokesR3.theorem_1_1`. The current
record therefore supports the following limited but positive statement:

\[
\text{Lean proves the formalised forced CMI-shaped endpoint proposition.}
\]

It would be incorrect to call that endpoint empty, a zero-velocity
countermodel, or a proof that merely assumes `NativeBounds` at the public
boundary.

### Where the correspondence remains incomplete

`ActualCandidateAssembly.lean:1079-1098` shows actual physical data feeding
the stage estimates. `ActualCycleResidualBounds.lean:1156-1172` derives
residual rates from `PhysicalData`, state realisation, exterior germs, and
native residual estimates. `CandidateFromLimits.lean:45-112` derives the
smooth force from residual recurrences and locally uniform limits.

However, `ActualCandidateAssembly.lean:1121-1151` defines the exported
`Witness` without a named final equality identifying the selected mixed
Cartesian velocity, pressure, residual, or force with the manuscript's
((M,I,J,S,C_p)). `selected_witness` at `1177-1181` proves that proposition,
and `selected_candidate` at `1183-1185` projects it into the top-level
candidate statement, without adding that observable-identification theorem.

This is not evidence that the selected moments are false. It is evidence that
the current formal record has not closed the stronger equivalence

\[
\text{manuscript five-moment construction}
\equiv
\text{selected Cartesian/pressure/force construction used in the endpoint}.
\]

The active upstream machinery may be used internally to prove coefficient
matching, finite Cartesian residual identities, residual rates, and flatness.
The remaining audit task is to locate or formalise an equivalent selected-path
transport theorem, not to assume that its absence from `Witness` proves a
field defect.

## Axiom and escape check

Fresh replay of
`NavierStokesReview/src/audit/WholeSpaceAxiomAudit.lean` under the repository
toolchain `leanprover/lean4:v4.34.0-rc2` reports only
`propext`, `Classical.choice`, and `Quot.sound` for the queried endpoint
theorems. A targeted scan of the endpoint files found no explicit `axiom`,
`sorry`, `admit`, `unsafe`, or `implemented_by` token. `noncomputable` and
classical choice are ordinary Lean mechanisms and are not compiler escapes.

The axiom result does not prove paper fidelity. It only removes one possible
explanation for the endpoint behaviour.

## Adjudication

| Claim | Current status |
| --- | --- |
| Literal Fefferman forced target is represented in Lean | Supported by `R3/ProblemStatement`, `R3/Theorem`, and `ComparatorR3Theorem`. |
| OpenAI's force and moment mechanism is irrelevant | Rejected by the manuscript text and source construction. |
| The selected endpoint is an empty generic-rate shell | Rejected by the physical-data and residual-rate declarations. |
| The final selected Cartesian fields are identified with the five paper moments | Not established in the inspected export. |
| The selected field has a nonzero moment defect | Not proved. |
| The force is nonsmooth or Fefferman's forced alternative fails | Not proved by this audit. |
| OpenAI's exact paper-to-code correspondence is established | Not established; `CTR-005` remains. |
| A kernel contradiction or compiler escape was found | No. |

## Controlled conclusion

The correct conclusion is not that the Lean theorem “works without” the
paper's mathematics, nor that the entire CMI proposition is already refuted.
The Lean endpoint formally proves a forced whole-space breakdown proposition
with substantial constructional dependencies. The audit still cannot credit
the stronger public claim that the Lean proof is an exact machine-checked
formalisation of every load-bearing manuscript mechanism, because the
selected-path identification of the final fields with the five-moment system
has not been located or proved.
