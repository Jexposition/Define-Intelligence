# Selected torus-average representation boundary

**Date:** 2026-09-25  
**Tree:** current review worktree, branch `review/cmi-first-navier-stokes-2026-09-22`  
**Claim level:** selected-source boundary; not a contradiction

## Result

The source exposes two different objects that are not yet identified by a
theorem.

1. `PressureStream.torusAverage` averages a scalar field over every auxiliary
   coordinate `Y : Plane`.
2. `ActualMeanStageData.radialSection` evaluates a selected physical field on
   the single positive-radial section
   `((p.1), AxisymmetricResidual.pack p.2.1 0 p.2.2)`.

The existing radial-section and angular-field theorems establish the selected
graph value. They do not establish that this graph value equals the auxiliary
torus average required by `barMoment_apply`.

## Source ledger

| Source | Lines | Exact role |
|---|---:|---|
| `NavierStokes/PressureStream.lean` | 66–71 | `torusInner` and `torusAverage`; the latter integrates the two auxiliary coordinates over `[0,1]`. |
| `NavierStokes/PressureStream.lean` | 122–134 | `pressureMass` and its radial integral use `torusAverage`. |
| `NavierStokes/ActualMeanStageData.lean` | 23–24 | `radialSection` fixes the second Cartesian coordinate to zero and samples one radial section. |
| `NavierStokes/ActualMeanStageData.lean` | 42–50 | `physicalPoint_radialSection` proves invariance of the selected graph under this radial-section replacement. |
| `NavierStokes/ActualMeanStageData.lean` | 56–74 | `coefficient_cylPoint` and `coefficient_angularField` transport the selected graph coefficient into the angular field. |
| `NavierStokes/DefectIncrementBounds.lean` | 214–220 | `barMoment_apply` identifies the required moment with the radial integral of `torusAverage`. |
| `NavierStokesReview/src/completions/SelectedDirectRadialMomentBridge.lean` | 28–49 | The direct branch reaches `barMoment_apply` and proves its selected order-two integral is zero. |

## Mathematical form of the open bridge

For a selected physical coefficient `D.field`, the source currently gives a
graph value of the form

$$
  a_j(n,R,s)=D_j\bigl(\operatorname{physicalPoint}(h,\operatorname{radialSection}(R,s))\bigr).
$$

The moment interface requires instead

$$
  \int_{\mathbb R}R^2
    \left(\int_0^1\!\int_0^1
      D_j\bigl(\operatorname{physicalPoint}(h,(R,s,Y))\bigr)\,dY_1\,dY_2\right)dR.
$$

No current selected-path theorem identifies these expressions. Such an
identity would require an explicit auxiliary-coordinate invariance theorem,
or a valid calculation of the graph-to-torus averaging map, together with the
support and integrability hypotheses.

## Consequence for the review

This sharpens `CALC-04` and `CTR-005`: the direct scalar branch has a proved
zero moment, but that result cannot be transferred to the full curled-potential
branch or to the mixed endpoint without the missing representation theorem.
The finding is a failure to exhibit a required selected-field bridge in the
published construction. It is not, by itself, a Lean proof of `False` or a
proof that the selected endpoint violates its own formal predicate.

## Verification

The existing zero-sorry direct bridge remains the executable check:

```text
elan run leanprover/lean4:v4.34.0-rc2 lake env lean \
  NavierStokesReview/src/completions/SelectedDirectRadialMomentBridge.lean
```

It exits successfully. No new theorem is claimed in this note; the source
boundary is recorded for the next selected potential/curl calculation.
