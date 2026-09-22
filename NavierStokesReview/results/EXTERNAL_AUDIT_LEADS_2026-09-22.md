# External audit leads

Date: 2026-09-22

## Source

Boduen Wang, “Lean 4 PDE Audit: Navier–Stokes semantic coverage”, SSRN,
14 September 2026:
<https://papers.ssrn.com/sol3/Delivery.cfm/7436502.pdf?abstractid=7436502&mirid=1&type=2>

This is an independent preprint, not a Clay or OpenAI determination. It does
not report a kernel exploit or a discovered `sorryAx` dependency. Its central
objection is semantic coverage: a Lean abstraction may be internally proved
without displaying a two-way correspondence to every analytic obligation in
the paper.

## Three actionable leads

1. **Common positive domain.** Check every inverse and differentiated inverse
   in the finite correction scheme against one common nonempty domain, not
   merely local domains attached to individual records.
2. **Residual closure.** Reconcile every nonlinear residual term, including
   curl remainders, self-interactions, pressure reconstruction, mean
   corrections, support, and normalisation, with the final residual bound.
3. **Stage-independent derivative loss.** Verify that the derivative-loss
   bound depends on derivative order but not on correction stage, and that the
   endpoint extension consumes this bound together with explicit smoothness.

## Current disposition

The present audit has already traced the finite-stage residual-rate path and
found explicit `ContDiffOn` fields at the principal residual-stability
consumers. That is not enough to close the three broader leads. They remain
`OPEN` and are now the next source-level dissection targets. The external
report is evidence for prioritisation, not evidence that the OpenAI result is
false.
