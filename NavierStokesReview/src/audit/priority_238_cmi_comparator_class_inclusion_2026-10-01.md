# Priority 238: CMI comparator class inclusion

## Finding

The inspected R3 adapter establishes the following one-way implication for
the same viscosity and force:

\[
  \text{Comparator solution}
  \Longrightarrow
  \texttt{GlobalFiniteEnergySolution}.
\]

The review probe
`NavierStokesReview/src/probes/CMIComparatorClassInclusionProbe.lean`
re-states that direction against the production adapter
`NavierStokesR3.globalSolutionOfComparator` and proves the corresponding
nonexistence transfer:

\[
\neg\exists\,\texttt{GlobalFiniteEnergySolution}
\Longrightarrow
\neg\exists\,\texttt{Comparator solution}.
\]

This is enough for the published C-shaped contradiction route. It does not
require the two competitor predicates to be definitionally identical or
extensionally equivalent.

## What the adapter actually transports

`globalSolutionOfComparator` supplies the R3 record fields from the
comparator record:

- smooth velocity and pressure on the future domain;
- the zero initial datum;
- incompressibility;
- the Navier--Stokes residual equation with the same viscosity and force;
- square-integrability at every nonnegative time;
- the R3 uniform kinetic-energy bound, with the explicit factor `1/2` handled
  in the adapter.

The force is not altered in this adapter: the comparator force is
`ComparatorBridge.toComparator f`, and the resulting R3 force is `f`.

## Boundary still open

No reverse theorem was located in this pass proving

\[
  \texttt{GlobalFiniteEnergySolution}
  \Longrightarrow
  \text{Comparator solution}.
\]

That reverse direction is not needed for the existing nonexistence transfer,
but it remains relevant to any claim that the Lean competitor class is an
exact bidirectional formalisation of the CMI class. The remaining work is to
check the component conventions, the derivative-normalisation lemmas, and the
whole-time energy/integrability translation before assigning an equivalence
status.

## Audit disposition

- Adapter edge: **ESTABLISHED** in the inspected source and review probe.
- Comparator/R3 class equivalence: **NOT TESTED THOROUGHLY**.
- CMI failure: **not inferred from this edge alone**.
- Relation to `CTR-005`: independent. This edge does not establish the
  selected-field moment bridge, and its success does not prove that bridge.

Evidence: `NavierStokesReview/evidence/priority_238_cmi_comparator_class_inclusion_2026-10-01.json`.
