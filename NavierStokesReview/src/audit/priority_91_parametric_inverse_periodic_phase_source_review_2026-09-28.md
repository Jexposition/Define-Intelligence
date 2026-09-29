# Priority 91 source review: parametric torus inverse and periodic phase assembly

## Scope

This tranche reviews the two priority-117 modules at the periodic inverse and common-cover phase boundary.

## Findings

| Module | Source-grounded result | Boundary |
|---|---|---|
| `ParametricTorusInverse.lean` | Defines a smooth source with a real parameter and torus plane variables; proves smooth parameter and torus derivatives, preservation of periodicity and zero mean, coefficient and multiplier bounds, Fourier inverse representations, rapid-decay/finite-jet estimates, and smooth application of the inverse multiplier. | This is a substantial parametric torus inverse layer. It establishes solvability and regularity for periodic sources, not the final radial five-observable equality of the selected Cartesian field. |
| `PeriodicPhaseAssembly.lean` | Defines compact clock windows and smooth cutoff support; proves local finiteness and periodicity of `tsum`-based scalar periodisation, clock germs/path identities, phase and angular-lift periodicity, native-phase germ/jet equality, geometry refinement/transport, physical block construction, and carrier adapter periodicity/germ/jet facts. | This is a genuine phase/common-cover transport layer. It does not by itself compose with `barMoment` or export the five paper moments through `ActualCandidateAssembly.Witness`. |

## Controlled conclusion

The source confirms that periodic inversion, phase construction, compact support, local finiteness, and germ/jet transport are formally developed. This rules out describing the periodic layer as an empty or purely nominal wrapper.

The remaining distinction is:

\[
\text{periodic inverse and phase/germ transport}
\;\not\Rightarrow\;
\text{selected Cartesian }(M,I,J,S,C_p)\text{ equality}.
\]

The reviewed declarations do not establish the complete composition through the selected vector-potential curl, spatial localisation, infinite stage sum, torus average, radial pullback, and public `Witness`. No nonzero defect, impossibility theorem, or kernel-level `False` is established.

## Register action

The two modules are to be marked `evidence_inspected` in the authoritative register after adding these bounded findings to `semantic_coverage_register.py` and regenerating all register mirrors.
