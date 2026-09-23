#   Bridge Audit
**Target Modules:** `ActualCandidateAssembly.lean`, `ActualCycleResidualBounds.lean`, `PhysicalResidualJetBounds.lean`

## Verification correction: absence of a direct moment import is not a PDE disproof

The source trace supports a real architectural question: the selected witness
uses native residual-jet bounds, while the public paper foregrounds named
five-moment identities. It does not support the stronger claim that the
residual chain contains no genuine 3D field. `TailGaugePotential` and
`AxisymmetricFields.potential` construct a three-component profile, and the
selected velocity is obtained through the spatial curl. The correct result is
therefore a missing selected-path moment-realisation theorem, not a fake-field
or lower-dimensionality theorem.

## 1.   Compiling Witness Interface Specification
**Target Exact Lines:** 
* `selected_witness` instantiation (`ActualCandidateAssembly.lean`, Line 1177)
* `Witness` type definition (`ActualCandidateAssembly.lean`, Line 1121)
* `estimates` instantiation (`ActualCandidateAssembly.lean`, Line 1090)
* `physicalData` type signature (`ActualCandidateAssembly.lean`, Line 1079)

**Analysis:**
The headline theorem unpacks `selected_witness`, which is instantiated by `witness B N0 hN`. The underlying `Witness` type explicitly consumes properties of `potentialSum`, `directStages`, and abstract `AwayExtensions`. To satisfy the bounds, `witness` passes `estimates`, which consumes `physicalData`. 
The exact type signature consumed is:
`∀ J, ActualCycleResidualBounds.PhysicalData B (ActualCandidateConstruction.residualBand B N0) (ActualCandidateConstruction.cycle B N0 J).state ...`
This unfolds to `PhysicalFields`, mapping straight back to `PhysicalResidualJetBounds.lean` and `CorrectionStep.lean`. The witness directly consumes geometric PDE residual decay bounds (`NativeBounds`). Upstream construction modules also contain moment/rank machinery, but the selected residual interface does not expose a theorem identifying those arrays with `(M, I, J, S, C_p)`.

## 2.   Ghost Moment Drift Severing
**Point of Divergence:** `PhysicalResidualJetBounds.lean` (Line 721 - `def residual`)
**Analysis:**
The PDE correctness is evaluated directly on the physical vector field using `residual u p` in `PhysicalResidualJetBounds.lean`. The compiler bounds the PDE by tracking spatial decay rates (`StateRealization.chartIdentity` and `residual_jetRate`). 
Because neither `FiveRowRank.lean` nor `PositiveOrderMoments.lean` is visibly
imported as a semantic identity by this residual-bounding module, the source
does not display how the paper's five named moments enter the selected bounds.
That supports a missing-transport objection. It does not prove that the
native residual estimates are false or that the moment modules are globally
dead code.

## 3. Final Closing Transmittal Text Generation
*(To be inserted into `OpenAI_NavierStokes_Peer_Review_v1.md` under 'Technical Discrepancies')*

**The Semantic Firewall and the Orphaned Moment Specification**
The repository achieves a Lean 4 compilation with a boundary between the physical PDE evaluation and the algebraic moment constraints. The foundational modules, including the base profile (`TailGaugePotential`) and the residual bounds (`PhysicalResidualJetBounds`), contain three-component spatial evaluations. The theorem does not rely on the pure-axial or fake-two-dimensional premise; the underlying field construction is genuinely three-component.

However, a critical divergence occurs at the final assembly boundary (`ActualCandidateAssembly.selected_witness`). The proof evaluates PDE correctness through direct geometric jet decay bounds (`NativeBounds`). The selected assembly's transitive import closure does contain `FiveProfileMoments`, `FiveRowRank`, and `PositiveOrderMoments` through upstream construction modules, but the residual-realisation chain does not expose those five-coordinate arrays $(M, I, J, S, C_p)$ as semantic premises or prove their identification with the selected residual.

Consequently, while the repository's modules compile, the paper-to-code
correspondence is not established by the selected public interface. The
five-moment machinery exists upstream, but its transport into the final
theorem bounds is not exhibited. The review can require an explicit
moment-realisation theorem and its transport through the residual estimates.
The pressure comparison interface has the same shape limitation: it compares
pressure gradients under hypotheses but does not state an absolute selected
pressure-Poisson representative. Neither gap alone is a formal contradiction
until a selected-path premise is shown false.
