# Semantic coverage audit: inverse, residual, and stage-loss obligations

Date: 2026-09-22  
Snapshot: `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`  
Classification: `PARTIALLY VERIFIED / OPEN`

## Scope

This pass tests three independent semantic-coverage obligations raised by the
external audit lead recorded in `EXTERNAL_AUDIT_LEADS_2026-09-22.md`:

1. every inverse and differentiated inverse must operate on a common, explicit
   admissible domain;
2. the final residual estimate must account for every load-bearing residual
   component;
3. derivative loss must be bounded by derivative order rather than by the
   correction stage.

This is a source-level audit. It is not a substitute for the pending kernel
axiom extraction, and it does not treat successful compilation as a CMI proof.

## Verified positive evidence

### 1. Inverse regularity and derivative loss

`NavierStokes/SmoothFamilyTorusInverse.lean:863-875` contains
`inverse_finiteJets`. Its conclusion takes a source bound at order `n + 5`
and returns a bound for the inverse at order `n`. The comment and theorem
quantifiers make the five-derivative loss explicit and choose the constant
before the source, parameter set, and input bound. The same file contains
parameter-derivative commutation lemmas for the inverse and an `inverse_solves`
statement requiring smoothness, periodicity, and zero mean. The zero mode is
handled by the multiplier definition rather than omitted from the statement.

This is positive evidence against the narrow claim that the inverse layer has
no fixed derivative-loss accounting. It does not yet prove that every caller
uses one common domain or that the paper's analytic domains are represented
bijectively.

### 2. Residual closure

`NavierStokes/PhysicalResidualJetBounds.lean:685-743` gives an explicit full
residual decomposition into source oscillation, mean-good residual, and total
state error. The subsequent bounds at `:773-923` combine the source sum, mean
residual, base error, Gaussian field, alias error, and excluded errors into a
`NativeBounds` result. The downstream theorem
`NavierStokes/ActualCycleResidualBounds.lean:1142-1203` applies this to the
literal state residual and then derives the diagonal residual rate.

This is positive evidence that the final residual is not represented only by a
single opaque placeholder. The theorem still depends on explicit invariant,
geometry, representation, and `PhysicalData` premises. Those premises need
their own mathematical and kernel-level audit before the result can be called
CMI-complete.

### 3. Stage-independent derivative loss

`PhysicalResidualJetBounds.NativeBounds` records a loss indexed by derivative
order, while the native residual theorem uses a fixed stage-independent loss
of the form `(2 * ActualPrimary.h) * m`. `ActualCycleResidualBounds` then
quantifies over every correction index `J` while reusing the same loss
function. The finite-stage constructor supplies these residual rates through
`ActualCandidateAssembly.lean:1079-1098` and
`ActualCycleResidualBounds.lean:1156-1173`.

This is positive evidence against the specific claim that the derivative loss
is visibly allowed to grow with the correction stage. The endpoint machinery
also supplies the missing regularity separately: `OneSidedExtension` requires
`ContDiffOn`, `JointResidualLimits.exists_smooth_compatible_limits` constructs
smooth boundary tensors, and `extendedResidual_smooth` proves closed-past
smoothness. The actual adapter reaches these obligations through
`PhysicalJets.of_rawStage` in `GermEndpointInputs.lean:436-470`.

The remaining specification caution is narrower: `DiagonalResidual.JetRate`
itself is only an eventual `iteratedFDeriv` inequality and does not bundle
smoothness. No inspected endpoint consumer used that rate alone as a
regularity certificate.

## Open obligations

### A. Common-domain correspondence

The inverse theorems provide explicit smoothness, periodicity, and mean
conditions, but this pass has not produced a complete table showing that all
inverse and differentiated-inverse calls share one nonempty domain throughout
the correction scheme. The obligation remains open until every call site and
the endpoint extension are mapped to the same admissibility data.

### B. Premise provenance

The residual theorem is structurally comprehensive, but its `Invariant`,
`PhysicalData`, geometry, and field-representation premises are substantial.
Source inspection confirms that they are passed through the construction and
that the endpoint adapter derives its smoothness obligations from stage
representations and `PhysicalJets`. It does not independently establish that
the analytic content of every invariant and `PhysicalData` field follows from
the paper's stated hypotheses. This is a proof-premise audit, not a lexical
`sorry` finding.

### C. Torus versus whole-space target

The torus candidate statements and the whole-space R3 comparator theorem are
separate propositions. The positive torus residual result must not be reported
as if it were already the whole-space CMI conclusion. The R3 path adds
localisation, compact positive-time support, force decay, and the global
comparison contradiction; those bridges require separate closure.

### D. Kernel interface

The corrected independent probe now runs from the fork root, but
`ComparatorSolution.olean` was not emitted by the bounded targeted build.
Consequently no transitive `#print axioms` result is asserted here. The exact
failure record is in `AXIOM_PROBE_4_34_RC2.txt`, and the ledger remains
pending rather than inferring anything from source text.

## Finding

The three semantic leads are narrowed but not closed. The current source gives
substantive positive evidence for fixed inverse loss, enumerated residual
closure, stage-independent loss, and endpoint smoothness at the inspected
adapter. No proof failure has been demonstrated by this pass. The correct
audit status is `PARTIALLY VERIFIED / OPEN`, with common-domain coverage,
premise provenance, and kernel axiom extraction still load-bearing.
