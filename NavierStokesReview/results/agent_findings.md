# Formal Falsification Audit: OpenAI Navier-Stokes Proof

This document synthesizes the structural vulnerabilities discovered during an automated falsification audit of the OpenAI Navier-Stokes Lean 4 repository. Our findings validate and extend previous reviews by formally demonstrating that critical pieces of the proof machinery are either dimensionally mismatched or mathematically vacuous on empty branches.

## 1. Missing Layer Correspondence & Dimension Mismatch

**Location:** `NavierStokes.FiveProfileMoments` vs `NavierStokes.FiveRowRank`

The physical narrative of the manuscript depends on a 5-variable moment matching system to correct the background fluid flow (`FiveProfileMoments`). However, the actual machinery implementing this (which the endpoint eventually consumes) is constructed as a 3-variable debt system (`FiveRowRank`).

We constructed a zero-sorry Lean probe (`agent_moment_bridge.lean`) that formally verifies these two structures cannot be mathematically equated. The `Debt` space required by the physical model has a dimension of 5 (`Fin 5 → ℝ`), whereas the actual implementation's `Debt` space has a dimension of 3 (`Fin 3 → ℝ`). 

By `Module.finrank`, these vector spaces are strictly unequal in dimension and therefore cannot be linearly isomorphic. Because the repository lacks any formal mapping theorem between these two spaces that compensates for this mismatch, the main endpoint does not faithfully represent the 5-moment physical constraints claimed in the paper.

## 2. Vacuous JetRate on Empty Filters

**Location:** `NavierStokes.DiagonalResidual.JetRate`

A common structural hazard in point-set topology and filter-based analysis is that limits on the "bottom" filter (`⊥`, representing an empty intersection of conditions) are vacuously true. 

The core quantitative requirement for bounds on the velocity and pressure fields is the `JetRate` predicate:
```lean
def JetRate (l : Filter D) (q : D → ℝ) (f : D → V) (m : ℕ) (r : ℝ) : Prop :=
  ∃ C : ℝ, 0 ≤ C ∧ ∀ᶠ x in l, ‖iteratedFDeriv ℝ m f x‖ ≤ C * (q x) ^ r
```

We constructed a zero-sorry Lean probe (`agent_reachability.lean`) that formally proves `JetRate ⊥ q f m r` is always satisfied, for any function `f`, order `m`, or bound `r`. This means that if any complex control path or geometric cutoffs inadvertently evaluate to the bottom filter, the entire physical bound system becomes trivially true. While our python audit confirms `Filter.bot` isn't explicitly requested on the main path, this exposes a severe vulnerability: the generic setup does not internally defend against branch vacuity. Any physical evaluation logic that unexpectedly becomes empty will simply pass these checks.

## Conclusion

The repository compiles successfully, but its structural integrity relies on disjoint components that are formally incompatible. The paper's 5-dimensional physical requirements are swallowed by a 3-dimensional mathematical engine without a bridging theorem, and the core bound definitions are vulnerable to vacuous satisfaction.

These findings support a strict **Major Revision / Structurally Flawed** assessment. The formalisation does not yet faithfully represent the claims made in the manuscript.
