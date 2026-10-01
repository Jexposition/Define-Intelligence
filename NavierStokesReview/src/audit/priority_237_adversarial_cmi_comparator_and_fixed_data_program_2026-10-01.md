# Priority 237: adversarial CMI comparator, fixed-data, and semantic-edge programme

## Purpose

The attached research note identifies a second audit programme that must run
alongside, not instead of, the selected-field and five-moment work. The review
must test three distinct relationships:

1. Fefferman's official specification ↔ the Lean comparator;
2. the manuscript's mathematical construction ↔ the Lean construction;
3. the internal Lean construction ↔ the exported endpoint.

Compilation is evidence only for the third relationship, and even there only
for the proposition actually compiled. It is not evidence that the comparator
faithfully translates the whole CMI document or that the manuscript's objects
are the objects used by the endpoint.

## Current status and boundaries

The current disposition remains `CTR-005: NOT ESTABLISHED`, not `REFUTED`.
The repair engine is positively traced into the production route, so this
programme must not repeat the obsolete claim that the five-row machinery was
bypassed wholesale. The unresolved questions are the arrows and their
quantifiers:

\[
\text{Fefferman specification}\to\text{Comparator}\to\text{endpoint},
\qquad
\text{manuscript mechanism}\to\text{selected }(u,p,f).
\]

Inverse residual forcing is an audit priority because it creates a provenance
contrast between prescribed data and a field-first residual construction. It
is not, by itself, a proof that Alternative (C) fails. Likewise, an external
report about Fefferman's reaction is not local evidence until its primary
source is fetched and fact-checked.

## Ordered work programme

### 1. Independent comparator reconstruction

Create a review-owned specification, without importing the OpenAI comparator,
for the relevant Fefferman alternatives. Compare predicates extensionally:

\[
\exists E\,\forall t\ge 0\;\|v(t)\|_{L^2}^2\le E
\quad\text{versus}
\quad
\forall t\ge0\,\exists E_t\;\|v(t)\|_{L^2}^2\le E_t.
\]

Audit quantifier order, smoothness at \(t=0\), periodicity, pressure,
spatial decay, force regularity, initial data, and the exact definition of
global solution. Record both inclusions:

\[
\text{Fefferman class}\subseteq\text{Lean class},\qquad
\text{Lean class}\subseteq\text{Fefferman class}.
\]

Neither inclusion may be inferred from similar names.

### 2. Fixed-data reconstruction

Freeze only the selected pair \((u^\circ,f)\), then rebuild the nonexistence
argument in a review namespace without access to the construction history of
the selected singular \((u,p)\). Check that the proof uses only fixed data,
the PDE, and admissibility facts about the hypothetical competitor. If it
needs privileged facts about how \(f\) was reverse-engineered, record a
provenance dependency rather than treating the force as an autonomous datum.

### 3. Force smoothness and flatness arrow

Build a derivative-order ledger for the actual selected residual:

\[
\forall k\;\exists C_k\quad D^k f(t,x)\to D^k f(1,x),
\]

including compatibility of all endpoint limits with one \(C^\infty\) extension.
For every operation in

\[
\text{profile}\to\text{sum}\to\text{curl}\to\text{cutoff}
\to\text{periodisation}\to\text{time switch}\to\mathbb R^3,
\]

prove the relevant flatness/regularity transport for the same selected
object. Do not substitute an abstract `StageEstimates` or `VanishingJointJets`
contract for this arrow.

### 4. Remainder and convention census

Expand the final differential operations and record every product-rule term,
cutoff-gradient term, pressure term, nonlinear term, Jacobian, and boundary
term. Each remainder must be proved cancelled, zero, harmless by support, or
controlled at the required order. Independently check Laplacian and pressure
signs, curl orientation, Fourier and torus normalisation, viscosity scaling,
energy factors, coordinate order, and radial Jacobians.

### 5. Quantifier, limit, and vacuity audit

Search for unsafe movements such as

\[
\forall n\,\exists N(n)\not\Rightarrow\exists N\,\forall n,
\qquad
\forall T<1\,\exists C_T\not\Rightarrow\exists C\,\forall T<1.
\]

Register every `lim`, `tsum`, derivative/sum, integral/sum, endpoint, axis,
and infinity interchange. Check nonempty filters, non-vacuous domains,
support predicates, chart coverage, denominators, and integrability.

### 6. Uniform energy and uniqueness class

Independently trace the selected-field energy estimate through shrinking
support, amplitudes, cross terms, localisation, and infinite stages. Then
compare the weakest Fefferman-admissible global competitor class with the
class accepted by the uniqueness theorem. A contradiction for a strict
subclass does not establish a nonexistence theorem for the larger CMI class.

### 7. Comparator mutation tests

In review-only modules, remove or weaken one comparator condition at a time:
energy, pressure regularity, decay, global smoothness, or pointwise
integrability. Record the first proof edge that fails. This identifies what
the formal nonexistence proof actually uses and whether it proves a stronger
or narrower proposition than the official specification.

## Evidence discipline

Every result receives separate labels for:

| Layer | Question |
|---|---|
| E1 kernel | Does the exact Lean proposition compile? |
| E2 correspondence | Is the declaration the manuscript/CMI object claimed? |
| E3 reconstruction | Does an independent calculation establish the arrow? |
| E4 numerical | Does a non-toy numerical test sanity-check the formula? |

No layer upgrades another. In particular, endpoint compilation does not
upgrade comparator fidelity or manuscript correspondence.

## Non-claims

This priority does not claim that residual-defined forcing automatically
invalidates Alternative (C), that Fefferman has accepted the proof, that the
public history proves concealment, or that an unproved selected-field bridge
is a proved nonzero defect. Those are separate outcomes requiring direct
evidence.

## Required destinations

- review probes and independent specifications: `NavierStokesReview/src/probes`
  and `NavierStokesReview/src/refutations`;
- semantic ledgers and graph reports: `NavierStokesReview/src/audit`;
- positive completion theorems: `NavierStokesReview/src/completions`;
- external/CMI source mappings: `NavierStokesReview/src/external_semantic`;
- machine-readable evidence: `NavierStokesReview/evidence`;
- OpenAI source remains read-only;
- no toy surrogate may be promoted to evidence.

Control dependencies: Priorities 235 and 236, the selected mixed product-rule
completions, the declaration-level manuscript ledger, and the document
consolidation/archive gate.

## Preliminary source extraction: comparator/class boundary

This is a source observation, not a completed semantic verdict.

- `NavierStokes.R3.ProblemStatement.UniformFiniteEnergy` defines one constant
  `E` for every time in the supplied set; the candidate contract uses
  `Ico 0 1`.
- `GlobalFiniteEnergySolution` uses `futureDomain` and `Ici 0`, and its source
  documentation explicitly says that the competitor has no support,
  periodicity, pressure-growth, derivative-growth, or energy-inequality
  assumptions beyond smoothness, the PDE, initial datum, and uniform energy.
- `ComparatorDefinitions.NavierStokesExistenceAndSmoothnessRn` extends the
  global solution predicate with square-integrability at every nonnegative
  time; `ForceConditionDecay` separately quantifies over derivative order and
  decay rate.
- `ComparatorR3Theorem.navier_stokes_breakdown_R3` obtains the selected
  `theorem_1_1` package and
  delegates to `NavierStokesR3.comparator_of_breakdown`. This is a real
  adapter edge that must be checked extensionally, not a proof that the two
  predicates are definitionally identical.

The next source pass must compare the exact fields of
`Comparator.NavierStokesExistenceAndSmoothnessRn` with
`GlobalFiniteEnergySolution`, then independently prove or disprove the two
class inclusions. The preliminary observation does not yet establish a CMI
failure or a comparator mismatch.

## Priority 238 result: the first comparator edge is established

The review-owned probe
`NavierStokesReview/src/probes/CMIComparatorClassInclusionProbe.lean`
compiled with exit code 0 under `leanprover/lean4:v4.34.0-rc2`. It confirms
that `NavierStokesR3.globalSolutionOfComparator` transports a comparator
solution into the R3 `GlobalFiniteEnergySolution` record, including the PDE,
initial datum, incompressibility, smoothness, integrability, and the energy
normalisation. Therefore the existing implication

\[
  \neg\exists\,\texttt{GlobalFiniteEnergySolution}
  \Rightarrow
  \neg\exists\,\texttt{Comparator solution}
\]

is source-backed and kernel-checked. The reverse inclusion remains open, so
this result does not establish class equivalence and does not create a CMI
failure finding. Full evidence is in
`priority_238_cmi_comparator_class_inclusion_2026-10-01.md` and its JSON
record.
