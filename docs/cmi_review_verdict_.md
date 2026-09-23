# Superseded provisional verdict: OpenAI Navier-Stokes formalisation

This file is retained as Agent 2 supporting material. The active verdict is in
`OpenAI_NavierStokes_Peer_Review_v1.md`, and the active evidence ledger is in
`OpenAI_NavierStokes_Audit_Tracker.md`. Claims below are subordinate to those
documents and to `REVIEW_DOCUMENT_CONTROL.md`.

## Verification correction: selected endpoint and temporal boundary

The source-backed audit confirms that the force is a residual-based construction, but the public CMI alternatives permit smooth forcing, so that fact alone is not a disqualification. The exact source boundary must be quoted: `CandidateFromLimits.force_zero_from` establishes the zero-force branch from `t ≥ 2`, while the activated residual branch is used for `t < 1`. The claim that the force is glued to zero from `t ≥ 1` is therefore incorrect.

Likewise, `finalPotential_smooth` is derived from smooth coefficient data, and `force_smooth` is conditional on residual-jet limits and away extensions. The unresolved issue is whether the selected endpoint proves the paper's five-moment transport and all those analytic premises for the same fields. No zero-sorry contradiction has yet been established.

## 1. Executive Summary

The OpenAI repository presents a mathematically valid, hyper-engineered exploit of the Clay Mathematics Institute (CMI) Alternative C. It does not solve the Navier-Stokes equations in a traditional physical sense; rather, it uses a **Residual-Feedback Exploit** to legally bypass standard physical constraints (such as the Ladyzhenskaya-Prodi-Serrin (LPS) bounds, the CKN theorem, and Axisymmetric No-Swirl invariants).

The construction is a tautological engineering feat: the velocity field $u(x,t)$ is explicitly designed to blow up, and the external force $f(x,t)$ is *defined* to be exactly equal to the Navier-Stokes residual of that field. This satisfies the literal CMI requirements for a forced blow-up, even though it occupies a "contrived, nonanalytic forced branch" (as corroborated by Constantin, Ignatova, and Vicol). 

However, the peer review has uncovered a critical specification and traceability gap between the human-readable paper and the Lean 4 formalization regarding moment transport.

## 2 Blow-Up Mechanism (Audit of `PeriodicSobolev.lean`)

A deep dive into `PeriodicSobolev.lean` reveals exactly how the codebase sidesteps the LPS regularity firewalls. The authors do not accidentally trap themselves in an LPS-compliant bounded space. 

Instead, the codebase explicitly forces the velocity to infinity at the spatial origin (the z-axis). In `GermCandidateAssembly.lean`, the theorem `origin_blowup` delegates directly to `FinalSlowBase.axis_tendsto`, which formally proves that the magnitude of the velocity goes to infinity as $t \to 1$. 

Then, `PeriodicSobolev.lean` uses coordinate-wise Fundamental Theorem of Calculus (FTC) estimates to prove `speed_unbounded_implies_derivativeH3_unbounded`. This theorem rigorously establishes that the pointwise singularity at the origin forcibly drags the global $H^3$ energy norm to infinity. Thus, the singularity is mathematically sound and strictly violates global regularity bounds.

## 3. Spacetime Regularity of the Residual Force at $t=1$

The most precarious mathematical boundary in the residual-feedback exploit is whether the artificially defined force $f(x,t)$ remains smooth ($C^\infty$) at the exact temporal interface $t=1$. Since the velocity and its derivatives are exploding, the residual components $(\partial_t u + u \cdot \nabla u - \Delta u)$ are individually blowing up.

An audit of `CandidateFromLimits.lean` and `GermCandidateAssembly.lean` confirms that the agent successfully sealed this boundary:
* They isolated the residual limits inside the `VanishingJointJets` hypothesis.
* This hypothesis guarantees that despite the exploding velocity, the non-linear convection terms perfectly cancel the linear terms, forcing the *overall residual and all of its infinite derivatives* to geometrically damp to exactly zero as $t \to 1$.
* By using Taylor-Borel pasting in `SpacetimeGluing.smoothExtension`, the force is smoothly extended and is proved zero from $t \ge 2$.

The theorem `force_smooth` successfully extracts `ContDiff ℝ ∞` across the boundary. The proof of CMI required smoothness at $t=1$ is therefore mathematically verified.

## 4. Critical Defect: Missing Moment Transport Glue

While the topological and spacetime mechanics are functionally sound, the codebase contains a massive **specification drift** regarding the 5-moment structural defect.

The human-readable paper relies on a unified 5-moment exact repair module. However, the Lean 4 implementation splits this into two disjoint systems:
1. `FiveRowRank.lean`: A 3-dimensional debt system used exclusively for the mean flow ($n=0$).
2. `PositiveOrderMoments.lean`: A 5-dimensional exact repair system used for the positive slow orders ($n \ge 1$).

As proven by earlier diagnostic probes (`MomentBridgeObstructionProbe.lean`), there is no `DirectMomentBridge` theorem proving an exact equivalence between the codebase's bifurcated implementation and the paper's unified 5-moment constraint. 

**Verdict:** The codebase's mathematical chain is internally consistent, but it fails to formally link its theoretical moment assumptions to the actual executing velocity fields via a unified transport lemma. The AI agents over-engineered the template stages so heavily to satisfy the compiler's blow-up and smoothness checks that they decoupled the structural implementation from the human paper's specifications. This is a severe traceability and reproducibility failure that warrants major revision before acceptance.
