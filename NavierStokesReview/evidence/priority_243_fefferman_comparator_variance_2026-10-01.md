# Priority 243: Fefferman-to-Comparator variance audit

**Date:** 2026-10-01
**Status:** source crosswalk recorded; implication proofs and proof-term extraction still open
**Purpose:** test the class inclusion needed for the nonexistence argument rather than assuming that similarly named predicates are equivalent

## 1. Why the direction matters

For a nonexistence transfer, the critical implication is not full equivalence. It is:

\[
\text{Fefferman-admissible competitor}
\Longrightarrow
\text{Comparator competitor}.
\]

Only then does

\[
\neg\exists\,\text{Comparator competitor}
\]

exclude every competitor permitted by the CMI specification. If the implication is reversed, or if Comparator imposes an unproved stronger class, the formal nonexistence statement may be too narrow.

## 2. Current source crosswalk

The challenge source makes several comparator obligations explicit:

- `ComparatorChallenges/NavierStokes.lean:139` gives smooth initial velocity.
- `ComparatorChallenges/NavierStokes.lean:177` gives force smoothness on the future domain.
- `ComparatorChallenges/NavierStokes.lean:223` encodes the PDE with `derivWithin` on `Set.Ici 0`.
- `ComparatorChallenges/NavierStokes.lean:232–235` gives velocity and pressure smoothness on the future domain.
- `ComparatorChallenges/NavierStokes.lean:250–253` requires `MemLp` at every nonnegative time and a uniform bound on the totalised energy integral.

The current R³ bridge uses the same force object in the important direction:

- `NavierStokes/R3/ComparatorBridge.lean:48–70` constructs `globalSolutionOfComparator` from a comparator solution and explicitly transports its integrability and global energy bound into `GlobalFiniteEnergySolution`.
- `NavierStokes/R3/ComparatorBridge.lean:76–88` applies that adapter to the same candidate force and closes the comparator nonexistence statement.
- `NavierStokes/R3/CandidateBreakdown.lean:21` and the surrounding uniqueness route use smoothness on the comparison slabs; this must be checked against the exact CMI competitor class rather than inferred from names.

This is positive evidence for the internal adapter. It is not yet a proof that every Fefferman competitor enters the comparator class.

## 3. Required independent checks

### Finite energy versus `MemLp`

The review must prove the direction:

\[
\left(\int_{\mathbb R^3}\lVert v(x,t)\rVert^2\,dx<\infty\right)
\Longrightarrow
\texttt{MemLp}(\lVert v(\cdot,t)\rVert)\,2.
\]

The converse is not enough for nonexistence transfer. Any use of the real-valued integral must also carry the integrability hypotheses that stop Lean's totalised integral from returning an uninformative value.

### Coordinate derivatives versus Fréchet derivatives

The CMI wording and the comparator use different representations of smoothness/decay. The audit must establish, in the required direction, that the CMI coordinate/multi-index bounds imply the comparator's full iterated Fréchet-derivative norm bounds, with the correct finite-dimensional constants and argument order.

### Domain and boundary semantics

The audit must check:

- `Set.Ici 0` versus the CMI time domain;
- `derivWithin` at (t=0) versus the PDE requirement for (t>0);
- pointwise versus almost-everywhere equalities;
- whole-space spatial decay versus compact-support assumptions;
- pressure regularity and pressure-gauge equivalence;
- the same viscosity ν and the same force (f), without an unrecorded rescaling.

### Constructed data direction

The separate direction

\[
\text{Comparator constructed data}
\Longrightarrow
\text{Fefferman admissible data}
\]

must also be checked, but it does not substitute for the competitor-class direction above.

## 4. Status discipline

Current status is **not a proven class failure** and **not a proven class equivalence**. The source trace supports a real internal adapter and same-force use. The CMI transfer remains an open semantic edge until the asymmetric implications are independently proved or a counterexample is formalised.

This lane is separate from, but linked to:

- selected-field moment transport;
- force smoothness and residual extension;
- pressure semantics;
- whole-space uniqueness hypotheses;
- September 8/10 proof-term differential;
- constructor-field provenance and totalisation.
