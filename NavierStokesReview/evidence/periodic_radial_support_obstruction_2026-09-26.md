# Periodic/radial support obstruction

Status: zero-sorry conditional transport result. This is not a contradiction to
`selected_witness`.

## Source trace

| Layer | Source location | Recorded fact |
|---|---|---|
| Cartesian space | `NavierStokes/ProblemStatement.lean:33-49` | `SpaceTime` is time together with `EuclideanSpace ℝ (Fin 3)`; `UnitSpatialPeriodsOn` imposes unit spatial translations. |
| Periodisation | `NavierStokes/PeriodicLocalization.lean:62,192-204` | `periodize` is defined and `periodize_add_lattice` proves its lattice translation identity. |
| Selected velocity construction | `NavierStokes/SpatialLocalization.lean:213,250-252` | `periodicVelocity` is the curl of a periodised potential and `periodicVelocity_periodic` proves its spatial periodicity. |
| Radial support | `NavierStokes/RadialAlias.lean:39-40` | `RadiallySupported a b f` means `support f ⊆ Prod.fst ⁻¹' Icc a b`. |
| Scalar observable | `NavierStokes/DefectIncrementBounds.lean:214-220` | `barMoment` consumes a scalar field and expands to a weighted integral of `torusAverage`. |

## Machine-checked result

`NavierStokesReview/src/completions/PeriodicRadialSupportObstruction.lean`
proves, without `sorry`, that if

$$
g(r+1,Y)=g(r,Y)quad	ext{for all }r,Y
$$

and `g` is supported in a bounded radial interval $[a,b]$, then

$$
g(r,Y)=0quad	ext{for all }r,Y.
$$

The pullback theorem additionally states the corresponding conditional result
for a Cartesian field along a map satisfying

$$
\phi(r+1,Y)=\phi(r,Y)+e_0.
$$

## Scope boundary

The result does not assert that the selected Cartesian velocity or its scalar
pullback has `RadiallySupported` support. It therefore does not show that the
selected field is zero, does not compute a nonzero radial remainder, and does
not derive `False`. It identifies an exact obligation for the missing
Cartesian-to-radial transport theorem: the proof must either establish a
compatible radial support model for the periodised field or explain why the
radial observable is not being applied to that field.

The live calculation remains CALC-38: pass the selected infinite `tsum`
through curl, `torusAverage`, `barMoment`, axis terms, tail terms, and the
weighted radial integral.
