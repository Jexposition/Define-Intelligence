# Priority 1-2 source review: cross defects, transport geometry, and activation infrastructure

Date: 2026-09-27
Review mode: direct inspection of current `NavierStokes/` source.
Scope: ten highest-priority reachable modules from the full semantic register.

## Source findings

### `NavierStokes/CrossBasedMeanComposition.lean`

- `24-34`: defines `crossDefect` as the difference between the averaged cross
  covariance and the requested physical stress, and proves the exact additive
  decomposition.
- `44-54`: shows that tail agreement gives all-exponent class membership while
  retaining the finite head.
- `56-74`: `cross_cancels_with_defect` explicitly says that no cancellation on
  the finite head is assumed; the cross-defect radial-divergence term remains
  in the identity.
- `269-333`: derives pressure, cumulative bounds, mean gains, and measured debt
  bounds for an actual signed stage with cross defects.
- `389-505`: the four-stage mean/debt theorem requires the zero radial-moment
  hypotheses `hmθ` and `hmz` and propagates them through later stages.
- Finding: this is important positive and negative audit evidence.  The cross
  defect is an explicit intermediate quantity, not silently discarded.  The
  theorem is still about local mean/debt stages, not the final selected
  Cartesian `tsum` field.

### `NavierStokes/ActualCarrierTransportBase.lean`

- `27-89`: defines the selected carrier domain, slow map, reference geometry,
  native clock, and transported geometry.
- `121-152`: proves finite band-distance and ordering consequences; the
  unordered carrier branch is shown empty under the geometric threshold.
- `156-203`: proves clock/coordinate transport and identifies the canonical
  source region with the broad carrier.
- `218-270`: defines the canonical source region and transported cutoff and
  proves outer injectivity.
- Finding: this is genuine carrier-support and coordinate transport.  It does
  not evaluate any radial moment of the final velocity or pressure field.

### `NavierStokes/BorelExtension.lean`

- `26-147`: constructs compactly supported monomial templates and derivative
  bounds from finite profile data.
- `177-239`: constructs diagonal scales and summable majorants.
- `250-325`: defines the actual series extension, proves smoothness, derivative
  interchange, prescribed jets, and compact support.
- `363-371`: packages smooth compact extension and right-extension interfaces.
- Finding: this is a substantive all-order jet/gluing mechanism.  It carries no
  fluid-field moment observable and cannot by itself prove selected-field
  moment transport.

### `NavierStokes/DiophantineGraph.lean`

- `22-104`: proves nonvanishing quadratic symbols and conjugate-product lower
  bounds for nonzero integer frequencies.
- `171-263`: proves explicit radial/time Diophantine lower bounds and inverse
  multiplier growth estimates.
- `265-315`: packages the two graph directions and covering-frequency scaling.
- Finding: this is genuine frequency nonresonance infrastructure.  It is not a
  moment, pressure, or endpoint Cartesian-field theorem.

### `NavierStokes/FlatKernelBounds.lean`

- `28-75`: defines the concrete square-root kernel and proves positivity,
  differentiability, and coordinate bounds.
- `86-150`: defines finite derivative expressions and proves derivative
  evaluation/continuity.
- `181-274`: proves polynomial bounds from finitely many profile jets.
- `333-440`: proves kernel derivative identities, smoothness, and unweighted
  derivative bounds.
- Finding: this is analytic kernel-bound infrastructure used by flat-profile
  estimates.  It does not establish weighted radial-moment convergence of the
  selected `tsum` field.

### `NavierStokes/ParametricODE.lean`

- `30-121`: constructs the Volterra integral operator and its norm bounds.
- `128-218`: proves invertibility of the finite-interval equation operator and
  constructs the resolvent.
- `239-305`: constructs the solution from initial data and forcing and proves
  the integral equation, initial value, and derivative equation.
- `309-420`: proves parameter derivative identities and finite stability bounds.
- `427-464`: proves smooth dependence of the solution family on coefficients,
  data, and forcing.
- Finding: this is a real forward finite-interval ODE solution operator.  It is
  not the Navier–Stokes selected-witness endpoint and does not transport the
  five paper observables.

### `NavierStokes/PhaseCalculus.lean`

- `39-117`: defines the actual phase and proves its Fréchet derivatives and
  cylindrical phase-normal formula.
- `122-175`: proves joint smoothness and exact material-operator cancellation,
  including the backward sign convention.
- `178-224`: proves angular shifts, harmonic single-valuedness/periodicity, and
  smoothness of the complex carrier.
- `226-305`: proves off-axis smoothness and quantitative nonvanishing under a
  comparison-vector hypothesis.
- Finding: this is a concrete phase/chart calculation with an explicit
  off-axis denominator condition.  It is not a global radial-moment bridge.

### `NavierStokes/SlotColoring.lean`

- `33-98`: defines dyadic mesh widths and proves positivity and uniform ratio
  bounds.
- `112-185`: defines physical boxes and constructs an explicit finite proper
  colouring with palette cardinality 2250.
- `189-304`: proves adjacency index bounds, finite candidate sets, and uniform
  degree control.
- `310-459`: proves native-index gap and auxiliary-slot consequences for the
  actual covering construction.
- Finding: this is explicit combinatorial grid/overlap infrastructure.  It
  supports localisation bookkeeping but contains no field-level observable
  transport.

### `NavierStokes/WaveEnvelopeTransport.lean`

- `23-106`: defines integration rectangles and proves copy uniqueness and path
  geometry.
- `52-99`: proves exact envelope identification along the full integration path.
- `203-355`: proves local finiteness, grouped-copy reduction, support exclusion,
  and wave-class/jet consequences.
- `362-523`: transports source and forcing jets through the actual affine maps
  and integration paths.
- `550-581`: proves the native source path and anchored-solve vanishing under
  support exclusions.
- Finding: this is genuine support and jet transport for wave/forcing
  envelopes.  It does not calculate radial moments of the final selected
  Cartesian field.

### `NavierStokes/ActivationCone.lean`

- `26-64`: defines the actual inverse relative activation error and proves
  smoothness and uniform derivative bounds.
- `68-154`: proves ramp/collar cone inequalities and constructs an explicit
  error tolerance.
- `246-420`: proves exact stress factorisation, smooth reduced stress, cone-gap
  factorisation, and transport of stock errors into cone-coordinate bounds.
- `447-661`: constructs activated histories and derives comparison and compact
  reference bounds.
- Finding: this is a substantive activation/cone estimate layer.  It proves
  local algebraic margins and smoothness, not a selected-field moment identity.

## Cross-layer audit result

This tranche confirms that the repository contains non-vacuous mechanisms for

\[
\text{cross-covariance/debt updates},
\quad \text{carrier geometry},
\quad \text{Borel jets},
\quad \text{frequency inversion},
\quad \text{phase transport},
\quad \text{support colouring},
\quad \text{wave-envelope jets},
\quad \text{activation margins}.
\]

The most relevant audit observation is the explicit `crossDefect` path.  The
source does not silently assume finite-head cancellation: it retains a defect
term and separately requires zero radial-moment hypotheses in the four-stage
mean/debt theorem.  That narrows the remaining question to whether those local
conditions are subsequently transported into the final selected Cartesian
field, rather than proving that the final field fails.

No declaration reviewed here proves

\[
\operatorname{barMoment}(u_{\mathrm{selected}})=(M,I,J,S,C_p),
\qquad \Delta m\ne0,
\qquad \text{or}\qquad \texttt{False}.
\]

The tranche therefore strengthens the correspondence audit without changing
the calibrated status: **CTR-005 remains not established at the endpoint**.
