# Mirror-force symmetry audit

## Result

The negated field

$$
f_{\mathrm{mirror}}=-f
$$

is a legitimate smooth field whenever `f` is smooth. This is proved in
`NavierStokesReview/src/probes/MirrorForceSymmetryProbe.lean` by the theorem
`mirrorForce_smooth`.

That fact does not refute an existential forced candidate. It constructs a
different input force. The original candidate remains a witness for the
existential proposition unless a contradiction is derived from its own
properties.

## Same-field test

The probe also proves, pointwise, that if the same `u` and `p` satisfy both

$$
\mathcal R_\nu(u,p)=f
\qquad\text{and}\qquad
\mathcal R_\nu(u,p)=-f,
$$

then `f = -f` at that point. Thus the mirror equation is incompatible with a
non-self-negative original force for the same fields. It does not say that the
solution driven by `-f` is the same solution driven by `f`.

## Why energy does not reverse automatically

The work term for the mirror problem is

$$
\int (-f)\cdot u_{\mathrm{mirror}}\,dx,
$$

where `u_mirror` is a new unknown solution. Replacing it by the original `u`
has no theorem behind it. Moreover, the advection term is quadratic, so the
Navier--Stokes operator is not odd under `u ↦ -u`. The whole-space uniqueness
theorem in `R3/WholeSpaceUniqueness.lean:30-68` compares solutions with the
same force and equal residuals; it does not compare solutions for `f` and `-f`.

## Disposition

The mirror construction is useful as a compiled symmetry check and as a way to
show that force regularity is preserved under negation. It is not a
counterexample to the C/D existential claim and does not establish a pressure,
energy, or uniqueness contradiction for the selected witness.

**Build:** Lean 4.34.0-rc2, zero errors, no `sorry`, no custom axiom.
