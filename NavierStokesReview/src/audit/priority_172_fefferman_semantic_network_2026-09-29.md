# Priority 172: Fefferman's connected semantic network and the selected CMI endpoint

Date: 2026-09-29
Status: source-grounded adjudication; no selected-field refutation claimed

## Purpose

This record prevents the CMI specification from being read as a list of
detached equation labels. It treats Fefferman's definitions, connectives,
admissibility conditions, branch choice, and alternatives as one semantic
network. The controlling source is the checked-in extraction
`docs/navierstokes.txt`, lines 25--81, together with the supplied CMI PDF.

The audit does not rewrite Fefferman's wording. The exact source quotation is
preserved in `docs/CMI_OpenAI_Full_Semantic_Crosswalk.md`. The present file
records the logical and physical dependencies created by that wording and
cross-checks them against the selected Lean path.

## 1. Source nodes and their connections

### Node F1: the mathematical model

Fefferman begins with unknown velocity `u(x,t)`, pressure `p(x,t)`, position
`x`, forward time `t >= 0`, incompressibility, viscosity, and the equations
(1)--(3). Equation (1) is not presented as a free symbolic identity. It is
explained as Newton's law for a fluid element subject to the external force,
pressure, and friction; equation (2) is the incompressibility constraint.

**Connection F1 -> F2.** The solution object is a fluid velocity-pressure
field on the stated space-time domain, not merely a reduced profile, a vector
potential, a residual jet, or a finite-dimensional correction state.

### Node F2: force and initial data are problem data

Fefferman calls `u^o` a given smooth divergence-free field and `f_i(x,t)` the
components of a given, externally applied force. This establishes the force
and initial field as data of the problem formulation. It does not, by itself,
introduce a formal first-order predicate saying that a force may never have
been designed after a trajectory. It does establish the physical meaning that
the audit must test against a residual-defined construction.

**Connection F2 -> F3.** A candidate force cannot be assessed only by the
identity `f = residual(u,p)`. It must also be checked as an admissible force
datum under (4), (5), or under (8), (9) on the periodic branch.

### Node F3: “For physically reasonable solutions ... Hence”

Fefferman's “For physically reasonable solutions” introduces the reason for
restricting attention to data whose derivatives decay. “Hence” connects the
physical requirement that velocity not grow at spatial infinity to the
all-order decay assumptions (4) and (5). These are not optional prose around
the PDE; they define the data class used by the alternatives.

For the whole-space branch, the force condition is

\[
 |\partial_x^\alpha\partial_t^m f(x,t)|
 \le C_{\alpha m K}(1+|x|+t)^{-K}
\quad\text{for every }\alpha,m,K.
\]

The initial field has the corresponding all-order spatial decay in (4).

**Connection F3 -> F4.** The decay conditions constrain the prescribed data,
not only a solution found later. Compact smooth support is one strong route to
these inequalities, but the audit must verify the route rather than infer it
from a field name.

### Node F4: “only if” defines the accepted solution class

Fefferman writes “We accept a solution ... as physically reasonable only if it
satisfies” (6) and (7). The word “only” makes global smoothness and bounded
energy necessary conditions for the accepted whole-space solution class:

\[
 p,u\in C^\infty(\mathbb R^n\times[0,\infty)),
 \qquad
 \int_{\mathbb R^n}|u(x,t)|^2\,dx<C
 \quad\text{for every }t\ge0.
\]

**Connection F4 -> F5.** A pre-singular field on `0 <= t < 1` is not itself a
physically reasonable global solution. In Alternative (C), the pre-singular
candidate is instead used to prove that no globally accepted solution exists
for the same data.

### Node F5: “Alternatively ... may look ... Thus” creates a complete branch

“Alternatively, to rule out problems at infinity, we may look for spatially
periodic solutions” is a branch choice. It does not waive the requirements.
“Thus” introduces the periodic data hypotheses (8), replaces the whole-space
decay conditions (4), (5) with (8), (9), and Fefferman then gives the
corresponding accepted-solution conditions (10), (11).

The periodic branch is therefore:

\[
 (8),(9)\ \text{for the data}
 \quad+\quad
 (10),(11)\ \text{for an accepted global solution}.
\]

It is not valid to cite periodicity as a convenience while silently retaining
only local smoothness or omitting periodicity of the pressure. The erratum
also explicitly records the missing periodic pressure condition.

### Node F6: “such smooth, physically reasonable solutions” and “retaining the
heart”

The phrase “such smooth, physically reasonable solutions” refers back through
F1--F5. It carries the equation, data class, branch, global smoothness, and
energy/periodicity meanings into the next sentence. “To give reasonable leeway
to solvers while retaining the heart of the problem” means that A--D are
alternative formulations of the same global existence/smoothness problem, not
permission to prove an unrelated existential proposition with a matching
surface syntax.

**Connection F6 -> F7.** A CMI audit must compare the selected endpoint with
the complete alternative it claims to instantiate, not only with the displayed
equations (1)--(3).

## 2. The actual whole-space C dependency

Alternative (C) has the following connected predicate:

\[
\begin{aligned}
&\nu>0,\quad n=3,\\
&\exists u^\circ,f:\quad
 u^\circ\text{ smooth and divergence-free},\\
&\qquad f\text{ smooth and satisfying (4),(5)},\\
&\qquad \neg\exists(p,u)\text{ on }\mathbb R^3\times[0,\infty):
 (1)\land(2)\land(3)\land(6)\land(7).
\end{aligned}
\]

The final negated existential is about a hypothetical global solution for the
same initial data and force. It is not the assertion that the constructed
pre-singular field itself belongs to (6), because that would contradict its
finite-time blow-up. The constructed pre-singular field supplies the
comparison argument; the prohibited competitor is the field required to
satisfy the global acceptance class.

## 3. What the selected Lean path actually establishes

The checked selected path is not empty and does not obtain `NativeBounds` from
an unproved `sorry` premise. Its relevant chain is:

```text
ActualCandidateAssembly.physicalData
  -> GluedStageEstimates.actualStageEstimates
  -> ActualCycleResidualBounds.finite_residual_rates
  -> StageEstimates / residual-rate data
  -> VanishingJointJets and locally-uniform residual limits
  -> CandidateFromLimits.tracedResidual_smooth
  -> CandidateFromLimits.force_smooth
  -> CandidateProperties
  -> whole-space comparison and no global finite-energy solution
  -> ComparatorR3Theorem.navier_stokes_breakdown_R3
```

The positive findings are:

1. `CandidateFromLimits.force_smooth` is derived from actual residual-limit and
   derivative-recurrence hypotheses. It is not justified by the false premise
   that velocity blow-up forces every residual summand to diverge.
2. `CandidateFromLimits.force_eq_activated_residual` identifies the extended
   force with the activated residual for `0 <= t < 1`.
3. The R3 candidate records smoothness on the pre-singular domain, compact
   spatial support, a globally smooth force, positive-time force support, the
   residual equation, incompressibility, and finite energy on `0 <= t < 1`.
4. `R3.ComparatorBridge` converts a hypothetical global comparator solution
   into a `GlobalFiniteEnergySolution` with the same force and zero initial
   datum. The comparison contradiction is therefore substantive.
5. `ComparatorR3Theorem.navier_stokes_breakdown_R3` has the C-shaped
   existential structure and is proved from `NavierStokesR3.theorem_1_1`.

These facts mean that it is incorrect to call the formal C-shaped path an
empty shell or a compiler cheat.

## 4. What remains unestablished for the paper's claimed mechanism

The OpenAI manuscript says that the background residual is singular, that
oscillatory pulses and later corrections cancel the singular part, and that
the five cumulative radial moments organise the matching and repair mechanism.
The extracted manuscript explicitly states that the residual is defined from
the chosen flow and pressure, while the challenge is to make that residual and
all derivatives extend smoothly through the singular time. The manuscript's
five moments are therefore scientifically load-bearing, even though the
manuscript also uses wave fluxes, cutoffs, pressure reconstruction, covariance
corrections, time inversion, and nonlinear estimates.

The selected Lean endpoint still has no inspected theorem of the form

\[
 \operatorname{Moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
 = (M,I,J,S,C_p),
\]

nor a theorem proving that the five reduced-profile quantities are preserved
through the completed selected potential sums, spatial curl, localisation,
periodisation, activation, and endpoint observables. The existing probes prove
type-level non-entailment: the exported `Witness` contract can coexist with an
abstract nonzero debt parameter. They do not prove that the concrete selected
field has a nonzero physical defect.

This is the exact audit boundary:

```text
Concrete residual/rate/jet/force route: established on the inspected path.
Full Fefferman-shaped C endpoint: established on that formal route, subject to
the repository build and source assumptions recorded in the evidence.
Paper-specific five-moment transport into the selected Cartesian endpoint:
NOT ESTABLISHED (CTR-005).
Concrete selected mismatch, force nonsmoothness, impossibility, or False:
NOT PROVED.
```

The distinction is not contradictory. A final theorem can prove a proposition
through a concrete residual-limit route without exposing every intermediate
scientific invariant in its public type. That can establish the final formal
CMI-shaped proposition. It cannot, without an additional bridge theorem,
establish that the final formal proof is the five-moment proof described in the
manuscript.

Conversely, the absence of the bridge is not enough to conclude that the
formal C proposition is false. To make that stronger claim, the audit must
prove at least one of the following against the selected concrete fields:

1. a failed force or initial-data condition (4) or (5);
2. a failed global-comparison premise used to derive nonexistence;
3. a concrete nonzero selected moment defect;
4. an impossibility theorem showing that the selected construction cannot
   realise the required cancellation; or
5. a selected-path contradiction or `False`.

## 5. Adjudication matrix

| Connected requirement | Source meaning | Selected Lean evidence | Status |
|---|---|---|---|
| Equations (1)--(3) | PDE, incompressibility, initial datum | Residual, divergence, and initial-condition fields | Substantially established |
| Given force data | Force is a stated problem datum with external-force interpretation | Force is globally smooth and agrees with activated residual before the singular time | Formal datum established; provenance correspondence remains a semantic question |
| Whole-space data decay (4),(5) | All-order spatial and space-time decay | Zero initial datum and compact smooth force imply the comparator decay contract | Established on selected comparator path |
| Accepted global solution class (6),(7) | Global smoothness and bounded energy for every nonnegative time | Required in `GlobalFiniteEnergySolution` and comparator theorem | Established as the prohibited competitor class |
| Periodic alternative | Separate branch with (8),(9),(10),(11) | Not interchangeable with whole-space C | Must remain separate; no branch waiver |
| Manuscript five-moment mechanism | Reduced-profile matching and residual repair | Upstream machinery is genuine; final selected-field equality is absent | CTR-005, not a concrete refutation |
| Literal C-shaped formal proposition | Existential admissible data plus no global accepted solution | `navier_stokes_breakdown_R3` | Established on inspected Lean path, not proof of full manuscript correspondence |

## 6. Required next source checks

1. Trace `H.debt`, `H.masses`, and `FiveRowRank` through the actual selected
   `physicalData`, potential sums, curl/localisation, periodisation, activation,
   and endpoint comparison declarations.
2. Search for definitionally equivalent observable maps, not only the names
   `M`, `I`, `J`, `S`, and `C_p`.
3. Check whether the concrete residual-rate hypotheses used by
   `CandidateFromLimits` are themselves proved from the same five-moment
   cancellation mechanism or from a separate complete estimate chain.
4. Keep the CUDA 3D cutoff result as a diagnostic of an explicit profile family,
   never as a theorem about `selected_witness`.
5. Only promote the verdict beyond `CTR-005` after a selected concrete mismatch,
   failed mandatory premise, impossibility theorem, or contradiction is proved.

## Evidence and source map

- Fefferman source: `docs/navierstokes.txt:25-81` and `docs/navierstokes.pdf`.
- Full semantic crosswalk: `docs/CMI_OpenAI_Full_Semantic_Crosswalk.md`.
- OpenAI manuscript: `docs/navier-stokes openai.txt:109-124; 307-319; 984-1024`.
- Selected endpoint: `NavierStokes/ActualCandidateAssembly.lean`.
- Residual-to-force route: `NavierStokes/CandidateFromLimits.lean`.
- Whole-space C bridge: `NavierStokes/R3/ComparatorBridge.lean` and
  `NavierStokes/ComparatorR3Theorem.lean`.
- Existing endpoint probes: `NavierStokesReview/src/probes/SelectedMomentBridgeAudit.lean`,
  `SelectedPhysicalDataMomentInterfaceProbe.lean`,
  `SelectedWitnessPathProbe.lean`, and `GlobalTransportBridgeProbe.lean`.
- Numerical boundary: `NavierStokesReview/evidence/cutoff_commutator_cuda_full_2026-09-29.md`.
