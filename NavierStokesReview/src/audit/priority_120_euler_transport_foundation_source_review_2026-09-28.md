# Priority 120: Euler transport-foundation source review

## Scope

This tranche reviews ten modules outside the captured Navier--Stokes endpoint
closure. They are part of the repository-wide Euler construction and must not
be labelled dead code merely because they do not import into the captured
Navier--Stokes root. The review asks what each module actually proves and
whether it can transport the Navier--Stokes selected Cartesian observables.

## Declaration-level findings

| File | Source anchors | What is actually defined/proved | Audit classification |
|---|---:|---|---|
| `Euler/BaseEulerSign.lean` | 1--2, 10, 22--78 | Imports Euler guard and packet-strain evolution modules; proves initial source/frame identities and positivity of a source numerator under norm/time hypotheses. | Euler sign/guard infrastructure; no Navier--Stokes endpoint transport. |
| `Euler/BaseEulerSobolev.lean` | 1--3, 11, 19, 31--43 | Builds `baseSobolevData` and `solutionSobolevData` for Euler base/solution evolutions. | Euler Sobolev packaging; no selected Navier--Stokes field or `barMoment`. |
| `Euler/BaseEulerUniform.lean` | 1, 9, 14--88 | Defines uniform amplitude and label bounds and proves sup, jet, label, and `Hq` bounds for the Euler base family. | Uniform Euler estimates; rates are not the selected Cartesian five-observable bridge. |
| `Euler/BaseSmoothState.lean` | 1--2, 10, 14--22 | Defines the initial Euler state from bounded parameters and a positive scale. | Euler state constructor; no force provenance or selected NS transport. |
| `Euler/BaseTransportCommutator.lean` | 1, 7, 17--113 | Defines a five-gradient norm and scalar word commutators, then proves recurrence and bounded commutator estimates for word lengths up to six. | Genuine Euler transport estimates; no radial moment identity. |
| `Euler/BaseTransportL2.lean` | 1--2, 8, 18--82 | Defines a base transport constant and proves finite-word gradient/L2 transport bounds. | Genuine Euler L2 estimate; no connection to `ActualCandidateAssembly.Witness`. |
| `Euler/BaseWordMetric.lean` | 1, 7, 13--62 | Defines finite word indices, word values, a word metric, cardinality, and two-sided comparison with a Sobolev norm. | Euler metric infrastructure; no selected NS observable. |
| `Euler/BoundedCoefficientSmooth.lean` | 1, 7, 16--101 | Bundles bounded coefficient fields, differentiates them, and proves translation differentiability and smoothness. | Euler coefficient regularity; no final NS packaging theorem. |
| `Euler/BoundedEvaluationDifferentiation.lean` | 1--3, 11, 21--70 | Proves a bounded-evaluation Fréchet derivative statement under a uniform operator bound. | Generic calculus lemma; no selected field or radial integral. |
| `Euler/BoundedFieldCalculus.lean` | 1--2, 15, 41--258 | Defines bounded bilinear, composition, path-composition, adjoint, and norm-control maps for fields and continuous paths. | Generic bounded-field calculus; no CMI C/D transport. |

## Reachability and isolation check

The ten files are imported by Euler-side modules such as
`Euler/BaseEulerInput.lean`, `Euler/BaseEulerState.lean`,
`Euler/SobolevBaseCommutator.lean`, `Euler/ExternalScalarCommutator.lean`,
`Euler/MeanCoefficientPath.lean`, and `Euler/TransversePacketHistoryData.lean`.
The source tree therefore shows genuine Euler-side reuse. This review does
not call those modules unreachable in the repository-wide sense.

The inspected imports do not cross into the Navier--Stokes `ActualCandidate`
or `NavierStokesR3.theorem_1_1` path. That is an architectural scope result,
not a claim that the modules are irrelevant to OpenAI's separate Euler
formalisation.

## Findings relevant to the anti-blindside protocol

No declaration in this tranche has the required selected Navier--Stokes
observable shape:

\[
  \texttt{selected Cartesian field}
  \longrightarrow
  \texttt{torusAverage/barMoment}
  \longrightarrow
  (M,I,J,S,C_p).
\]

The absence of such a declaration in these ten files is not itself an
impossibility theorem. It only classifies the tranche as Euler-side
foundation/regularity infrastructure and prevents it from being misused as
evidence that the Navier--Stokes paper-to-endpoint bridge has been established.

No `sorry`, `admit`, or custom axiom token was found in the ten source files
during this review. Compiler verification of the new review prose is not
applicable; the separate selected-field completions remain subject to the
review-package `.olean` build gate.

## Status

This is source-reviewed evidence for repository-wide classification. It is not
a kernel refutation, not a CMI verdict, and not a substitute for the remaining
selected-field curl/localisation/periodisation/`tsum` calculation.
