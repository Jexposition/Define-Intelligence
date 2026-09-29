# Priority 87 source review: residual grouping, diagonal rates, and compact-force bounds

**Review date:** 2026-09-28
**Scope:** six reachable modules selected from the semantic-coverage queue
**Evidence rule:** direct source declarations were inspected; import reachability was not treated as semantic transport.

## Controlled result

This tranche strengthens the verified residual and force-regularity side of the repository. It does not produce a nonzero radial-moment defect, an impossibility theorem, or `False`.

The modules establish:

1. axisymmetric-mode bookkeeping and angular residual grouping;
2. finite disjoint-support residual decomposition and reconstruction;
3. diagonal jet-rate transfer through stage limits and spatial curl;
4. compact-future-time and compact-spatial-force decay estimates;
5. a uniform pre-singular (L^2_x) force bound in the (R^3) model.

They do **not** establish the remaining selected-path composition

\[
\text{reduced moments}
\longrightarrow
\text{Cartesian potential/curl}
\longrightarrow
\text{localisation and periodisation}
\longrightarrow
\texttt{tsum}
\longrightarrow
\texttt{Witness}/\texttt{theorem\_1\_1}
\]

for the five paper observables. This finding is narrower than saying that moment machinery is absent. The earlier source reviews have already confirmed genuine reduced five-moment and physical `FiveRows` bridges in `RepairConeBounds.lean` and `BaseRankPatch.lean`.

## Module findings

| Module | Source result | Boundary status |
|---|---|---|
| `AxisymmetricResidualGrouping.lean` | Defines axisymmetric aliases, proves full-residual add/erase identities, and proves that angular averaging removes the nonconstant part under integrability assumptions. | Residual mode decomposition; no final radial observable transport. |
| `LocalResidualGrouping.lean` | Proves nonlinear residual identities for finite sums with smooth, pairwise-disjoint supports, then derives grouped and angular-mean residual formulas and reconstruction. | Local finite assembly; no global selected `Witness` equality. |
| `DiagonalResidual.lean` | Defines `JetRate`/`FiniteJetRate`, transfers stage residual rates to the limit, records the spatial-curl loss, and proves order-by-order all-jet flatness for the diagonal construction. | Genuine curl/jet bridge; not a fixed-tail moment theorem. |
| `CompactForceDecay.lean` | Uses spatial periodicity and compact future-time support to derive global weighted derivative decay in time. | Force regularity on the periodic model; no radial moment statement. |
| `CompactSpatialForceDecay.lean` | Converts fixed compact spatial support and smooth compact future-time support into weighted spacetime jet decay and a comparator force condition. | Compact-force semantics; no selected-field moment or pressure-Poisson transport. |
| `R3/CompactForceBound.lean` | Proves a uniform spatial (L^2)-square bound for continuous compact spacetime-supported force on the pre-singular interval. | Real (R^3) energy estimate; no five-observable composition. |

## Important semantic distinction

`DiagonalResidual.allJetsFlat...` is not evidence that the final field preserves the paper's radial moments. Its quantification is order-by-order: for each derivative order and requested flatness order, a suitable finite stage can be selected. That is materially different from a single theorem transporting weighted radial integrals through the complete infinite, localised Cartesian field.

Likewise, the compact-force theorems establish support and decay properties. They do not by themselves establish an absolute pressure-Poisson representative or the causal status of an a posteriori residual-defined force.

## Register action

The six modules are now explicit `evidence_inspected` rows in `semantic_coverage_register.py`. The JSON register and its Markdown/HTML mirrors must be regenerated after this report is added. The next queue is obtained from the regenerated register rather than copied from an earlier count.

