# Priority 149 source review: Euler cylinder tensor, scalar, reflection, and representative infrastructure

**Date:** 2026-09-29
**Scope:** twelve source files under `Euler/`, selected from the repository-wide direct-review queue.
**Method:** raw source inspection of imports, declarations, theorem signatures, targeted semantic tokens, and source-hygiene tokens.
**Status:** tranche evidence only. This report does not claim that unreviewed files lack a declaration.

## Direct source findings

| File | Source anchors | What the source establishes | Audit boundary |
|---|---:|---|---|
| `Euler/CylinderPathWords.lean` | 1; 19-65; 72-126 | Builds finite translation words and derivative paths in continuous `L2` path spaces, with orbit, almost-everywhere, pointwise, Sobolev, block, majorant, and time-derivative results. | No selected Navier-Stokes field or five-observable equality. |
| `Euler/CylinderPhysicalTensor.lean` | 1-2; 17-46; 50-72 | Pulls a cylinder field back along graph coordinates, proves smoothness, and bounds iterated physical derivatives by cylinder derivative words with a frequency factor. | A graph pullback and derivative bound are not radial moment transport or pressure-Poisson semantics. |
| `Euler/CylinderPhysicalTensorDifference.lean` | 1; 14-30 | Transfers pointwise and difference bounds for physical tensors from almost-everywhere field hypotheses. | No selected endpoint or moment observable. |
| `Euler/CylinderPhysicalTensorLp.lean` | 1; 14-49 | Proves graph-word and physical-tensor `Lp` membership, defines the `Lp` tensor representative, and bounds its norm. | `Lp` control does not imply the paper's global radial identities. |
| `Euler/CylinderRawSupport.lean` | 1-2; 13-39 | Proves representative vanishing outside a closed support, support containment, and compact support under compactness hypotheses. | Support containment does not prove moment cancellation or cutoff commutator cancellation. |
| `Euler/CylinderReflection.lean` | 1; 12-61; 77-98 | Defines the cylinder reflection, proves measure preservation, isometry, translation interaction, derivative behaviour, and reflected test/gradient identities. | Reflection symmetry is not the selected Cartesian transport theorem. |
| `Euler/CylinderRetractRepresentative.lean` | 1-2; 19-56; 62-80 | Builds pointwise representatives from a retract pair, proves continuity, smoothness, almost-everywhere equality, and a time derivative along paths. | No selected Navier-Stokes candidate or five-moment tuple. |
| `Euler/CylinderScalarAverage.lean` | 1-2; 15-19 | Proves a scalar angular mean-zero result for the scalar primitive construction. | This is an explicitly assumed/constructed scalar angular invariant, not `(M,I,J,S,Cp)` transport. |
| `Euler/CylinderScalarClassical.lean` | 1-2; 13-79 | Defines the classical scalar angular primitive, proves periodic cover identities, mean-zero, smoothness, continuity, and zero under a zero-input hypothesis. | No global selected pressure representative or CMI endpoint. |
| `Euler/CylinderScalarParity.lean` | 1-2; 12-15 | Proves joint-even parity of the classical scalar primitive under the stated hypotheses. | Parity does not identify the selected-field radial observables. |
| `Euler/CylinderScalarPrimitive.lean` | 1-2; 20-51; 66-116 | Defines scalar embedding/projection and primitive operators, proves norm bounds, translation commutation, path operators, smoothness, and block bounds. | Operator bounds and commutation do not establish selected-field moment transport. |
| `Euler/CylinderScalarRepresentative.lean` | 1-4; 22-67 | Transfers smooth embedding and identifies the constructed scalar primitive with its classical representative almost everywhere and on the constructed field. | Exact representative agreement is not the OpenAI selected Navier-Stokes bridge. |

## Cross-checks against the audit questions

### Endpoint relevance

These files are part of the repository inventory but are not part of the captured `NavierStokes.R3.Theorem` import closure used for the current endpoint register. That is a scope label for the present endpoint graph, not a claim that the files are dead or that OpenAI does not use them in another root.

### Hidden bridge search within the tranche

The inspected declarations contain no occurrence of `barMoment`, `FiveRowRank`, `PositiveOrderMoments`, `selected_witness`, or `CandidateProperties`. They also contain no declaration whose input and output jointly identify a final Cartesian field with the paper's five-observable tuple `(M,I,J,S,C_p)`.

The result is therefore:

\[
\text{tensor/representative regularity} \not\Rightarrow
\text{selected-field five-observable transport}.
\]

The scalar files do contain genuine mean-zero and parity results. Those are narrower invariants on the cylinder scalar primitive and must not be relabelled as the paper's five cumulative radial identities.

### Source hygiene

A direct token scan of all twelve files found no `sorry`, `admit`, or `axiom` token. This is a tranche-level source observation and does not certify every imported dependency.

## Classification

- **Positive infrastructure:** graph pullback, physical derivative and `Lp` estimates, support, reflection, scalar primitive, mean-zero, parity, representative, and path results.
- **No selected-field transport evidence in this tranche:** no five-observable equality, `barMoment` result, selected-witness theorem, or absolute pressure-Poisson theorem.
- **No escalation:** the tranche proves neither a nonzero selected-field defect nor `False`.

## Next action

Continue the direct source queue with the remaining cylinder slow-curl and weight modules, while keeping repository inventory, captured endpoint closure, and declaration-level semantic inspection as separate dimensions.
