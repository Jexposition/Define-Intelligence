# Priority 189: OpenAI physical-wording source check

**Date:** 2026-09-30
**Status:** source-checked correction to the semantic record

## Finding

The supplied OpenAI manuscript does not state that its forced blow-up flow
“would never occur in physical reality”. That attribution must not appear in
the review unless a separate source is supplied and verified.

The manuscript instead uses an explicit physical framing and then states the
mathematical construction problem:

* `docs/navier-stokes openai.txt:106-124` labels the section “Physical
  description of the blowup”; defines the force as the residual for an
  incompressible flow and pressure; and says the challenge is to choose a
  blowing-up flow for which the residual remains smooth.
* The same passage says individual momentum-residual terms may diverge, while
  their sum and all derivatives must extend smoothly through the singular
  time.
* It then says the background residual is made smooth by adding oscillatory
  pulses and further corrections. This is the manuscript's stated mechanism,
  not evidence that the flow is physically impossible by definition.
* `docs/navier-stokes openai.txt:31-47` states the theorem with a smooth,
  compactly supported force and concludes the no-global-solution consequence.
* `docs/navier-stokes openai.txt:252-304` repeats that the background force
  would be singular, then describes internal momentum transport, pulse flux,
  further corrections, and smooth cutoff forcing.
* `docs/navier-stokes openai.txt:306-321` describes the proof obligation as
  smooth extension of the residual while velocity becomes unbounded, followed
  by summation, localisation, and force extension.

## Semantic consequence

The review must distinguish three claims:

1. **Physical framing:** the manuscript presents the force as an external
   force and describes the flow in fluid-mechanical terms.
2. **Displayed CMI admissibility:** the construction must supply the force,
   initial data, smoothness, decay, domain, and global nonexistence package
   specified by Fefferman.
3. **Manuscript-mechanism fidelity:** the selected Lean endpoint must be shown
   to realise the manuscript's profile matching, moment correction, stress
   cancellation, localisation, residual extension, and global consequence.

The source supports the first two as the authors' stated target. The current
audit establishes a substantive residual-jet route in the Lean endpoint, but
has not established the third route's complete selected-field transport. That
is `CTR-005`; it is not a source-grounded claim that OpenAI declared the flow
physically impossible, nor is it by itself a proof that Fefferman C or D is
false.

## Required wording control

Do not write:

> OpenAI's paper says the construction would never occur physically.

Write instead:

> The manuscript presents a physically framed, residual-designed forced
> construction. The audit must test whether its selected Lean fields realise
> the manuscript's stated cancellation and extension mechanism and satisfy
> Fefferman's connected admissibility package. The present endpoint record
> leaves the complete moment-to-selected-field transport unestablished.

## Evidence boundary

This record does not decide the unresolved selected value-level question. The
remaining test is the actual implication from the selected Cartesian field,
pressure, residual, force, support, and all-order limits to the manuscript's
five moment identities and Fefferman's global conditions.
