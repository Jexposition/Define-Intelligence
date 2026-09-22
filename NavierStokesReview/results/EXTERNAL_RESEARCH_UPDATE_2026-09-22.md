# External research update

Date: 2026-09-22

This file records external material used to prioritise the peer review. It is
not evidence that the OpenAI result is true or false. Primary CMI and OpenAI
sources are separated from independent technical leads and downstream work
that assumes the OpenAI construction.

## 1. Official claim and acceptance standard

- OpenAI's announcement presents the work as a proof of forced finite-time
  singularity constructions and describes a Lean formalisation and checking
  process. It also says OpenAI is not claiming the Clay Millennium Prize.
  Source: <https://openai.com/index/navier-stokes-solution/>.
- The CMI problem statement defines the whole-space and periodic alternatives,
  including smooth forcing, decay conditions, bounded-energy global solutions,
  and the pressure-periodicity erratum. Source:
  <https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf>.
- CMI's rules require a qualifying publication, two years of rigorous
  examination, and general acceptance before CMI considers a proposed
  solution. Source: <https://www.claymath.org/millennium-problems/rules/>.

Consequently, Lean kernel evidence and CMI prize recognition are separate
gates. The present review targets the former and the exact CMI proposition;
it does not treat a public announcement as satisfying the procedural gate.

## 2. Independent semantic-coverage lead

Boduen Wang's September 2026 SSRN preprint, “Lean 4 PDE Audit:
Navier–Stokes semantic coverage”, proposes three concrete audits:

1. establish one common nonempty domain for every inverse and differentiated
   inverse used by the finite correction construction;
2. close the nonlinear residual term by term, including pressure, means,
   support, normalisation, and curl/self-interaction terms; and
3. make derivative loss depend on derivative order rather than correction
   stage, while connecting the bound to explicit endpoint smoothness.

Source: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7436502>.

The local source audit has found positive interfaces for several parts of
these checks, including a five-derivative torus inverse loss, an expanded
residual decomposition, a correction-index-independent loss parameter, and
endpoint extension structures. It has not yet proved one common physical
domain or the complete correspondence from the torus construction to the
selected R3 witness. These remain open review questions, not refutations.

## 3. Downstream work that is not independent validation

Cao and Chi's September 2026 arXiv paper studies distributional data generated
by the compact forced blowup construction, but its abstract explicitly takes
the OpenAI forced blowup theorem and associated formalisation as an input.
It is therefore downstream analysis, not an independent confirmation of the
construction or its CMI equivalence.

Source: <https://arxiv.org/abs/2609.10262>.

## 4. Related methodological evidence

Li's September 2026 arXiv paper on neural forcing distinguishes numerical or
training objectives from a continuum proof certificate and emphasises that a
specific analytic loss theorem and a robust positive margin are needed. This
is relevant methodology for checking any finite-dimensional or computational
surrogate, but it does not audit the OpenAI Lean files and is not evidence of
a defect in them.

Source: <https://arxiv.org/abs/2609.23934>.

## Disposition

The external research sharpens the audit lanes but changes no verdict. The
current status remains: source-level CMI mapping is substantially traced,
intermediate analytic declarations have a standard kernel axiom footprint,
headline transitive axiom output is pending, and no concrete CMI mismatch has
yet been established.
