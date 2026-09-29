# Priority 161: rebuttal adjudication of moment transport and force smoothness

Date: 2026-09-29

Status: source-grounded adjudication; no selected-field mismatch or `False`
claimed.

## Question

The supplied rebuttal argues that `ActualCandidateAssembly.Witness` omits the
paper's five-moment equality, that the five moments are the manuscript's only
residual pole-cancellation mechanism, and that the Lean endpoint therefore
assumes rather than proves smoothness of the residual-defined force.

## Raw source findings

### 1. The endpoint does omit a named final tuple

`NavierStokes/ActualCandidateAssembly.lean:1121-1151` defines `Witness` with a
selected schedule, three potential sums, away extensions, a forcing field,
`CandidateProperties`, `ContDiff` of that forcing, `CandidateConsequences`, an
H3 blow-up limit, derivative decay, and boundary limits. The declaration does
not contain a field or conjunct named `moments`, `barMoment`,
`FiveRowRank.FiveRows`, or an equality of a final selected field to
`(M, I, J, S, C_p)`.

This supports a precise `CTR-005` finding: the public result type does not
export the paper-level observable identification. It does not by itself show
that the selected values are wrong.

### 2. The endpoint does not accept `NativeBounds` from thin air

The selected construction is materially stronger than an abstract interface
countermodel:

- `ActualCandidateAssembly.lean:1079-1088` constructs `physicalData` through
  `ActualPhysicalPrefixFields.physicalFields_all` and an actual cycle
  representation.
- `ActualCandidateAssembly.lean:1090-1098` constructs `estimates` with
  `GluedStageEstimates.actualStageEstimates`, passing the actual physical data.
- `GluedStageEstimates.lean:684-725` defines that constructor with a concrete
  `PhysicalData` family and supplies `finite_residual` through the actual
  residual-rate theorem.
- `ActualStageEstimates.lean:348-400` invokes
  `ActualCycleResidualBounds.finite_residual_rates` for those concrete fields.
- `LocalResidualFlatness.lean:80-125` consumes the selected estimates to derive
  a common schedule and `AllResidualJetRates`; it does not merely assume the
  finished rate result as a free premise.

Therefore the phrase “Lean checks rate bounds but assumes them” is false if it
means the selected endpoint has an unproved `StageEstimates` hypothesis. The
correct statement is narrower: the selected rate chain is genuinely derived,
but the inspected declarations do not identify its final Cartesian output
with the paper's five reduced-profile observables.

### 3. Force smoothness is derived from full residual limits

`NavierStokes/CandidateFromLimits.lean:35-57` derives smoothness of the traced
residual from the derivative recurrence and locally uniform limits
`hlim`. Lines 80-87 define the force by smooth extension of that traced
residual and prove `force_smooth`. Lines 97-112 prove agreement with the
activated Navier--Stokes residual for `0 ≤ t < 1`. The same route is consumed
by `MixedPeriodicAssembly.exists_candidate_force` at
`MixedPeriodicAssembly.lean:338-365`.

This is a real formal route to force regularity. It is not evidence that the
paper's moment explanation has been transported, but it also is not evidence
that the force is merely assumed smooth. The source constructs smoothness from
the full residual-jet limit package.

### 4. What the manuscript actually says about the five moments

The extracted manuscript `docs/navier-stokes openai.txt` states:

- `523-546`: cumulative radial integrals govern pressure, radial velocity, and
  stress; modulation changes them by `O(N^-1)` and a local correction restores
  all five exactly.
- `695-735`: the correction cycle separately handles wave amplitudes, signed
  covariance stress, auxiliary-time inversion, and the five radial moment
  equations. The text explicitly says that full updated products, pressure,
  curls, cutoffs, and nonlinear remainders are retained.
- `746-757` and `761-784`: shrinking-cutoff summation, full residual comparison,
  flatness, and smooth-force extension are separate completion steps.
- `8091-8107` and `8451-8517`: Appendix B/C gives exact reduced-profile moment
  matching, five fixed bumps, and propagation of equality to pressure and
  `Q_s,N_s` in the exterior profile.

These passages establish that the five moments are load-bearing within the
written profile construction. They do not, by themselves, prove that the
final selected Cartesian field has a separately exported five-observable
identity in Lean.

## Claims in the supplied rebuttal that are not source-established

### “The five moments are the only mechanism”

This is too strong. The manuscript explicitly lists several distinct operations
in `695-735` and says the full residual is recomputed after each operation. The
five equations are a crucial finite-dimensional correction block, but the
source does not establish that they are the only mechanism responsible for
the final residual flatness.

The raw text search of the extracted manuscript found zero occurrences of
`Fredholm`, `adjoint`, and `Laurent`, and zero occurrences of the phrase
`if and only if`. It therefore does not support attributing the specific
Fredholm-adjoint equivalence and Laurent-pole formula in the rebuttal to this
manuscript without a different source citation.

### “The individual residual terms diverge, and moments are iff the force is smooth”

This has not been established by the inspected sources. The manuscript says
the full residual is corrected and extended smoothly, but the quoted source
does not prove that each individual term diverges or that smoothness is
equivalent to one final five-moment equality. The Lean construction likewise
uses full residual derivative limits, not a theorem of that iff form.

### “AX-033 constructs a physical nonzero-debt countermodel”

`NavierStokesReview/src/extensions/SelectedEndpointMomentTransportObstruction.lean`
proves only

```lean
∃ d : Debt, d ≠ 0 ∧ Witness selectedBudget selectedThreshold
  selectedThreshold_geometry
```

where `d` is an independent abstract payload. The theorem proves that the
`Witness` proposition does not entail every abstract debt parameter is zero.
It does not construct a different selected velocity, pressure, residual, or
force whose actual physical moments are nonzero. Calling this a physical
countermodel is an overclaim.

## Adjudicated conclusion

The strongest supported adverse conclusion is:

> The repository contains genuine moment/rank/repair mathematics and uses
> concrete physical data to derive residual jet rates and force smoothness.
> Nevertheless, the inspected public endpoint does not export a theorem that
> identifies the completed selected Cartesian velocity/pressure/residual/force
> with the manuscript's five reduced-profile observables. Consequently the
> claim that Lean machine-checks the manuscript's complete five-moment
> explanation remains **not established** (`CTR-005`).

This conclusion is not a repair request to OpenAI and is not softened into a
claim that the authors merely need to add a label. It is an adverse
paper-to-code finding. Its boundary is equally strict: the current record does
not prove a nonzero selected-field defect, force nonsmoothness, impossibility,
or `False`.

