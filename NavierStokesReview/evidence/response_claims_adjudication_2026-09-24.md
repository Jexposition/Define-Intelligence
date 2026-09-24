# Response-claims adjudication

## Purpose

This note checks the supplied summaries against the current source tree and
the zero-sorry review probes. It is a clarification record, not a replacement
for the peer review.

## Claims confirmed

1. The inspected headline declarations report only `propext`,
   `Classical.choice`, and `Quot.sound`. The repository as a whole is not
   zero-sorry: the separate `ComparatorChallenges` area contains two admitted
   Navier–Stokes challenge declarations and two Euler challenge declarations.
   The challenge module is not on the inspected exported R³ dependency path.

2. `CTR-005` is correctly identified as the missing selected-path transport of
   the paper's `(M, I, J, S, C_p)` data into the fields, residual estimates,
   and force exposed by `selected_witness`.

3. `FiveRowPositiveOrderBridgeProbe.lean` proves the algebraic identities
   
   $$
   (P,J_\theta,J_z)\longmapsto(0,0,-P,-J_\theta,-J_z),
   $$

   including equality of the repair functions and the five weighted
   identities for the promoted target.

4. The selected force is residual-derived on the interior interval. The
   selected origin probe also proves endpoint residual cancellation at the
   origin: the local residual/force norm tends to zero while the origin speed
   is unbounded.

5. The pressure recovery and whole-space comparison chain is present. The
   compact-pressure-support objection does not by itself imply zero pressure
   or zero velocity. The comparison chain is relative and does not, by its
   interface alone, identify an absolute selected pressure representative.

6. `R3.CompactEnergy.energy_balance` and
   `R3.CompactEnergy.hasDerivAt_energy_balance` are exact conditional energy
   identities. `uniform_finite_energy` supplies the corresponding bound under
   the stated candidate hypotheses.

## Claims requiring correction

### Promotion is not selected-path transport

The promotion probe proves compatibility of the repair formulas. It does not
prove that the selected Cartesian fields have the paper's five integrals, nor
that those integrals are transported through `GermCandidateAssembly`, the
residual estimates, and `selected_witness`. The type-level dimensional
objection is therefore only an objection to direct identification, not a
contradiction of the repair construction.

### Literal predicate compatibility is not CMI adjudication

The residual construction is compatible with the existential `CandidateProperties`
predicate as currently formalised. That does not settle whether an
after-the-fact residual satisfies the intended meaning of a “given,
externally applied force”. The latter is a provenance and interpretation
question unless a source-backed independence condition is formalised and then
shown to fail.

### Endpoint force language must be localised

The force is not “proved nonzero through the singular time”. Interior equality
with the residual is proved for `0 < t < 1`; the endpoint is supplied by a
smooth extension. At the spatial origin, the selected residual/force tends to
zero. This is a local cancellation result, not a claim about the global force
norm or every spatial point.

### Generic interface probes do not describe the selected witness

The zero-velocity inhabitation and five-debt non-implication probes test the
generic `StageEstimates`/witness interfaces. They show what those interfaces
alone cannot certify. They do not show that the selected velocity is zero or
that its selected path is empty. The selected-label construction probe gives
explicit witnesses for the selected primary label and active pair.

### Uniqueness remains conditional

`WholeSpaceUniqueness.classical_uniqueness_on_Icc` proves equality for a
competitor satisfying its smoothness, divergence, residual, initial-data, and
finite-energy hypotheses. `CandidateProperties.no_global_solution_one` then
applies that comparison to the selected candidate. These are conditional
theorems, not an independent validation of every analytic premise in the
paper's informal narrative.

## Current verdict

The supplied response set is usable after these qualifications. The active
verdict remains: **not established as a CMI solution; not formally refuted by
the inspected selected path**. The load-bearing unresolved issue is CTR-005,
not selected-label vacuity, compact-pressure trivialisation, or the mere use
of a residual-defined force.

The first clause is the substantive review result. OpenAI must supply the
selected-path bridge and the analytic justifications for the claim it
publishes. The second clause is only a report about the current state of the
review's attempted Lean contradiction. It must not be read as a presumption
that the unproved bridge is valid or as a shift of the proof burden to the
reviewer.

## Correction to the supplied response set

The phrase “major revision” is too weak if it is read as a neutral midpoint.
The operative review conclusion is **not established**: the authors have not
met the affirmative burden for the stronger paper and CMI interpretation. A
kernel-level `False` theorem would be a stronger result, but its absence does
not convert an unproved composition theorem into evidence for the authors.
