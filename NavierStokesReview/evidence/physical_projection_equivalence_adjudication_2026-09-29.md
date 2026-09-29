# Physical-projection equivalence and literal CMI compliance

Date: 2026-09-29
Status: source-grounded adjudication. This note corrects the loose statement that Hypotheses A and B are equally supported.

## Finding

The two hypotheses do not have equal evidentiary status.

The manuscript supports the first half of Hypothesis B: the reduced variables are the similarity-coordinate cylindrical components of the leading physical field, and the five cumulative radial quantities are load-bearing physical profile observables. They must not be described as disconnected or merely abstract scaffolding.

The second half of Hypothesis B requires a narrower qualification. The paper does not state the endpoint obligation as one record equation

\[
  \operatorname{moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
    =(M,I,J,S,C_p).
\]

It uses the five quantities at particular profile joins, stress identities, correction stages, and preservation steps. The review must therefore verify those exact consequences through the selected construction. Failure to find one endpoint tuple is not a proof that the consequences are false; it is evidence that the complete paper-to-endpoint correspondence has not yet been demonstrated.

## Paper evidence

1. `docs/navier-stokes openai.txt:331-368` states the similarity coordinates and that `E`, `U`, and `Pi` determine the leading azimuthal, axial, radial-flux, and pressure fields. The profile variables are therefore physically connected to the leading field.

2. `:488-496` states that matching the five radial integrals preserves the exterior fields. `:523-546` states that the five cumulative integrals govern pressure, radial velocity, and stress across joins, and that a localised correction restores all five after modulation changes them by `O(N^-1)`.

3. `:727-735` explicitly solves five radial moment equations. Two preserve specified integrals and three cancel pressure and tangential-momentum defects. The updated pressure, curls, cutoffs, and nonlinear products are included in the residual.

4. `:746-757` then sums local corrections with shrinking cutoffs and claims smooth fields and residual flatness. The manuscript also states at `:1226-1229` that cutoffs are applied to potentials before curls. These later operations create the transport obligations that the review must trace.

## Lean evidence

The raw source does not support the claim that the moment/rank mechanism is absent from the selected construction.

- `NominalProfile.lean:2079-2089` defines `FiveMomentCertificate`; `:2108-2135` proves the heated certificate; `:2536-2541` proves the nominal witness certificate.
- `BasePrefixIdentity.lean:280-285` defines coefficient matching for velocity, pressure, and both stress components; `:374-380` derives `BaseResidual.FiniteIdentities` from those matches.
- `ConstructedSlowBase.lean:95-108` derives repaired finite identities; `BaseResidual.lean:1521-1525` and `:1614-1618` use those identities for jet-rate and all-jets-flat results.
- `FinalSlowBase.lean:330-378` supplies the final residual identity and axis asymptotic; `BaseWitnessClosure.lean:89-93` returns actual smooth coefficients together with actual finite identities.
- `ActualCandidateConstruction.lean:759-820` identifies the selected chart/base velocity and pressure with `FinalSlowBase.velocity` and `FinalSlowBase.pressure`.
- `ActualCandidateAssembly.lean:1121-1151` packages the candidate and consequences. It does not export a named five-tuple field, but that packaging fact does not prove the upstream mechanism was unused.

The supported source-level chain is therefore:

\[
\text{profile moments/rank repair}
\Longrightarrow
\text{coefficient and stress matching}
\Longrightarrow
\text{finite Cartesian residual identity}
\Longrightarrow
\text{residual estimates and flatness}
\Longrightarrow
\text{selected candidate consequences}.
\]

The separate axis blow-up route is not a contradiction to this chain. `GermCandidateAssembly.origin_blowup` proves the local axis limit and passes it as one conjunct to the mixed candidate constructor. Its short type does not show that the residual, support, pressure, and regularity obligations are independent of the repair chain.

## Fefferman and force provenance

Fefferman's text calls `u0` and `f` given data and describes `f` as an externally applied force (`docs/navierstokes.txt:25-40`). Alternative (C), however, is formally existential over one smooth admissible pair and asks for nonexistence of a global smooth bounded-energy solution (`:74-77`). The text does not add a formal predicate prohibiting construction of the admissible force from a selected trajectory.

OpenAI's manuscript openly states the inverse-design route: choose an incompressible flow and pressure, define the force as the momentum residual, and arrange smooth cancellation (`docs/navier-stokes openai.txt:109-124`). Therefore residual construction is not a hidden Lean escape and is not, by itself, a formal contradiction of the literal existential Alternative (C). It remains a material provenance mismatch with the forward physical interpretation.

## Adjudication

The review must not issue either unsupported conclusion:

- “The moments are irrelevant or absent.” This is contradicted by the paper and the active Lean chain.
- “The selected whole-space field is already proved to realise every paper-level moment claim.” This has not been established by the inspected endpoint and cannot be inferred from compilation or from the absence of a mismatch theorem.

The defensible conclusion is asymmetric:

1. The paper's five-moment mechanism is physically meaningful and internally used by the formal construction.
2. The literal Lean endpoint is a substantive existential candidate proposition with an explicit blow-up conjunct and selected residual/support consequences.
3. Exact equivalence between that endpoint and every paper-level profile, localisation, pressure, force, and whole-space claim remains unestablished until the corresponding transport/consequence theorems are traced or a concrete mismatch is proved.
4. Residual-designed forcing is a separate force-provenance objection, not a literal refutation of the existential CMI predicate.

This is not a request that OpenAI repair its work. It is the current evidentiary classification of the advertised proof claim. No nonzero moment defect, impossibility theorem, or kernel-level `False` has been established by the evidence cited here.
