# Priority source review: profile, covariance, axis, and stress modules

Review date: 2026-09-27
Scope: direct source reading of ten endpoint-reachable `NavierStokes/` modules selected from the full-tree queue.  This report records bounded source findings; it is not a build certificate and does not claim that the remaining reachable queue has been reviewed.

## Controlled conclusion

The tranche contains substantive mathematical infrastructure:

- actual radial histories and pressure primitives;
- exact local five-row repair identities and conservative stress cancellations;
- exact covariance averages for periodised pulse products;
- smooth axis extensions for finite lower-order sources;
- smooth ODE/Volterra reconstruction and energy bounds;
- profile, pressure, and jet estimates used by later assembly.

These results strengthen the evidence that the upstream construction is real.  They do not, in the declarations reviewed here, prove the endpoint statement

\[
  \operatorname{Moments}(u_{\mathrm{selected}},p_{\mathrm{selected}},f_{\mathrm{selected}})
    =(M,I,J,S,C_p)
\]

after the final Cartesian potential sums, curls, localisation, periodisation, and endpoint packaging.  No non-zero selected-field remainder, impossibility theorem, or `False` is claimed here.

## Source findings

| Source | Direct anchors inspected | What is actually proved | Endpoint relevance |
|---|---|---|---|
| `AxisSourceRegularity.lean` | `omegaDivX_smooth` 192-219; lower pressure source 522-636 | Finite lower-order quotient/pressure-source expressions are smooth and analytic, including an axis extension. | Axis regularity of reduced sources; no whole-space Cartesian moment transport. |
| `NativeBandExtension.lean` | endpoint jets 45-131; phase/pressure regularity 179-265; prepared band 297-355; zero germs 501-580 | Support-endpoint jets, strict-cone continuity, phase pressure/velocity smoothness, closed-band regularity, and zero germs are proved. | Regularity/gluing support; no `barMoment` or five-observable endpoint identity. |
| `OutgoingProfile.lean` | fields and observables 24-75; integral identities 316-428; specification 555-590; existence 592-665 | The selected outgoing profile has genuine `M`, `J`, energy, pressure, axis, and total-zero identities. `Specification` packages these reduced-profile facts. | Strong reduced-profile certificate; it is not a theorem about the final selected Cartesian field. |
| `PartitionedCovariance.lean` | cutoff/support 28-49; `Pulse` 62-82; periodised covariance 112-130 | Compact grid masks, periodisation, slot injectivity, and covariance averaging are handled exactly for pulse products. | Supports covariance assembly; it does not evaluate the five radial observables of the final field. |
| `ProfileHistories.lean` | histories 158-230; profile structure 303-350; pressure derivatives 434-436 | Histories are defined as genuine radial integrals with fundamental-theorem derivatives; pressure is built from an actual primitive plus axis data. | Establishes reduced integral semantics, not endpoint Cartesian transport. |
| `ReferenceBounds.lean` | pressure/history bounds 50-177; five-jet parameter 394-399; source/jet bounds 601-689 | Provides source models, pressure/history estimates, a `Fin 5 → ℝ` bounded jet parameter, and natural-coordinate bounds. | Bound and parameter infrastructure; no selected-field moment equality. |
| `PrimaryODE.lean` | `FrameData` 31-111; solution reconstruction 189-245; smoothness 254-342; primary bounds 415-460 | Defines actual moving-frame input, forcing projection, Volterra solution, ambient reconstruction, smoothness, and coefficient/energy estimates. | A real local ODE/PDE component; no radial moment or endpoint packaging theorem. |
| `NaturalCoefficientBridge.lean` | natural coefficient zeros 114-205; history/germ transfer 296-320; radial zero primitives/stresses 463-505 | Transfers natural reduced equations to coefficient zeros, radial averages, histories, and zero inner stress primitives under explicit hypotheses. | Reduced natural-to-radial bridge; not the final Cartesian `tsum`-to-moment bridge. |
| `GaugeDebtIncrement.lean` | three-coordinate debt declaration 5-10; moment change 169-220; wave update 323-423; temporal update 448-667 | Defines the actual `Fin 3` debt, proves moment-change formulas for wave and temporal updates, and proves rate-class bounds. | Genuine physical rank/debt update machinery; its debt is not the paper’s final five-observable tuple at `Witness`. |
| `GlobalStressSupport.lean` | histories 20-38; positive-order moments 119-180; density/stress zeros 196-247; nominal support 428-473 | Pulls slow profiles to signed radial histories, proves `PositiveOrderMoments.moments = 0`, conservative moment cancellations, exterior stress zeros, and compact stress support for nominal coefficients. | Strong upstream five-row/stress result. It stops at slow/radial sequence objects and does not state final selected Cartesian endpoint transport. |

## Important distinction exposed by this tranche

`GlobalStressSupport.moments_zero` is a real theorem about

```lean
PositiveOrderMoments.moments n
  (PositiveOrderMoments.slice (axialHistory s) eta)
  (PositiveOrderMoments.slice (angularHistory s) eta)
  (fun R => previousOmega s n (R, eta)) = 0
```

and `conservative_moments_zero` converts that repair information into four slow-stress/radial cancellations.  This is materially stronger than merely importing a file.  It is nevertheless not the same proposition as evaluating the final activated Cartesian `ASum`/`BSum`/`PSum` field after all curls, cutoffs, periodisation, and infinite summation.

Likewise, `OutgoingProfile.Specification` carries exact reduced-profile mass and angular-integral zeros, while `PartitionedCovariance.Pulse.wave_covariance` evaluates a periodised covariance.  Neither declaration has the endpoint `Witness` as its target, and neither supplies the missing composition theorem.

## Audit classification

- Upstream profile/stress machinery: **confirmed real and mathematically substantive**.
- Reduced radial/history transport: **confirmed for the inspected hypotheses and domains**.
- Final selected Cartesian five-observable transport: **not established by these ten files**.
- Concrete selected-field defect \(\Delta m\neq0\): **not computed here**.
- Kernel contradiction `False`: **not obtained**.

The full-tree register remains the authoritative completeness counter.  This tranche reduces the open reachable queue only after the register generator is rerun successfully.
