# Selected force at the singular origin

## Result

`NavierStokesReview/src/probes/SelectedForceOriginCompositionProbe.lean`
compiles with zero errors and contains no `sorry` or project-specific
`axiom` declaration.

The probe extracts the actual schedule and force from
`ActualCandidateAssembly.selected_witness`. It then proves, for the selected
origin path and eventually for (t	o1^-), that

$$
f(t,0)=\mathcal R_{\mathrm{periodic}}(t,0)
       =\mathcal R_{\mathrm{original}}(t,0).
$$

The first equality uses the late-time activation identities and the
`CandidateProperties.navier_stokes` premise. The second equality uses the
periodic localisation and spatial plateau identities at the origin. The
selected `VanishingJointJets` premise then gives

$$
\lim_{t\to1^-}\lVert f(t,0)\rVert=0.
$$

## Consequence for the review

This closes the specific proposal that the selected force must diverge at the
origin merely because the selected velocity diverges. The source constructs a
flat residual cancellation at that point, and the final force inherits that
limit on the selected path. The earlier conditional theorem remains useful:
any fixed positive lower bound of the form

$$
c\lVert u(t,0)\rVert\leq\lVert\mathcal R(u,p)(t,0)\rVert,
\qquad c>0,
$$

is incompatible with the selected endpoint. The source does not provide that
lower bound, and the new result shows why it cannot be used as an objection to
this construction.

The live formal review target is therefore not force explosion. It is the
unresolved semantic transport from the paper's five moments and global pressure
meaning into the actual selected fields whose residual jets are being used.

## Source trace

- `ActualCandidateAssembly.selected_witness` supplies the selected fields and
  force.
- `CandidateProperties.navier_stokes` identifies the force with the residual
  on the pre-singular interval.
- `TimeLocalization.activatedVelocity_eventuallyEq_late` and
  `activatedPressure_eventuallyEq_late` remove the late-time activation layer.
- `MixedPeriodicAssembly.periodicResidual_eventuallyEq_cut` and
  `cutResidual_eventuallyEq_original` identify the origin residuals.
- `VanishingJointJets` supplies the selected raw residual limit.

This is a selected-path result. It neither proves the CMI claim correct nor
establishes a formal contradiction.
