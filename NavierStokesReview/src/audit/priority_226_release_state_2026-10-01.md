# Priority 226: curated release-state snapshot

Date: 2026-10-01
Status: verified release-control snapshot

## Branches

- Private source-of-truth branch:
  `review/cmi-first-navier-stokes-reconciled-2026-09-30`
- Private curated tip:
  `0fbd409e5cdef8b6fd2c34384ab1ae6362f760f7`
- Public review branch:
  `review/cmi-first-navier-stokes-disposition-public-2026-09-30`
- Public local and remote tip:
  `6199aabad0f8cf7af6ad38383099f2c7303b4885`

The public remote ref was verified after push at the snapshot gate. Only the curated audit,
evidence, control, and tree files from the Priority 224–225 pass were
published. The protected `NavierStokes/R3/TestPressure.lean` file and the raw
environment-closure JSON were not staged or published.

This record is a dated release snapshot. Later control commits change the
branch tip; current refs must always be read from Git at the release gate.

## Scientific status

The release does not change the controlled finding:
`CTR-005: NOT ESTABLISHED` for complete manuscript-to-selected-endpoint
fidelity. The selected route is substantive; the final mixed `barMoment`
support/integrability gate remains open. No selected defect, force
nonsmoothness, literal CMI failure, impossibility theorem, compiler escape, or
`False` is established.
