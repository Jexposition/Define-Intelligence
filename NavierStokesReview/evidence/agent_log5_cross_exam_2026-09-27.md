# Cross-examination of the additional `agent log 5` comments

**Date:** 2026-09-27  
**Scope:** Fact-check of the supplied comments against the live Lean source,
the current endpoint trace, the extracted OpenAI manuscript, and the CMI
problem statement.

## Findings that are supported

1. `ActualCandidateAssembly.Witness` is a proposition whose exported
   conjuncts do not contain a named equality identifying the final Cartesian
   field with the paper tuple `(M, I, J, S, C_p)`, `FiveRowRank.FiveRows`, or
   `PositiveOrderMoments.Debt`.
2. Five-moment and rank machinery is real and reachable upstream. The source
   includes profile certificates, correction rows, outgoing-history identities,
   local radial balances, and Cartesian potential/curl constructions.
3. The selected endpoint is therefore not established merely by showing that
   those modules are imported. The required proof is a value-level composition
   through the actual selected sums, curl/localisation, periodisation,
   torus-average, radial pullback, support/integrability, and axis handling.
4. The residual provenance result is real: the selected force is constructed
   from the selected residual on the stated pre-singular domain, and the fixed-
   force perturbation probe proves trajectory sensitivity under a new field.

## Claims in the supplied comments that are not yet established

### Curls and cutoffs “destroy” the moments

The source proves the cutoff-before-curl identity and exposes the associated
cutoff-gradient commutator in `SpatialLocalization.lean`. It also proves
divergence, support, local equality, and residual-transfer facts for the
periodised fields. These identities make the commutator a mandatory term in a
global moment calculation, but they do not by themselves prove that its radial
integral is nonzero. A designed cancellation, a boundary term, or an exact
transport theorem remains possible. The correct status is **open calculation**,
not “the moments are destroyed”.

### “The endpoint uses only generic rates”

This is too broad. `StageEstimates` is moment-blind as an interface, and the
`Witness` proposition does not export a final moment equality. However,
`ActualStageEstimates`, `ActualCycleResidualBounds`, and the selected
construction consume concrete physical data and `NativeBounds`; upstream
moment/correction results may contribute to those data. The supported claim is
that the final proposition does not expose the required selected-field value
equality, not that every upstream estimate is generic or independent of the
moment branch.

### “Zero percent of the paper is verified”

This is also too broad. The source verifies substantial components of the
paper's construction: profile repair, correction algebra, local Cartesian
curl fields, cutoff handling, periodised residual identities, energy bounds,
and whole-space packaging. What is not established is the complete
paper-to-endpoint composition for the five global observables. This is a
load-bearing correspondence failure, not proof that every paper lemma is
outside the Lean proof tree.

### Residual forcing is formally illegal under CMI

The CMI text describes a given externally applied force, so the provenance
question is material to the physical interpretation. But the literal C/D
formalisation is existential and the source record does not contain a formal
force-independence predicate. The fixed-force perturbation proves operator-level
path dependence; it does not, by itself, derive `False` from the exported C/D
proposition. Keep CTR-012 as a serious causal/provenance mismatch without
calling it an unconditional CMI kernel disproof.

## Current adversarial target

The falsification target remains the concrete value-level statement

```text
selected Cartesian field
  -> actual tsum/potentialSum
  -> curl and localisation, including the commutator
  -> periodisation and torus averaging
  -> radial pullback and axis/outer-domain limits
  -> (M, I, J, S, C_p)
```

The audit must seek one of three outcomes:

- a zero-sorry theorem proving a concrete nonzero remainder;
- a zero-sorry impossibility theorem for the required transport; or
- a positive full bridge theorem.

Until one is obtained, the defensible classification is **not established as
paper-to-code correspondence**, not an unconditional `False` result. The
comments therefore sharpen the next calculation but do not change the verdict.
