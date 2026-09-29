# Selected profile-moment dependency adjudication

**Date:** 2026-09-29
**Scope:** OpenAI Navier--Stokes source, OpenAI paper, Fefferman/CMI formulation, and the review-side CTR-005 record.
**Disposition:** Corrective source adjudication.  This document supersedes the narrower claim that moment/rank restoration is absent from the selected construction.

## Adjudication in one paragraph

The earlier statement that the selected construction “drops” or “bypasses” the five-moment repair mechanism was too strong and is withdrawn.  The live Lean source contains genuine reduced-profile moment certificates, rank/repair identities, pressure/stress consequences, and finite Cartesian residual identities.  Those identities feed the selected slow-base construction and the residual flatness estimates used downstream.  The fact that `origin_blowup` proves one axis-limit conjunct without taking a five-tuple as a direct argument does not show that the complete candidate is independent of the repair mechanism.

The remaining adverse question is narrower: whether the entire paper-level construction is semantically identified with the final selected mixed, localised, periodised, infinite-sum fields and the public endpoint.  That question must be tested using the paper’s actual profile-level meaning of the five quantities.  The absence of a field named `(M,I,J,S,C_p)` in `ActualCandidateAssembly.Witness` is not, by itself, a refutation and is no longer treated as the required failure predicate.

## What the paper actually says

The extracted OpenAI paper (`docs/navier-stokes openai.txt`) describes the five quantities as cumulative radial integrals of reduced profile variables.  The relevant passages state that they preserve pressure, radial velocity, and stress across profile joins; that (C_p) is the pressure increment from the axis; that high-frequency modulation changes the five integrals by (O(N^{-1})); and that local correction bumps restore the five integrals.  The correction-cycle passages describe two preserved zero integrals and three cancelled defects ((P,J_\theta,J_z)).

Thus the paper-level invariant has the schematic form

\[
  \mathcal M(U,E,\Pi;X)
  = (M,I,J,S,C_p),
\]

where (U,E,\Pi) are reduced radial/profile data and the equality is used at a join or correction stage.  The paper does not, in the inspected passages, define the five entries simply as an observable of the final whole-space Cartesian triple

\[
  (u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}}).
\]

That distinction matters.  A valid correspondence theorem need not have the literal type

\[
  \operatorname{moments}(u,p,f)=(M,I,J,S,C_p),
\]

but it must connect the paper’s reduced-profile identities to the selected construction at every point where the paper uses them: exterior matching, pressure/stress cancellation, modulation repair, correction-cycle compatibility, and the subsequent Cartesian/localised assembly.

## Positive source chain established by direct inspection

The current source record establishes the following chain.

\[
\begin{aligned}
&\texttt{PositiveOrderMoments.moments\_zero}\\
&\quad\Longrightarrow\texttt{GlobalStressSupport.conservative\_moments\_zero}\\
&\quad\Longrightarrow\texttt{GlobalSlowProfiles.profiles\_pressureCoefficient}\\
&\quad\Longrightarrow\texttt{EntranceAlignedBase.aligned\_finiteIdentities}\\
&\quad\Longrightarrow\texttt{FinalSlowBase.finiteIdentities}\\
&\quad\Longrightarrow\texttt{BaseResidual.baseResidual\_jetRate/allJetsFlat}\\
&\quad\Longrightarrow\text{selected stage estimates and candidate consequences}.
\end{aligned}
\]

The direct source anchors are:

| Layer | Source evidence | What it establishes |
|---|---|---|
| Five-coordinate repair | `NavierStokes/PositiveOrderMoments.lean:275-285` | Exact repair of an arbitrary five-coordinate debt. |
| Stress/pressure conversion | `NavierStokes/GlobalStressSupport.lean:144-186` | Repaired rows are converted into actual radial stress/pressure/transport identities. |
| First-order exterior consequences | `NavierStokes/FirstOrderBaseEdge.lean:50-108` | Conservative moments enter first-order edge and exterior-stress results. |
| Selected slow-base transport | `NavierStokes/EntranceAlignedBase.lean:666-697,871-874` | Actual profile histories, pressure coefficients, and finite identities are assembled from the repaired data. |
| Exact finite Cartesian identity | `NavierStokes/BasePrefixIdentity.lean:278-284,372-386` | Coefficient matching yields `BaseResidual.FiniteIdentities`. |
| Residual estimates | `NavierStokes/ConstructedSlowBase.lean:93-108,145-166,351-383,901-909` | Finite identities are consumed by jet-rate and all-jets-flat proofs. |
| Formal residual contract | `NavierStokes/BaseResidual.lean:1511-1530,1618-1627` | The exact finite residual identity is a premise of the residual estimates, not a decorative import. |
| Blow-up conjunct | `NavierStokes/GermCandidateAssembly.lean:146-159,264-271` | `origin_blowup` supplies one endpoint conjunct through the axis asymptotic. |

This is a real dependency chain.  It rules out the earlier description of the selected proof as a generic rate-only witness that is independent of the profile/rank construction.

## Why the local blow-up theorem does not settle the whole candidate

The endpoint has a conjunction of obligations.  In schematic form,

\[
  \mathrm{CandidateProperties}(u,p,f,K)
  = H_{\mathrm{smooth}}\land H_{\mathrm{support}}
    \land H_{\mathrm{div}}\land H_{\mathrm{NS}}
    \land H_{\mathrm{energy}}\land H_{\mathrm{blowup}}.
\]

The theorem `origin_blowup` proves (H_{\mathrm{blowup}}) from the axis asymptotic.  It does not purport to prove all other conjuncts, and its type therefore need not mention every datum used elsewhere.  The full candidate construction separately needs finite residual identities, support/localisation, smoothness, pressure and force properties, and the stage estimates.  Since the source shows that `FiniteIdentities` feeds the residual-rate and all-jets-flat obligations, it is incorrect to infer either of the following:

1. “`origin_blowup` does not mention the moments, therefore the full proof does not rely on them”; or
2. “`Witness` does not contain a literal five-tuple field, therefore the moment mechanism is absent.”

The mathematically correct conclusion is that the local axis proof and the global construction are different propositions in the same conjunction.

## What remains genuinely open

The positive chain above does not automatically prove full paper correspondence.  The remaining audit must answer, from declarations and values rather than names:

1. whether the exact reduced-profile quantities used in the paper are the same quantities used at every selected correction and join;
2. whether the finite identities survive the selected mixed-stage assembly, including `potentialSum`/`tsum`, curl, spatial and temporal localisation, and periodisation;
3. whether the selected pressure and force have the paper’s intended whole-space meanings, rather than only satisfying a residual identity or comparison theorem;
4. whether all support, integrability, axis, and tail hypotheses needed for the paper’s radial observables are transported to the final endpoint;
5. whether the endpoint’s C/D proposition is the intended CMI mathematical statement, not merely a weaker formally inhabited predicate.

These are composition and semantic questions.  The current evidence does **not** prove a nonzero moment defect, an impossibility theorem, or `False`.  It also does not justify saying that the paper’s mechanism is absent or that the endpoint has been shown to realise the complete paper construction.

## Corrected status of CTR-005

The earlier criterion “`Witness` must export `moments(u,p,f)=(M,I,J,S,C_p)`” is withdrawn as insufficiently grounded in the paper’s definitions.  CTR-005 should now be recorded as:

> **Selected paper-to-endpoint semantic correspondence remains unclosed after a substantial positive internal profile/rank/residual chain.**  The review must not infer failure from the absence of a literal tuple field.  It must test the actual reduced-profile identities and their complete selected-field composition.

This is an adverse audit finding because a compiled endpoint alone does not establish that the paper’s complete construction has been reproduced.  It is not a claim that the internal repair mechanism is missing, not a claim that the blow-up conjunct is unproved, and not a kernel-level refutation.

## Required next evidence

The next decisive artefact is a declaration-level and value-level crosswalk, not another generic interface countermodel.  It should list each paper use of \\(M,I,J,S,C_p\\), the exact Lean declaration that supplies it, the selected object to which it applies, and the first downstream transformation for which no matching theorem is found.  Any escalation to `FORMALLY REFUTED` requires a direct theorem showing a false mandatory identity or deriving `False` from the selected premises.

**Supersedes:** earlier wording that called the moment/rank restoration “missing”, “bypassed”, or “completely outside the active proof tree”.
