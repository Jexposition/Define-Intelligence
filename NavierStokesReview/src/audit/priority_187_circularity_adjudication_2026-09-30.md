# Priority 187: adjudication of the jet-flatness circularity rebuttal

**Date:** 2026-09-30
**Status:** source-checked; the rebuttal identifies the correct correspondence gate but overstates its logical consequence

## Executive finding

The latest rebuttal is correct about one material point: the manuscript's five
radial quantities \\((M,I,J,S,C_p)\\) are load-bearing in profile matching,
modulation restoration, stress control, and the finite-dimensional correction
architecture. The audit must not describe them as optional or removable.

It is not correct, however, to infer from the absence of a final named
five-moment equality that the Lean force is therefore nonsmooth, or that the
selected force-smoothness proof is circular. The selected Lean path contains an
actual conditional residual-jet theorem and a concrete construction of its
premises:

\\[
H_{\\mathrm{selected}}
\\Rightarrow J_{\\mathrm{flat}}
\\Rightarrow F\\in C^\\infty,
\\qquad
F=\\mathcal R(u_{\\mathrm{selected}},p_{\\mathrm{selected}})
\\text{ for }0\\le t<1.
\\]

The unresolved and material correspondence gate is different:

\\[
J_{\\mathrm{flat}}
\\stackrel{?}{\\Longrightarrow}
\\operatorname{PaperMoments}(u_{\\mathrm{selected}},p_{\\mathrm{selected}})
=(M,I,J,S,C_p).
\\]

The current source trace has not established that implication after the
completed selected sums, curl, localisation, periodisation, torus averaging,
radial integration, support, integrability, and axis limits. The correct status
therefore remains **NOT ESTABLISHED (CTR-005)**. This is a paper-to-endpoint
fidelity failure, not yet a selected nonzero defect, a force-nonsmoothness
theorem, a literal CMI failure, or `False`.

## 1. What the circularity criticism gets right

The manuscript does not treat the five quantities as decorative notation. The
source record assigns them concrete jobs:

| Source anchor | Mathematical job |
|---|---|
| `docs/navier-stokes openai.txt:488--496` | Matching the five radial quantities preserves the exterior fields and removes the corresponding annular stress outside the joining region. |
| `:523--546` | High-frequency modulation changes the moments by an inverse-frequency error, followed by a five-bump restoration. |
| `:727--735` | The fourth correction operation solves five radial equations while the other listed operations handle distinct wave, covariance, and auxiliary-time defects. |
| `:746--784` | Curl/cutoff terms, locally finite summation, residual recomputation, and flatness remain part of the full construction. |
| `:8451--8517` and `:8602` | Exact radial moments are propagated into the exterior matching and are used together with the other correction and residual estimates. |

Thus the following criticism is valid:

> A residual-jet theorem in Lean is not automatically a machine-checked copy
> of the manuscript's five-observable argument. The proof must connect the
> actual selected Cartesian fields and their residual construction to the
> paper's moment identities and their stated consequences.

That is exactly the adverse `CTR-005` finding.

## 2. Why the termwise-divergence argument is not valid

The implication

\\[
\\|u(t)\\|_{L^\\infty}\\to\\infty
\\quad\\Longrightarrow\\quad
\\|\\partial_tu\\|,\\|(u\\cdot\\nabla)u\\|,\\|\\Delta u\\|,
\\|\\nabla p\\|\\to\\infty
\\]

does not hold without additional estimates. A sum can remain smooth while its
individual summands are singular. For example, if

\\[
a(t)=(1-t)^{-1},\\qquad b(t)=-(1-t)^{-1}+g(t),
\\]

then both summands diverge as \(t\\uparrow1\), while \(a(t)+b(t)=g(t)\) is
smooth. The example is not a Navier--Stokes proof; it establishes only the
logical point that the rebuttal's Step 3 is not a valid implication.

The manuscript itself describes cancellation of the total residual and its
derivatives. Therefore the audit cannot promote velocity blow-up alone into a
force singularity. To prove that stronger claim, it would need a selected
value-level lower bound or an uncancelled coefficient in the actual residual.

## 3. Exact Lean force path

The current source gives the following dependency chain.

1. `ActualCandidateAssembly.physicalData`
   (`NavierStokes/ActualCandidateAssembly.lean:1079--1088`) is constructed by
   `ActualPhysicalPrefixFields.physicalFields_all`.

2. `ActualCandidateAssembly.estimates`
   (`:1090--1098`) calls
   `GluedStageEstimates.actualStageEstimates` with the actual coherent run,
   representations, and `physicalData`.

3. `GluedStageEstimates.actualStageEstimates`
   (`NavierStokes/GluedStageEstimates.lean:684--725`) constructs the complete
   `StageEstimates` record. Its `finite_residual` field is discharged by
   `ActualCycleResidualBounds.finite_residual_rates`
   (`:436--440`).

4. `ActualCycleResidualBounds.residual_jetRate`
   (`NavierStokes/ActualCycleResidualBounds.lean:1158--1172`) uses the actual
   invariant, `StateRealization`, the native residual rate, physical field
   data, exterior germs, and the base-exterior rate. The local `PhysicalFields`
   structure (`:1015--1037`) contains smoothness, pressure differentiability,
   velocity/pressure germs, and exterior agreement. It does not contain the
   final paper five-tuple.

5. `ActualCycleResidualBounds.finite_residual_rates`
   (`:1190--1206`) applies that theorem at every correction cycle. The
   invariant is a real `CycleAnalyticInvariant`, not an unconstrained dummy;
   the surrounding source contains rank, support, smoothness, and residual
   obligations. This is why calling the selected rate proof a free-standing
   `NativeBounds` assumption is inaccurate.

6. `MixedCandidateAssembly.StageEstimates.exists_schedule`
   (`NavierStokes/MixedCandidateAssembly.lean:67--91`) converts those finite
   rates into a schedule and `VanishingJointJets`.

7. `GermCandidateAssembly.exists_candidate_witness_of_finite_stages`
   (`NavierStokes/GermCandidateAssembly.lean:164--304`) passes the schedule,
   extensions, vanishing jets, and the axis asymptotic to
   `CandidateConsequences.mixed_exists_force_with_consequences`.

8. `CandidateFromLimits.tracedResidual_smooth`
   (`NavierStokes/CandidateFromLimits.lean:39--55`) proves smoothness from the
   residual derivative recurrence and the supplied locally uniform residual
   limits. `force_smooth` (`:80--87`) then applies the smooth gluing theorem,
   while `force_eq_activated_residual` (`:97--112`) identifies the force with
   the activated residual before the singular time.

This is a theorem chain with premises. It is not a proof that the manuscript's
five-moment mechanism has been transported, but it is also not an assumption
that `force_smooth` is true merely because a field is called `NativeBounds`.

## 4. Where the real gap remains

`ActualCandidateAssembly.Witness` (`:1121--1151`) exports the selected
schedules, `ASum`, `BSum`, `PSum`, extensions, forcing, candidate properties,
smoothness, residual consequences, H3 blow-up, force decay, and boundary jets.
`selected_witness` is at `:1177--1181`. No inspected field or theorem in that
contract identifies the completed selected Cartesian construction with

\\[
\\operatorname{PaperMoments}(u_{\\mathrm{selected}},p_{\\mathrm{selected}})
=(M,I,J,S,C_p).
\\]

The omission matters because the manuscript uses the moments in named physical
consequences. It does not mean that the residual-jet route cannot prove a
smooth force by another formally valid route. It means that the present audit
has not proved the bridge which would show that this other route is the
manuscript's advertised five-moment route.

The review-side `AX-033`/`SelectedEndpointMomentTransportObstruction` result
must also be read narrowly. It proves that an abstract nonzero `Debt` payload
can coexist with the proposition `selected_witness`, because `Debt` is absent
from the `Witness` contract. It does **not** construct a selected Cartesian
field whose actual physical integrals equal that payload. Treating it as a
physical counterexample would be an overclaim.

## 5. Noncomputability and compiler-loophole check

The targeted path contains `noncomputable` definitions and some uses of
`Classical.choice` to select extensions. Those mechanisms do not prove a
missing proposition, alter the type of `Witness`, or turn a false theorem into
a true one. The relevant declarations inspected here contain no `sorry` or
custom axiom declaration. That lexical result is not a substitute for a fresh
full build, and it does not settle the paper-to-code correspondence.

The correct compiler question is therefore not “did Lean cheat?” It is:

\\[
\\text{Which exact hypotheses prove }J_{\\mathrm{flat}},
\\text{ and where is their equality with the paper's five moments proved?}
\\]

The first half is source-traced. The second half remains open.

## Adjudication

| Rebuttal claim | Status |
|---|---|
| The five moments are load-bearing in the manuscript. | **Confirmed.** |
| Blow-up forces every residual summand to diverge. | **Rejected.** The implication is mathematically invalid. |
| The five equations are the only cancellation mechanism. | **Not established.** The manuscript lists distinct correction, cutoff, summation, pressure, and residual-flatness operations. |
| `force_smooth` rests on an unlinked generic rate assumption. | **Rejected as stated.** The selected path constructs actual residual-rate premises and derives smoothness from them. |
| `Witness` exports the manuscript's final five-observable identity. | **Not established.** No inspected endpoint theorem supplies it. |
| Missing export proves the selected force is nonsmooth or CMI C is false. | **Rejected.** That requires a selected mismatch, failed connected condition, impossibility theorem, or contradiction. |
| Complete machine-checked correspondence with the manuscript is established. | **Not established (CTR-005).** |

The adversarial conclusion is therefore precise: the repository contains a
substantive residual-flatness and smooth-force proof route, while the current
record still does not establish that the route is the paper's complete
five-moment physical construction. The audit should attack that missing
semantic implication directly, not replace it with an unsupported force-
singularity claim.

**Evidence:**

- `NavierStokes/ActualCandidateAssembly.lean:1079--1098,1121--1151,1177--1181`
- `NavierStokes/ActualCycleResidualBounds.lean:1015--1037,1158--1172,1190--1206`
- `NavierStokes/GluedStageEstimates.lean:684--744`
- `NavierStokes/MixedCandidateAssembly.lean:67--91`
- `NavierStokes/GermCandidateAssembly.lean:146--158,164--304`
- `NavierStokes/CandidateFromLimits.lean:39--55,80--112`
- `docs/navier-stokes openai.txt:488--496,523--546,727--784,8451--8517,8602`
- `NavierStokesReview/src/extensions/SelectedEndpointMomentTransportObstruction.lean`
