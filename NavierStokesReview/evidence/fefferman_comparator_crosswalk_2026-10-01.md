# Evidence record: Fefferman comparator crosswalk

Date: 2026-10-01

The official-text mirror and Lean comparator definitions were read together.
Fefferman's conditions (4)--(7) and Alternative (C) are recorded at
`docs/navierstokes.txt:25-77`. Lean has corresponding structures for initial
data decay, force smoothness/decay, global smooth solutions, and global energy
at `NavierStokes/ComparatorDefinitions.lean:124-227`.

The R3 candidate predicate is pre-singular and contains the explicit
Navier--Stokes residual, force smoothness, compact support, energy bound on
`0 ≤ t < 1`, and speed unboundedness at
`NavierStokes/R3/ProblemStatement.lean:92-109`. The exported theorem supplies
the forced breakdown statement at `NavierStokes/R3/Theorem.lean:46-49`, and
`navier_stokes_breakdown_R3` maps it to the comparator's Alternative (C)
quantifiers at `NavierStokes/ComparatorR3Theorem.lean:37-44`.

This establishes a real formal comparator path. It does not establish that
the selected endpoint exports the manuscript's complete five-observable
transport identity. The current disposition is therefore:

> `CTR-005: NOT ESTABLISHED` for complete paper-to-selected-endpoint fidelity.

Residual force provenance remains a semantic forward-Cauchy objection, not a
literal existential contradiction. No selected moment defect, force
nonsmoothness, impossibility theorem, or `False` is claimed by this record.

Audit companion:
`NavierStokesReview/src/audit/priority_221_fefferman_comparator_crosswalk_2026-10-01.md`.
