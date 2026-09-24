# External-force independence adjudication

## Official statement checked

Fefferman's official problem description says that the initial field and the
components of `f(x,t)` are “given” and describes `f` as an externally applied
force. It then states C/D existentially: there exist a smooth initial field and
a smooth force satisfying the decay conditions for which no globally smooth,
physically reasonable solution exists. The periodic version requires the force
to be periodic and to satisfy the derivative decay bound (9).

The statement does not introduce a separate formal condition of the form

$$
f\ \text{is independent of }(u,p),
$$

nor does it prohibit a proof from constructing a particular smooth function
`f` after constructing candidate fields, provided the final quantified
properties are proved for the same functions.

The CMI prize rules separately require publication, a two-year period, and
general acceptance. They do not add a causal-independence predicate to the
Navier--Stokes equations.

## Repository fact

`NavierStokes/CandidateFromLimits.lean:80-87` defines `force` from `u`, `p`,
and residual-limit data. The exported R3 candidate then packages the resulting
function as an existential `f` and proves the candidate properties. This is a
residual-designed construction, not a forward evolution with a force fixed
before the state is selected.

## Correct mathematical consequence

This creates a serious correspondence and interpretation objection if the
paper represents the force as an independently prescribed physical driver. It
also means that the construction is tautological at the level of the equation
unless the nontrivial velocity, pressure, decay, support, and endpoint claims
are independently established for the same selected fields.

It does not by itself prove `False` from the formal C/D proposition. In an
existential statement, a witness may be defined from other witness components;
after definition it is still a function of `(x,t)`. To obtain a formal
disproof, the review would need either:

1. a source-backed additional admissibility condition requiring independence,
   or
2. a contradiction in one of the actual candidate predicates for the selected
   fields.

The mirror force `-f` does not supply either condition. It is a different
existential input and does not reverse the nonlinear solution associated with
`f`.

## Sources

- Charles L. Fefferman, *Existence and Smoothness of the Navier--Stokes
  Equation*, official CMI problem description, equations (1)--(11):
  `https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf`
- Clay Mathematics Institute, *Rules for the Millennium Prize Problems*:
  `https://www.claymath.org/millennium-problems/rules/`

**Disposition:** correspondence objection confirmed; formal CMI independence
violation not established.
