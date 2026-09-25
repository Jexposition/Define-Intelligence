# Euler parent-child interval audit

## Scope

This note checks the quoted claims about a Zeno-style loss of temporal runway,
unmatched stage derivatives, and an implicit pinning force against the Lean
source actually present in the fork. It is a companion audit, not a transfer of
Navier–Stokes findings into the Euler result.

## Source findings

The recursive time data are explicit. `Euler/PacketSourceScaleSequence.lean`
defines `timeWidth` from consecutive scale values and proves positivity at
lines 42 and 141–145. `Euler/PacketSourceScaleGuards.lean:71-75` proves the
actual width contraction

$$
\operatorname{timeWidth}_{n+1}\leq \frac12\operatorname{timeWidth}_n.
$$

`Euler/PacketNestedHorizons.lean:11-108` defines the finite activation sum and
proves that every step is positive, `activationTime` is strictly increasing,
and every `horizonTime` remains above the common positive lower bound
`baseHorizon / 12`. `Euler/PacketStageRestriction.lean:17-58` transfers the
stage to its next horizon and proves that the next horizon stays below the
parent horizon.

These results do not prove a Zeno failure. They prove a controlled nested
schedule. The final singularity statement is packaged through the constructed
finite-lifespan object in `Euler/EulerSingularity.lean:104-151`, using the
maximal-field limit and divergent vorticity integral. No source theorem was
found asserting convergence to a separate quiet time `T_static < T*`, nor a
theorem showing that the activation sequence misses the maximal endpoint.

## Seam regularity

The source does not glue arbitrary values and then assume smoothness. The
general seam theorem `Euler/IntervalPathConcatenation.lean:13-118` requires
both endpoint value matching and derivative matching, then proves
`join_hasDerivAt_seam` and `join_hasDerivAt`. The actual path
`Euler/TransversePacketJoinedPaths.lean:29-90` supplies
`velocity_match`, `derivative_match`, and proves `velocityPath_time` through
the junction. The corresponding primary path has the same structure in
`Euler/TransversePacketPrimaryPaths.lean:27-84`.

This clears the specific claim that a first-order seam is silently accepted.
It does not establish an all-order time-jet theorem at every parent-child seam:
the inspected seam theorem is a first-derivative theorem, while the
`ContDiff ℝ ∞` results in these modules concern the translated spatial/orbit
parameter. A valid higher-order objection would therefore need an explicit
second-or-higher time derivative mismatch, not merely the presence of an
`if`-based glue definition.

## Pinning-force allegation

The inspected path equations use the actual past and future velocity paths and
their derivative traces. `velocityPath_time` depends on
`pastVelocity_time`, `futureVelocity_time`, and `derivative_match`; the primary
path's future branch is built from `zeroForcing` in
`Euler/TransversePacketPrimaryPaths.lean:86-108`. The source inspected here
does not establish a hidden external force holding the parent fixed. That
allegation remains unproved unless a concrete residual identity shows an extra
term in the assembled Euler equation.

## Review result

The quoted Zeno and first-order patching objections are not source-proven. The
live Euler audit target is narrower: determine whether the final construction
exports all time regularity required by the paper, rather than only the first
derivative needed by the evolution interface. This is an open verification
question, not a contradiction.

The audit does, however, correct the review record: it must not describe the
Euler interval machinery as an unverified discontinuous chain when the source
contains explicit value/derivative matching theorems.
