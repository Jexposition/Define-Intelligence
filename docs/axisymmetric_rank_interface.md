# The Axisymmetric-Rank Interface Audit Ledger
**Target Modules:** `TailGaugePotential.lean`, `FiveRowRank.lean`, `LocalHeatExterior.lean`

## 1. The Angular Debt Extrication
**Target Interface:** `gaugedSwirl` mapping to $J_\theta$ (`d 1` / `Debt`).
**Analysis:** 
I executed a strict symbol dependency and import trace between the axisymmetric core and the production rank system.
* **The Trace:** The `gaugedSwirl` term is isolated entirely within `TailGaugePotential.lean` and `LocalHeatExterior.lean`.
* **The Interface Missing Link:** `FiveRowRank.lean` and `MeanRankUpdate.lean` **never import or reference** `gaugedSwirl` or `TailGaugePotential`.
* **Verdict:** No selected-path theorem was located that identifies the gauge
  subtraction with the paper's $J_\theta$ quantity or transports it into the
  production rank data. This is a correspondence question, not proof that the
  algebraic rank system is disconnected from the full construction.

## 2. The Axial Field Isolation
**Target Interface:** Convective terms `(u \cdot \nabla)u` evaluated on `heatPotential`.
**Analysis:** 
`heatPotential` (Line 217 of `TailGaugePotential.lean`) strictly activates only `coordinateVector 2` (the axial $z$-component, so $u_r = 0, u_\theta = 0$).
* **The Convective Transport:** In cylindrical coordinates, the non-linear convective interaction terms for the radial and angular momentum equations depend heavily on $u_\theta^2/r$ (centrifugal force) and $u_r u_\theta / r$ (Coriolis force). 
* **Scope correction:** The gauge anchor fixes a radial reference value; it does not prove that the selected field is globally purely axial or that $u_r$ and $u_\theta$ vanish everywhere. Any claim of global component collapse requires a separate theorem about the selected field.
* **Verdict:** The displayed `heatPotential` component is a specialised
  auxiliary field. It does not establish that the assembled velocity is purely
  axial or that the selected Navier–Stokes residual loses its cross-component
  terms. The endpoint field is produced from the full potential and spatial curl.

## 3. The Fixed Constraint Verification
**Target Interface:** `FiveRows` (Lines 241-244 in `FiveRowRank.lean`) vs 2D `streamFactor`.
**Analysis:** 
I cross-referenced the 5-row rank system with the base profile logic.
* **The Constraint Definitions:** 
  `FiveRows` explicitly hardcodes the first two rows (representing mass/energy moments $M$ and $I$) to absolute zero:
  ` (∫ R, R ^ (2 : ℕ) * dv R) = 0 `
  ` (∫ R, R * ga R) = 0 `
* **The Disconnect:** The debt parameter `d` only starts feeding into the equations at row 3 (`d 0`), row 4 (`d 1`), and row 5 (`d 2`) (corresponding to $P$, $J_\theta$, $J_z$).
* **Verdict:** `FiveRows` contains two zero constraints and a three-coordinate
  debt interface. The review still requires the selected-path theorem showing
  how these constraints correspond to the paper's named moments; the row shape
  alone does not prove that the physical energy cascade is absent.

***
### Interface Falsification Summary
The surviving result is narrower. The inspected files do not exhibit the
selected-path theorem that identifies the paper's boundary variables with the
`FiveRowRank` debt and carries that identification through the residual bounds.
The source does establish a three-component potential and a curl-generated,
divergence-free endpoint, so this note does not prove a disconnected or
tautological fluid. The pressure comparison probe adds a separate limitation:
comparison identities do not, by themselves, establish an absolute global
pressure-Poisson representative for the selected pressure.
