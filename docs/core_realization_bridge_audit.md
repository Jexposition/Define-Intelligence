# The Core Realization Bridge Audit
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

## 1. The Compiling Witness Interface Specification
**Target Exact Lines:** 
* `selected_witness` instantiation (`ActualCandidateAssembly.lean`, Line 1177)
* `Witness` type definition (`ActualCandidateAssembly.lean`, Line 1121)
* `estimates` instantiation (`ActualCandidateAssembly.lean`, Line 1090)
* `physicalData` type signature (`ActualCandidateAssembly.lean`, Line 1079)

**Analysis:**
The headline theorem unpacks `selected_witness`, which is instantiated by `witness B N0 hN`. The underlying `Witness` type explicitly consumes properties of `potentialSum`, `directStages`, and abstract `AwayExtensions`. To satisfy the bounds, `witness` passes `estimates`, which consumes `physicalData`. 
The exact type signature consumed is:
`∀ J, ActualCycleResidualBounds.PhysicalData B (ActualCandidateConstruction.residualBand B N0) (ActualCandidateConstruction.cycle B N0 J).state ...`
This unfolds to `PhysicalFields`, mapping straight back to `PhysicalResidualJetBounds.lean` and `CorrectionStep.lean`. The witness natively consumes pure geometric PDE residual decay bounds (`NativeBounds`), NOT algebraic moment ranks.

## 2. The Ghost Moment Drift Severing
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
The repository achieves a flawlessly valid Lean 4 compilation by constructing a robust semantic firewall between the physical PDE evaluation and the algebraic moment constraints. The foundational modules, including the base profile (`TailGaugePotential`) and the residual bounds (`PhysicalResidualJetBounds`), contain mathematically sound, genuine 3D spatial evaluations. The theorem does not rely on dimension-dropping tricks or 'fake' 2D math; the underlying vectors interact dynamically in full 3D space. 

However, a critical divergence occurs at the final assembly boundary (`ActualCandidateAssembly.selected_witness`). The proof satisfies the CMI type checker by evaluating PDE correctness exclusively through direct geometric jet decay bounds (`NativeBounds`). The 5-coordinate moment arrays $(M, I, J, S, C_p)$ discussed heavily in the accompanying paper—and structurally formalized in `FiveRowRank` and `PositiveOrderMoments`—are never actually imported into the residual realization chain. 

Consequently, while the repository's modules compile, the paper-to-code
correspondence is not established by the selected public interface. The
review can require an explicit moment-realisation theorem and its transport
through the residual estimates. It must not call the five-moment narrative
dead code or claim that the selected fields are decoupled from 3D geometry
without a further theorem.
