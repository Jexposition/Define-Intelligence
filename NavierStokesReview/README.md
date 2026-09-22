# Navier–Stokes review lane

This folder is an independent review workspace. The downloaded OpenAI extraction at `..\NavierStokesAndEuler-main-open Ais solution` is read-only and is not edited.

## Layout

- `src/upstream-current/`: shallow clone of `openai/NavierStokesAndEuler`, pinned locally to commit `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`.
- `src/audit/`: review scripts and non-upstream harnesses.
- `evidence/`: command logs, hashes, and generated audit output.
- `../docs/OpenAI_NavierStokes_CMI_First_Review_Plan.md`: main plan.
- `../docs/OpenAI_NavierStokes_Axiom_Ledger.md`: transitive axiom ledger.
- `../docs/OpenAI_NavierStokes_Audit_Tracker.md`: living tracker.
- `../docs/OpenAI_NavierStokes_Research_Paper.md`: research-paper record.

Do not commit generated `.lake` output or modify upstream source while reviewing it.
# Navier–Stokes peer-review workspace

This workspace reviews the public OpenAI Navier–Stokes and Euler formalisation without modifying the downloaded snapshot or the public source repository.

## Review inputs

- `src/upstream-current`: current public clone pinned to commit `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`.
- `D:\Research Lab\Jexposition\Define Intelligence\NavierStokesAndEuler-main-open Ais solution`: preserved downloaded comparison snapshot.
- `D:\Research Lab\Jexposition\Define Intelligence\docs`: consolidated CMI plan, axiom ledger, tracker, and research paper.

## Review outputs

- `results/UPSTREAM_SOURCE_CENSUS.md` and `.json`: project-only source inventory and lexical census.
- `results/UPSTREAM_PROOF_PATH_MAP.md`: exported declaration provenance map.
- `results/BUILD_CURRENT_4_34_RC2.txt`: current-toolchain build record.
- `results/AXIOM_PROBE_4_34_RC2.txt`: independent kernel dependency record when the build is complete.

The review uses the official Clay formulation as the CMI reference. It does not treat forcing as disqualifying because the official C and D alternatives explicitly include smooth forcing. It will classify the result only after the exact theorem propositions, source imports, compiler output, and `#print axioms` output have been checked.

The consolidated report is `D:\Research Lab\Jexposition\Define Intelligence\docs\OpenAI_NavierStokes_Peer_Review_v1.md`.
