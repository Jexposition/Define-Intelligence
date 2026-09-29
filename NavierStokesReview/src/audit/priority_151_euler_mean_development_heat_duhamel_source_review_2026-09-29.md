# Priority 151 source review: Euler means, development bridge, heat invariants, and Duhamel calculus

**Date:** 2026-09-29
**Scope:** twelve current source files under `Euler/`, selected from the direct-review queue.
**Method:** raw source inspection of imports, declarations, theorem signatures, targeted endpoint/moment tokens, and source-hygiene tokens.
**Status:** tranche evidence only. This report does not claim that an unreviewed file lacks a declaration.

## Direct source findings

| File | Source anchors | What the source establishes | Audit boundary |
|---|---:|---|---|
| `Euler/CylinderSpatialMeanPath.lean` | 8; 25-70 | Defines a bounded spatial path mean, translation operator, translation covariance, norm bound, differentiability, and block majorants. | Cylinder mean/path estimates are not selected-field radial moment transport. |
| `Euler/CylinderSpatialMeanRepresentative.lean` | 17-64 | Proves continuity and `MemLp` properties for lifted raw means and almost-everywhere representative identities. | Representative and measure facts do not identify the CMI observables. |
| `Euler/CylinderTerminalAmplitude.lean` | 24-47 | Bounds constant-path blocks and terminal amplitudes. | A terminal amplitude bound is not `CandidateProperties` or a selected Navier-Stokes endpoint theorem. |
| `Euler/DevelopmentBridge.lean` | 20-55 | Proves the divergence/development identity and states admissible initial-data and smooth-`L²` equivalences. `velocityField` requires explicit all-order spatial integrability. | The source comment at lines 45-46 explicitly says the comparator does not provide that conversion hypothesis. This is an honest bridge condition, not a supplied global transport theorem. |
| `Euler/DivergenceFreeHeat.lean` | 17-132 | Defines projected gradient evaluations and proves heat, convolution, and mild-solution preservation of the zero-gradient invariant. | A cylinder heat invariant is not Cartesian five-moment transport or a pressure-Poisson representative. |
| `Euler/DriftGlobalInviscidGevrey.lean` | 9-21 | States a global inviscid Gevrey PDE construction under explicit order and scale hypotheses. | This is Euler drift infrastructure, not the selected Navier-Stokes `Witness`. |
| `Euler/DriftMetricForcing.lean` | 8-19 | States metric correction-forcing bounds using drift, pressure, transport, and coefficient estimates. | A forcing estimate is not the CMI force-provenance theorem or selected endpoint equality. |
| `Euler/DriftNonlinearEstimate.lean` | 8-45 | Proves drift-loss absorption, polynomial assembly, and correction-forcing polynomial bounds. | Nonlinear bound assembly does not establish the five named radial observables. |
| `Euler/DuhamelDifferentiation.lean` | 9-114 | Defines heat/Duhamel flows and proves continuity, Lipschitz, measurability, and derivative identities. | Duhamel calculus does not transport selected Cartesian moments. |
| `Euler/DuhamelEquation.lean` | 7-90 | Decomposes Duhamel terms, differentiates the source tail, and proves the inhomogeneous heat derivative identity. | An inhomogeneous heat equation identity is not the exported Navier-Stokes endpoint. |
| `Euler/DuhamelPasting.lean` | 8-55 | Proves initial congruence, shifted restart, source-integral, and mild-solution gluing identities. | Pasting identities do not supply global CMI correspondence. |
| `Euler/ExternalScalarCommutator.lean` | 8-120 | Defines scalar commutators, smoothness and `MemLp` results, non-negativity, successor bounds, and convolution bounds. | Commutator bounds are not a computed nonzero selected-field defect. |

## Cross-checks against the audit questions

This tranche contains real functional analysis and PDE-support infrastructure. The most important anti-overclaim finding is `Euler/DevelopmentBridge.lean`: the conversion to `velocityField` is guarded by an explicit all-order spatial-integrability hypothesis, and the source states that the comparator does not supply it. Therefore the bridge must not be reported as an unconditional theorem merely because the declaration exists.

The spatial-mean files establish bounded cylinder means, translation covariance, representative compatibility, and `L²` control. `DivergenceFreeHeat` establishes preservation of a projected zero-gradient invariant under heat and mild operations. The drift and Duhamel files establish Euler-side estimates and gluing/differentiation identities. None of the twelve files declares or consumes `barMoment`, `FiveRowRank`, `PositiveOrderMoments`, `selected_witness`, or `CandidateProperties`, and none has a conclusion identifying a final Cartesian field with `(M,I,J,S,C_p)`.

The `DevelopmentBridge` conditionality is not evidence of a contradiction. It is evidence that one conversion obligation is explicit rather than silently discharged. Likewise, the presence of heat, commutator, and Duhamel identities does not prove or disprove the Navier-Stokes selected-field moment bridge.

This is a **tranche-level absence result**. It does not prove repository-wide nonexistence and does not assert that these modules are dead. The register keeps repository inventory, captured endpoint closure, and declaration-level semantic inspection separate.

## Source hygiene

A direct token scan of all twelve files found no `sorry`, `admit`, or `axiom` token. This is a tranche-level observation and does not certify every imported dependency.

## Classification

- **Positive infrastructure:** spatial means, representative theorems, heat invariants, drift estimates, Duhamel differentiation/equations/pasting, and scalar commutator bounds.
- **Explicit conditional bridge:** `DevelopmentBridge.velocityField` requires all-order spatial integrability that the comparator does not provide.
- **No selected-field transport evidence in this tranche:** no five-observable equality, `barMoment` result, selected-witness theorem, or absolute pressure-Poisson theorem.
- **No escalation:** the tranche proves neither a nonzero selected-field defect nor `False`.

## Next action

Continue the direct source queue with the next highest-priority unresolved modules, preserving the rule that `reachable_not_semantically_inspected` is a worklist state rather than a negative mathematical finding.
