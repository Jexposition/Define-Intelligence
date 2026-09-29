# Profile-moment / selected-path adjudication

Date: 2026-09-29
Status: source adjudication; this file supersedes the earlier blanket claim that the selected construction omits or bypasses the five-moment/rank restoration.

## Finding

The earlier formulation of CTR-005 was too strong and used the wrong target proposition. The paper's five quantities `(M, I, J, S, C_p)` are introduced as cumulative radial profile quantities used to match the inner construction to the exterior, control stress tails, and repair the modulated profile. They are not presented in the paper as a required final whole-space record field of the form

\[
  \operatorname{moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
    =(M,I,J,S,C_p).
\]

The raw Lean source contains genuine five-moment certificates, rank/debt equations, repaired coefficient matching, and a finite Cartesian residual identity. Those results are connected to the actual selected construction. The omission of a named five-tuple from `ActualCandidateAssembly.Witness` is therefore not evidence that the repair engine was absent, bypassed, or mathematically unnecessary.

The scope must still be stated precisely. `NominalProfile.FiveMomentCertificate`
is a certificate for the literal final reduced-profile fields `W.U` and `W.E`
at the profile layer. It is not itself a theorem whose conclusion is a named
five-tuple for the final whole-space `ASum`/`BSum` field. The raw chain matters
because `FinalSlowBase.exists_final_base` and `BaseWitnessClosure.actual_finite_base`
use the profile witness and repair data to construct the finite Cartesian
identity and downstream candidate properties. Thus the source establishes
internal use and consequence transport, while the remaining audit question is
whether any specific paper assertion requires a stronger whole-space identity
than those proved consequences provide.

## Raw source chain

1. **Paper scope.** `docs/navier-stokes openai.txt` describes the five cumulative integrals as profile-level quantities used for exterior matching, stress-tail removal, post-modulation restoration, and the five-equation correction cycle. The relevant passages are around lines 490–545, 727–753, 977–986, and 1231–1247 in the checked text export.

2. **Five-moment certificates exist.** `NavierStokes/NominalProfile.lean:2079–2089` defines `FiveMomentCertificate`; `:2108–2135` proves `heated_five_moments`; and `:2536–2541` proves `NominalProfile.Witness.five_moments`. `FirstOrderBaseEdge.lean:387` consumes the certificate rather than merely importing it.

3. **Rank/debt restoration exists.** `NavierStokes/FiveRowRank.lean:241–253` defines and solves `FiveRows`. `MeanRankUpdate.lean:163–200` proves `physical_five_rows` and its scaled correction form. `CorrectionState.lean:453–472` consumes those rows in the actual cycle state. These are not dead declarations.

4. **The repaired coefficients are matched to the slow profiles.** `NavierStokes/BasePrefixIdentity.lean:278–285` defines `CoefficientMatches`, including velocity, pressure, theta-stress, and axial-stress equalities. The comment immediately above the structure states that the scalar pressure and canonical stress primitives are part of the remaining agreements.

5. **Those matches produce an exact finite Cartesian identity.** `BasePrefixIdentity.lean:374–386`, theorem `finiteIdentities_of_coefficients`, derives `BaseResidual.FiniteIdentities` from `CoefficientMatches`, smoothness, and the canonical stress identities. Its proof rewrites the actual prefix velocity and pressure and invokes `SlowResidualMatching.navierStokesResidual_eq_stress_add_truncation`.

6. **The finite identity is load-bearing for the residual estimates.** `BaseResidual.lean:1511–1531` defines `FiniteIdentities` and takes it as an explicit premise of `baseResidual_jetRate`; `:1612–1627` takes it again for `baseResidual_allJetsFlat`. This is the mathematical route from repaired profile data to the residual bounds, not a generic `StageEstimates` countermodel.

7. **The final slow base retains the identity.** `ConstructedSlowBase.lean:93–108` proves `repaired_finiteIdentities` from repaired coefficient matching. Its nominal, modified, and final constructions call that theorem. `FinalSlowBase.lean:107–109` defines the final `finiteIdentities`, and `:330–354` uses it in the residual and all-jets-flat theorems.

8. **The selected base is not disconnected from that theorem.** `BaseWitnessClosure.lean:87–96`, theorem `actual_finite_base`, returns both smooth coefficients and `BaseResidual.FiniteIdentities` for the actual primary certificate and modulation. `ActualBaseResidual.lean:582` invokes `FinalSlowBase.residual_identity`; `:768–789` states that the fixed-base equation is derived from that identity. `ActualCycleResidualBounds.lean:541–553` invokes the same final residual identity in the actual cycle residual germ.

9. **The selected fields are the fields proved by the base construction.** `ActualCandidateConstruction.lean:759–820` proves `base_velocity_on_cylinder`, `base_pressure_on_cylinder`, and `chartBaseVelocity_eq`, identifying the stage/chart fields with `FinalSlowBase.velocity` and `FinalSlowBase.pressure`. `ActualPhysicalPrefixFields.lean:475–491` then constructs the physical-data family from the stage realizations and cycle representations.

10. **The endpoint packages consequences, not every internal lemma.** `ActualCandidateAssembly.lean:1121–1181` packages schedules, potential sums, extensions, `CandidateProperties`, and `CandidateConsequences`. It is normal in dependent theorem composition for a final existential proposition not to repeat every upstream lemma as a named field. The fact that `Witness` has no field called `five_moments` does not show that the theorem used no moment/rank machinery.

## What the blow-up statement means

`GermCandidateAssembly.origin_blowup` is a local conjunct proved through the axis asymptotic (`:146–159`) and passed into `CandidateConsequences.mixed_exists_force_with_consequences` (`:264–271`). That local proof does not list the five-moment certificate as an argument because its immediate proposition is only the axis limit.

The full candidate is stronger than that one conjunct. Its residual, exterior, smoothness, and rate obligations are constructed through the finite identity and actual physical-data chain above. The correct logic is therefore:

\[
\begin{aligned}
  &\text{profile moments/rank repair}\\
  &\quad\Longrightarrow \text{coefficient matching}\\
  &\quad\Longrightarrow \text{finite Cartesian residual identity}\\
  &\quad\Longrightarrow \text{jet-rate and all-order flatness bounds}\\
  &\quad\Longrightarrow \text{actual physical-data/stage estimates}\\
  &\quad\Longrightarrow \text{candidate properties},
\end{aligned}
\]

while the axis-growth conjunct is supplied by a parallel asymptotic route. The parallel route does not make the repair route dispensable; it only means that one conjunct has a shorter proof term.

## What remains open, precisely

The source record does **not** justify the earlier claim that the selected endpoint bypasses the five-moment engine. It does justify a narrower documentation/correspondence question: the public `Witness` type does not expose a named profile certificate or a final tuple of the five quantities. That omission matters only if the paper claims that such a tuple is itself the exported endpoint object. The checked paper text instead uses the quantities to establish profile matching and residual consequences.

The remaining audit must therefore test the exact paper consequences, not demand an invented final tuple:

- whether every paper assertion about exterior matching, pressure increment, stress-tail removal, and post-modulation restoration has a corresponding Lean theorem;
- whether the selected final fields used by those theorems are definitionally/propositionally the same fields used in `CandidateProperties`;
- whether the whole-space pressure semantics and residual-designed force satisfy Fefferman's CMI interpretation;
- whether any concrete selected-field mismatch or impossibility can be proved.

No nonzero moment defect, impossibility theorem, or kernel-level `False` follows from the missing `Witness` field alone. The earlier `StageEstimates` moment-blindness probe remains valid as an interface result, but it is not a countermodel of the concrete selected witness because the concrete witness supplies actual upstream data before entering that generic interface.

## Adjudication

The previous headline “the five-moment restoration is missing from the selected proof” is **retracted**. The supported statement is:

> The repository contains and uses a substantial profile/rank/repair-to-residual chain. The final existential envelope does not re-export the profile certificate as a named field, but that packaging fact does not establish a paper-to-code failure or falsify the blow-up construction. Any remaining CMI objection must be tied to a specific unmet paper consequence, pressure/force semantic condition, or proved selected-field mismatch.

This report is evidence for revising CTR-005; it is not a claim that the OpenAI paper has thereby been proved correct as a CMI solution.
