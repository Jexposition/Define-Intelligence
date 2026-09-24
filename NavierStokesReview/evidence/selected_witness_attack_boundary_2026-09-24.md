# Selected-witness attack boundary

## Result

The zero-sorry probe `SelectedWitnessAttackBoundaryProbe.lean` establishes
two precise facts.

First, the exported `ActualCandidateAssembly.Witness` proposition does not
entail `d = 0` for every `PositiveOrderMoments.Debt d`.  This is a genuine
interface-level specification gap: the `Witness` result contains the three
stage sums, away extensions, force predicates, residual consequences, force
decay, and boundary jets, but no field-level five-coordinate moment equality.
It does not, by itself, prove that the selected fields violate those
equalities.

Second, the scalar endpoint predicates used by the proposed force attack are
compatible: a sequence can tend to infinity while another tends to zero.
The proved contradiction requires an additional positive lower bound of the
form

$$
c\,\|u(t,0)\| \leq \|R(u,p)(t,0)\|,
\qquad c>0,
$$

on the same approach filter.  The selected source currently proves upper
jet-rate bounds and explicit core cancellation, not this lower bound.

## Consequence for the review

The force-smoothness lane is closed as a force-explosion route: the companion
selected-force composition probe connects the selected force to the flat
residual at the origin and proves that its norm tends to zero. It remains
invalid to infer residual divergence from velocity divergence alone.

The moment result remains CTR-005: the upstream five-coordinate repair is
real, but no theorem has been exhibited that transports its named rows into
the selected `Witness` output and then into the residual/force construction.
