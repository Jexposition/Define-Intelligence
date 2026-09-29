"""Conservative semantic coverage register for the Lean source tree.

The hardened source map records structure. This tool records review status.
Import reachability is intentionally kept separate from semantic transport.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


# These are bounded source reviews, not inferred claims.
EVIDENCE: dict[str, dict[str, Any]] = {
    "NavierStokesReview/src/audit/priority_174_force_smoothness_rebuttal_adjudication_2026-09-29.md": {
        "clusters": ["cmi", "fefferman", "force-smoothness", "ctr-005"],
        "finding": "Adjudicates the force-smoothness rebuttal: velocity blow-up does not imply divergence of every residual summand; the manuscript describes multiple correction layers; the selected route has an actual residual-jet smooth-force construction; complete five-observable endpoint transport remains CTR-005.",
        "anchors": "docs/navier-stokes openai.txt:109-124,695-733; NavierStokes/CandidateFromLimits.lean:28-112",
    },
    "NavierStokesReview/evidence/source_tranche_priority_174_force_smoothness_rebuttal_adjudication_2026-09-29.json": {
        "clusters": ["cmi", "fefferman", "force-smoothness", "evidence"],
        "finding": "Machine-readable Priority 174 force-smoothness rebuttal adjudication with explicit rejected, not-established, and not-proved classifications.",
        "anchors": "JSON findings and classification fields",
    },
    "NavierStokesReview/src/audit/priority_175_lexical_bridge_candidate_classification_2026-09-29.md": {
        "clusters": ["endpoint", "bridge", "moments", "transport"],
        "finding": "Declaration-level classification of all seven lexical bridge candidates: rate, germ, axis, and schedule declarations, with no selected Cartesian five-observable transport theorem found.",
        "anchors": "NavierStokesReview/evidence/selected_endpoint_source_census_2026-09-27.md and cited Lean declarations",
    },
    "NavierStokesReview/evidence/source_tranche_priority_175_lexical_bridge_candidate_classification_2026-09-29.json": {
        "clusters": ["endpoint", "bridge", "moments", "transport", "evidence"],
        "finding": "Machine-readable Priority 175 classification of the seven lexical endpoint candidates, preserving the distinction between selected-route evidence and missing paper-specific transport.",
        "anchors": "JSON findings and classification fields",
    },
    "NavierStokesReview/src/audit/priority_176_selected_field_composition_domain_trace_2026-09-29.md": {
        "clusters": ["endpoint", "composition", "periodisation", "activation", "moments"],
        "finding": "Source-bound trace of selected ASum/BSum/PSum through tsum, Cartesian curl, localisation, periodisation, direct-field addition, and time activation; barMoment remains a distinct pressure-stream observable domain without a final five-observable identity.",
        "anchors": "NavierStokes/SolenoidalDiagonal.lean, LocalScheduleWitness.lean, MixedPeriodicAssembly.lean, SpatialLocalization.lean, TimeLocalization.lean, DefectIncrementBounds.lean",
    },
    "NavierStokesReview/evidence/source_tranche_priority_176_selected_field_composition_domain_trace_2026-09-29.json": {
        "clusters": ["endpoint", "composition", "periodisation", "activation", "moments", "evidence"],
        "finding": "Machine-readable Priority 176 selected-field composition and observable-domain trace, preserving positive endpoint construction and the unestablished paper-specific bridge.",
        "anchors": "JSON findings and classification fields",
    },
    "NavierStokesReview/src/audit/priority_177_fefferman_word_connection_adjudication_2026-09-29.md": {
        "clusters": ["cmi", "fefferman", "external-semantics", "methodology"],
        "finding": "Connected Fefferman word-level adjudication: given force/data, whole-space and periodic branches, accepted-solution conditions, and Alternatives C/D must be audited as connected packages.",
        "anchors": "docs/navierstokes.txt:25-81; NavierStokes/ComparatorR3Theorem.lean:21-44; NavierStokes/R3/ProblemStatement.lean:90-136",
    },
    "NavierStokesReview/evidence/source_tranche_priority_177_fefferman_word_connection_adjudication_2026-09-29.json": {
        "clusters": ["cmi", "fefferman", "external-semantics", "methodology", "evidence"],
        "finding": "Machine-readable Priority 177 connected Fefferman semantic-network adjudication with stronger literal failure claims explicitly left unproved.",
        "anchors": "JSON findings and stronger_claims_not_proved",
    },
    "NavierStokesReview/src/audit/priority_173_fefferman_c_connected_adjudication_2026-09-29.md": {
        "clusters": ["cmi", "fefferman", "semantic-network", "force-provenance"],
        "finding": "Connected adjudication of Fefferman Alternative (C): periodicity is a branch choice, physically reasonable is tied to the full data and accepted-solution package, the selected Lean route contains explicit formal C components, and residual force provenance is semantic rather than an unstated independence predicate. Complete manuscript five-moment transport remains CTR-005.",
        "anchors": "docs/navierstokes.txt:25-81; docs/navier-stokes openai.txt:109-124,252-321,984-1035",
    },
    "NavierStokesReview/evidence/source_tranche_priority_173_fefferman_c_connected_adjudication_2026-09-29.json": {
        "clusters": ["cmi", "fefferman", "semantic-network", "evidence"],
        "finding": "Machine-readable Priority 173 tranche distinguishing connected formal C compliance, physical force provenance, and manuscript five-moment endpoint fidelity.",
        "anchors": "JSON findings F173-1 through F173-5",
    },
    "NavierStokesReview/src/audit/priority_172_fefferman_semantic_network_2026-09-29.md": {
        "clusters": ["cmi", "fefferman", "semantic-network", "methodology"],
        "finding": "Connected semantic audit of Fefferman's exact wording: physically reasonable, Hence, only if, Alternatively, Thus, and retaining the heart of the problem. Whole-space C and periodic D are kept as separate connected requirement packages. The selected Lean route is recorded positively, while the manuscript-specific five-moment endpoint transport remains CTR-005 and no literal failure is claimed.",
        "anchors": "docs/navierstokes.txt:25-81; audit report sections 1-6",
    },
    "NavierStokesReview/evidence/source_tranche_priority_172_fefferman_semantic_network_2026-09-29.json": {
        "clusters": ["cmi", "fefferman", "semantic-network", "evidence"],
        "finding": "Machine-readable Priority 172 source tranche preserving exact-wording, branch-separation, selected-path, and CTR-005 status boundaries.",
        "anchors": "JSON claims F1-F6, LEAN-C, CTR-005, REFUTATION",
    },
    "Euler/StaticEulerSolution.lean": {
        "clusters": ["euler", "force", "pressure", "regularity"],
        "finding": "Direct review finds a genuine rescaled local Euler field with interior zero momentum residual, divergence-free identity, continuity, and smoothness. It is not a Navier-Stokes selected endpoint and carries no selected five-observable transport result.",
        "anchors": "24-35; 60-68; 78-90; 116-133; 158-164",
    },
    "Euler/AllOrderDriftPressure.lean": {
        "clusters": ["euler", "pressure", "moments", "regularity"],
        "finding": "Direct review finds common lifted pressure, point representative, graph pressure, radial scalar potential, smoothness, parity, and gradient recovery. It does not establish a global Navier-Stokes Poisson endpoint or selected Cartesian moment transport.",
        "anchors": "20-48; 56-126; 131-190",
    },
    "Euler/CorrectionAssemblyPressureParity.lean": {
        "clusters": ["euler", "pressure", "symmetry"],
        "finding": "Direct review finds graph reflection, pressure oddness, normalized-potential evenness, and uniqueness under a fixed gradient field. These are Euler graph-local results, not the selected Navier-Stokes bridge.",
        "anchors": "13-29; 43-81",
    },
    "Euler/CorrectionAssemblyReconstruction.lean": {
        "clusters": ["euler", "pressure", "cartesian-assembly", "regularity"],
        "finding": "Direct review finds finite-family pressure representative and graph-potential reconstruction from lifted-space hypotheses, including smoothness and gradient recovery. No selected Navier-Stokes endpoint equality is stated.",
        "anchors": "21-49; 52-106",
    },
    "Euler/ExactLiftedGraphPressure.lean": {
        "clusters": ["euler", "pressure", "cartesian-assembly", "regularity"],
        "finding": "Direct review finds exact lifted-packet graph pressure/potential and a graph divergence-free identity. The result remains an Euler graph-local construction and does not establish the selected Navier-Stokes field or five-observable transport.",
        "anchors": "20-34; 36-57; 60-80",
    },
    "NavierStokesReview/src/audit/priority_138_euler_pressure_static_source_review_2026-09-28.md": {
        "clusters": ["euler", "pressure", "methodology", "repository-root"],
        "finding": "Human-readable Priority 138 direct source review of five Euler pressure/static/graph modules, with imports, direct dependents, exact anchors, positive findings, and explicit endpoint-scope boundaries.",
        "anchors": "1-76",
    },
    "NavierStokesReview/evidence/source_tranche_euler_pressure_static_2026-09-28.json": {
        "clusters": ["euler", "pressure", "methodology", "repository-root"],
        "finding": "Machine-readable Priority 138 evidence for five directly reviewed Euler modules and their source-map dependents.",
        "anchors": "generated JSON; 5 source records",
    },
    "Euler/ContinuousBoundedTensor.lean": {
        "clusters": ["euler", "functional-analysis", "regularity", "bounded-fields"],
        "finding": "Direct review finds finite-dimensional tensor reassembly from continuous bounded paths, pointwise evaluation, norm control, and iterated-derivative commutation. It is generic Euler functional-analysis infrastructure and does not state selected Navier-Stokes endpoint transport.",
        "anchors": "26-45; 50-74; 97-150",
    },
    "Euler/ContinuousGramAcceleration.lean": {
        "clusters": ["euler", "functional-analysis", "regularity", "energy"],
        "finding": "Direct review finds a continuous Gram-inverse acceleration path, its projected equation, norm bound, and conditional almost-everywhere identification. The PDE equation is a hypothesis of the AE theorem, not a derived selected Navier-Stokes endpoint identity.",
        "anchors": "27-39; 41-78; 81-95",
    },
    "Euler/ContinuousGramPath.lean": {
        "clusters": ["euler", "functional-analysis", "regularity", "operator-path"],
        "finding": "Direct review finds continuous Gram-path inversion, two-sided inverse identities, uniform norm control, parameter smoothness, and derivative bounds under coercivity. No selected Cartesian five-observable transport is stated.",
        "anchors": "31-50; 53-74; 77-114",
    },
    "Euler/ContinuousGramGevrey.lean": {
        "clusters": ["euler", "functional-analysis", "regularity", "gevrey"],
        "finding": "Direct review finds conditional factorial/Gevrey propagation through the continuous Gram inverse and solution operator using explicit derivative majorants. It is not a CMI endpoint or pressure/force provenance theorem.",
        "anchors": "23-43; 47-72; 75-163",
    },
    "Euler/ContinuousGramSobolev.lean": {
        "clusters": ["euler", "functional-analysis", "regularity", "sobolev"],
        "finding": "Direct review finds conditional fixed Sobolev-word-block/Gevrey propagation through the continuous Gram solve. It does not state selected Navier-Stokes field transport or a contradiction.",
        "anchors": "21-37",
    },
    "NavierStokesReview/src/audit/priority_141_euler_continuous_gram_source_review_2026-09-29.md": {
        "clusters": ["euler", "functional-analysis", "methodology", "repository-root"],
        "finding": "Human-readable Priority 141 direct source review of five Euler continuous Gram/tensor modules, with exact declarations, imports, dependent-module trace, and endpoint-scope limits.",
        "anchors": "1-75",
    },
    "NavierStokesReview/evidence/source_tranche_euler_continuous_gram_2026-09-29.json": {
        "clusters": ["euler", "functional-analysis", "methodology", "repository-root"],
        "finding": "Machine-readable Priority 141 evidence for five directly reviewed Euler continuous Gram/tensor modules and their import consumers.",
        "anchors": "generated JSON; 5 source records",
    },
    "Euler/ContinuousInverseDerivative.lean": {
        "clusters": ["euler", "calculus", "functional-analysis"],
        "finding": "Direct review finds a generic derivative-of-inverse theorem under explicit local composition and left-inverse hypotheses. It is not a PDE existence or selected Navier-Stokes endpoint theorem.",
        "anchors": "1; 17-35",
    },
    "Euler/ContinuousPathCalculus.lean": {
        "clusters": ["euler", "functional-analysis", "regularity", "gevrey"],
        "finding": "Direct review finds continuous operator-valued path multiplication, norm bounds, differentiability, and application estimates under explicit hypotheses; no selected-field transport is stated.",
        "anchors": "1-2; 36-92",
    },
    "Euler/ContinuousPathComposition.lean": {
        "clusters": ["euler", "functional-analysis", "regularity", "operator-path"],
        "finding": "Direct review finds continuous operator composition and adjoint-path regularity and norm propagation. It does not state a CMI endpoint or five-observable equality.",
        "anchors": "1-2; 47-85; 121-144",
    },
    "Euler/CylinderActionWords.lean": {
        "clusters": ["euler", "cylinder", "functional-analysis", "regularity"],
        "finding": "Direct review finds isometric path/time translations and conditional cylinder L2 regularity and block bounds. It has no selected Navier-Stokes endpoint transport or contradiction.",
        "anchors": "1-4; 22-35; 39-97",
    },
    "Euler/CylinderAngleEvolution.lean": {
        "clusters": ["euler", "cylinder", "regularity", "calculus"],
        "finding": "Direct review finds angular primitive and time-derivative identities under explicit mean-zero and regularity hypotheses; no global pressure, force-provenance, or five-observable result is stated.",
        "anchors": "1-3; 20-43; 66-73",
    },
    "NavierStokesReview/src/audit/priority_142_euler_continuous_path_source_review_2026-09-29.md": {
        "clusters": ["euler", "functional-analysis", "methodology", "repository-root"],
        "finding": "Human-readable Priority 142 direct source review of five Euler continuous-path and cylinder modules, with declarations, imports, dependents, and endpoint-scope limits.",
        "anchors": "1-65",
    },
    "NavierStokesReview/evidence/source_tranche_euler_continuous_path_2026-09-29.json": {
        "clusters": ["euler", "functional-analysis", "methodology", "repository-root"],
        "finding": "Machine-readable Priority 142 evidence for five directly reviewed Euler continuous-path and cylinder modules and their import consumers.",
        "anchors": "generated JSON; 5 source records",
    },
    "Euler/CylinderAnglePrimitive.lean": {
        "clusters": ["euler", "cylinder", "functional-analysis", "translation", "regularity"],
        "finding": "Direct review finds a bounded angular primitive on cylinder L2, its continuous operator structure, norm estimate, translation commutation, and Sobolev lift. It does not state a selected Navier-Stokes endpoint theorem.",
        "anchors": "15-29; 41-82; 98-101",
    },
    "Euler/CylinderAngleRepresentative.lean": {
        "clusters": ["euler", "cylinder", "regularity", "representatives"],
        "finding": "Direct review finds Sobolev primitive integral and classical representative identities under explicit representative and mean hypotheses; no global pressure or five-observable result is stated.",
        "anchors": "1-3; 16-21; 31-73",
    },
    "Euler/CylinderAngleWordBounds.lean": {
        "clusters": ["euler", "cylinder", "bounds", "gevrey", "regularity"],
        "finding": "Direct review finds angular primitive translation and mixed-word/Gevrey block-bound propagation through a bounded continuous operator. It is not a selected Navier-Stokes transport or contradiction theorem.",
        "anchors": "1-3; 17-34; 49-74",
    },
    "Euler/CylinderBoundedCover.lean": {
        "clusters": ["euler", "cylinder", "bounded-fields", "regularity"],
        "finding": "Direct review finds a Sobolev cylinder field lifted to bounded continuous functions on the real cover with norm, orbit, and translation identities under explicit hypotheses.",
        "anchors": "1-2; 24-58; 69-127",
    },
    "Euler/CylinderClassicalWordBounds.lean": {
        "clusters": ["euler", "cylinder", "bounds", "regularity", "l2"],
        "finding": "Direct review finds actual classical mixed derivatives identified with finite L2 word sums under SmoothOrbit hypotheses. It does not state selected Navier-Stokes field transport or a nonzero defect.",
        "anchors": "1-2; 23-90; 96-140",
    },
    "NavierStokesReview/src/audit/priority_143_euler_cylinder_angle_source_review_2026-09-29.md": {
        "clusters": ["euler", "cylinder", "functional-analysis", "methodology", "repository-root"],
        "finding": "Human-readable Priority 143 direct source review of five Euler cylinder-angle and classical-field modules, with declarations, imports, dependents, and endpoint-scope limits.",
        "anchors": "1-55",
    },
    "NavierStokesReview/evidence/source_tranche_euler_cylinder_angle_2026-09-29.json": {
        "clusters": ["euler", "cylinder", "functional-analysis", "methodology", "repository-root"],
        "finding": "Machine-readable Priority 143 evidence for five directly reviewed Euler cylinder-angle and classical-field modules and their import consumers.",
        "anchors": "generated JSON; 5 source records",
    },
    "Euler/CylinderCompactTranslation.lean": {
        "clusters": ["euler", "cylinder", "functional-analysis", "regularity", "support"],
        "finding": "Direct review finds compact smooth cylinder fields with genuine L2 translation orbits, support control, dominated Frechet differentiation, and smoothness; no selected NS endpoint is stated.",
        "anchors": "28-44; 47-103; 124-166",
    },
    "Euler/CylinderCompactBounds.lean": {
        "clusters": ["euler", "cylinder", "bounds", "gevrey", "support"],
        "finding": "Direct review finds compact support and local derivative bounds converted into L2 translation/Gevrey and block estimates through a fixed support mass.",
        "anchors": "24-39; 52-89; 97-114",
    },
    "Euler/CylinderConstantMap.lean": {
        "clusters": ["euler", "cylinder", "functional-analysis", "translation", "regularity"],
        "finding": "Direct review finds fixed bounded maps preserving cylinder L2 classes, translations, paths, and regularity with norm control; no selected five-observable equality is stated.",
        "anchors": "18-41; 52-75",
    },
    "Euler/CylinderConstantMapBounds.lean": {
        "clusters": ["euler", "cylinder", "bounds", "functional-analysis"],
        "finding": "Direct review finds external-word block-bound propagation through a fixed bounded map up to the operator norm. It is not a CMI endpoint theorem.",
        "anchors": "1; 18-32",
    },
    "Euler/CylinderCorrectorMeanZero.lean": {
        "clusters": ["euler", "cylinder", "moments", "translation", "regularity"],
        "finding": "Direct review finds conditional preservation of the angular average by primitive, potential-path, and slow-curl operations. This is a genuine upstream invariant but not the five-observable selected NS transport theorem.",
        "anchors": "19-31; 37-60; 66-80",
    },
    "NavierStokesReview/src/audit/priority_144_euler_compact_meanzero_source_review_2026-09-29.md": {
        "clusters": ["euler", "cylinder", "functional-analysis", "methodology", "repository-root"],
        "finding": "Human-readable Priority 144 direct source review of five Euler compact-translation, bounded-map, and mean-zero modules, with declarations, imports, dependents, and endpoint-scope limits.",
        "anchors": "1-57",
    },
    "NavierStokesReview/evidence/source_tranche_euler_compact_meanzero_2026-09-29.json": {
        "clusters": ["euler", "cylinder", "functional-analysis", "methodology", "repository-root"],
        "finding": "Machine-readable Priority 144 evidence for five directly reviewed Euler compact-translation, bounded-map, and mean-zero modules and their import consumers.",
        "anchors": "generated JSON; 5 source records",
    },
    "Euler/CylinderCoverDescent.lean": {
        "clusters": ["euler", "cylinder", "cover", "quotient", "measure"],
        "finding": "Direct review finds periodic-cover section and descent with continuity, measure preservation, and inverse properties; it is not a selected Navier-Stokes endpoint theorem.",
        "anchors": "1-4; 14-114",
    },
    "Euler/CylinderCoveringDerivative.lean": {
        "clusters": ["euler", "cylinder", "cover", "regularity"],
        "finding": "Direct review finds covered-field derivative and smoothness identities on the Euler cylinder cover; no selected-field observable is stated.",
        "anchors": "1; 17-38",
    },
    "Euler/CylinderCoverTensor.lean": {
        "clusters": ["euler", "cylinder", "cover", "derivatives", "bounds"],
        "finding": "Direct review finds coordinate-word derivatives converted to Euclidean iterated derivatives with norm bounds; no five-observable transport is stated.",
        "anchors": "1-4; 18-68",
    },
    "Euler/CylinderDirichletMean.lean": {
        "clusters": ["euler", "cylinder", "dirichlet", "mean-zero", "operator-intertwining"],
        "finding": "Direct review finds angular averaging commutes with Euler cylinder coefficient operators and preserves explicit angular zero mean for velocity, acceleration, and physical derivative paths. This is not the radial five-observable selected Navier-Stokes transport theorem.",
        "anchors": "1-12; 27-50; 65-99; 101-159",
    },
    "Euler/CylinderDirichletNaturality.lean": {
        "clusters": ["euler", "cylinder", "dirichlet", "naturality", "translation"],
        "finding": "Direct review finds coefficient-space translation and adjoint naturality for Euler cylinder paths; no selected Navier-Stokes endpoint is stated.",
        "anchors": "1-4; 38-91",
    },
    "Euler/CylinderDirichletParity.lean": {
        "clusters": ["euler", "cylinder", "dirichlet", "symmetry", "parity"],
        "finding": "Direct review finds reflection, sign, and oddness identities for Euler cylinder coefficient paths; no five-observable equality or contradiction is stated.",
        "anchors": "1-3; 22-115",
    },
    "Euler/CylinderDirichletRegularity.lean": {
        "clusters": ["euler", "cylinder", "dirichlet", "regularity", "translation"],
        "finding": "Direct review finds smoothness of translated coefficient and physical-path orbits in the Euler cylinder model; no selected Navier-Stokes transport is stated.",
        "anchors": "1-2; 41-166",
    },
    "Euler/CylinderDirichletSobolev.lean": {
        "clusters": ["euler", "cylinder", "dirichlet", "sobolev", "bounds"],
        "finding": "Direct review finds Sobolev, word, and block bounds for Euler cylinder coefficient and velocity paths; no five-observable equality is stated.",
        "anchors": "1-4; 44-111",
    },
    "Euler/CylinderDirichletTranslation.lean": {
        "clusters": ["euler", "cylinder", "dirichlet", "translation", "covariance"],
        "finding": "Direct review finds translation covariance for Euler cylinder coefficient and physical paths; it is not a global Cartesian moment theorem.",
        "anchors": "1-2; 17-130",
    },
    "Euler/CylinderEndpointBounds.lean": {
        "clusters": ["euler", "cylinder", "endpoint", "bounds"],
        "finding": "Direct review finds Euler cylinder endpoint budgets for coordinate, acceleration, velocity, and derivative; these are not the Navier-Stokes NativeBounds endpoint.",
        "anchors": "1; 11-60",
    },
    "Euler/CylinderEndpointEquation.lean": {
        "clusters": ["euler", "cylinder", "endpoint", "equation", "balance"],
        "finding": "Direct review finds an almost-everywhere projected endpoint equation and physical balance under explicit range, tangency, and flow hypotheses. It is an Euler cylinder theorem, not CandidateProperties, Witness, selected_witness, or theorem_1_1.",
        "anchors": "1-8; 24-87",
    },
    "Euler/CylinderEndpointLabels.lean": {
        "clusters": ["euler", "cylinder", "endpoint", "labels", "coordinates"],
        "finding": "Direct review finds labelled coefficient, frame, coordinate, Hessian, and velocity maps for the Euler cylinder endpoint; no selected Navier-Stokes bridge is stated.",
        "anchors": "1-2; 19-67",
    },
    "NavierStokesReview/src/audit/priority_145_euler_cylinder_dirichlet_endpoint_source_review_2026-09-29.md": {
        "clusters": ["euler", "cylinder", "endpoint", "methodology", "repository-root"],
        "finding": "Human-readable Priority 145 direct source review of twelve Euler cylinder cover, Dirichlet, and endpoint modules, with import boundaries and explicit limits on selected Navier-Stokes interpretation.",
        "anchors": "1-57",
    },
    "NavierStokesReview/evidence/source_tranche_euler_cylinder_dirichlet_endpoint_2026-09-29.json": {
        "clusters": ["euler", "cylinder", "endpoint", "methodology", "repository-root"],
        "finding": "Machine-readable Priority 145 evidence for twelve directly reviewed Euler cylinder cover, Dirichlet, and endpoint modules.",
        "anchors": "generated JSON; 12 source records",
    },
    "Euler/CylinderEndpointParity.lean": {
        "clusters": ["euler", "cylinder", "endpoint", "symmetry"],
        "finding": "Direct review proves odd reflection identities for the Euler cylinder endpoint forcing, coordinate, acceleration, velocity, and derivative under even coefficient hypotheses. It is not a Navier-Stokes selected-field or radial-moment theorem.",
        "anchors": "1-2; 24-55",
    },
    "Euler/CylinderEndpointPointwise.lean": {
        "clusters": ["euler", "cylinder", "endpoint", "pointwise", "equation"],
        "finding": "Direct review constructs pointwise endpoint paths, proves initial and terminal displacement data, a projected equation, label-coordinate identification, and pointwise velocity identification. The result is conditional Euler cylinder data and does not reference CandidateProperties, Witness, selected_witness, or theorem_1_1.",
        "anchors": "1-6; 90-173",
    },
    "Euler/CylinderEndpointRegularity.lean": {
        "clusters": ["euler", "cylinder", "endpoint", "regularity"],
        "finding": "Direct review propagates smooth translation orbits through the endpoint forcing, coordinate, acceleration, velocity, and derivative paths. These are Euler cylinder regularity statements, not selected Cartesian Navier-Stokes transport.",
        "anchors": "1-3; 50-101",
    },
    "Euler/CylinderEndpointSupport.lean": {
        "clusters": ["euler", "cylinder", "endpoint", "support", "mean"],
        "finding": "Direct review proves support inheritance and preservation of explicit zero angular mean for endpoint forcing, coordinate, acceleration, velocity, and derivative paths. Angular mean preservation is not the five radial observable tuple `(M,I,J,S,Cp)`.",
        "anchors": "1-8; 28-109",
    },
    "Euler/CylinderEndpointUnitBounds.lean": {
        "clusters": ["euler", "cylinder", "endpoint", "bounds", "regularity"],
        "finding": "Direct review proves conditional unit endpoint budgets for constant, forcing, coordinate, acceleration, velocity, and derivative paths using block majorants and orbit regularity. These bounds are not the Navier-Stokes NativeBounds endpoint and do not transport radial moments.",
        "anchors": "1-8; 30-147",
    },
    "Euler/CylinderFieldReflection.lean": {
        "clusters": ["euler", "cylinder", "reflection", "support"],
        "finding": "Direct review defines the Lp cylinder reflection, proves involution and representative identities, and lifts reflection to supported fields, paths, and coefficient operators. No selected Navier-Stokes endpoint or five-observable equality is stated.",
        "anchors": "1-4; 21-138",
    },
    "Euler/CylinderForwardParity.lean": {
        "clusters": ["euler", "cylinder", "parity", "evolution"],
        "finding": "Direct review proves reflection naturality and odd-solution preservation for a supported linear evolution under even coefficients. This is Euler forward evolution symmetry, not a CMI Navier-Stokes witness theorem.",
        "anchors": "1-4; 24-54",
    },
    "Euler/CylinderGradientEmbedding.lean": {
        "clusters": ["euler", "cylinder", "gradient", "embedding"],
        "finding": "Direct review proves scalar lifting, gradient evaluation, and embedding of the closed mean-solenoidal gradient space into the cylinder gradient space, conditionally on the embedding scale. It is functional-analysis infrastructure and contains no selected-field moment transport.",
        "anchors": "1-4; 18-82",
    },
    "Euler/CylinderGraphAffine.lean": {
        "clusters": ["euler", "cylinder", "graph", "derivative", "bounds"],
        "finding": "Direct review proves affine representative and derivative identities and an L2 graph-trace norm estimate for three-field affine combinations. It supports Euler graph restriction and does not identify the selected Navier-Stokes field or radial moments.",
        "anchors": "1-4; 14-57",
    },
    "Euler/CylinderGraphDerivative.lean": {
        "clusters": ["euler", "cylinder", "graph", "derivative"],
        "finding": "Direct review proves a genuine derivative transfer from cylinder and angular L2 derivatives to a fixed spatial phase graph, using the graph trace estimate. No Navier-Stokes endpoint or five-observable transport is stated.",
        "anchors": "1-4; 16-57",
    },
    "Euler/CylinderGraphGevrey.lean": {
        "clusters": ["euler", "cylinder", "graph", "gevrey", "bounds"],
        "finding": "Direct review proves factorial/Gevrey and L2 bounds after graph pullback, with an explicit graph-frequency factor and periodic-cover jet hypotheses. These are conditional Euler graph regularity bounds, not a radial moment identity or selected Navier-Stokes bridge.",
        "anchors": "1-8; 19-108",
    },
    "Euler/CylinderGraphPath.lean": {
        "clusters": ["euler", "cylinder", "graph", "continuity"],
        "finding": "Direct review constructs a continuous spatial L2 path from cylinder values and angular derivatives through graph realization. The theorem is Euler graph-local and has no CandidateProperties, selected_witness, pressure-Poisson, or five-moment conclusion.",
        "anchors": "1-4; 23-71",
    },
    "NavierStokesReview/src/audit/priority_146_euler_cylinder_endpoint_graph_source_review_2026-09-29.md": {
        "clusters": ["euler", "cylinder", "endpoint", "graph", "methodology", "repository-root"],
        "finding": "Human-readable Priority 146 direct review of twelve Euler cylinder endpoint, reflection, embedding, and graph modules. It records positive operator theorems and strict limits on Navier-Stokes interpretation.",
        "anchors": "1-93",
    },
    "NavierStokesReview/evidence/source_tranche_euler_cylinder_endpoint_graph_2026-09-29.json": {
        "clusters": ["euler", "cylinder", "endpoint", "graph", "methodology", "repository-root"],
        "finding": "Machine-readable Priority 146 evidence for twelve directly reviewed Euler cylinder endpoint, reflection, embedding, and graph modules.",
        "anchors": "generated JSON; 12 source records",
    },
    "NavierStokes/ActualCandidateAssembly.lean": {
        "clusters": ["endpoint", "candidate-packaging"],
        "finding": "Witness is a proposition with candidate, force, consequence, decay, and blow-up fields; no selected Cartesian five-moment equality field is present.",
        "anchors": "1121-1151; 1177-1181",
    },
    "NavierStokes/ActualCandidateConstruction.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "moments", "pressure", "time"],
        "finding": "Constructs the selected cycle, chart velocity/pressure stages, direct and stream mean stages, and potential-stage fields. The checked stage equalities stop at local/chart/stage identities; they do not export the final Cartesian field's five-moment tuple.",
        "anchors": "205-257; 289-345; 832-970",
    },
    "NavierStokes/R3/ProblemStatement.lean": {
        "clusters": ["endpoint", "r3", "pressure", "energy"],
        "finding": "CandidateProperties exports smoothness, support, divergence, residual, energy, and speed fields; it does not export moments or force-independence.",
        "anchors": "92-109; 137-153",
    },
    "NavierStokes/MixedCandidateAssembly.lean": {
        "clusters": ["endpoint", "stage-interface"],
        "finding": "StageEstimates is a generic rate/smoothness interface and carries no five-moment or debt payload.",
        "anchors": "29-91",
    },
    "NavierStokes/GermCandidateAssembly.lean": {
        "clusters": ["endpoint", "stage-interface", "global-assembly"],
        "finding": "The stage interface is consumed to produce schedules, vanishing residual jets, and candidate consequences; no selected-field moment equality is required.",
        "anchors": "164-271",
    },
    "NavierStokes/CandidateConsequences.lean": {
        "clusters": ["endpoint", "global-assembly", "pressure", "force"],
        "finding": "The global consequence theorem consumes smoothness, divergence, residual-flatness, extensions, and axis blow-up premises; its conclusion is not a five-moment transport theorem.",
        "anchors": "185-215",
    },
    "NavierStokes/CandidateFromLimits.lean": {
        "clusters": ["endpoint", "force", "jets"],
        "finding": "The specified force is constructed from the traced residual and actual normal jets, then proved equal to the activated residual.",
        "anchors": "80-112",
    },
    "NavierStokes/ActualStageEstimates.lean": {
        "clusters": ["endpoint", "stage-interface", "physical-data"],
        "finding": "Concrete stage estimates use local physical fields and residual-rate bounds; no selected-field radial-moment equality is exported at this layer.",
        "anchors": "10-12; 399-403",
    },
    "NavierStokes/GluedStageEstimates.lean": {
        "clusters": ["endpoint", "stage-interface", "time"],
        "finding": "The glued estimate packages rates and smoothness; it does not itself carry a five-moment transport conclusion.",
        "anchors": "684-694",
    },
    "NavierStokes/ActualCycleResidualBounds.lean": {
        "clusters": ["stage-interface", "residual", "physical-data"],
        "finding": "Residual-rate invariants are stated over local PhysicalFields and rates, not as a final Cartesian-to-radial observable equality.",
        "anchors": "1015-1038; 1142-1172",
    },
    "NavierStokes/NominalProfile.lean": {
        "clusters": ["moments", "profiles"],
        "finding": "FiveMomentCertificate and Witness.five_moments are real upstream profile certificates and are consumed by profile construction; endpoint transport remains separate.",
        "anchors": "2079-2145; 2536-2541",
    },
    "NavierStokes/FirstOrderBaseEdge.lean": {
        "clusters": ["moments", "profiles"],
        "finding": "Consumes a NominalProfile five-moment certificate locally; this is not evidence that the final selected Cartesian field exports the same tuple.",
        "anchors": "387-388",
    },
    "NavierStokes/DefectIncrementBounds.lean": {
        "clusters": ["rank", "moments", "corrections"],
        "finding": "Defines correction-layer barMoment and related zero-row reasoning; direct evaluation on the final selected Cartesian field remains open.",
        "anchors": "214; 607-645",
    },
    "NavierStokes/PositiveOrderMoments.lean": {
        "clusters": ["moments", "rank", "profiles", "pressure"],
        "finding": "Defines a genuine five-coordinate Debt and proves exact repair and target-moment identities, plus exterior pressure/flux consequences under explicit moment hypotheses. These profile-level results are not themselves a theorem about the final selected Cartesian endpoint.",
        "anchors": "21-23; 77-84; 192-301; 511-674",
    },
    "NavierStokes/MeanRankUpdate.lean": {
        "clusters": ["rank", "moments", "corrections"],
        "finding": "Defines scaling for the three-coordinate physical debt and proves scaled/physical FiveRows for correction increments. The result constrains rank correction functions; no theorem here identifies those rows with total moments of the exported selected field.",
        "anchors": "24-44; 137-169; 195-200",
    },
    "NavierStokes/CorrectionInitialization.lean": {
        "clusters": ["corrections", "rank", "moments", "cartesian-assembly", "residual"],
        "finding": "Constructs primary correction pieces, actual cutoff curls, pressure modes, support bounds, and local radial/zero-mass consequences. These are correction and stage-level results; the inspected declarations do not identify the final selected Cartesian field with the paper's five observables.",
        "anchors": "112-270; 1153-1234; 1201-1234",
    },
    "NavierStokes/StateMomentBalances.lean": {
        "clusters": ["moments", "rank", "corrections", "pressure"],
        "finding": "Proves actual radial and pressure moment balances for local state and flux inputs. Its own FluxInputs comment states that regularity premises do not include an averaged equation or moment identity; the results remain local state/correction identities rather than a selected whole-space Cartesian export.",
        "anchors": "719-721; 767-824; 956-1005; 1063-1118",
    },
    "NavierStokes/IntegratedMeanBalances.lean": {
        "clusters": ["moments", "rank", "pressure"],
        "finding": "Defines actual radial moments, integration-by-parts identities, torus averages, and local smooth-shell transport. These operators are genuine analytical infrastructure, but the inspected declarations do not compose them with the final selected ASum/BSum/PSum field.",
        "anchors": "10-18; 24-224; 237-330; 360-520; 581-697",
    },
    "NavierStokes/PhysicalMeanDomain.lean": {
        "clusters": ["moments", "profiles", "pressure", "cartesian-assembly", "axis"],
        "finding": "Provides local slow-domain localisation, fibre germs, support, periodicity, finite-jet and radial-moment bounds. It proves domain-local transport properties, not the final selected Cartesian-to-radial five-moment equality.",
        "anchors": "33-181; 227-429; 493-616; 717-805; 1085-1105; 1177-1234",
    },
    "NavierStokes/ActualSignedPhysicalData.lean": {
        "clusters": ["cartesian-assembly", "moments", "pressure", "jets"],
        "finding": "Builds the concrete Cartesian signed carrier, potential and pressure sums, with explicit tsum and periodised physical equalities. This strengthens the selected-field construction record, but the inspected route still lacks a final theorem evaluating the five paper moments after all sums and transforms.",
        "anchors": "248-250; 554-570; 699-752; 965-990; 1064-1066; 1141-1181",
    },
    "NavierStokes/RadialSchedule.lean": {
        "clusters": ["moments", "profiles", "time"],
        "finding": "Defines the scheduled radial profiles and proves an exact two-moment reset together with pulse-energy and release-lag estimates. These are reduced schedule/profile identities, not a theorem transporting the five paper observables to the exported Cartesian field.",
        "anchors": "27-38; 147-160; 177-218",
    },
    "NavierStokes/PressureStream.lean": {
        "clusters": ["pressure", "moments", "cartesian-assembly"],
        "finding": "Defines torus-averaged pressure mass and a pressure-source correction whose mass is exactly zero, with periodic and fibre-local consequences. This is genuine intermediate pressure normalisation; it is not an absolute whole-space Poisson theorem or a final selected five-moment transport result.",
        "anchors": "121-185; 596-707; 800-813",
    },
    "NavierStokes/TerminalEdgeFactor.lean": {
        "clusters": ["profiles", "pressure", "moments", "time"],
        "finding": "Proves improper-FTC radial and scalar flat-density integral identities, smooth terminal coefficients, pressure-gradient primitives, and axial-stress factorisations on the terminal edge. These are explicit reduced edge integrals and pressure constructions, not evaluations of the final selected Cartesian field's five observables.",
        "anchors": "158-239; 394-429; 588-603; 643-690; 980-1072",
    },
    "NavierStokes/ActualPeriodizedSignedRealization.lean": {
        "clusters": ["cartesian-assembly", "pressure", "jets", "time"],
        "finding": "Proves finite-native-support tsum collapse, smooth masked sums, periodised coefficient transport, and that the physical velocity is an explicit spatial curl of the physical potential. It provides real assembly and coordinate identities, but no final barMoment or (M,I,J,S,Cp) identity for the exported whole-space field.",
        "anchors": "46-145; 261-374; 480-519; 641-670",
    },
    "NavierStokes/ActualSignedPhysicalBinding.lean": {
        "clusters": ["cartesian-assembly", "pressure", "residual", "jets"],
        "finding": "Binds native signed physical data to common/reference copies and proves exact amplitude, pressure, curl-potential, and tsum reference equalities. The declarations establish value-level local binding across periodisation, but do not transport the five radial paper observables to the selected endpoint.",
        "anchors": "103-220; 602-773; 785-808",
    },
    "NavierStokes/ParticularWaveAssembly.lean": {
        "clusters": ["cartesian-assembly", "residual", "rank", "jets"],
        "finding": "Constructs signed harmonic blocks, proves mean-zero reconstruction, invariant propagation through curl corrections and tsum, periodised copy transport, and exact local cancellation identities. These are mode/block and local residual results; they are not a global selected-field radial-moment evaluation.",
        "anchors": "79-183; 268-323; 619-659; 802-854; 1565-1617; 1790-1813",
    },
    "NavierStokes/ActualCurrentParticularPhysical.lean": {
        "clusters": ["cartesian-assembly", "axis", "residual", "jets"],
        "finding": "Builds current particular cylindrical potentials and pressures, proves chart/full-turn periodicity, native smoothness, radial-face boundary zero, and exact native/local cylindrical-to-Cartesian curl transport under cycle invariants. This is strong local field realisation, but no final five-observable transport theorem is exported.",
        "anchors": "31-122; 135-335; 347-463; 620-706; 778-887",
    },
    "NavierStokes/HarmonicResidual.lean": {
        "clusters": ["residual", "cartesian-assembly", "moments", "jets"],
        "finding": "Extracts finite harmonic residual blocks, proves conjugate symmetry, band limits, zero modes, smoothness, angular mean-zero, and reconstruction of the full differentiated residual. These are exact Fourier/harmonic residual identities and do not identify the selected Cartesian field with the five paper moments.",
        "anchors": "1006-1195; 1438-1604",
    },
    "NavierStokes/PhysicalMeanJetBounds.lean": {
        "clusters": ["cartesian-assembly", "pressure", "moments", "jets"],
        "finding": "Proves spatial-curl jet bounds and smoothness for coherent mean fields, fibre-local pressure/stream coherence, and reconstruction of pressure from the coherent source. These are local regularity and pressure operators; no final selected-field radial five-moment equality is stated.",
        "anchors": "782-812; 838-870",
    },
    "NavierStokes/PulseCone.lean": {
        "clusters": ["profiles", "moments", "residual", "pressure"],
        "finding": "Proves the actual pulse mass expansion, quantified cone margins, error budgets, and axial-history error bounds from the profile data. This is a genuine reduced pulse/energy mechanism, but it does not evaluate the assembled Cartesian tsum field against (M,I,J,S,Cp).",
        "anchors": "1039-1074; 1094-1192; 1194-1223",
    },
    "NavierStokes/InitialPhysicalData.lean": {
        "clusters": ["physical-data", "cartesian-assembly", "jets"],
        "finding": "Builds selected physical source coefficients, carriers, copy amplitudes, pressure coefficients, and support/domain facts for the actual stage data. The inspected declarations feed concrete field construction but do not state the final five-observable equality.",
        "anchors": "40-114; 141-211; 258-355; 404-488; 535-572; 589-685",
    },
    "NavierStokes/CrossBasedMeanComposition.lean": {
        "clusters": ["moments", "rank", "residual", "pressure", "cartesian-assembly"],
        "finding": "Defines an explicit crossDefect between averaged cross covariance and physical stress, retains finite-head defect terms, and proves four-stage mean/debt gains under explicit zero radial-moment hypotheses. This is a local/intermediate debt theorem, not final selected Cartesian moment transport.",
        "anchors": "24-74; 269-333; 389-505",
    },
    "NavierStokes/ActualCarrierTransportBase.lean": {
        "clusters": ["cartesian-assembly", "time", "jets"],
        "finding": "Constructs selected carrier geometry, slow/source regions, native clock and coordinate transport, canonical source regions, cutoffs, and outer injectivity. It contains no final radial-moment evaluation.",
        "anchors": "27-89; 121-152; 156-203; 218-270",
    },
    "NavierStokes/BorelExtension.lean": {
        "clusters": ["jets", "time", "cartesian-assembly"],
        "finding": "Constructs compactly supported Taylor-Borel extensions with all-order derivative bounds, summable majorants, prescribed jets, and right-endpoint gluing. It carries no selected-fluid moment observable.",
        "anchors": "26-147; 177-239; 250-371",
    },
    "NavierStokes/DiophantineGraph.lean": {
        "clusters": ["cartesian-assembly", "jets"],
        "finding": "Proves nonresonant graph symbols, explicit Diophantine lower bounds, inverse multiplier growth, and covering-frequency scaling for nonzero integer modes. It is frequency infrastructure, not endpoint moment transport.",
        "anchors": "22-104; 171-263; 265-315",
    },
    "NavierStokes/FlatKernelBounds.lean": {
        "clusters": ["profiles", "jets", "residual"],
        "finding": "Defines the square-root flat kernel and proves derivative expressions, polynomial profile-jet bounds, smoothness, and unweighted derivative estimates. It does not prove weighted radial-moment convergence of the selected tsum field.",
        "anchors": "28-75; 86-150; 181-274; 333-440",
    },
    "NavierStokes/ParametricODE.lean": {
        "clusters": ["time", "profiles", "jets"],
        "finding": "Constructs and inverts a finite-interval Volterra operator, builds the solution from initial data and forcing, proves the derivative equation, and establishes smooth parameter dependence and stability bounds. It is an ODE subsystem, not the Navier-Stokes endpoint bridge.",
        "anchors": "30-121; 128-218; 239-305; 309-464",
    },
    "NavierStokes/PhaseCalculus.lean": {
        "clusters": ["cartesian-assembly", "axis", "jets", "time"],
        "finding": "Defines the actual phase, proves its Frechet derivatives, material-operator cancellation, harmonic periodicity, off-axis smoothness, and nonvanishing under comparison hypotheses. It contains no global radial-moment equality.",
        "anchors": "39-117; 122-224; 226-305",
    },
    "NavierStokes/SlotColoring.lean": {
        "clusters": ["cartesian-assembly", "jets"],
        "finding": "Constructs dyadic mesh widths, physical overlap boxes, an explicit finite proper colouring, finite candidate/neighbor sets, degree bounds, and native-index gaps. It supports localisation bookkeeping but does not transport field observables.",
        "anchors": "33-98; 112-185; 189-304; 310-459",
    },
    "NavierStokes/WaveEnvelopeTransport.lean": {
        "clusters": ["cartesian-assembly", "jets", "time", "force"],
        "finding": "Proves copy-envelope/path identities, local finite grouping, support exclusion, wave-class bounds, source/forcing jet transport, and anchored-solve vanishing. It does not evaluate radial moments of the final selected field.",
        "anchors": "23-106; 203-355; 362-523; 550-581",
    },
    "NavierStokes/ActivationCone.lean": {
        "clusters": ["profiles", "moments", "residual", "jets"],
        "finding": "Proves smooth activation errors, uniform derivative bounds, ramp/collar cone margins, exact stress factorisation, cone-gap factorisation, and stock-to-cone error transport. These are local activation estimates, not final selected-field moment transport.",
        "anchors": "26-154; 246-420; 447-661",
    },
    "NavierStokes/ActualCycleParameters.lean": {
        "clusters": ["cartesian-assembly", "time", "rank"],
        "finding": "Constructs the current cycle parameters from initialized labels, proves reindexing, band, source, carrier, and signed-request identities, and explicitly does not assert analytic correction-cycle preservation. No final radial observable is defined.",
        "anchors": "5-18; 29-116; 124-182; 219-339; 351-508",
    },
    "NavierStokes/FlatCovariance.lean": {
        "clusters": ["profiles", "jets", "rank"],
        "finding": "Defines edge-scaled covariance matrices and inverse amplitudes, proves exact target reconstruction including the edge-zero branch, strict positivity, smoothness, and flat weighted derivatives. No radial moment or selected-endpoint transport theorem is present.",
        "anchors": "28-51; 195-255; 266-404; 432-551",
    },
    "NavierStokes/HarmonicMeanInteraction.lean": {
        "clusters": ["residual", "cartesian-assembly", "rank", "jets"],
        "finding": "Defines the mean cross coefficient and proves the corresponding harmonic residual update, wave-class bounds, band limits, conjugacy, smoothness, and zero modes. The output remains a harmonic residual block, not a final five-observable equality.",
        "anchors": "119-215; 245-341; 352-432; 441-582",
    },
    "NavierStokes/SimilarityCoordinates.lean": {
        "clusters": ["axis", "time", "profiles", "jets"],
        "finding": "Defines and differentiates the positive similarity-coordinate inverse and rescaled coordinate X under explicit positive-radius and pre-terminal-time hypotheses. It records off-axis domain scope but no global radial moment transport.",
        "anchors": "22-232; 195-294; 390-455; 500-559",
    },
    "NavierStokes/ActualSignedMeanBinding.lean": {
        "clusters": ["moments", "rank", "residual", "cartesian-assembly"],
        "finding": "Constructs the actual signed cross tensor, proves the partition-factor stress identity and exact prepared-tail cancellation, and retains an explicit earlier-band missing-weight cross defect. Family defect estimates consume ordinary residual and mean-class hypotheses; they do not evaluate the final selected Cartesian five moments.",
        "anchors": "341-438; 440-516; 578-667; 669-695",
    },
    "NavierStokes/VolterraParity.lean": {
        "clusters": ["axis", "profiles", "jets"],
        "finding": "Defines reflected coefficient/forcing data, symmetric gluing, and the radial Volterra solution, then proves parity commutes with the radial inverse and integral solution. This is axis/parity regularity, not a whole-space Cartesian moment theorem.",
        "anchors": "22-214; 383-444; 454-661",
    },
    "NavierStokes/ActualCycleAssembly.lean": {
        "clusters": ["cartesian-assembly", "residual", "jets", "time"],
        "finding": "Proves actual signed-block support, cutoff-source, zero-mode, zero-germ, Gaussian-germ, curl-support, source/copy factorisation, and final finite assembly support. No barMoment, FiveRows, or selected whole-space five-observable equality is exported.",
        "anchors": "40-321; 354-547; 610-839; 896-955; 1019-1134",
    },
    "NavierStokes/TorusInverse.lean": {
        "clusters": ["cartesian-assembly", "moments", "jets", "pressure"],
        "finding": "Defines rapid Fourier series, smooth derivatives, directional inversion, torus descent, and the actual Haar integral extracting the zero coefficient. This is substantive torus mean infrastructure, but no theorem maps the final selected Cartesian tsum field to (M,I,J,S,C_p).",
        "anchors": "21-186; 195-333; 335-420; 424-439; 503-586",
    },
    "NavierStokes/ModulatedCone.lean": {
        "clusters": ["profiles", "moments", "rank", "jets"],
        "finding": "Indexes five profile-history rows, proves localized C/n history and derivative bounds, constructs profile repair preserving exterior radial germs, and derives five-row jet estimates. These remain profile-level identities, not selected Cartesian moment transport.",
        "anchors": "623-730; 966-1016; 1018-1080",
    },
    "NavierStokes/PrimaryTargetBounds.lean": {
        "clusters": ["profiles", "rank", "jets", "cartesian-assembly"],
        "finding": "Defines the primary covariance model and target, proves strict-cone and target-amplitude bounds, and constructs restricted/actual covariance bounds. No field-level radial integral or endpoint five-observable equality occurs.",
        "anchors": "27-229; 457-631; 802-917; 960-1035",
    },
    "NavierStokes/LoopVariance.lean": {
        "clusters": ["moments", "profiles", "jets"],
        "finding": "Defines actual angular exponential-family moments and proves normaliser, derivative, analyticity, positivity, variance, and determinant identities. These are angular subsystem moments, not the selected whole-space radial barMoment.",
        "anchors": "24-139",
    },
    "NavierStokes/JointODE.lean": {
        "clusters": ["time", "jets", "profiles"],
        "finding": "Reparametrises fixed-interval linear ODE solutions and proves joint parameter/current-time smoothness and agreement with the actual integral solution. It does not claim smoothness of an external clamped extension or provide endpoint moment transport.",
        "anchors": "35-114; 129-219",
    },
    "NavierStokes/MixedCandidateWitness.lean": {
        "clusters": ["endpoint", "candidate-packaging", "cartesian-assembly", "jets", "force"],
        "finding": "SelectedSchedule requires growing indices, smooth sums, and vanishing residual jets; the finite-stage witness constructs ASum/BSum/PSum, activated fields, force, CandidateProperties, consequences, H3 blow-up, force derivative bounds, and boundary limits. The type still has no (M,I,J,S,C_p) equality or FiveRows premise.",
        "anchors": "23-31; 41-97; 101-150",
    },
    "NavierStokes/R3/CompactTimeIntegral.lean": {
        "clusters": ["r3", "energy", "pressure", "time"],
        "finding": "Proves continuity and differentiation under ordinary whole-space spatial integrals with uniform compact support and interior-time hypotheses. This is real integration infrastructure, not selected radial moment transport.",
        "anchors": "47-109; 111-184",
    },
    "NavierStokes/R3/HeatKernelCancellation.lean": {
        "clusters": ["r3", "pressure", "residual"],
        "finding": "Defines the squared-cutoff heat-kernel commutator, proves diagonal cancellation, Lipschitz/minimum bounds, and inverse-cube majorants before integration. It does not assert vanishing of selected-field radial moments.",
        "anchors": "24-89; 105-166; 196-203",
    },
    "NavierStokes/R3/HeatKernelFubini.lean": {
        "clusters": ["r3", "pressure", "residual"],
        "finding": "Proves absolute product-space integrability of the cutoff-cancelled heat-kernel integrand and justifies the time-space integral swap. No selected-field five-observable evaluation is present.",
        "anchors": "24-81; 83-107",
    },
    "NavierStokes/R3/HeatKernelTimeBound.lean": {
        "clusters": ["r3", "pressure", "energy"],
        "finding": "Evaluates inverse-time Gamma integrals and proves the three-dimensional heat-kernel Hessian envelope and inverse-cube absolute bound. This is R3 comparison/pressure support, not radial profile transport.",
        "anchors": "33-80; 82-114; 157-214",
    },
    "NavierStokes/R3/WeakTimeContinuity.lean": {
        "clusters": ["r3", "time", "pressure"],
        "finding": "Proves compact-test continuity and upgrades it to continuous whole-space pairings under uniform spatial L1 bounds and tests vanishing at infinity. It contains no endpoint five-moment identity.",
        "anchors": "44-119; 121-175",
    },
    "NavierStokes/CoordinateAlgebra.lean": {
        "clusters": ["axis", "time", "profiles"],
        "finding": "Checks manuscript coordinate algebra, positivity, Jacobian and inverse identities, and chain-rule coefficients. Its header explicitly excludes construction of a smooth inverse chart, a Navier-Stokes solution, or a singularity.",
        "anchors": "5-12; 18-128; 138-214",
    },
    "NavierStokes/FlatCutoff.lean": {
        "clusters": ["time", "profiles", "jets"],
        "finding": "Defines the exponential-flat scalar cutoff and proves smoothness, vanishing jets, and inverse-power quotient regularity. The header explicitly excludes stress factorisation, PDE estimates, and force-extension claims.",
        "anchors": "5-17; 23-50; 66-199",
    },
    "NavierStokes/PositiveTimeCopyFamily.lean": {
        "clusters": ["cartesian-assembly", "time", "jets"],
        "finding": "Proves positive-time gate equality, zero outside preterminal time, germ and all-jet equality, and transport through periodised and vector sums. This is copy-field transport, not global radial moment transport.",
        "anchors": "90-158; 160-188",
    },
    "NavierStokes/SpatialCurl.lean": {
        "clusters": ["cartesian-assembly", "axis", "jets"],
        "finding": "Defines the physical Euclidean Frechet curl and proves divergence-of-curl, regularity loss, periodicity, time support, and closed-support non-enlargement. No radial integral or selected five-observable equality is stated.",
        "anchors": "23-128; 168-208",
    },
    "NavierStokes/TangentODE.lean": {
        "clusters": ["time", "profiles", "jets"],
        "finding": "Constructs finite-interval integral curves and proves contraction/fixed-point existence, uniqueness, and linear uniformly Lipschitz solutions. It is a tangent ODE subsystem with no whole-space field observable.",
        "anchors": "26-197",
    },
    "NavierStokes/CutStageEstimates.lean": {
        "clusters": ["jets", "cartesian-assembly", "time"],
        "finding": "Derives actual scaled-cutoff and diagonal stage jet bounds, including one common doubling schedule for stream potentials, angular fields, and pressures. These are local rate estimates, not radial moment preservation.",
        "anchors": "28-180; 349-428",
    },
    "NavierStokes/EvenSmoothDescent.lean": {
        "clusters": ["axis", "profiles", "jets"],
        "finding": "Proves even-function descent through the square map, regularised radial derivatives, Hadamard formulas, and axis derivative vanishing. It contains no selected whole-space moment equality.",
        "anchors": "32-121; 126-231",
    },
    "NavierStokes/R3/ComparisonCutoffs.lean": {
        "clusters": ["r3", "pressure", "energy"],
        "finding": "Defines smooth compact whole-space comparison cutoffs, weights, and pressure multipliers with exact one/zero regions and support bounds. These support comparison estimates, not selected radial moment transport.",
        "anchors": "28-100",
    },
    "NavierStokes/SmoothCutoffs.lean": {
        "clusters": ["time", "jets", "cartesian-assembly"],
        "finding": "Defines C-infinity Mathlib bump cutoffs and proves support, plateau, scaled, and time-switch properties. The header makes no analyticity claim and no moment theorem is present.",
        "anchors": "25-78",
    },
    "NavierStokes/SpacetimeGluing.lean": {
        "clusters": ["time", "jets", "cartesian-assembly"],
        "finding": "Proves Frechet, finite-order, and C-infinity past/future gluing from value and one-sided normal time-jet matching. This establishes regularity, not preservation of radial observables.",
        "anchors": "192-300",
    },
    "NavierStokes/ParametricModulation.lean": {
        "clusters": ["profiles", "moments", "jets"],
        "finding": "Constructs normalised periodic interval primitives with exact zero mean and compact parameter extensions, proving smoothness, periodicity, and zero-mean identities. These are modulation identities, not final Cartesian five-moment transport.",
        "anchors": "23-107; 181-218; 218-287",
    },
    "NavierStokes/PrimaryCopyBridge.lean": {
        "clusters": ["cartesian-assembly", "time", "jets", "force"],
        "finding": "Reindexes copy frames and sources, proves the reconstructed path satisfies the projected tangent equation, and identifies it with the anchored copy solve by uniqueness, including ordinary tensor derivatives. It explicitly assumes no ambient energy inequality and does not identify the final field's radial moments.",
        "anchors": "42-116; 167-174; 210-228; 459-483; 487-539",
    },
    "NavierStokes/PrimaryCovarianceBounds.lean": {
        "clusters": ["profiles", "rank", "jets"],
        "finding": "Defines the actual normalised-slot covariance and proves compact cone margins, chart scale, determinant/inverse-weight, and positive-weight bounds. These are substantive covariance estimates, not a final radial moment observable.",
        "anchors": "30-49; 89-181; 337-389",
    },
    "NavierStokes/ActualSignedNativeProfiles.lean": {
        "clusters": ["profiles", "jets", "cartesian-assembly"],
        "finding": "Defines active native label regions, signed profile pairs, profile domains, polynomial jets, native profile families, and support/closure coverage. These are prepared-region profile and jet results, not a final Cartesian radial-moment tuple.",
        "anchors": "31-63; 100-184; 206-251",
    },
    "NavierStokes/ActualPrimaryCovariance.lean": {
        "clusters": ["profiles", "rank", "moments", "jets"],
        "finding": "Proves common-cover and wave transport identities, pair covariance, active-label support, native-point geometry, scale/mask properties, tangent sums, partition factors, missing-weight decomposition, and mean-class bounds. Intermediate averagedDefect/missingWeight quantities are not identified with the final selected five observables.",
        "anchors": "26-115; 128-204; 352-384; 632-856",
    },
    "NavierStokes/ActualCurrentParticularBounds.lean": {
        "clusters": ["profiles", "jets", "residual", "cartesian-assembly"],
        "finding": "Builds literal current particular-wave potential and pressure coefficients from actual current state data and proves local/common source, envelope, and native control bounds. This is an actual coefficient/rate layer, not radial-moment transport.",
        "anchors": "39-130; 141-244",
    },
    "NavierStokes/ActualSignedNativeBounds.lean": {
        "clusters": ["profiles", "jets", "force", "cartesian-assembly"],
        "finding": "Defines native potential/pressure sources, label selection, inactive-label zero results, source identification, and uniform/native/source bounds. Concrete signed physical data and MovingField enter upstream, but the exported results are source/jet bounds and contain no final (M,I,J,S,C_p) equality.",
        "anchors": "35-128; 152-205; 426-480; 566-704",
    },
    "NavierStokes/ActualSignedPhysicalCoherence.lean": {
        "clusters": ["cartesian-assembly", "profiles", "pressure", "jets"],
        "finding": "Proves finite-support/finsum reindexing, active physical-index selection, potential/pressure term and sum labels, native chart identities, reference cutoffs, canonical potential/pressure values, current zero behaviour, and measured potential/pressure equality to finite physical sums. It does not compose the final field with barMoment.",
        "anchors": "39-161; 167-342; 437-575; 608-761; 768-831",
    },
    "NavierStokes/ParticularWaveBounds.lean": {
        "clusters": ["cartesian-assembly", "jets", "force", "residual", "pressure"],
        "finding": "Provides forced/copy/modal wave envelope jets, copy-solve pressure cancellation, pressure/velocity regularity, exact curl/divergence realisation, support after curl, and constructed particular-wave residual classes. These are substantive local wave/residual bounds, not selected global radial moments.",
        "anchors": "35-461; 657-810; 846-945; 1932-2110; 2172-2217",
    },
    "NavierStokes/PeriodicUniqueness.lean": {
        "clusters": ["r3", "energy", "pressure", "force"],
        "finding": "Derives the periodic difference equation, periodic integration-by-parts energy identities, pressure cancellation, Gronwall zero, and classical uniqueness on closed preterminal intervals. This is same-force periodic comparison, not five-moment transport or absolute selected-pressure semantics.",
        "anchors": "110-154; 316-441; 470-616; 638-705",
    },
    "NavierStokes/ActualCyclePeriodicity.lean": {
        "clusters": ["cartesian-assembly", "time", "pressure", "jets"],
        "finding": "Tracks coefficient translation, angular periodicity, finite-prefix agreement, valid chart domains, pressure periodicity, and stage-realisation fields. StageRealizations and physicalFields_of_stages/all provide finite-prefix PhysicalData, with no five-observable endpoint equality.",
        "anchors": "34-195; 204-338; 342-483",
    },
    "NavierStokes/ActualParticularStageControls.lean": {
        "clusters": ["profiles", "cartesian-assembly", "time", "jets"],
        "finding": "Reindexes the selected phase/frame, constructs reference/native/background particular data, proves common phase bounds, clock-envelope transport, and active label/parameter control. These are genuine upstream stage identities and do not state selected-field radial moment preservation.",
        "anchors": "31-167; 209-338; 342-560",
    },
    "NavierStokes/ActualPhysicalPrefixFields.lean": {
        "clusters": ["cartesian-assembly", "pressure", "residual", "jets", "axis"],
        "finding": "Defines source and Cartesian chart domains, proves chart existence and source sublevel control, and records StageRealizations with finite-stage potential/direct/pressure agreement. Prefix/germ theorems derive PhysicalData for the same literal prefix, not the final selected infinite sum or moments(selected_field)=(M,I,J,S,C_p).",
        "anchors": "240-320; 327-386; 438-499",
    },
    "NavierStokes/ActualSignedCommonDynamics.lean": {
        "clusters": ["cartesian-assembly", "residual", "axis", "pressure", "jets"],
        "finding": "Defines actual signed common-wave slopes, phase/geometry data, local/common equations, zero-germ cancellation, exact curl/divergence realisation, pressure invariance, and good/gaussian invariant representations. These are intermediate copy-state identities, not a final selected Cartesian five-moment equality.",
        "anchors": "23-104; 128-218; 229-309; 370-420",
    },
    "NavierStokes/ActualSignedExterior.lean": {
        "clusters": ["cartesian-assembly", "pressure", "axis", "profiles"],
        "finding": "Proves normalised-coordinate consistency, physical lifting, mask-or-target zero alternatives, active-label reindexing, amplitude/term zero results, periodised potential/pressure sums vanishing outside the active region, and zero germs/velocity outside the annulus. This is exact support evidence, not final radial-observable evaluation or absolute pressure semantics.",
        "anchors": "30-86; 91-167; 194-321; 325-395",
    },
    "NavierStokes/MeanIncrementBounds.lean": {
        "clusters": ["residual", "moments", "pressure", "rank"],
        "finding": "Defines radial/angular/axial field triples, graph derivatives, radial divergence, time/viscous operators, nonlinear residual blocks, and base/cumulative/increment bounds. The exact residual-difference framework retains old/new cross terms; it does not identify an increment with the final selected global field or prove a nonzero remainder.",
        "anchors": "24-69; 76-186; 200-292; 310-392",
    },
    "NavierStokes/TemporalStateCoherence.lean": {
        "clusters": ["time", "profiles", "pressure", "cartesian-assembly"],
        "finding": "Proves scaling identities for physical speed, stream potentials, graph derivatives, pressure/alias updates, temporal stages, and band transport. These are genuine naturality results for intermediate temporal state fibres, not final selected-field five-observable transport.",
        "anchors": "27-145; 166-237; 280-372; 397-537",
    },
    "NavierStokes/ActualSignedCurrentSupport.lean": {
        "clusters": ["cartesian-assembly", "pressure", "axis", "jets"],
        "finding": "Proves raw/common/cylindrical potential and pressure zero results from native-mask, exterior, and target-support hypotheses, including current-band zero germs. These are exact support-propagation results, not a global moment calculation.",
        "anchors": "20-80; 180-316",
    },
    "NavierStokes/ActualSignedOutputBounds.lean": {
        "clusters": ["jets", "cartesian-assembly", "pressure", "force"],
        "finding": "Defines actual signed output copies and proves local potential/pressure jet bounds, zero germs, support localisation, and output-family control. This connects request data to rate/support outputs, not the selected field's (M,I,J,S,C_p) tuple.",
        "anchors": "20-118; 145-220; 250-357",
    },
    "NavierStokes/ActualSignedPhysicalZeros.lean": {
        "clusters": ["cartesian-assembly", "pressure", "axis", "profiles"],
        "finding": "Proves zero propagation from physical native-radius masks through raw, cylindrical, and canonical periodised potential/pressure modes. These exact local vanishing results do not prove a nonzero or zero global selected radial moment.",
        "anchors": "20-88; 180-316",
    },
    "NavierStokes/ActualSignedPotentialCoherence.lean": {
        "clusters": ["cartesian-assembly", "profiles", "pressure", "axis"],
        "finding": "Defines the literal current-band vector potential and pressure mode, proving carrier/weight identities, request transport, rescaled potential/pressure transport, chart/natural-point identities, and cylindrical values/germs. It is potential-level transport before final assembly and has no barMoment theorem.",
        "anchors": "26-63; 82-219; 225-267; 283-357",
    },
    "NavierStokes/ActualValidBandWaves.lean": {
        "clusters": ["cartesian-assembly", "profiles", "axis", "jets", "pressure"],
        "finding": "Defines actual local/global band potentials and pressure, proving native-point overlap maps, inactive-mode zero, local-field equality, compatibility, potential/pressure germs, shrinking support, axis zero, and smoothness. This is a valid-chart wave bridge, not final selected Cartesian five-observable transport.",
        "anchors": "32-106; 131-239; 260-357",
    },
    "NavierStokes/ActualWaveCoefficientPeriodicity.lean": {
        "clusters": ["time", "cartesian-assembly", "profiles"],
        "finding": "Proves deck translations of native sections, conjugate-pair translation, assembled velocity/pressure translation, and signed coefficient periodicity under explicit source assumptions. It does not supply radial-moment preservation after complete selected-field sum, curl, localisation, and packaging.",
        "anchors": "21-116; 130-209",
    },
    "NavierStokes/CurrentParticularLabelBounds.lean": {
        "clusters": ["jets", "cartesian-assembly", "axis", "profiles"],
        "finding": "Defines the signed-label/window/chart map, proves refined support inclusion, finite harmonic mode counts, local potential/pressure jet bounds, and smoothness/axis-zero-germ statements. These are finite-label rate/support estimates, not final radial-observable evaluation.",
        "anchors": "21-74; 94-191; 227-298; 317-417",
    },
    "NavierStokes/CurrentSignedCurl.lean": {
        "clusters": ["cartesian-assembly", "axis", "pressure", "jets"],
        "finding": "Defines the actual amplitude bound and proves common tangency, potential smoothness, native exact curl, forward Cartesian curl, finite label-sum curl, periodicity, overlap agreement, and current pressure-mode identities. This is a genuine current-band bridge, not final selected barMoment equality.",
        "anchors": "29-119; 197-300; 304-373; 382-461",
    },
    "NavierStokes/InitialNativeRegularity.lean": {
        "clusters": ["jets", "profiles", "axis", "cartesian-assembly"],
        "finding": "Defines copied amplitude/potential/pressure coefficients and proves smoothness across flat radial attachments, positive-time chart coverage, angular invariance, and nonzero-normal properties. This is initial native regularity, not global moment transport.",
        "anchors": "26-141; 150-181",
    },
    "NavierStokes/PeriodicResidualLimits.lean": {
        "clusters": ["residual", "cartesian-assembly", "time", "force"],
        "finding": "Defines original, cut, and periodic residuals, proves smoothness/eventual equality/extension results, and constructs joint residual-jet limits after localisation. The module explicitly does not assume a residual identity or residual limit after periodisation.",
        "anchors": "24-111",
    },
    "NavierStokes/SubcoverPeriodicity.lean": {
        "clusters": ["cartesian-assembly", "time", "profiles"],
        "finding": "Defines subcover/translation data and proves periodicity and agreement of subcover fields across chart copies. These are geometric deck/cover identities, not radial-observable calculations.",
        "anchors": "20-154; 160-295",
    },
    "NavierStokes/TerminalHistoryBridge.lean": {
        "clusters": ["profiles", "time", "axis", "moments"],
        "finding": "Defines terminal history/clock and proves profile switching, radial support, regular-clock derivative identities, and history transport across terminal bands. This remains a profile/history layer and does not export final selected five moments.",
        "anchors": "20-180; 840-1079",
    },
    "NavierStokes/ActualCurrentParticularAssembly.lean": {
        "clusters": ["cartesian-assembly", "residual", "pressure", "jets"],
        "finding": "Proves finite label/harmonic sum formulas for current potential and pressure, identifies Cartesian curl with particular velocity, and proves valid-chart equality for the finite current sum. It does not cover the final infinite selected envelope or radial observables.",
        "anchors": "25-127; 137-197; 214-276",
    },
    "NavierStokes/ActualEndpointInputs.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "pressure", "jets", "residual"],
        "finding": "Defines EndpointInputs and initial potential/direct/pressure models, proves their extensions, and constructs endpoint inputs from concrete stage representations. This feeds actual data into finite-stage/rate consumers; its fields do not require the paper's five-observable equality.",
        "anchors": "28-120; 120-191; 218-264",
    },
    "NavierStokes/ActualParticularPotentialCoherence.lean": {
        "clusters": ["cartesian-assembly", "profiles", "pressure", "axis"],
        "finding": "Proves phase/velocity and pressure scaling identities, current potential/pressure definitions, band transport, ambient germs, and cylindrical values. This is potential-level transport before physical curl and final packaging; no barMoment theorem is present.",
        "anchors": "28-71; 77-121; 123-188; 192-278",
    },
    "NavierStokes/ActualSeedPeriodicity.lean": {
        "clusters": ["time", "cartesian-assembly", "profiles"],
        "finding": "Proves torus deck-shift identities, conjugate pairing, phase periodicity, and periodicity of primary velocity, pressure, and Gaussian coefficients. This confirms seed periodicity but not moment preservation through the final selected sum.",
        "anchors": "24-115",
    },
    "NavierStokes/SpatialBorelExtension.lean": {
        "clusters": ["cartesian-assembly", "jets", "time"],
        "finding": "Constructs jointly smooth spatial Taylor-Borel localisation templates with compact support, derivative bounds, and scale/doubling control. It addresses spatial jet extension, not selected-field radial moment transport.",
        "anchors": "29-86; 122-211",
    },
    "NavierStokes/TrueConeLoop.lean": {
        "clusters": ["profiles", "rank", "moments"],
        "finding": "Builds the actual exponential-moment inverse, smooth speed and variance corrections, cone margins, and phase change. Its moment objects are angular exponential-family moments, not the final whole-space barMoment tuple.",
        "anchors": "22-170",
    },
    "NavierStokes/TransportPrimitive.lean": {
        "clusters": ["moments", "profiles", "cartesian-assembly"],
        "finding": "Defines translated compact radial integrals and proves Bochner integrability, parameter smoothness, support truncation, fixed-interval representations, and derivative retention. No selected Cartesian field is supplied and no (M,I,J,S,C_p) equality is concluded.",
        "anchors": "34-100; 112-245",
    },
    "NavierStokes/ActualGaussianCoverage.lean": {
        "clusters": ["profiles", "time", "jets"],
        "finding": "Defines actual Gaussian/clock rates and proves uniform envelopes, compact source/outer cells, source-cell inclusion, time support, and whole-path zero-germ properties. These support actual Volterra paths but do not evaluate selected radial observables.",
        "anchors": "25-109; 129-209",
    },
    "NavierStokes/ActualSignedPhysicalGeometry.lean": {
        "clusters": ["axis", "profiles", "cartesian-assembly"],
        "finding": "Proves preterminal annular coverage, chart existence, positive radius, physical chart membership, scale identities, and mapping into the physical polar domain. This is concrete coordinate geometry, not a global moment bridge.",
        "anchors": "25-119; 130-184",
    },
    "NavierStokes/AxisPreservation.lean": {
        "clusters": ["axis", "cartesian-assembly", "jets"],
        "finding": "Proves local finite-wave-sum collapse near the preterminal axis, curl vanishing, potential/velocity collapse to the first stage, eventual origin equality, and origin blow-up consequences. The header excludes a uniform stage radius and final-velocity estimate; no five-moment evaluation is present.",
        "anchors": "20-60; 64-174",
    },
    "NavierStokes/AxisReference.lean": {
        "clusters": ["axis", "profiles", "jets"],
        "finding": "Identifies the natural-axis reference with its leading series and proves derivative/coefficient identities, positivity, logarithmic-slope margins, and scaled profile stability. It is a reference-profile result, not the selected whole-space radial observable.",
        "anchors": "21-154; 168-275",
    },
    "NavierStokes/PhysicalHeatCoordinates.lean": {
        "clusters": ["profiles", "axis", "cartesian-assembly"],
        "finding": "Proves actual implicit physical heat-coordinate identities, normalisation, heat-carrier equivalence, and q/eta/X normalised-section formulas. These are coordinate/profile identities and do not export a global field moment theorem.",
        "anchors": "20-111",
    },
    "NavierStokes/PositiveTimeSignedLocalization.lean": {
        "clusters": ["time", "axis", "jets", "cartesian-assembly"],
        "finding": "Defines positive-native-time mask/radius conditions and proves normalised-radius bounds and mask pullback properties. Its header expressly makes no support assertion outside the positive-time domain; no endpoint moment equality is present.",
        "anchors": "25-108",
    },
    "NavierStokes/CorrectionStep.lean": {
        "clusters": ["corrections", "residual", "rank", "cartesian-assembly"],
        "finding": "Retains nonlinear covariance, transport, pressure, and residual cross-terms in one correction cycle and constructs local perturbation/correction residuals. These formulas show the correction mechanism is explicit; the inspected route does not export a final selected-field five-moment value theorem.",
        "anchors": "66-225; 231-342; 396-519; 611-739; 1024-1110; 1173-1190",
    },
    "NavierStokes/BaseResidual.lean": {
        "clusters": ["residual", "cartesian-assembly", "moments", "axis", "jets"],
        "finding": "Constructs the actual asymptotic slow-base sums, Cartesian potential/velocity prefixes, spatial-curl rate bounds, pressure prefixes, and growth/axis estimates. It proves substantial sum-to-curl and rate infrastructure, but no final radial barMoment evaluation for the selected whole-space field.",
        "anchors": "36-116; 611-666; 708-739; 776-826; 842-910; 1024-1110; 1173-1190",
    },
    "NavierStokes/SlowBorelBase.lean": {
        "clusters": ["profiles", "residual", "cartesian-assembly", "jets", "moments", "pressure"],
        "finding": "Constructs the smooth slow asymptotic series, finite-prefix and tail bounds, derivative/sum-map infrastructure, and coefficient data including pressure/stress. These are genuine base-layer results; the inspected declarations do not state the selected Cartesian field's final five-observable tuple.",
        "anchors": "23-50; 72-232; 292-375; 381-468; 810-871; 1043-1147",
    },
    "NavierStokes/SlowResidualMatching.lean": {
        "clusters": ["residual", "profiles", "moments", "pressure", "axis", "jets"],
        "finding": "Provides slow residual/stress primitives, radial identities, finite truncation and tail decompositions, and explicit stress equalities. The result remains at the reduced slow-profile layer; no selected whole-space Cartesian moment value is exported.",
        "anchors": "47-152; 175-250; 267-333; 392-618; 833-1144; 1204-1381",
    },
    "NavierStokes/SignedStressPrimitive.lean": {
        "clusters": ["moments", "pressure", "axis", "cartesian-assembly", "rank"],
        "finding": "Constructs compact signed bumps with exact weighted moment cancellation and proves physical pullback, torus-support, and chart finite-jet properties. These are concrete local correction identities, not a final selected-endpoint equality after every assembly operation.",
        "anchors": "20-149; 159-311; 692-804; 857-920; 1159-1234",
    },
    "NavierStokes/UniformAngularReset.lean": {
        "clusters": ["moments", "rank", "pressure", "profiles"],
        "finding": "Proves uniform invertibility of the two-bump angular moment system, a smooth reset branch, and scheduled damping/endpoint identities. It verifies the profile/history correction layer, not the final selected Cartesian five-moment value.",
        "anchors": "25-80; 142-191; 273-364; 438-480; 922-937; 1001-1052; 1251-1342",
    },
    "NavierStokes/MeanChartCompatibility.lean": {
        "clusters": ["moments", "rank", "cartesian-assembly", "pressure", "axis", "time"],
        "finding": "Proves scaling and pullback/naturality identities for cutoffs, torus averages, pressure, temporal families, source moments, and debt/rank data. It narrows the transport gap but does not compose the final selected ASum/BSum/PSum field with the five paper observables.",
        "anchors": "22-189; 314-414; 427-574; 609-651; 763-900; 1209-1338",
    },
    "NavierStokes/ActualParticularDynamics.lean": {
        "clusters": ["cartesian-assembly", "residual", "axis", "rank", "jets"],
        "finding": "Constructs actual selected primary carriers, transported coordinates, harmonic residual blocks, divergence-free sums, and common-cover cancellation identities. The dynamics layer proves local mode/residual structure, not the final selected radial five-moment value.",
        "anchors": "26-239; 454-573; 1462-1481; 1509-1534; 1547-1625",
    },
    "NavierStokes/LocalRankDefect.lean": {
        "clusters": ["rank", "moments", "corrections", "axis"],
        "finding": "Defines local-shell and local-rank operators on the open slow domain, proves local smoothness/divergence properties, and derives zero `barMoment` rows for rank increments and updated local means. These conclusions are explicitly local correction identities and are not evaluations of the final selected Cartesian field.",
        "anchors": "25-213; 430-464; 590-608; 743-808",
    },
    "NavierStokes/TerminalCompensation.lean": {
        "clusters": ["moments", "pressure", "profiles", "corrections"],
        "finding": "Constructs three separated compact bumps, proves weighted integrability and a uniform compensation map, and identifies physical positive-radius moment changes and cancellation. This is a terminal profile compensation layer; it does not export the selected whole-space field's final five-observable tuple.",
        "anchors": "24-181; 217-260; 700-760; 907-1009",
    },
    "NavierStokes/SlowExpansionResidual.lean": {
        "clusters": ["residual", "profiles", "axis", "moments", "jets"],
        "finding": "Expands finite slow products and convolutions exactly, exposes finite remainders, proves coefficient cancellation criteria, divergence-free slow velocity, and the reduced Cartesian residual reconstruction away from the axis. It remains a reduced finite-expansion result, not a selected `tsum`-to-radial moment theorem.",
        "anchors": "24-246; 285-330; 769-850; 908-995",
    },
    "NavierStokes/StateReindex.lean": {
        "clusters": ["cartesian-assembly", "residual", "moments", "axis", "pressure"],
        "finding": "Proves isometric pullback of fields, derivatives, correction states, residual operators, and auxiliary torus/radial integrals under coordinate reindexing. These naturality identities preserve the reindexing interface but do not compute the selected endpoint's five moments.",
        "anchors": "23-175; 108-159; 500-590; 650-727; 742-794",
    },
    "NavierStokes/ActualInitialization.lean": {
        "clusters": ["physical-data", "cartesian-assembly", "corrections", "rank", "residual"],
        "finding": "Builds the actual initial correction state from selected primary pieces, exact pressure and Gaussian blocks, support facts, mean/debt data, zero-mass and covariance invariants, and initial divergence/residual properties. It is a populated initial-state layer, not the final selected-field five-observable theorem.",
        "anchors": "31-190; 1132-1246; 1354-1427; 1471-1512",
    },
    "NavierStokes/FinalSlowBase.lean": {
        "clusters": ["profiles", "moments", "pressure", "residual", "axis", "cartesian-assembly"],
        "finding": "Constructs the aligned slow base, weighted/stress identities, support and exterior vanishing, completed velocity/pressure, and terminal extension. It proves selected base and exterior behaviour, but does not compute the final Cartesian field's full five-moment tuple after all later assembly operations.",
        "anchors": "26-166; 223-280; 335-380; 433-482; 495-600; 627-639",
    },
    "NavierStokes/R3/ActualCandidate.lean": {
        "clusters": ["endpoint", "r3", "pressure", "energy", "cartesian-assembly"],
        "finding": "Packages the localized velocity, pressure, and smooth positive-time force into R3 CandidateProperties, including compact support, residual equality, uniform finite energy, and the selected C/D statements. The wrapper confirms the endpoint contract but contains no five-moment or absolute pressure-semantics field.",
        "anchors": "24-121; 124-153",
    },
    "NavierStokes/TerminalStress.lean": {
        "clusters": ["pressure", "moments", "residual", "axis", "profiles"],
        "finding": "Defines terminal heat-tail and backward-stress operations, proves radial residual, positivity, boundary, flattening, and terminal-stress identities. Its module comment explicitly separates backward stress from the separate global moment condition; this is a profile stress layer, not the final selected-field transport theorem.",
        "anchors": "23-112; 147-206; 226-268; 340-453; 640-778; 805-945",
    },
    "NavierStokes/MeanResidual.lean": {
        "clusters": ["residual", "moments", "pressure", "cartesian-assembly", "axis"],
        "finding": "Defines normalized angular averaging and proves exact mean balances, Cartesian residual/divergence identities, periodic invariance, and covariance/error retention. These are genuine averaged equations for represented components; the inspected declarations do not identify the selected global field with the paper's five cumulative observables.",
        "anchors": "24-229; 790-915; 1021-1091; 1132-1154",
    },
    "NavierStokes/ProblemStatement.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "pressure", "energy", "force"],
        "finding": "Defines the exact formal candidate contract: smoothness, periodicity, support, divergence, residual equality, energy, initial value, and speed blow-up. It explicitly states no existence is asserted in this module and contains no five-moment, absolute-pressure, or force-independence predicate.",
        "anchors": "42-120; 140-159",
    },
    "NavierStokes/PeriodizedWaveBounds.lean": {
        "clusters": ["cartesian-assembly", "jets", "force", "profiles", "time"],
        "finding": "Proves local-finite support-cell and copy-sum germ, support, jet, and whole-lift bounds, including cutoff derivative/source terms. These results control periodised wave sums but do not evaluate the selected field's radial five moments.",
        "anchors": "30-183; 188-289; 303-344",
    },
    "NavierStokes/GaugeMomentBalances.lean": {
        "clusters": ["moments", "pressure", "rank", "cartesian-assembly"],
        "finding": "Defines the measured pressure coefficient as an actual scaled second moment and proves moving-gauge pressure moment identities. Its LocalField structure records regularity, support, and periodicity as hypotheses distinct from moment equations; no final selected-field tuple is exported.",
        "anchors": "24-102; 151-186; 184-207",
    },
    "NavierStokes/BaseExterior.lean": {
        "clusters": ["profiles", "pressure", "residual", "moments", "axis"],
        "finding": "Constructs the canonical radial heat exterior and pressure, proves smoothness, integrability, residual zero, and exterior stream/velocity/pressure identities. Its exterior coefficient interface explicitly separates coefficient vanishing from a hypothesis about the summed velocity or residual; it is not the final global moment transport theorem.",
        "anchors": "30-156; 164-240; 278-314; 328-338",
    },
    "NavierStokes/ActualBaseResidual.lean": {
        "clusters": ["residual", "cartesian-assembly", "axis", "pressure", "jets"],
        "finding": "Proves residual germ congruence and invariance, coordinate/chart identities, and defines scaled base pressure, error, velocity, and stress fields with smoothness claims. This is a real fixed-base Cartesian/chart residual layer, not an evaluation of the final selected five observables.",
        "anchors": "28-113; 116-218; 247-317; 332-384; 479-507",
    },
    "NavierStokes/SpatialLocalization.lean": {
        "clusters": ["cartesian-assembly", "pressure", "axis", "jets"],
        "finding": "Proves smooth compact cutoff support, expands curl(cutoff·potential) with an explicit cutoff-gradient commutator, then periodises and proves local equality, periodicity, divergence-free velocity, and residual equality. It supplies transformation identities but not a radial-moment value after those transformations.",
        "anchors": "10-14; 164-203; 209-290; 313-340",
    },
    "NavierStokes/SolenoidalDiagonal.lean": {
        "clusters": ["cartesian-assembly", "jets", "axis", "time"],
        "finding": "Defines locally finite cut stages, potentialSum and velocitySum, proves eventual finite-prefix equality, smoothness, all-jet local equality, spatial-curl divergence freedom, and finite-prefix velocity identities. These results establish the sum-to-curl regularity route, not a radial five-observable evaluation.",
        "anchors": "32-37; 46-93; 107-180; 188-263; 271-315",
    },
    "NavierStokes/MixedPeriodicAssembly.lean": {
        "clusters": ["cartesian-assembly", "endpoint", "residual", "axis", "time"],
        "finding": "Builds periodicVelocity and periodicResidual from spatially localised fields, proves local equality to cut fields, divergence freedom, residual jet transfer, boundary limits, speed unboundedness, and candidate-force packaging. It does not compute the final selected field's five paper observables.",
        "anchors": "28-106; 119-164; 179-245; 267-368; 388-401",
    },
    "NavierStokes/CorrectionState.lean": {
        "clusters": ["corrections", "rank", "moments", "residual", "pressure"],
        "finding": "Defines concrete correction states, angular covariances, radial pressure moments, reconstructed radial residuals, and rank-model FiveRows for correction functions. These are state and correction-layer identities, not a theorem for the final selected Cartesian field.",
        "anchors": "31-78; 211-250; 256-355; 405-492",
    },
    "NavierStokes/HeatTailEdit.lean": {
        "clusters": ["profiles", "moments", "pressure", "residual", "jets"],
        "finding": "Defines smooth heat-tail switching/edit factors and proves weighted integrability, pressure, energy, and angular debt bounds together with outgoing profile factorisation and jet control. This is a radial tail/profile layer, not the final selected Cartesian moment transport.",
        "anchors": "41-185; 297-355; 387-529; 545-653",
    },
    "NavierStokes/ActualMeanPhysicalData.lean": {
        "clusters": ["physical-data", "moments", "rank", "pressure", "jets", "cartesian-assembly"],
        "finding": "Builds actual atlas/state overlap data and transports initial, temporal, gauge, rank, pressure, and native-jet identities across cycle stages. The inspected declarations connect physical data to stage construction, but do not export the final selected Cartesian five-observable equality.",
        "anchors": "29-193; 204-305; 311-440; 579-742; 784-902",
    },
    "NavierStokes/OffplaneCorrectionExtensions.lean": {
        "clusters": ["corrections", "pressure", "rank", "cartesian-assembly", "jets"],
        "finding": "Extends slow pressure/rank models from positive-radius local windows to supported Cartesian continuation data and proves smoothness, agreement, support, and shrinking support. The extension route supplies local continuation lemmas but no selected-field radial moment equality.",
        "anchors": "21-203; 217-327; 339-455; 730-812; 875-1060",
    },
    "NavierStokes/SlowBaseEndpoint.lean": {
        "clusters": ["profiles", "cartesian-assembly", "axis", "jets", "pressure"],
        "finding": "Lifts nominal profile and potential data to smooth Cartesian extensions, proves away-from-axis extension properties, and exposes final field extensions for a profile witness. The endpoint declarations remain extension/germ statements and do not calculate the selected whole-space five observables.",
        "anchors": "44-181; 226-258; 292-356; 421-438",
    },
    "NavierStokes/ConstructedSlowBase.lean": {
        "clusters": ["profiles", "moments", "cartesian-assembly", "residual", "axis", "jets"],
        "finding": "Builds a genuine axisymmetric potential and its spatial curl, derives finite coefficient identities, stress-zero-core facts, jet flatness, smoothness, divergence freedom, speed growth, and residual identities for nominal and modified scales. These are substantial construction results, but their theorem outputs are not a final selected-field-to-five-moment transport statement.",
        "anchors": "40-53; 65-113; 145-188; 210-329; 339-438; 616-697; 714-770; 828-931",
    },
    "NavierStokes/BasePrefixIdentity.lean": {
        "clusters": ["profiles", "moments", "cartesian-assembly", "residual", "pressure"],
        "finding": "Derives finite-prefix curl/profile, radial flux, pressure, stress-force, and finite identity bridges from coefficient matches. The explicit finite-prefix bridge is positive evidence for intermediate correspondence, while the selected infinite localized Cartesian moment evaluation remains a separate unproved composition.",
        "anchors": "23-157; 217-260; 270-319; 341-383",
    },
    "NavierStokes/ActualReferenceRebase.lean": {
        "clusters": ["residual", "physical-data", "corrections", "cartesian-assembly", "jets"],
        "finding": "Proves rebase/pullback identities for actual stage assembly contexts, residual sources, frames, directions, amplitudes, pressures, phases, and periodic subcover transport. It establishes parameter/state reindexing correspondence, not the selected Cartesian five-moment observable equality.",
        "anchors": "77-146; 260-336; 560-625; 787-834; 877-932; 1062-1091",
    },
    "NavierStokes/HarmonicWaveInteraction.lean": {
        "clusters": ["corrections", "residual", "rank", "jets", "cartesian-assembly"],
        "finding": "Formalises harmonic blocks, zero modes, convolution transport, nonlinear interaction updates, divergence coefficients, and residual-difference blocks. It proves local wave/interaction algebra and zero-mode behaviour, but does not export final-field radial moment transport.",
        "anchors": "107-235; 277-386; 440-576; 605-789; 839-880; 917-1116",
    },
    "NavierStokes/ActualPrimaryDynamics.lean": {
        "clusters": ["cartesian-assembly", "residual", "axis", "jets", "corrections"],
        "finding": "Derives actual primary pulse geometry, copied velocity/pressure germs, cutoff/curl smoothness, local linear identities, and residual formulas for the primary pieces. It is a real local Cartesian residual route, not a proof that the final selected field transports the five paper moments.",
        "anchors": "57-177; 249-343; 429-529; 963-1144",
    },
    "NavierStokes/RankStateCoherence.lean": {
        "clusters": ["corrections", "rank", "moments", "pressure", "physical-data"],
        "finding": "Defines fibre moments, measured debt, rank-on predicates, radial/axial rank identities, normalized rank stages, and a FiveRows conclusion on correction/rank state slices. This strengthens the upstream correction evidence but still does not identify those rows with observables of the final selected Cartesian field.",
        "anchors": "26-74; 116-225; 248-336; 364-394; 428-452",
    },
    "NavierStokes/AxisymmetricResidual.lean": {
        "clusters": ["axis", "cartesian-assembly", "force", "jets", "moments", "pressure"],
        "finding": "Defines regular axisymmetric Cartesian velocity and pressure lifts and proves exact advection, derivative, Laplacian, pressure-gradient, divergence, and Navier-Stokes residual formulas, including the on-axis route. This is a genuine local residual bridge, not a final selected-field moment evaluation.",
        "anchors": "155-264; 274-350; 366-408; 417-432",
    },
    "NavierStokes/PhysicalParticularWave.lean": {
        "clusters": ["axis", "cartesian-assembly", "force", "jets", "pressure"],
        "finding": "Builds particular-wave raw carriers, potentials, curls, pressures, chart changes, periodicity, smoothness, and reference-domain transport identities. Its reference domains and local carrier declarations stop short of evaluating the final selected Cartesian five-observable tuple.",
        "anchors": "31-120; 246-300; 367-443; 519-697",
    },
    "NavierStokes/LeadingStress.lean": {
        "clusters": ["axis", "force", "jets", "moments", "pressure"],
        "finding": "Derives leading angular and axial stress divergences, pressure derivatives, radial pullback identities, physical stress scaling, and residual transport on regular positive-radius profile domains. These are reduced stress-to-residual bridges, not selected whole-space moment transport.",
        "anchors": "33-224; 258-309; 363-421; 458-519",
    },
    "NavierStokes/LiftedMeanResidual.lean": {
        "clusters": ["cartesian-assembly", "force", "jets", "pressure"],
        "finding": "Defines angular averaging and proves smooth parameter integration, periodic invariance, conservative flux identities, averaged Laplacian/gradient relations, and nonlinear residual lifting. This supplies a real mean-residual route, but not the final selected radial barMoment equality.",
        "anchors": "25-113; 128-198; 201-265; 350-431; 472-508; 625-675",
    },
    "NavierStokes/LinearWaveBounds.lean": {
        "clusters": ["axis", "cartesian-assembly", "force", "jets", "pressure", "rank", "time"],
        "finding": "Defines actual wave coefficients, cutoff/curl corrections, input bounds, wave classes, exact conditions, and coefficient-level harmonic residual identities. Its input-bound structures explicitly separate rate estimates from residual identities and contain no final selected radial moment observable.",
        "anchors": "93-184; 176-269; 270-392; 444-556; 630-675",
    },
    "NavierStokes/ActualPhysicalStageBounds.lean": {
        "clusters": ["cartesian-assembly", "pressure", "rank"],
        "finding": "Derives physical-stage smoothness, support, jet, potential, pressure, and gain bounds from coherent mean and wave inputs, then packages cycle inputs and stage fields. This is a substantive stage-bound layer, not the final selected-field five-moment equality.",
        "anchors": "24-115; 130-158; 171-269; 274-302",
    },
    "NavierStokes/ActualSignedWaveData.lean": {
        "clusters": ["cartesian-assembly", "force", "jets", "pressure"],
        "finding": "Builds active/inactive support cells, potential and pressure copy families, carrier bounds, source amplitudes, frequency identities, and native stage data for the signed physical family. The inspected declarations establish carrier-level construction and germs, not final selected Cartesian moment transport.",
        "anchors": "29-56; 119-240; 251-365; 373-456",
    },
    "NavierStokes/PrimaryResidualClass.lean": {
        "clusters": ["cartesian-assembly", "corrections", "force", "jets", "pressure", "rank"],
        "finding": "Defines primary correction inputs, invariant angular data, curl-corrected wave classes, exact conditions, divergence, linear residual, field projection, and smooth primary velocity/pressure coefficients. It proves coefficient-level primary identities, not the final selected-field radial observable tuple.",
        "anchors": "36-169; 173-309; 344-419; 430-565",
    },
    "NavierStokes/ActualInitialMeanEquation.lean": {
        "clusters": ["axis", "cartesian-assembly", "force", "jets", "moments", "pressure", "time"],
        "finding": "Builds the initialized angular data and proves local mean/divergence, periodicity, mean-zero, primary-sum divergence, and initialized full-divergence identities. These are genuine initial-mean and Cartesian stage bridges, not the final selected-field transport of (M,I,J,S,C_p).",
        "anchors": "41-91; 104-166; 265-332; 337-431; 462-632",
    },
    "NavierStokes/CyclePhysicalPrefixes.lean": {
        "clusters": ["cartesian-assembly", "force", "jets", "pressure", "rank", "time"],
        "finding": "Defines cylindrical and local Cartesian velocity/pressure maps, step updates, finite stage prefixes, potential/direct splits, and local residual-prefix identities. The prefix theorems require individual curl-realisation hypotheses and do not establish infinite selected-field moment transport.",
        "anchors": "32-141; 149-214; 216-308; 315-458",
    },
    "NavierStokes/FiveProfileMoments.lean": {
        "clusters": ["jets", "moments", "rank", "pressure"],
        "finding": "Defines the five-coordinate profile debt and proves integrability, exact linear moment maps, continuous-linear equivalence, normalized debt, compact correction families, and jet bounds. This is a real reduced-profile repair layer; no theorem inspected here identifies its moments with the final selected Cartesian field.",
        "anchors": "1-120; 121-240; 569-651; 780-805; 1115-1200",
    },
    "NavierStokes/AngularMomentReset.lean": {
        "clusters": ["axis", "moments", "pressure", "rank"],
        "finding": "Constructs compact translated bump pairs and proves an invertible two-parameter angular/pressure moment reset, pressure-neutral branches, support, positivity, and exact endpoint moment adjustment. This is a local reduced reset mechanism, not a selected Cartesian radial-observable theorem.",
        "anchors": "20-169; 197-279; 298-436; 542-601; 656-766",
    },
    "NavierStokes/R3/CandidateBreakdown.lean": {
        "clusters": ["endpoint", "r3", "energy", "force"],
        "finding": "Derives non-agreement with every smooth global finite-energy competitor from compact support, speed unboundedness, and whole-space comparison; also derives a uniform L2 square bound from CandidateProperties. This establishes the R3 C/D consequence under the formal contract, not the missing five-observable transport or an absolute pressure representation.",
        "anchors": "18-40; 43-64; 66-81",
    },
    "NavierStokes/ActualPrimaryBounds.lean": {
        "clusters": ["cartesian-assembly", "jets", "pressure", "time"],
        "finding": "Builds actual primary signed labels, moving envelopes, native velocity/pressure jet bounds, periodised copy sums, cutoff copy identities, and chart-level uniform wave classes. These estimates support the concrete stage construction but do not compute a final selected Cartesian five-moment value.",
        "anchors": "40-91; 287-305; 439-499; 732-832",
    },
    "NavierStokes/ActualSlowAxis.lean": {
        "clusters": ["axis", "profiles", "pressure", "jets", "time"],
        "finding": "Constructs holomorphic/natural slow-axis profile elements, proves real-domain regularity, base values, positive-order equations on the collar, initial and stock field identities, smooth profiles, axis vanishing, and axis-jet formulas. This is a reduced profile/axis route, not the selected Cartesian observable transport.",
        "anchors": "24-70; 104-221; 287-357; 361-485",
    },
    "NavierStokes/MovingMomentBounds.lean": {
        "clusters": ["moments", "rank", "pressure", "residual", "profiles"],
        "finding": "Proves moving-strip pressure-mass and radial-moment class bounds, support closure under differential operators, and rank-stage defect classes under explicit local geometry and increment hypotheses. These are local moving-profile and correction estimates, not a final selected whole-space five-observable equality.",
        "anchors": "30-104; 118-228; 298-359",
    },
    "NavierStokes/R3/PressureTestBounds.lean": {
        "clusters": ["pressure", "r3", "energy"],
        "finding": "Proves Fourier weighted Cauchy-Schwarz estimates, H3 control, derivative and Riesz-test bounds, and one uniform constant for pressure-recovery test functionals. This supports comparative pressure analysis; it is not an absolute selected-pressure Poisson representation.",
        "anchors": "20-79; 86-116; 118-253",
    },
    "NavierStokes/ActualPrimaryCoherence.lean": {
        "clusters": ["cartesian-assembly", "axis", "jets", "pressure", "time"],
        "finding": "Constructs actual primary Cartesian potentials and velocities from periodic chart data, proves smoothness, axis-zero germs, positive-radius global potential representation, periodisation, and piece-to-Cartesian curl identities. These are concrete local-to-Cartesian bridges, but no final selected tsum-to-(M,I,J,S,C_p) equality is exported.",
        "anchors": "1722-1804; 1866-1902; 1905-1950",
    },
    "NavierStokes/MeanMomentBounds.lean": {
        "clusters": ["moments", "pressure", "jets", "cartesian-assembly"],
        "finding": "Proves smoothness, support, finite-jet bounds, torus-average reduction, radial weighting, pressure-mass identities, and radial-moment slow-class bounds. The moment operators are explicitly connected to torus averages at this layer, but the selected whole-space Cartesian field is not evaluated through them here.",
        "anchors": "283-304; 426-450; 467-498",
    },
    "NavierStokes/PhysicalSignedWave.lean": {
        "clusters": ["cartesian-assembly", "pressure", "jets", "time"],
        "finding": "Defines signed physical potentials, velocities, pressure modes, cutoffs, periodicity, smoothness, and literal Cartesian-curl representations for wave and primary-wave components. It proves component-level transport from chart data, not a final selected-field radial observable or five-moment equality.",
        "anchors": "1040-1128; 1266-1304; 1380-1425",
    },
    "NavierStokes/GlobalSlowProfiles.lean": {
        "clusters": ["profiles", "moments", "pressure", "cartesian-assembly"],
        "finding": "Builds reduced even profiles, mass/pressure histories, cutoff lifts, and exterior identities. The domain is the reduced profile layer; the inspected declarations do not establish the selected Cartesian tsum-to-barMoment transport.",
        "anchors": "26-66; 167-205; 281-334; 337-400; 479-569",
    },
    "NavierStokes/TerminalPressure.lean": {
        "clusters": ["pressure", "energy", "axis"],
        "finding": "Defines and proves smoothness, integrability, and derivative identities for the canonical terminal heat-tail pressure on its presingular positive-radius domain. This is a physical pressure construction layer, not an absolute global Poisson theorem for the final selected whole-space field.",
        "anchors": "39-145; 149-239; 406-519; 604-627",
    },
    "NavierStokes/PressureRecoveryHelpers.lean": {
        "clusters": ["pressure", "r3"],
        "finding": "Provides compact-test pressure-Poisson identities for comparison hypotheses; it is not an absolute selected-pressure representative.",
        "anchors": "114-150",
    },
    "NavierStokes/PressureRecovery.lean": {
        "clusters": ["pressure", "r3", "uniqueness"],
        "finding": "Provides relative pressure-difference recovery; it does not introduce a selected physical pressure representative on Schwartz tests.",
        "anchors": "257-305; 388-438",
    },
    "NavierStokes/RieszTestOperators.lean": {
        "clusters": ["pressure", "r3"],
        "finding": "Provides a canonical pressure functional/test-function Poisson identity; selected-field absolute semantics require a separate bridge.",
        "anchors": "277-301",
    },
    "NavierStokes/R3/CompactEnergy.lean": {
        "clusters": ["energy", "r3"],
        "finding": "Contains forced energy identities, derivative form, and uniform finite-energy bounds.",
        "anchors": "201-249; 321-352",
    },
    "NavierStokes/R3/Theorem.lean": {
        "clusters": ["endpoint", "r3", "energy"],
        "finding": "Exports the C/D theorem with candidate properties, nonexistence of global finite-energy competitor, and energy/dissipation bounds.",
        "anchors": "66-79",
    },
    "NavierStokes/PhysicalResidualJetBounds.lean": {
        "clusters": ["jets", "axis", "cartesian-assembly"],
        "finding": "Contains off-axis chart and jet-rate bounds; off-axis and origin routes are separate semantic domains.",
        "anchors": "927-965",
    },
    "NavierStokes/GlobalBaseError.lean": {
        "clusters": ["jets", "axis", "time"],
        "finding": "Provides an origin-past vanishing-jet route; this does not by itself transport off-axis chart observables to the axis.",
        "anchors": "200-237",
    },
    "Euler/EulerSingularity.lean": {
        "clusters": ["euler"],
        "finding": "Euler evolution and finite-lifespan/singularity declarations are separate from the Navier-Stokes endpoint.",
        "anchors": "26-33; 47-151",
    },
    "Euler.lean": {
        "clusters": ["euler", "repository-root"],
        "finding": "Repository Euler entry point; imports Euler.EulerSingularity and is separate from the captured Navier-Stokes R3 endpoint closure.",
        "anchors": "1",
    },
    "Euler/AngleMeanZeroPrimitive.lean": {
        "clusters": ["euler", "periodicity", "integrals"],
        "finding": "Defines raw and mean-subtracted angular primitives and proves derivative, continuity, periodicity, zero-mean, and uniqueness results. This is genuine Euler infrastructure, not a Navier-Stokes endpoint moment transport theorem.",
        "anchors": "22-26; 29-47; 49-78",
    },
    "Euler/AnglePrimitiveBounds.lean": {
        "clusters": ["euler", "bounds"],
        "finding": "Proves raw and normalised angular primitive bounds under continuity and period assumptions; no selected Navier-Stokes field is present.",
        "anchors": "14-32",
    },
    "Euler/AnglePrimitiveKernel.lean": {
        "clusters": ["euler", "integrals", "periodicity"],
        "finding": "Proves a translation-kernel representation for the normalised angular primitive from periodicity and zero-mean assumptions.",
        "anchors": "14-25",
    },
    "Euler/AnglePrimitiveMap.lean": {
        "clusters": ["euler", "functional-analysis"],
        "finding": "Proves continuous-linear-map compatibility for raw and normalised angular primitives.",
        "anchors": "14-21",
    },
    "Euler/AnglePrimitiveParity.lean": {
        "clusters": ["euler", "symmetry"],
        "finding": "Proves negation and reflection identities for the angular primitive.",
        "anchors": "14-31",
    },
    "Euler/AnglePrimitiveSpatialRegularity.lean": {
        "clusters": ["euler", "regularity"],
        "finding": "Proves joint continuity and ContDiff for parameterised angular primitives; no Cartesian-to-radial Navier-Stokes transport is stated.",
        "anchors": "18-65",
    },
    "Euler/AnglePrimitiveTranslation.lean": {
        "clusters": ["euler", "translation"],
        "finding": "Proves translation of the normalised angular primitive under periodic zero-mean forcing.",
        "anchors": "13-23",
    },
    "Euler/AsymmetricTransport.lean": {
        "clusters": ["euler", "transport", "sobolev"],
        "finding": "Defines the Sobolev asymmetric transport operator and proves its coordinate formula, background equality, application bound, and operator norm bound.",
        "anchors": "20-31; 36-68",
    },
    "Euler/BaseEulerDatum.lean": {
        "clusters": ["euler", "cartesian-assembly", "support", "solenoidal"],
        "finding": "Builds compactly supported smooth Euler velocity data as a curl of a cut-off potential and proves support, divergence-free, oddness, plateau, L2, and solenoidal properties.",
        "anchors": "16-41; 43-77",
    },
    "Euler/BaseEulerLabelData.lean": {
        "clusters": ["euler", "bounds", "labels"],
        "finding": "Constructs label costs and proves displacement, velocity, and acceleration label bounds before packaging LabelData.",
        "anchors": "16-40; 42-82",
    },
    "Euler/BaseEulerParity.lean": {
        "clusters": ["euler", "symmetry", "parent-data"],
        "finding": "Propagates oddness of the input field to parent displacement data; this is an Euler parent/packet symmetry result.",
        "anchors": "15-22",
    },
    "NavierStokesReview/src/audit/priority_external_euler_foundation_source_review_2026-09-28.md": {
        "clusters": ["euler", "repository-scope", "source-review"],
        "finding": "Direct source review of the Euler foundation tranche. It separates repository-root scope from the captured Navier-Stokes endpoint and records no admission tokens in the 11 inspected modules.",
        "anchors": "1-116",
    },
    "Euler/IntervalPathConcatenation.lean": {
        "clusters": ["euler", "time"],
        "finding": "Contains seam value/derivative matching; a raw indexed mismatch is not evidence of a temporal PDE kink without a further smoothness failure theorem.",
        "anchors": "13-118",
    },
    "NavierStokesReview/src/completions/SelectedMixedProductionBarMoment.lean": {
        "clusters": ["moments", "cartesian-assembly"],
        "finding": "Defines the selected mixed scalar pullback and proves its typed barMoment interface; it explicitly does not assert a zero/nonzero value or identify the mixed scalar with either branch.",
        "anchors": "5-12; 34-59",
    },
    "NavierStokesReview/src/completions/SelectedMixedProductionTorusAverage.lean": {
        "clusters": ["moments", "cartesian-assembly"],
        "finding": "Proves the auxiliary torus-average reduction to a radial-section integral. The resulting weighted integral is exposed, not evaluated.",
        "anchors": "25-44",
    },
    "NavierStokesReview/src/completions/PeriodicGlobalIntegral.lean": {
        "clusters": ["moments", "cartesian-assembly"],
        "finding": "Proves a conditional zero using non-integrability and Mathlib integral_undef under a strict positivity premise. The premise is not established for the selected pullback, so this is not the physical selected-field moment value.",
        "anchors": "5-13; 31-75",
    },
    "NavierStokesReview/src/completions/SelectedCartesianRadialGate.lean": {
        "clusters": ["cartesian-assembly", "axis", "moments"],
        "finding": "Recovers a mean field from one Cartesian component only under a positive-radius/nonzero-component hypothesis. It does not provide a global axis-safe radial transport theorem.",
        "anchors": "4-10; 20-46",
    },
    "NavierStokesReview/src/completions/SelectedMixedRadialSupportObstruction.lean": {
        "clusters": ["moments", "cartesian-assembly"],
        "finding": "Records that the selected mixed radial pullback is periodic and that bounded radial support would force it to vanish. It does not supply the bounded-support premise for the selected endpoint.",
        "anchors": "5-13; 31-47",
    },
    "NavierStokesReview/src/completions/PeriodicRadialSupportObstruction.lean": {
        "clusters": ["moments", "cartesian-assembly"],
        "finding": "Proves the generic periodic-plus-bounded-radial-support obstruction. It is a conditional theorem and does not identify the R3 compact-support field with the selected periodic radial pullback.",
        "anchors": "26-74",
    },
    "NavierStokesReview/src/completions/SelectedR3PackagingBoundary.lean": {
        "clusters": ["candidate-packaging", "moments"],
        "finding": "Shows that the R3 CandidateProperties contract can coexist with an external nonzero five-coordinate payload. It does not evaluate the selected field's moments.",
        "anchors": "5-49",
    },
    "NavierStokesReview/src/refutations/CTR005ProfileTailCollisionScope.lean": {
        "clusters": ["moments", "rank", "candidate-packaging"],
        "finding": "Confirms FiveRows constrains correction increments and that selected cycle zero rows are not automatically total Cartesian moments. It records a conditional obstruction, not selected-path False.",
        "anchors": "7-68",
    },
    "NavierStokesReview/src/refutations/SelectedPeriodicSupportTransportGate.lean": {
        "clusters": ["moments", "cartesian-assembly", "candidate-packaging"],
        "finding": "Binds the actual selected mixed radial pullback to the exact support-transport and nonzero-value premises that would yield False from periodicity. It proves only the conditional gate; neither premise is asserted for the current endpoint.",
        "anchors": "5-24; 31-60",
    },
    "NavierStokesReview/src/completions/SelectedMixedMomentResidualDecomposition.lean": {
        "clusters": ["moments", "cartesian-assembly", "candidate-packaging"],
        "finding": "Reduces the selected mixed order-two barMoment to the selected potential branch only under explicit Shell hypotheses and a zero selected direct-branch premise. It does not substitute the native-stage zero theorem, evaluate the potential branch, or derive False.",
        "anchors": "1-68",
    },
    "NavierStokesReview/src/audit/priority_118_selected_mixed_residual_decomposition_2026-09-28.md": {
        "clusters": ["moments", "cartesian-assembly", "candidate-packaging"],
        "finding": "Documents the source-checked distinction between the native angular-stage zero moment and the actual periodised cut-potential direct branch, and records the compiler timeout honestly.",
        "anchors": "1-67",
    },
    "NavierStokesReview/src/completions/SelectedDirectCutoffMomentBoundary.lean": {
        "clusters": ["moments", "cartesian-assembly", "localisation"],
        "finding": "Records the exact selected direct-stage identity: the cut radial component differs from the native angular component by (spatialCutoff - 1) times the native component. It does not assert a nonzero integral or identify the periodised tsum with a finite stage.",
        "anchors": "1-71",
    },
    "NavierStokesReview/src/audit/priority_119_probe_logic_adversarial_review_2026-09-28.md": {
        "clusters": ["probe-logic", "moments", "cartesian-assembly", "candidate-packaging"],
        "finding": "Adversarially classifies existing probes by their actual hypotheses and conclusions, records prohibited inference rules, and separates interface non-determination from concrete selected-field evaluation.",
        "anchors": "1-92",
    },
    "NavierStokesReview/src/audit/priority_120_euler_transport_foundation_source_review_2026-09-28.md": {
        "clusters": ["euler", "transport", "regularity", "scope-classification"],
        "finding": "Reviews ten Euler-side foundation, commutator, Sobolev, word-metric, bounded-field, and coefficient-regularity modules. They are genuine repository-wide Euler infrastructure, outside the captured Navier-Stokes endpoint closure, and do not establish the selected Cartesian Navier-Stokes observable bridge.",
        "anchors": "1-68",
    },
    "Euler/BaseEulerSign.lean": {
        "clusters": ["euler", "sign", "guards"],
        "finding": "Proves Euler base source/frame identities and positivity guards; no Navier-Stokes selected-field transport theorem.",
        "anchors": "1-81",
    },
    "Euler/BaseEulerSobolev.lean": {
        "clusters": ["euler", "sobolev", "base-data"],
        "finding": "Constructs Euler base and solution Sobolev data; no selected Navier-Stokes observable transport.",
        "anchors": "1-43",
    },
    "Euler/BaseEulerUniform.lean": {
        "clusters": ["euler", "uniform-bounds", "jets"],
        "finding": "Defines Euler uniform amplitude, label, sup, jet, and Hq bounds; no final Navier-Stokes moment equality.",
        "anchors": "1-88",
    },
    "Euler/BaseSmoothState.lean": {
        "clusters": ["euler", "state", "initial-data"],
        "finding": "Defines an Euler initial state from bounded parameters and scale; no selected Navier-Stokes field or force bridge.",
        "anchors": "1-22",
    },
    "Euler/BaseTransportCommutator.lean": {
        "clusters": ["euler", "transport", "commutator", "bounds"],
        "finding": "Defines word commutators and proves recurrence and finite-order bounds for Euler transport words; no radial selected-field observable.",
        "anchors": "1-113",
    },
    "Euler/BaseTransportL2.lean": {
        "clusters": ["euler", "transport", "l2", "sobolev"],
        "finding": "Proves Euler finite-word gradient and L2 transport estimates; no connection to ActualCandidateAssembly.Witness.",
        "anchors": "1-82",
    },
    "Euler/BaseWordMetric.lean": {
        "clusters": ["euler", "word-metric", "sobolev"],
        "finding": "Defines finite word values and a metric with Sobolev comparison; no selected Navier-Stokes moment transport.",
        "anchors": "1-62",
    },
    "Euler/BoundedCoefficientSmooth.lean": {
        "clusters": ["euler", "coefficients", "regularity"],
        "finding": "Bundles bounded smooth coefficient fields and proves translation differentiability/smoothness; no final Navier-Stokes endpoint theorem.",
        "anchors": "1-101",
    },
    "Euler/BoundedEvaluationDifferentiation.lean": {
        "clusters": ["euler", "calculus", "bounded-evaluation"],
        "finding": "Proves a generic bounded-evaluation Fréchet derivative lemma; no selected field or radial integral.",
        "anchors": "1-70",
    },
    "Euler/BoundedFieldCalculus.lean": {
        "clusters": ["euler", "bounded-fields", "bilinear", "calculus"],
        "finding": "Defines bounded bilinear/composition/path/adjoint maps with norm controls; no CMI C/D or selected Navier-Stokes observable transport.",
        "anchors": "1-258",
    },
    "NavierStokesReview/src/audit/priority_121_euler_bounded_flow_analytic_source_review_2026-09-28.md": {
        "clusters": ["euler", "transport", "regularity", "calculus", "scope-classification"],
        "finding": "Reviews ten Euler-side bounded-field, Gram/Gevrey, flow, continuation, path-family, and classical-divergence modules. They are genuine repository-wide Euler infrastructure outside the captured Navier-Stokes closure; no selected Cartesian Navier-Stokes observable bridge is established.",
        "anchors": "1-70",
    },
    "Euler/BoundedFieldForwardGenerator.lean": {
        "clusters": ["euler", "operator-path", "regularity"],
        "finding": "Defines inverse and generator paths for bounded operator fields and proves path smoothness and bounds; no selected Navier-Stokes observable transport.",
        "anchors": "1-3; 16; 47-107",
    },
    "Euler/BoundedFieldGramGevrey.lean": {
        "clusters": ["euler", "gevrey", "regularity"],
        "finding": "Proves Gram-path bounds, Gevrey inverse-path regularity, and coefficient bounds; no radial barMoment or selected Navier-Stokes bridge.",
        "anchors": "1-4; 10; 41-125",
    },
    "Euler/BoundedFieldGramInverse.lean": {
        "clusters": ["euler", "bounded-fields", "regularity"],
        "finding": "Defines bounded Gram fields/inverses and proves continuity, norm, ring-inverse, and path smoothness results; no selected endpoint transport.",
        "anchors": "1-2; 15; 40-160",
    },
    "Euler/BoundedFieldMultilinear.lean": {
        "clusters": ["euler", "bounded-fields", "calculus"],
        "finding": "Lifts continuous multilinear maps to bounded fields and proves norm controls; no selected Cartesian field or radial observable.",
        "anchors": "1-2; 12; 23-83",
    },
    "Euler/BoundedFlowContinuity.lean": {
        "clusters": ["euler", "transport", "regularity"],
        "finding": "Proves flow distance/joint continuity and forward/backward flow regularity; no CMI C/D force or selected Navier-Stokes moment theorem.",
        "anchors": "1; 12; 17-93",
    },
    "Euler/BoundedInverseGevrey.lean": {
        "clusters": ["euler", "gevrey", "regularity"],
        "finding": "Proves Gevrey regularity for an inverse solution object; no selected Navier-Stokes branch transport.",
        "anchors": "1; 13; 23-31",
    },
    "Euler/BoundedLipschitzFlow.lean": {
        "clusters": ["euler", "transport", "regularity"],
        "finding": "Defines Lipschitz-flow data and proves curve existence, derivatives, uniqueness, cocycle, and distance estimates; no selected Navier-Stokes packaging.",
        "anchors": "1; 17; 21-116",
    },
    "Euler/BoundedMildContinuation.lean": {
        "clusters": ["euler", "transport", "continuation"],
        "finding": "Proves time-grid identities and global mild continuation from a bound; this is Euler-side infrastructure, not the R3 forced witness.",
        "anchors": "1; 7; 14-52",
    },
    "Euler/BoundedPathFamily.lean": {
        "clusters": ["euler", "bounded-fields", "calculus"],
        "finding": "Defines bounded slices and continuous bounded paths on compact time intervals with norm control; no radial observable.",
        "anchors": "1; 10; 23-52",
    },
    "Euler/ClassicalDivergence.lean": {
        "clusters": ["euler", "calculus", "cartesian-assembly"],
        "finding": "Proves a classical divergence-free identity under explicit hypotheses; it is not the selected Navier-Stokes curl/localisation chain.",
        "anchors": "1; 7; 16-28",
    },
    "NavierStokesReview/src/audit/priority_122_euler_operator_projection_source_review_2026-09-28.md": {
        "clusters": ["euler", "transport", "pressure", "calculus", "scope-classification"],
        "finding": "Reviews ten Euler translation, coefficient-path, operator-bound, compact-curl, parametric-integral, projected-law, projection-pairing, compact-smoothness, and compact-support modules. They are genuine Euler infrastructure outside the captured Navier-Stokes closure; no selected Cartesian observable bridge is established.",
        "anchors": "1-76",
    },
    "Euler/ClosedTranslationGraph.lean": {
        "clusters": ["euler", "transport", "regularity"],
        "finding": "Proves additive translation paths, derivative propagation, uniform orbit convergence, and closedness of a translation-derivative graph in Euler cylinder L2 space; no selected NS observable.",
        "anchors": "1; 16-18; 21-37; 40-50; 53-84",
    },
    "Euler/CoefficientPathOrbit.lean": {
        "clusters": ["euler", "regularity", "coefficients"],
        "finding": "Proves smoothness, derivative identities, orbit derivative paths, and coefficient-path norm bounds for bounded coefficient fields; no radial barMoment.",
        "anchors": "1; 21-23; 31-54; 56-95",
    },
    "Euler/CoefficientPathSobolev.lean": {
        "clusters": ["euler", "sobolev", "regularity"],
        "finding": "Defines Sobolev operators along coefficient paths and proves value, derivative, and continuity results; no selected NS endpoint transport.",
        "anchors": "1-2; 28-36; 43-94",
    },
    "Euler/CoerciveEndpointBounds.lean": {
        "clusters": ["euler", "bounds", "operator-path"],
        "finding": "Defines correction, endpoint, and form operators and proves operator norm/subtraction bounds; no selected Cartesian field.",
        "anchors": "1; 24-37; 40-119; 129-132",
    },
    "Euler/CompactCurlBounds.lean": {
        "clusters": ["euler", "cartesian-assembly", "bounds"],
        "finding": "Derives a compact-set Euler vorticity bound from spatial derivative bounds and the curl matrix operator; not the selected NS curl/localisation chain.",
        "anchors": "1-2; 19-30",
    },
    "Euler/CompactParameterIntegral.lean": {
        "clusters": ["euler", "calculus", "integrals"],
        "finding": "Defines a parameter derivative and proves differentiability and smooth parameter dependence of compact interval integrals; no five-moment transport.",
        "anchors": "1-4; 20-26; 29-51; 53-72",
    },
    "Euler/CompactProjectedEulerLaw.lean": {
        "clusters": ["euler", "pressure", "transport"],
        "finding": "Proves the weak projected Euler derivative identity on compact smooth solenoidal tests; no CMI C/D selected witness or NS radial tuple.",
        "anchors": "1-3; 32-51; 55-66",
    },
    "Euler/CompactProjectedPairing.lean": {
        "clusters": ["euler", "pressure", "integrals"],
        "finding": "Removes the Helmholtz projection in solenoidal pairings and derives integral forms for projected Euler right-hand sides; no selected NS pressure or radial tuple.",
        "anchors": "1; 21-26; 30-46; 49-65",
    },
    "Euler/CompactSmoothBounds.lean": {
        "clusters": ["euler", "regularity", "bounds"],
        "finding": "Relates spatial to joint derivatives and proves compact spatial/time derivative bounds for smooth Euler solutions; no selected NS packaging.",
        "anchors": "1-3; 22-30; 32-48",
    },
    "Euler/CompactSupportBoundedPath.lean": {
        "clusters": ["euler", "support", "bounded-fields"],
        "finding": "Bundles compactly supported continuous families as bounded-continuous-function paths and proves uniform-norm continuity; no radial observable.",
        "anchors": "1-2; 17-25; 29-55; 57-70",
    },
    "NavierStokesReview/src/audit/priority_123_selected_ns_paper_endpoint_junction_review_2026-09-28.md": {
        "clusters": ["endpoint", "moments", "cartesian-assembly", "global-assembly", "r3", "support"],
        "finding": "Reviews eight non-obvious Navier-Stokes endpoint junctions. Confirms real periodic corollary, support compression, physical stage/rate bounds, tsum potential data, and continuation invariants; no inspected declaration provides final selected Cartesian/periodic barMoment=(M,I,J,S,Cp) transport.",
        "anchors": "1-111",
    },
    "NavierStokesReview/src/audit/priority_124_selected_ns_dynamics_comparator_appendix_review_2026-09-28.md": {
        "clusters": ["endpoint", "moments", "cartesian-assembly", "global-assembly", "r3", "support"],
        "finding": "Reviews ten selected Navier-Stokes dynamics/comparator/appendix junctions. Confirms concrete dynamics, profile and joining bounds, finite local sums, comparator residual packages, endpoint jet hypotheses, and compact primitives; no inspected declaration provides final selected Cartesian barMoment=(M,I,J,S,Cp) transport.",
        "anchors": "1-122",
    },
    "NavierStokesReview/src/audit/selected_transport_audit.py": {
        "clusters": ["endpoint", "moments", "cartesian-assembly", "global-assembly"],
        "finding": "Hardened declaration-level audit instrument. It separates source co-occurrence triage from optional Lean-environment declaration types, records exact selected endpoint signatures, and refuses to promote co-occurrence or historical closure data into transport, defect, or False claims.",
        "anchors": "1-310",
    },
    "NavierStokesReview/evidence/selected_transport_audit_environment_2026-09-28.md": {
        "clusters": ["endpoint", "moments", "cartesian-assembly", "global-assembly"],
        "finding": "Historical Lean-environment cross-check over a review-side source root. It is not a current endpoint closure: the supplied snapshot is missing the configured selected endpoint roots, and snapshot freshness is not asserted.",
        "anchors": "generated report; source candidates and endpoint type rows",
    },
    "NavierStokesReview/src/audit/priority_125_probe_logic_hardening_2026-09-28.md": {
        "clusters": ["endpoint", "moments", "cartesian-assembly", "global-assembly"],
        "finding": "Documents the comment-stripped repository-wide selected-transport audit. It separates three positive manual-review pullback identities from conditional/interface probes and refuses transport, defect, or False claims.",
        "anchors": "1-105",
    },
    "NavierStokesReview/evidence/selected_transport_audit_full_2026-09-28.md": {
        "clusters": ["endpoint", "moments", "cartesian-assembly", "global-assembly"],
        "finding": "Full-workspace declaration triage after comment stripping: 34,583 declarations, 11 joint candidates, all 11 auditor-authored review completions, and no promoted transport/disproof result.",
        "anchors": "generated report; repository-wide source pass",
    },
    "NavierStokesReview/evidence/selected_transport_audit_full_2026-09-28.json": {
        "clusters": ["endpoint", "moments", "cartesian-assembly", "global-assembly"],
        "finding": "Machine-readable repository-wide selected-transport audit result; all escalation verdict flags remain false.",
        "anchors": "generated JSON; verdict object",
    },
    "NavierStokesReview/evidence/selected_transport_audit_openai_source_2026-09-28.md": {
        "clusters": ["endpoint", "moments", "cartesian-assembly", "global-assembly"],
        "finding": "OpenAI-source-only declaration triage over NavierStokes/: 31,472 declarations, zero joint candidates, and zero positive manual candidates under the detector. This is a provenance boundary and triage result, not an absence theorem.",
        "anchors": "generated report; source-only pass",
    },
    "NavierStokesReview/evidence/selected_transport_audit_openai_source_2026-09-28.json": {
        "clusters": ["endpoint", "moments", "cartesian-assembly", "global-assembly"],
        "finding": "Machine-readable OpenAI-source-only selected-transport audit; all escalation verdict flags remain false.",
        "anchors": "generated JSON; source-only verdict object",
    },
    "NavierStokesReview/src/audit/priority_126_selected_field_finite_prefix_transport_review_2026-09-28.md": {
        "clusters": ["endpoint", "moments", "cartesian-assembly", "global-assembly", "periodicity", "commutator"],
        "finding": "Reviews the concrete selected finite-prefix, curl, cutoff commutator, mixed-branch, torus-average, radial pullback, and periodicity chain. It records genuine selected-field transport while preserving the remaining tsum/global five-observable boundary.",
        "anchors": "1-103",
    },
    "NavierStokesReview/src/audit/priority_127_source_provenance_and_environment_integrity_review_2026-09-28.md": {
        "clusters": ["endpoint", "moments", "cartesian-assembly", "global-assembly"],
        "finding": "Separates full-workspace review completions from OpenAI NavierStokes source declarations and records the failed fresh environment export. It prevents auditor-authored completion theorems or stale closure data from being presented as OpenAI endpoint evidence.",
        "anchors": "1-54",
    },
    "NavierStokesReview/src/audit/probe_logic_contract_audit.py": {
        "clusters": ["endpoint", "moments", "cartesian-assembly", "global-assembly", "methodology"],
        "finding": "Audits review-authored probe declarations for provenance, conditional premises, interface/ghost payloads, fixed-force scope, and conclusion strength. It is a blindside detector, not a Lean proof or absence theorem.",
        "anchors": "1-275",
    },
    "NavierStokesReview/evidence/probe_logic_contract_audit_2026-09-28.md": {
        "clusters": ["endpoint", "moments", "cartesian-assembly", "global-assembly", "methodology"],
        "finding": "Static adversarial contract audit of 262 review declarations: 20 have explicit conditional-premise markers, 88 have strong-conclusion markers, and zero unconditional endpoint claims are authorised. It forces interface, conditional, ghost-payload, fixed-force, and completion identities into separate scopes.",
        "anchors": "generated report; counts and declaration matrix",
    },
    "NavierStokesReview/evidence/probe_logic_contract_audit_2026-09-28.json": {
        "clusters": ["endpoint", "moments", "cartesian-assembly", "global-assembly", "methodology"],
        "finding": "Machine-readable adversarial probe-contract audit with declaration-level provenance and scope classifications.",
        "anchors": "generated JSON; counts and rows",
    },
    "NavierStokesReview/src/audit/source_tranche_summary.py": {
        "clusters": ["endpoint", "pressure", "cartesian-assembly", "periodicity", "methodology"],
        "finding": "Reusable line-addressed source navigation index for the Priority 129 pressure/local-paper/comparator tranche. It is explicitly not a theorem prover or absence detector.",
        "anchors": "1-111",
    },
    "NavierStokesReview/evidence/source_tranche_summary_2026-09-28.json": {
        "clusters": ["endpoint", "pressure", "cartesian-assembly", "periodicity", "methodology"],
        "finding": "Generated source navigation index for 15 endpoint-external OpenAI files, recording imports, declarations, keyword locations, and sorry-token locations.",
        "anchors": "generated JSON; 15 files",
    },
    "NavierStokesReview/src/audit/priority_129_external_r3_pressure_comparator_source_review_2026-09-28.md": {
        "clusters": ["endpoint", "pressure", "cartesian-assembly", "periodicity", "moments", "methodology"],
        "finding": "Source-grounded review of 15 endpoint-external pressure, local-paper, periodization, comparator, support, and stage-bound files. It credits genuine conditional identities and preserves the remaining global observable gate.",
        "anchors": "1-113",
    },
    "NavierStokesReview/src/audit/priority_130_euler_comparator_cylinder_average_source_review_2026-09-28.md": {
        "clusters": ["euler", "operator-path", "periodicity", "cartesian-assembly", "moments", "methodology"],
        "finding": "Reviews 15 endpoint-external Euler comparator, curl-transport, cylinder angular-average, Dirichlet, and acceleration files. It credits genuine Euler zero-mean and curl identities while keeping them separate from the selected Navier-Stokes global five-observable bridge.",
        "anchors": "1-104",
    },
    "NavierStokesReview/src/audit/priority_132_external_ns_junction_h3_periodic_candidate_review_2026-09-28.md": {
        "clusters": ["endpoint", "cartesian-assembly", "periodicity", "pressure", "comparison", "regularity", "methodology"],
        "finding": "Reviews 15 endpoint-external OpenAI Navier-Stokes candidate, periodic, local-schedule, H3, comparator, and uniqueness files. It credits genuine alternate candidate/comparator chains while preserving the missing selected Cartesian five-observable transport obligation.",
        "anchors": "1-113",
    },
    "NavierStokesReview/evidence/source_tranche_external_ns_junction_2026-09-28.json": {
        "clusters": ["endpoint", "cartesian-assembly", "periodicity", "pressure", "comparison", "regularity", "methodology"],
        "finding": "Generated line-addressed source navigation index for the fifteen Priority 132 endpoint-external OpenAI Navier-Stokes junction files.",
        "anchors": "generated JSON; 15 files",
    },
    "NavierStokesReview/src/audit/priority_134_comparator_eulerproof_source_review_2026-09-28.md": {
        "clusters": ["repository-root", "euler", "methodology", "endpoint"],
        "finding": "Bounded source review of the two standalone comparator files with four intentional admitted theorem bodies and of EulerProof's admitted-token-free analytic/ODE foundation. It separates repository metadata defects from active endpoint contamination.",
        "anchors": "1-115",
    },
    "NavierStokesReview/evidence/source_tranche_comparator_eulerproof_2026-09-28.json": {
        "clusters": ["repository-root", "euler", "methodology", "endpoint"],
        "finding": "Machine-readable Priority 134 source identity, declaration counts, admitted-token results, and bounded classifications for the comparator and Euler foundation tranche.",
        "anchors": "generated JSON; 3 source records",
    },
    "ComparatorChallenges/NavierStokes.lean": {
        "clusters": ["repository-root", "cmi-paper", "methodology"],
        "finding": "Standalone Mathlib-only comparator whose header identifies two intentional sorry challenge theorem bodies; not imported by the captured proof root according to the source scope and import register.",
        "anchors": "21-35; 273-284",
    },
    "ComparatorChallenges/Euler.lean": {
        "clusters": ["repository-root", "euler", "cmi-paper", "methodology"],
        "finding": "Standalone Mathlib-only Euler comparator whose header identifies two intentional sorry challenge theorem bodies; not imported by the captured proof root according to the source scope and import register.",
        "anchors": "21-35; 85-88; 170-184",
    },
    "Euler/EulerProof.lean": {
        "clusters": ["repository-root", "euler", "regularity", "pressure", "methodology"],
        "finding": "Large admitted-token-free Euler analytic, Sobolev, pressure, packet, scale, and parameterised ODE development. Bounded review does not treat its conditional/ODE declarations as a final CMI endpoint or as selected Navier-Stokes transport.",
        "anchors": "12489-12545; 12621-12720; 18240-18265; 18420-18473; 18487-18560; 18934-19005; 20519-20745",
    },
    "NavierStokesReview/src/audit/priority_135_external_moment_realization_junction_source_review_2026-09-28.md": {
        "clusters": ["endpoint", "moments", "cartesian-assembly", "pressure", "residual", "methodology"],
        "finding": "Bounded source review of twelve external moment-repair, Cartesian realisation, summation, pressure, continuation, and residual-junction files. It credits genuine upstream repair and local transport results while keeping the final selected-field five-observable bridge open.",
        "anchors": "1-145",
    },
    "NavierStokesReview/evidence/source_tranche_external_moment_realization_junction_2026-09-28.json": {
        "clusters": ["endpoint", "moments", "cartesian-assembly", "pressure", "residual", "methodology"],
        "finding": "Machine-readable Priority 135 source identities, hashes, anchors, positive results, and bounded final-bridge classifications for twelve external junction files.",
        "anchors": "generated JSON; 12 source records",
    },
    "NavierStokes/ActualCorrectionModels.lean": {
        "clusters": ["moments", "cartesian-assembly", "operator-path"],
        "finding": "Transports local model/fibre agreement through coordinate and differential operations; this is genuine local transport, not a final selected-field five-observable equality.",
        "anchors": "model definitions; fibre agreement; differential preservation",
    },
    "NavierStokes/ClosedIntervalMomentRepair.lean": {
        "clusters": ["moments", "profiles", "corrections"],
        "finding": "Constructs a smooth local profile correction branch solving the stated quadratic interval equation under explicit hypotheses.",
        "anchors": "Data; exists_continuous_branch; pointwise_equation; exists_smooth_same_branch",
    },
    "NavierStokes/ExponentialMomentMatrix.lean": {
        "clusters": ["moments", "profiles", "linear-algebra"],
        "finding": "Proves invertibility/nonzero determinants for exponential moment matrices under separation and positivity hypotheses; it is not the selected-field transport theorem.",
        "anchors": "expIntervalMomentMatrix; expBumpMomentMatrix_det_ne_zero",
    },
    "NavierStokes/GenericAngularRecovery.lean": {
        "clusters": ["cartesian-assembly", "regularity", "divergence"],
        "finding": "Proves angular recovery, smoothness, tangency, and divergence facts including axis handling; no radial five-observable transport is exported.",
        "anchors": "angular_divergence_axis; angular_rate_smooth_of_cartesian; angular_admissibility",
    },
    "NavierStokes/GenericSolenoidalRealization.lean": {
        "clusters": ["cartesian-assembly", "divergence", "support"],
        "finding": "Constructs smooth divergence-free Cartesian velocities and proves cutoff/germ properties; no five-moment equality for the exported witness.",
        "anchors": "velocity; velocity_smooth; velocity_divergence; positiveVelocity_outer_germ",
    },
    "NavierStokes/GenericSummationRealization.lean": {
        "clusters": ["cartesian-assembly", "residual", "summation"],
        "finding": "Converts detailed raw-stage rate/support hypotheses into realisation and flat-residual conclusions; no moment observable equality.",
        "anchors": "base_rate_of_raw_log; exists_angular_realization; flat_residual_of_raw_bounds",
    },
    "NavierStokes/LocalHeatExterior.lean": {
        "clusters": ["cartesian-assembly", "pressure", "local-exterior"],
        "finding": "Proves local heat-exterior axial/curl and germ identities; it does not connect them to a global selected-field moment tuple.",
        "anchors": "axialPotential_curl; finalPotential_eq_axialPart; axialPart_finalPotential_germ",
    },
    "NavierStokes/LocalHeatPressure.lean": {
        "clusters": ["pressure", "moments", "local-exterior"],
        "finding": "Proves positive-radius radial pressure-tail formulas and integrability conditions; no absolute global selected-pressure Poisson/Leray theorem.",
        "anchors": "canonicalPressure_radius_integral; heatPressure_radius_integral; heatAmplitude_sq_div_integrable",
    },
    "NavierStokes/LocalResidualFlatness.lean": {
        "clusters": ["endpoint", "residual", "jets"],
        "finding": "Builds all-order residual jet-rate schedules from stage estimates and cut bounds; no radial moment transport.",
        "anchors": "AllResidualJetRates; allResidualJetRates_of_cutBounds; selected_schedule",
    },
    "NavierStokes/MeanLocalDefectBounds.lean": {
        "clusters": ["rank", "moments", "corrections", "residual"],
        "finding": "Proves local support, three-component debt/remainder classes, and rank-stage gain under explicit local hypotheses; no final Cartesian five-observable identification.",
        "anchors": "rankIncrement_streamSupport; moving_remainders_mem; rankStage_defect_class; rankStage_gain_of_targets",
    },
    "NavierStokes/MeanStageContinuation.lean": {
        "clusters": ["periodicity", "pressure", "continuation", "moments"],
        "finding": "Propagates periodic primitives, pressure, source, and continuation agreements; no selected-witness five-observable equality.",
        "anchors": "PeriodicAlgebra; reconstructPrimitives_periodic; continuedDebt_agrees; pressureMass_agreement",
    },
    "NavierStokes/ModulatedProfileJetRates.lean": {
        "clusters": ["moments", "profiles", "corrections", "residual"],
        "finding": "Proves exact reduced-profile physical moment repair/restoration, cone membership, exterior profileRows equality, and derivative rates; it does not output a theorem about the final selected Cartesian field.",
        "anchors": "SmoothRepairFamily.solves; exists_smooth_repair_family; exists_with_moment_repair_all_jets",
    },
    "NavierStokesReview/src/audit/external_source_profile.py": {
        "clusters": ["repository-root", "methodology", "endpoint"],
        "finding": "Profiles every indexed module outside the captured endpoint closure by source hash, imports, declarations, marker locations, and admitted-token locations. It is explicitly structural inventory, not semantic transport proof.",
        "anchors": "1-299",
    },
    "NavierStokesReview/evidence/external_source_profile_full_2026-09-28.json": {
        "clusters": ["repository-root", "methodology", "endpoint"],
        "finding": "Full structural profile of all 2,204 indexed modules outside the captured endpoint closure; it keeps all rows visible without calling them dead or mathematically reviewed.",
        "anchors": "generated JSON; 2,204 files",
    },
    "NavierStokesReview/evidence/external_source_profile_full_2026-09-28.md": {
        "clusters": ["repository-root", "methodology", "endpoint"],
        "finding": "Human-readable structural profile and risk queue for all 2,204 outside-closure modules. Marker hits remain navigation signals, not semantic conclusions.",
        "anchors": "1-200",
    },
    "NavierStokes/CandidateAssembly.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "force", "residual"],
        "finding": "Conditionally assembles a residual-derived early force with a supplied late force and packages CandidateProperties; it does not construct the input fields or export five-observable transport.",
        "anchors": "25-227",
    },
    "NavierStokes/R3/H3CandidateStrong.lean": {
        "clusters": ["endpoint", "regularity", "support"],
        "finding": "Converts CandidateProperties and compact slab hypotheses into a classical H3 solution on shorter intervals; no selected moment equality.",
        "anchors": "87-119",
    },
    "NavierStokes/R3/H3Continuity.lean": {
        "clusters": ["endpoint", "regularity", "bounds"],
        "finding": "Proves H3 continuity from compact support and smooth derivative data; no global radial observable transport.",
        "anchors": "25-105",
    },
    "NavierStokes/R3/H3CandidateUniqueness.lean": {
        "clusters": ["endpoint", "pressure", "comparison", "force"],
        "finding": "Proves pressure-pairing cancellation, strong uniqueness, and candidate force integrability under explicit hypotheses; comparative rather than absolute pressure/moment semantics.",
        "anchors": "20-101",
    },
    "NavierStokes/ComparatorTheorem.lean": {
        "clusters": ["endpoint", "comparison", "periodicity", "force"],
        "finding": "Transfers a candidate predicate into the periodic option-D comparator statement using rescaling and force decay; no five-moment transport.",
        "anchors": "25-52",
    },
    "NavierStokes/LocalAngularGrowth.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "moments", "residual"],
        "finding": "Builds selected schedule aliases and proves angular growth from existing selected-witness/residual-band data; no equality with the paper's five-observable tuple.",
        "anchors": "138-248",
    },
    "NavierStokes/LocalScheduleWitness.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "periodicity", "support", "residual"],
        "finding": "Defines potential/direct/pressure sums and conditional periodic/compact candidate packaging from a schedule predicate; no exported five-moment field theorem.",
        "anchors": "22-160",
    },
    "NavierStokes/PeriodicPaperTheorem.lean": {
        "clusters": ["endpoint", "periodicity", "pressure", "support", "comparison"],
        "finding": "Defines a periodic paper-level candidate predicate and periodic corollary. Support is explicitly fundamental-cube-relative for periodic lifts, not global compact support.",
        "anchors": "26-155",
    },
    "NavierStokes/R3/H3Blowup.lean": {
        "clusters": ["endpoint", "regularity", "comparison"],
        "finding": "Derives H3 norm unboundedness and non-continuation from candidate origin blow-up and compact-slab bounds; no profile-moment transport.",
        "anchors": "20-68",
    },
    "NavierStokes/PeriodicPaperComparator.lean": {
        "clusters": ["endpoint", "periodicity", "comparison", "force"],
        "finding": "Transfers the periodic paper candidate into the comparator's periodic force condition and same-force option-D statement; no five-moment bridge.",
        "anchors": "21-52",
    },
    "NavierStokes/R3/H3CompactCurve.lean": {
        "clusters": ["endpoint", "regularity", "support"],
        "finding": "Establishes compact-slab Lp/H3 curve regularity for candidate fields; no global radial observable.",
        "anchors": "16-74",
    },
    "NavierStokes/PaperLocalization.lean": {
        "clusters": ["endpoint", "pressure", "cartesian-assembly", "support"],
        "finding": "Shows late-time local pressure agreement and packages a local candidate; local agreement is not global tsum/curl/localisation/periodisation/barMoment transport.",
        "anchors": "20-50",
    },
    "NavierStokes/R3/H3MaximalLifespan.lean": {
        "clusters": ["endpoint", "regularity", "comparison", "pressure"],
        "finding": "Defines and compares H3 lifespans and packages maximality at time one under CandidateProperties; no independent paper-field semantic validation.",
        "anchors": "43-111",
    },
    "NavierStokes/R3/ComparatorBridge.lean": {
        "clusters": ["endpoint", "comparison", "force", "support"],
        "finding": "Converts compact force support into comparator decay and derives option C from candidate breakdown using the same force; conditional and not a moment bridge.",
        "anchors": "22-86",
    },
    "NavierStokes/R3/ViscousUniqueness.lean": {
        "clusters": ["endpoint", "comparison", "force"],
        "finding": "Applies viscosity rescaling and comparison to establish pre-singular uniqueness; no absolute pressure or profile-moment transport.",
        "anchors": "23-57",
    },
    "NavierStokesReview/evidence/source_tranche_euler_cylinder_2026-09-28.json": {
        "clusters": ["euler", "operator-path", "periodicity", "methodology"],
        "finding": "Generated source navigation index for 15 Euler comparator, cylinder-average, curl, Dirichlet, and acceleration modules.",
        "anchors": "generated JSON; 15 files",
    },
    "Euler/ComparatorEvolutionIdentification.lean": {
        "clusters": ["euler", "operator-path", "cartesian-assembly"],
        "finding": "Defines compact-curl local evolution and proves conditional comparator-field agreement; no selected Navier-Stokes field or five-observable tuple.",
        "anchors": "1-105",
    },
    "Euler/ComparatorIdentification.lean": {
        "clusters": ["euler", "operator-path"],
        "finding": "Proves maximal velocity identification under the conditional local-evolution upgrade; no selected Navier-Stokes endpoint transport.",
        "anchors": "1-38",
    },
    "Euler/ComparatorLocalEvolution.lean": {
        "clusters": ["euler", "cartesian-assembly", "bounds"],
        "finding": "Constructs recovered Euler velocity from compact vorticity and proves field equality and uniform jet bounds; no selected Navier-Stokes global observable.",
        "anchors": "1-101",
    },
    "Euler/ComparatorMaximalSolution.lean": {
        "clusters": ["euler", "regularity", "bounds"],
        "finding": "Packages maximal Euler derivative/velocity fields and Sobolev existence characterisation; no selected Navier-Stokes five-moment bridge.",
        "anchors": "1-107",
    },
    "Euler/ComparatorSingularityNorms.lean": {
        "clusters": ["euler", "regularity", "cartesian-assembly"],
        "finding": "Relates Euler vorticity and velocity norms to curl fields; no selected Navier-Stokes endpoint or radial tuple.",
        "anchors": "1-40",
    },
    "Euler/ContinuousAccelerationForcing.lean": {
        "clusters": ["euler", "force", "regularity"],
        "finding": "Defines and regularity-bounds a continuous acceleration forcing map; no selected Navier-Stokes force provenance or moment transport.",
        "anchors": "1-37",
    },
    "Euler/ContinuousAccelerationGevrey.lean": {
        "clusters": ["euler", "regularity", "bounds"],
        "finding": "Proves Gevrey/regularity properties for the continuous acceleration construction; no selected Navier-Stokes endpoint theorem.",
        "anchors": "1-52",
    },
    "Euler/ContinuousAccelerationSobolev.lean": {
        "clusters": ["euler", "sobolev", "bounds"],
        "finding": "Proves block bounds for continuous acceleration in Sobolev layers; no selected Navier-Stokes five-observable transport.",
        "anchors": "1-67",
    },
    "Euler/CurlMatrixSymmetry.lean": {
        "clusters": ["euler", "operator-path", "cartesian-assembly"],
        "finding": "Proves the linear curl matrix vanishes exactly for symmetric derivative matrices; local algebra only.",
        "anchors": "1-49",
    },
    "Euler/CurlTransportAlgebra.lean": {
        "clusters": ["euler", "operator-path", "cartesian-assembly"],
        "finding": "Proves Cartesian curl transport for Euler convection, divergence-free simplification, zero curl of gradients, and the vorticity RHS; no radial barMoment or selected NS binding.",
        "anchors": "1-114",
    },
    "Euler/CylinderAngleAverage.lean": {
        "clusters": ["euler", "periodicity", "operator-path"],
        "finding": "Defines the bounded cylinder angular-average operator and proves translation/operator intertwining and support preservation; not the selected NS five-observable map.",
        "anchors": "1-210",
    },
    "Euler/CylinderAngleAverageEvolution.lean": {
        "clusters": ["euler", "periodicity", "operator-path"],
        "finding": "Proves Duhamel/evolution commutation with the supported angular average and propagation of zero angular mean; no selected NS radial tuple.",
        "anchors": "1-106",
    },
    "Euler/CylinderAngleAverageRepresentative.lean": {
        "clusters": ["euler", "periodicity", "integrals"],
        "finding": "Relates L2 angular averaging to continuous Sobolev representatives and an interval-integral zero-mean criterion; no selected NS endpoint.",
        "anchors": "1-94",
    },
    "Euler/CylinderDirichletEquation.lean": {
        "clusters": ["euler", "operator-path", "residual"],
        "finding": "Proves almost-everywhere coefficient, physical velocity, derivative, and balance equations for an explicit cylinder system; local coefficient semantics only.",
        "anchors": "1-82",
    },
    "Euler/CylinderDirichletPhysicalBounds.lean": {
        "clusters": ["euler", "bounds", "regularity"],
        "finding": "Provides physical velocity and derivative block bounds for the cylinder Dirichlet system; no selected NS global moment transport.",
        "anchors": "1-106",
    },
    "NavierStokes/R3PressureNearKernel.lean": {
        "clusters": ["pressure", "r3", "integrals", "bounds"],
        "finding": "Reviewed source tranche: near/remainder radial profiles, scaling, and Lp bounds; no selected-field or five-observable transport conclusion.",
        "anchors": "1-275",
    },
    "NavierStokes/R3PressureKernel.lean": {
        "clusters": ["pressure", "r3", "integrals", "bounds", "commutator"],
        "finding": "Reviewed source tranche: model kernel majorant, integrability, exact scaling, and L4/3 norm; module comment separates this from identifying the Riesz-transform commutator.",
        "anchors": "1-168",
    },
    "NavierStokes/R3SmoothPressure.lean": {
        "clusters": ["pressure", "r3", "functional-analysis"],
        "finding": "Reviewed source tranche: conditional smooth pressure-gradient representation from explicit smoothness, MemLp, divergence, and momentum hypotheses; no selected-witness binding or five-observable theorem.",
        "anchors": "1-146",
    },
    "NavierStokes/LocalHeatFormula.lean": {
        "clusters": ["pressure", "profiles", "axis", "integrals", "regularity"],
        "finding": "Reviewed source tranche: heat-exterior amplitude, radial heat equation, angular velocity representation, radial pressure integral, and integrability.",
        "anchors": "1-140",
    },
    "NavierStokes/NaturalAxisJointAnalytic.lean": {
        "clusters": ["axis", "pressure", "profiles", "regularity"],
        "finding": "Reviewed source tranche: analytic coefficient, amplitude, pullback, angular, and pressure profiles; no selected global moment transport.",
        "anchors": "1-163",
    },
    "NavierStokes/InitialHarmonicContinuation.lean": {
        "clusters": ["continuation", "pressure", "periodicity", "cartesian-assembly"],
        "finding": "Reviewed source tranche: harmonic continuation objects and periodicity/support declarations for initial data; no selected five-observable equality.",
        "anchors": "1-1459",
    },
    "NavierStokes/LocalPotentialRebundle.lean": {
        "clusters": ["cartesian-assembly", "residual", "pressure", "tsum", "commutator"],
        "finding": "Reviewed source tranche: selected schedule rebundling, pointwise exterior finite-sum collapse, curl/extension identities, and exterior field identities; no global tsum/radial observable interchange.",
        "anchors": "1-271",
    },
    "NavierStokes/PeriodizePDE.lean": {
        "clusters": ["periodicity", "residual", "cartesian-assembly", "support"],
        "finding": "Reviewed source tranche: conditional translation covariance, divergence preservation, and forced residual preservation under supported periodization; no five-observable transport.",
        "anchors": "1-153",
    },
    "NavierStokes/ComparatorR3Theorem.lean": {
        "clusters": ["endpoint", "energy", "force", "cartesian-assembly"],
        "finding": "Reviewed source tranche: option-C comparator packaging from compact candidate properties and the R3 endpoint; no five-observable transport.",
        "anchors": "1-46",
    },
    "NavierStokes/ComparatorTheorem.lean": {
        "clusters": ["endpoint", "energy", "force", "periodicity"],
        "finding": "Reviewed source tranche: option-D comparator packaging from candidate and periodic-paper properties; no five-observable transport.",
        "anchors": "1-55",
    },
    "NavierStokes/LocalPaperTheorem.lean": {
        "clusters": ["cartesian-assembly", "residual", "jets", "axis", "profiles"],
        "finding": "Reviewed source tranche: local Properties package smoothness, curl decomposition, divergence, extensions, jets, residual flatness, exterior zero, and angular growth; no M/I/J/S/Cp field observable.",
        "anchors": "1-186",
    },
    "NavierStokes/R3/ParabolicSupport.lean": {
        "clusters": ["r3", "support", "time", "cartesian-assembly"],
        "finding": "Reviewed source tranche: affine support scaling and compact-set cube placement; no pressure semantics or moment transport.",
        "anchors": "1-71",
    },
    "NavierStokes/SharpGluedStageBounds.lean": {
        "clusters": ["stage-interface", "jets", "pressure", "cartesian-assembly", "bounds"],
        "finding": "Reviewed source tranche: stagewise potential, pressure, direct, and curl LogBound estimates; no radial observable equality.",
        "anchors": "1-178",
    },
    "NavierStokes/SharpParticularGluing.lean": {
        "clusters": ["stage-interface", "pressure", "cartesian-assembly", "bounds"],
        "finding": "Reviewed source tranche: local potential and pressure gluing bounds; no global selected-field transport theorem.",
        "anchors": "1-102",
    },
    "NavierStokes/WholeDomainInitializationBounds.lean": {
        "clusters": ["stage-interface", "pressure", "cartesian-assembly", "bounds", "initial-data"],
        "finding": "Reviewed source tranche: initial potential, pressure, direct, velocity, and pressure rate bounds; no five-observable transport.",
        "anchors": "1-128",
    },
    "NavierStokesReview/src/completions/SelectedFieldFinitePrefix.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "global-assembly"],
        "finding": "Defines the concrete selected schedule and proves local and all-jet eventual finite-prefix equality for the selected potentialSum; no radial moment evaluation.",
        "anchors": "19-83",
    },
    "NavierStokesReview/src/completions/SelectedPotentialPrefixCurlExpansion.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "commutator"],
        "finding": "Applies spatial curl to the selected finite-prefix eventual equality; no radial pullback, tsum-integral interchange, or defect value.",
        "anchors": "19-53",
    },
    "NavierStokesReview/src/completions/SelectedPotentialStagewiseCurlOnPhysicalDomain.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "commutator"],
        "finding": "Proves physical-domain eventual equality to a finite sum of stage curls under the selected schedule; no global radial moment conclusion.",
        "anchors": "19-76",
    },
    "NavierStokesReview/src/completions/SelectedPotentialProductionProductRule.lean": {
        "clusters": ["cartesian-assembly", "commutator"],
        "finding": "Instantiates the selected potential branch cutoff product rule and exposes the fderiv commutator; no sign or nonzero claim.",
        "anchors": "19-57",
    },
    "NavierStokesReview/src/completions/SelectedPotentialProductionFinitePrefix.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "commutator", "moments"],
        "finding": "Expands the selected finite prefix through curl/localisation and applies barMoment to the typed finite-prefix scalar; no infinite-limit theorem.",
        "anchors": "19-149",
    },
    "NavierStokesReview/src/completions/SelectedPotentialProductionRadialScalar.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "moments", "commutator"],
        "finding": "Defines the actual selected potential radial component and proves a schedule-level product-rule transport theorem under physical-domain and differentiability hypotheses.",
        "anchors": "19-122",
    },
    "NavierStokesReview/src/completions/SelectedMixedVelocityDecomposition.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "periodicity"],
        "finding": "Proves the actual order of mixed assembly: localised potential velocity plus separately cut/periodised direct potential; prevents an invalid combined-curl shortcut.",
        "anchors": "19-82",
    },
    "NavierStokesReview/src/completions/SelectedMixedProductionRadialComponent.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "moments", "periodicity"],
        "finding": "Defines the first Cartesian component of the actual mixed periodic selected velocity on the radial section and its potential/direct split; no moment value.",
        "anchors": "19-54",
    },
    "NavierStokesReview/src/completions/SelectedMixedProductionBarMoment.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "moments"],
        "finding": "Pulls the actual mixed radial component into the scalar family accepted by barMoment and proves the generic integral formula; no five-tuple identification.",
        "anchors": "19-72",
    },
    "NavierStokesReview/src/completions/SelectedMixedProductionBranchSplit.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "moments"],
        "finding": "Proves the pointwise potential/direct scalar branch split; no integral linearity, cancellation, or nonzero remainder.",
        "anchors": "19-53",
    },
    "NavierStokesReview/src/completions/SelectedMixedProductionTorusAverage.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "moments", "periodicity"],
        "finding": "Reduces the actual mixed scalar torus average to the radial section and rewrites barMoment as the remaining radial integral; no value evaluation.",
        "anchors": "19-58",
    },
    "NavierStokesReview/src/completions/SelectedPotentialProductionBarMomentSection.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "moments", "axis"],
        "finding": "Provides the positive-radius physical-point pullback identity for the selected potential scalar; no on-axis/global bridge.",
        "anchors": "19-77",
    },
    "NavierStokesReview/src/completions/SelectedPotentialProductionTorusAverage.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "moments", "periodicity"],
        "finding": "Proves finite-prefix torus-average and radial reduction for the selected potential branch; finite prefix only.",
        "anchors": "19-52",
    },
    "NavierStokesReview/src/completions/SelectedMixedRadialPeriodicity.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "moments", "periodicity"],
        "finding": "Proves exact radius-periodicity of the actual mixed radial integrand; periodicity alone is not nonzero value, integrability, or contradiction.",
        "anchors": "19-74",
    },
    "NavierStokes/ActualParticularDynamicsNoOptions.lean": {
        "clusters": ["profiles", "cartesian-assembly", "residual", "jets"],
        "finding": "Computes the selected fast-direction and principal dynamics from concrete carrier, wave, patch, radius, time, and geometry hypotheses. This is selected-stage dynamics, not a theorem transporting the final Cartesian field to the five paper moments.",
        "anchors": "48-80; 82-190",
    },
    "NavierStokes/AppendixHeatResults.lean": {
        "clusters": ["profiles", "moments", "pressure", "jets"],
        "finding": "Proves heat-profile rising, gamma, derivative, endpoint, and remainder bounds, including local moment-zero uses. The inspected results remain reduced heat/profile estimates and do not identify the final selected Cartesian barMoment tuple.",
        "anchors": "16-166",
    },
    "NavierStokes/AppendixJoiningResults.lean": {
        "clusters": ["profiles", "pressure", "support"],
        "finding": "Proves axis-margin, source-identity, denominator, and reference lower bounds for the joining construction. These bounds support the assembly but are not a selected-field moment transport theorem.",
        "anchors": "17-80",
    },
    "NavierStokes/BaseWitnessClosure.lean": {
        "clusters": ["profiles", "moments", "rank", "cartesian-assembly"],
        "finding": "Closes actual profile, outgoing, axis, scale, cone, pressure, finite-slow-identity, threshold, and initial-cycle compatibility data. It supplies genuine upstream witness closure without exporting final Cartesian five-observable equality.",
        "anchors": "22-73; 89-131",
    },
    "NavierStokes/CommonCoverWithin.lean": {
        "clusters": ["cartesian-assembly", "support", "jets", "time"],
        "finding": "Proves smooth localised copies, finite locally common-torus sums, and one-sided boundary jet limits. The local finite-sum/common-torus scope is not an infinite radial tsum moment identity.",
        "anchors": "84-125",
    },
    "NavierStokes/CompactHolomorphicFamily.lean": {
        "clusters": ["profiles", "calculus"],
        "finding": "Proves circle-integral evaluation commutation and holomorphic-family regularity. This is analytic auxiliary infrastructure and contains no selected Navier-Stokes field moment bridge.",
        "anchors": "13-40",
    },
    "NavierStokes/ComparatorR3Bridge.lean": {
        "clusters": ["r3", "global-assembly", "energy", "pressure"],
        "finding": "Defines the global Rn solution package and proves the rescaled comparator residual equation with smoothness, divergence, initial, force, and finite-energy assumptions. It is a comparator bridge, not a proof that the selected profile mechanism is transported into the endpoint.",
        "anchors": "24-80",
    },
    "NavierStokes/ComparatorSolution.lean": {
        "clusters": ["endpoint", "r3", "energy", "global-assembly"],
        "finding": "Packages Navier-Stokes breakdown and periodic comparator wrappers. The wrapper conclusions concern candidate existence and comparator structure; they do not add a final five-moment or barMoment equality.",
        "anchors": "16-32",
    },
    "NavierStokes/EndpointLimits.lean": {
        "clusters": ["jets", "time", "endpoint"],
        "finding": "Separates smooth left-endpoint extension from independently assumed right-hand jet realisation and proves endpoint limit identities. It does not bridge off-axis chart data, origin limits, and final radial moments.",
        "anchors": "137-167",
    },
    "NavierStokes/FlatPrimitivePaper.lean": {
        "clusters": ["profiles", "support", "jets"],
        "finding": "Constructs smooth compact-support flat factors and local extension bounds from bump functions. These are support/regularity primitives, not evidence that localisation preserves selected five-moment observables.",
        "anchors": "17-100",
    },
    "NavierStokes/CorrectionInitializationNoOptions.lean": {
        "clusters": ["moments", "rank", "cartesian-assembly", "profiles"],
        "finding": "Builds genuine correction-initialisation pieces, support/cutoff facts, native bounds, zero-mass initialization, and radial residual data; no final selected Cartesian five-observable bridge is exported.",
        "anchors": "81-97; 124-289; 1212-1245",
    },
    "NavierStokes/ActualParticularPhysicalData.lean": {
        "clusters": ["cartesian-assembly", "jets", "support", "global-assembly", "moments"],
        "finding": "Defines actual amplitude/pressure/potential sums, summability and tsum identities, support/geometry, and native-to-physical bounds; no final selected barMoment tuple theorem is exported in the inspected declarations.",
        "anchors": "56-161; 678-718; 728-872; 1148-1150; 1226-1255",
    },
    "NavierStokes/SignedRequestContinuation.lean": {
        "clusters": ["support", "pressure", "moments", "cartesian-assembly"],
        "finding": "Proves supported-operation closure, smoothness, shell agreement, physical stress support, and actual-base continuation; no final selected observable equality is exposed.",
        "anchors": "26-220; 323-377; 411-499; 535-557; 581-743",
    },
    "NavierStokes/PeriodicPaperTheorem.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "support", "pressure", "force"],
        "finding": "Provides a genuine periodic C/D endpoint corollary transporting smoothness, periodicity, fundamental-cube support, divergence, residual equality, zero initial data, and speed blow-up; the candidate predicate has no five-moment or barMoment field.",
        "anchors": "9-15; 24-73; 89-162",
    },
    "NavierStokes/MeanStageContinuation.lean": {
        "clusters": ["moments", "cartesian-assembly", "support", "time"],
        "finding": "Proves periodic operator algebra and continuation identities for bases, profiles, sources, primitives, debt, and rank data; no final selected Cartesian barMoment transport theorem was found in the inspected declarations.",
        "anchors": "140-192; 209-339; 465-478; 596-647",
    },
    "NavierStokes/CycleContinuationInvariant.lean": {
        "clusters": ["moments", "rank", "cartesian-assembly", "support"],
        "finding": "Packages periodic primitives/harmonics, axis-supported continuation, representation, and periodicity after cycle updates; it does not identify final global barMoment values.",
        "anchors": "411-420; 447-491; 567-652",
    },
    "NavierStokes/PeriodicPaperScalingSupport.lean": {
        "clusters": ["support", "endpoint", "cartesian-assembly"],
        "finding": "Proves compression of velocity, pressure, and force support into a fundamental cube; support transport is not a five-moment transport theorem.",
        "anchors": "15-109",
    },
    "NavierStokes/WholeDomainPhysicalStageTheorem.lean": {
        "clusters": ["endpoint", "jets", "residual", "cartesian-assembly"],
        "finding": "Proves concrete physical stage bounds, finite-field bounds, residual/rate packages, and paper-loss inequalities. This corrects any claim that the endpoint uses only abstract rates; it still exports no five-moment equality.",
        "anchors": "29-132; 154-208; 243-280",
    },
    "NavierStokesReview/src/audit/priority_117_periodic_compact_field_identity_review_2026-09-28.md": {
        "clusters": ["moments", "cartesian-assembly", "candidate-packaging", "r3"],
        "finding": "Separates the compact R3 velocity from the periodic velocity used by the selected radial pullback. Local inner-cube equality does not transport compact support globally. This blocks an automatic application of the periodic-support obstruction and records the exact field-identity obligation.",
        "anchors": "7-108",
    },
    "NavierStokesReview/src/completions/SelectedPotentialProductionTsumScope.lean": {
        "clusters": ["moments", "cartesian-assembly", "jets"],
        "finding": "Controls an eventual finite-prefix/tsum jet scope. It explicitly leaves torus averaging, barMoment, and radial-integral evaluation separate.",
        "anchors": "4-13; 29-48",
    },
    "NavierStokesReview/src/completions/SelectedCutoffCurlCommutator.lean": {
        "clusters": ["cartesian-assembly", "jets"],
        "finding": "Expands curl of a localised potential into the localised curl plus the cutoff-gradient commutator. It identifies the term that a global moment bridge must control.",
        "anchors": "4-23",
    },
    "NavierStokesReview/src/completions/SelectedCycleMomentTransport.lean": {
        "clusters": ["moments", "rank", "corrections"],
        "finding": "Proves selected cycle-state zero-mass/zero-row consequences for correction data. It is a cycle-level invariant, not a final selected Cartesian-field equality.",
        "anchors": "19-72",
    },
    "NavierStokes/ClosedNativeWaveIdentities.lean": {
        "clusters": ["cartesian-assembly", "jets", "residual"],
        "finding": "Derives cylindrical/curl and residual identities for native wave modes. These are mode-level identities; no selected endpoint radial-moment transport theorem was found in the inspected declarations.",
        "anchors": "imports; declarations for cylindrical/curl/residual mode identities",
    },
    "NavierStokes/MeanStateRegularity.lean": {
        "clusters": ["moments", "pressure", "cartesian-assembly"],
        "finding": "Defines regularity and periodicity data for reduced mean scalar/tensor states. It does not identify those states with the final R3 CandidateProperties velocity or with selected Cartesian barMoment values.",
        "anchors": "imports; periodic scalar/tensor fields and operator-data declarations",
    },
    "NavierStokes/OutgoingHistories.lean": {
        "clusters": ["pressure", "time", "moments"],
        "finding": "Builds outgoing pressure weights, histories, smoothness, and past-integral bounds. The inspected route is history-level and does not transport the five observables to ASum/BSum/PSum.",
        "anchors": "imports; pressure weight/history and improper-integral declarations",
    },
    "NavierStokes/LocalizedWaveBounds.lean": {
        "clusters": ["cartesian-assembly", "jets", "pressure"],
        "finding": "Packages local wave, curl, pressure, support, and jet bounds, including localisation identities. These bounds support regularity and residual control but do not assert endpoint moment equality.",
        "anchors": "approximately 1148-1263; local curl, pressure-support, germ, and jet declarations",
    },
    "NavierStokes/AssembledSlowBase.lean": {
        "clusters": ["moments", "pressure", "cartesian-assembly"],
        "finding": "Assembles slow base profiles and uses PositiveOrderMoments mass/flux histories and profile moment primitives. This is genuine upstream reduced-profile machinery, not evidence that the final selected Cartesian field exports the same tuple.",
        "anchors": "508-545; 606-613; 665-735",
    },
    "NavierStokes/VariableGaugeMean.lean": {
        "clusters": ["pressure", "moments", "axis"],
        "finding": "Develops variable-gauge reduced mean and pressure identities, including pressure mass and reconstructed-state relations. The inspected declarations remain in the reduced pressure/chart layer and do not target final CandidateProperties transport.",
        "anchors": "approximately 1777+; 2191+; 2810+; 2934+",
    },
    "NavierStokes/PulseAmplitude.lean": {
        "clusters": ["time", "moments", "jets"],
        "finding": "Defines outgoing pulse amplitudes, energies, and radial schedule bounds. It supplies quantitative stage estimates rather than a selected-field moment identity.",
        "anchors": "imports and pulse-amplitude/energy-bound declarations",
    },
    "NavierStokes/SlowStressSupport.lean": {
        "clusters": ["moments", "rank", "pressure"],
        "finding": "Defines reduced radial moments and proves local zero-moment/stress consequences from explicit PositiveOrderMoments.moments and row-density hypotheses. This is a local profile stress result, not a theorem about the final infinite localized Cartesian sum.",
        "anchors": "117-119; 634-655; approximately 1058",
    },
    "NavierStokes/SlowRecursion.lean": {
        "clusters": ["axis", "jets", "moments"],
        "finding": "Constructs regular raw axis functions, analytic/even fields, and radial jets for slow recursion. No declaration inspected here identifies the resulting jets with endpoint radial observables.",
        "anchors": "imports and regular-axis/radial-jet declarations",
    },
    "NavierStokes/PositiveAxisSystem.lean": {
        "clusters": ["axis", "jets", "moments"],
        "finding": "Defines jet systems and expanded equations for the positive axis profile. It is an upstream reduced-coordinate regularity system, not a selected Cartesian-field transport layer.",
        "anchors": "imports and Jets/BaseJet/SourceJet/ExpandedEquations/JetSystem declarations",
    },
    "NavierStokes/ShapeTransition.lean": {
        "clusters": ["moments", "rank", "time"],
        "finding": "Defines profile-level restore/reset operations for M, I, J, S, and P debt-like quantities and their jet bounds. These are constructive profile transitions; the inspected declarations do not connect them to final ASum/BSum/PSum observables.",
        "anchors": "1120-1130; 1256-1277",
    },
    "NavierStokes/OutgoingTail.lean": {
        "clusters": ["time", "jets", "moments"],
        "finding": "Defines smooth outgoing-tail flattening data and tail coefficient bounds. It contributes to stage estimates and does not state a five-observable endpoint transport theorem.",
        "anchors": "imports and tail/flattening declarations",
    },
    "NavierStokes/ModulatedProfileAssembly.lean": {
        "clusters": ["moments", "rank", "time"],
        "finding": "Assembles modulated reduced profiles from nominal witnesses, reserved patches, and slow bases. It confirms active upstream profile construction, while the inspected declarations stop before final selected Cartesian observable identification.",
        "anchors": "imports and ParameterData/modulation-assembly declarations",
    },
    "NavierStokes/OutgoingPulseBounds.lean": {
        "clusters": ["time", "jets", "moments"],
        "finding": "Provides slope, logarithmic amplitude, radial amplitude, and pulse bounds. These quantitative bounds are not a proof that the final selected field preserves the profile moment tuple.",
        "anchors": "imports and slope/log-amplitude/radial-amplitude declarations",
    },
    "NavierStokes/ErrorHarmonics.lean": {
        "clusters": ["residual", "cartesian-assembly", "rank"],
        "finding": "Defines harmonic error blocks and conjugate-pair data for correction/residual analysis. The inspected declarations do not expose a final-field barMoment or five-moment equality.",
        "anchors": "imports and conjugate-pair/harmonic-error declarations",
    },
    "NavierStokes/ActualCarrierTransport.lean": {
        "clusters": ["profiles", "cartesian-assembly", "moments"],
        "finding": "Transports carrier geometry and labels between actual-cycle parameterisations. The inspected transport lemmas concern coordinates and carrier data, not the final selected Cartesian five-moment observable.",
        "anchors": "32-60; imports ActualCarrierTransportBase and ActualCycleParameters",
    },
    "NavierStokes/ActualCopySliceRegularity.lean": {
        "clusters": ["physical-data", "jets", "cartesian-assembly"],
        "finding": "Builds regularity and transported slice data for copied stages, including frame, coefficient, forcing, and slice objects. No endpoint moment equality was found.",
        "anchors": "23-89; imports ActualParticularStageControls, ActualParticularStageCore, and CarrierGeometry",
    },
    "NavierStokes/ActualSignedDynamics.lean": {
        "clusters": ["time", "profiles", "jets"],
        "finding": "Defines signed native units, pulses, motion, and smoothness for the dynamics layer. These declarations do not identify the final field with the paper's five moments.",
        "anchors": "28-66; imports ActualPrimaryDynamics",
    },
    "NavierStokes/ActualSignedGaussianCoherence.lean": {
        "clusters": ["profiles", "cartesian-assembly", "moments"],
        "finding": "Proves Gaussian and block transport identities between signed chart data and physical scales. The transport is local to the Gaussian/chart layer and does not reach selected_witness moment equality.",
        "anchors": "95-225; gaussian_transport and gaussianBlock_transport",
    },
    "NavierStokes/ActualSignedReferenceGeometry.lean": {
        "clusters": ["profiles", "axis", "cartesian-assembly"],
        "finding": "Provides singleton, reband, and reference-geometry facts for signed exterior data. No global radial observable theorem was found.",
        "anchors": "25-156; imports ActualSignedExterior",
    },
    "NavierStokes/AnnularAuxiliary.lean": {
        "clusters": ["profiles", "axis", "jets"],
        "finding": "Constructs positive radial auxiliary maps, germs, and derivative data for annular extensions. These are auxiliary profile facts, not selected-field moment transport.",
        "anchors": "20-69; imports ParametricRadialExtension and TransportPrimitive",
    },
    "NavierStokes/BandReindexedSignedMeanGain.lean": {
        "clusters": ["moments", "rank", "cartesian-assembly"],
        "finding": "Reindexes finite signed mean-gain fields and proves cross identities for StateMomentBalances.meanBar and physicalSigma. It does not produce the final DefectIncrementBounds.barMoment identity.",
        "anchors": "45-155; fieldSum_reindex_of_coefficients, native_fields, native_family_cross",
    },
    "NavierStokes/BlowupImplication.lean": {
        "clusters": ["endpoint", "jets"],
        "finding": "Provides an abstract implication from an unbounded speed profile to failure of a bounded extension. It is a logical consequence module, not a construction of the paper's moment mechanism.",
        "anchors": "24-113; mathlib-only abstract blowup implication",
    },
    "NavierStokes/CompactSmoothFamily.lean": {
        "clusters": ["profiles", "jets"],
        "finding": "Supplies compact continuous-map and derivative infrastructure for smooth families. No field-level radial moment transport was found.",
        "anchors": "29-93; compact-family and derivative declarations",
    },
    "NavierStokes/ConeAlgebra.lean": {
        "clusters": ["profiles", "rank"],
        "finding": "Proves scalar cone and root inequalities used by profile admissibility arguments. It contains no selected-field construction or moment equality.",
        "anchors": "17-57; scalar cone/root declarations",
    },
    "NavierStokes/CurrentModeGeometry.lean": {
        "clusters": ["axis", "cartesian-assembly", "profiles"],
        "finding": "Defines chart radii, annular geometry, and native mode maps. These geometric facts support local field construction but do not establish global radial moment preservation.",
        "anchors": "21-87; chart-radius and annular-geometry declarations",
    },
    "NavierStokes/DiagonalScale.lean": {
        "clusters": ["profiles", "time", "jets"],
        "finding": "Defines logarithmic weights, diagonal scales, and doubling envelopes for estimates. These are rate controls, not transport of the five observables.",
        "anchors": "26-112; log-weight/scale/doubling declarations",
    },
    "NavierStokes/FiniteHeadClass.lean": {
        "clusters": ["jets", "cartesian-assembly"],
        "finding": "Defines finite-head comparison and jet classes used for truncation estimates. It does not connect finite heads to the final barMoment tuple.",
        "anchors": "23-97; finite-head comparison and jet-class declarations",
    },
    "NavierStokes/Flatness.lean": {
        "clusters": ["jets", "time", "residual"],
        "finding": "Proves composition rules for PowerFlat quantities. Flatness is an asymptotic jet property and is not by itself a radial-moment transport theorem.",
        "anchors": "24-126; PowerFlat composition declarations",
    },
    "NavierStokes/GaussianEnvelope.lean": {
        "clusters": ["profiles", "jets"],
        "finding": "Builds Gaussian envelopes and quadratic bounds for decay and regularity estimates. No selected Cartesian five-moment identification appears.",
        "anchors": "19-138; Gaussian envelope and quadratic-bound declarations",
    },
    "NavierStokes/GrowingMode.lean": {
        "clusters": ["profiles", "time", "jets"],
        "finding": "Defines modal operators and growth estimates for the profile dynamics. It supplies rate information, not a final-field radial observable equality.",
        "anchors": "19-121; modal operator and growth declarations",
    },
    "NavierStokes/HarmonicCovariance.lean": {
        "clusters": ["rank", "profiles", "residual"],
        "finding": "Handles angular covariance, error membership, and harmonic admissibility. The inspected declarations stop at mode/covariance data rather than selected_witness transport.",
        "anchors": "29-176; angular/covariance/error declarations",
    },
    "NavierStokes/LocalizedCurlRealization.lean": {
        "clusters": ["cartesian-assembly", "residual", "axis"],
        "finding": "Realises localised curl modes, proves divergence-free and smoothness properties, and records zero germs. This confirms genuine Cartesian curl infrastructure, but no radial five-moment theorem after localisation.",
        "anchors": "83-150; native_realizes_curl, native_divergence_zero, native_velocity_smooth, native_zero_germs",
    },
    "NavierStokes/MixedDiagonalExtensions.lean": {
        "clusters": ["time", "jets", "cartesian-assembly"],
        "finding": "Constructs one-sided endpoint extensions, eventual-zero properties, and shrinking support data. These extension facts do not identify the final field's radial moments.",
        "anchors": "27-123; endpoint-extension and shrinking-support declarations",
    },
    "NavierStokes/MixedFiniteBackground.lean": {
        "clusters": ["physical-data", "jets", "cartesian-assembly"],
        "finding": "Builds finite-prefix backgrounds and their jet rates, including stageVelocity. It supports the rate interface but exposes no selected-field five-moment equality.",
        "anchors": "25-136; raw finite-prefix/background jet rates",
    },
    "NavierStokes/ModulatedStockBounds.lean": {
        "clusters": ["profiles", "moments", "jets"],
        "finding": "Defines stock profile data, profile coordinates, and stock smoothness bounds for modulation. The inspected declarations do not transport those profile identities into the final Cartesian field.",
        "anchors": "21-74; stock-data/profile-coordinate declarations",
    },
    "NavierStokes/NativePrincipalEquations.lean": {
        "clusters": ["profiles", "residual", "rank"],
        "finding": "States principal coefficient equations for native profile data. These equations are upstream local identities and are not an endpoint theorem for selected_witness.",
        "anchors": "35-107; principal coefficient-equation declarations",
    },
    "NavierStokes/ParticularPaddedBackground.lean": {
        "clusters": ["physical-data", "profiles", "cartesian-assembly"],
        "finding": "Constructs padded cells, local normal data, germs, and polynomial background pieces. No theorem was found carrying the five cumulative moments through the final selected sums.",
        "anchors": "23-165; padded-cell/local-normal/germ declarations",
    },
    "NavierStokes/R3/CompactSchwartz.lean": {
        "clusters": ["r3", "pressure", "cartesian-assembly"],
        "finding": "Provides compact Schwartz test-function infrastructure for the R3 comparison layer. It does not construct the selected candidate or transport profile moments into it.",
        "anchors": "imports R3.ProblemStatement and Schwartz derivative infrastructure; compact-test declarations",
    },
    "NavierStokes/R3/ComparisonRateBound.lean": {
        "clusters": ["r3", "energy", "jets"],
        "finding": "Establishes comparison rate bounds used by whole-space estimates. The inspected declarations carry no selected-field radial moment identity.",
        "anchors": "imports ComparisonYoung; comparison-rate declarations",
    },
    "NavierStokes/R3/ComparisonYoung.lean": {
        "clusters": ["r3", "energy"],
        "finding": "Supplies Young-type inequalities for comparison estimates. These are analytic inequalities, not transport of the paper's five moments.",
        "anchors": "comparison inequality declarations and positivity/linarith support",
    },
    "NavierStokes/R3/FourierConvolution.lean": {
        "clusters": ["r3", "pressure", "cartesian-assembly"],
        "finding": "Proves Fourier convolution and inverse-transform integrability facts used by the pressure/comparison layer. No selected_witness moment bridge appears.",
        "anchors": "22-95; inverse Fourier product and convolution declarations",
    },
    "NavierStokes/R3/FourierSobolevWeights.lean": {
        "clusters": ["r3", "energy", "pressure"],
        "finding": "Defines weighted Fourier/Sobolev estimates for comparison fields. It does not identify a Cartesian candidate with radial moment data.",
        "anchors": "imports ComparisonFourierSetup; weighted Fourier declarations",
    },
    "NavierStokes/R3/FourierTestDerivatives.lean": {
        "clusters": ["r3", "pressure"],
        "finding": "Provides derivative identities for Fourier test functions. These are test-functional lemmas and not endpoint field transport.",
        "anchors": "imports ComparisonFourierSetup; Fourier test derivative declarations",
    },
    "NavierStokes/R3/HarmonicTestFunctionals.lean": {
        "clusters": ["r3", "pressure", "energy"],
        "finding": "Proves representation and vanishing results for harmonic test functionals, including compact harmonic uniqueness. It does not address the five profile moments of selected_witness.",
        "anchors": "25-100; FrequencyL2 and harmonic-functional uniqueness declarations",
    },
    "NavierStokes/R3/HeatKernel.lean": {
        "clusters": ["r3", "pressure", "time"],
        "finding": "Defines heat-kernel comparison objects and their regularity/bound infrastructure. No final candidate moment transport is present.",
        "anchors": "imports ComparisonSetup; heat-kernel declarations",
    },
    "NavierStokes/R3/HeatKernelCommutator.lean": {
        "clusters": ["r3", "pressure", "residual"],
        "finding": "Derives heat/Riesz commutator identities and pairing bounds for comparison analysis. These do not evaluate barMoment on the selected Cartesian field.",
        "anchors": "37-97; heatSecondTest and riesz_commutator declarations",
    },
    "NavierStokes/R3/HeatKernelFourier.lean": {
        "clusters": ["r3", "pressure", "energy"],
        "finding": "Proves Gaussian heat-kernel Fourier identities and integrability of heat-symbol terms. It is an analytical comparison module, not a selected-field profile transport module.",
        "anchors": "24-202; Gaussian inverse-transform and heat-symbol declarations",
    },
    "NavierStokes/R3/HeatKernelPairedBound.lean": {
        "clusters": ["r3", "pressure", "energy"],
        "finding": "Bounds paired heat-kernel terms using radial and paired-kernel estimates. No endpoint five-moment equality is exposed.",
        "anchors": "imports HeatKernelCancellation, HeatKernelTimeBound, RadialKernelBounds, PairedKernelBound",
    },
    "NavierStokes/R3/HilbertFunctionalExtension.lean": {
        "clusters": ["r3", "energy"],
        "finding": "Extends bounded functionals by Hilbert-space duality/Hahn-Banach infrastructure. It has no selected candidate or radial moment transport content.",
        "anchors": "dual-space and Hahn-Banach declarations",
    },
    "NavierStokes/R3/LocalizedTensorBounds.lean": {
        "clusters": ["r3", "pressure", "cartesian-assembly"],
        "finding": "Bounds localised tensor differences and quadratic cutoff terms for whole-space comparison. These are estimates, not a five-moment identification of the assembled field.",
        "anchors": "31-170; scalar/cross/quadratic cutoff and tensor-difference declarations",
    },
    "NavierStokes/R3/LpNormTools.lean": {
        "clusters": ["r3", "energy"],
        "finding": "Provides Lp and seminorm tools for comparison estimates. No endpoint candidate moment theorem is present.",
        "anchors": "imports ComparisonSetup; Lp norm declarations",
    },
    "NavierStokes/R3/PairedKernelBound.lean": {
        "clusters": ["r3", "pressure"],
        "finding": "Establishes paired-kernel integral bounds in the R3 comparison layer. It does not connect kernel estimates to the paper's five cumulative profile moments.",
        "anchors": "kernel pairing and Haar/product integral declarations",
    },
    "NavierStokes/R3/RadialKernelBounds.lean": {
        "clusters": ["r3", "pressure", "moments"],
        "finding": "Defines and bounds a radial commutator kernel, including scale and integrability results. This is not the paper's barMoment on the selected field and supplies no endpoint transport equality.",
        "anchors": "25-245; radialCommutatorKernel, scale, integrability, and Lp declarations",
    },
    "NavierStokes/R3/SchwartzCompactApproximation.lean": {
        "clusters": ["r3", "pressure"],
        "finding": "Builds compact/Schwartz approximation tools for comparison arguments. No selected-field moment transport declaration was found.",
        "anchors": "imports CompactSchwartz and ComparisonCutoffs; approximation declarations",
    },
    "NavierStokes/R3/SchwartzParseval.lean": {
        "clusters": ["r3", "energy", "pressure"],
        "finding": "Supplies Parseval-style identities for Schwartz data in the comparison layer. It does not establish the five profile moments for the exported candidate.",
        "anchors": "imports ComparisonFourierSetup; Parseval declarations",
    },
    "NavierStokes/R3/TemporalTestUniqueness.lean": {
        "clusters": ["r3", "time"],
        "finding": "Proves temporal uniqueness from test-function integral identities. This is a comparison/uniqueness tool, not selected-field moment transport.",
        "anchors": "16-40; open-set and Ioo test-integral uniqueness declarations",
    },
    "NavierStokes/R3/WeakFourierUniqueness.lean": {
        "clusters": ["r3", "pressure", "energy"],
        "finding": "Proves weak Fourier/test-functional uniqueness results. It does not identify the final Cartesian field with any five-moment tuple.",
        "anchors": "25-75; real/Schwartz test and weighted norm uniqueness declarations",
    },
    "NavierStokes/R3/WeightedInterpolation.lean": {
        "clusters": ["r3", "energy", "jets"],
        "finding": "Provides weighted interpolation estimates for comparison fields. No selected_witness five-moment transport is exposed.",
        "anchors": "imports ComparisonSetup and CompareExp; weighted interpolation declarations",
    },
    "NavierStokes/R3/WholeSpaceUniqueness.lean": {
        "clusters": ["r3", "endpoint", "pressure", "energy"],
        "finding": "Proves classical and candidate uniqueness on pre-singular Icc intervals under the same force, plus agreement before one. This confirms a real active endpoint comparison chain, but it transports no paper five-moment observable.",
        "anchors": "30-116; classical_uniqueness_on_Icc, candidate_unique_on_Icc, candidate_global_agrees_before_one",
    },
    "NavierStokes/SignedCrossDefectClass.lean": {
        "clusters": ["rank", "residual", "moments"],
        "finding": "Classifies signed cross defects and residual defect families with exponent bounds. These are intermediate defect classes, not final selected-field moment equalities.",
        "anchors": "28-173; primary/cross/physicalSigma/defect/residual-defect declarations",
    },
    "NavierStokes/SignedPhysicalSumCalculus.lean": {
        "clusters": ["cartesian-assembly", "profiles"],
        "finding": "Proves finite-sum and real-coordinate calculus identities for signed physical sums. It supports algebraic assembly but does not transport radial moments through the final selected endpoint.",
        "anchors": "19-48; finsum_eq_sum_of_zero_off, sum_realCoordinate, and real-coordinate sum declarations",
    },
    "NavierStokesReview/src/completions/SelectedBarMomentInterface.lean": {
        "clusters": ["cartesian-assembly", "moments"],
        "finding": "Defines a typed pullback from a spacetime scalar to the domain consumed by barMoment and proves the resulting integral rewrite. Its SelectedBarMomentTransportData structure makes the missing point-to-spacetime map and scalar equality explicit; selected_witness does not export this data.",
        "anchors": "1-67; selected_component_barMoment_apply, SelectedBarMomentTransportData, selected_component_requires_transport_data",
    },
    "NavierStokesReview/src/completions/SelectedBaseProfileTransport.lean": {
        "clusters": ["moments", "cartesian-assembly", "axis"],
        "finding": "Proves that the constructed gauged potential curls to the selected slow-base velocity and transports the base axis blow-up limit through that equality. This is positive selected-base evidence, not a five-observable equality for the final assembled field.",
        "anchors": "21-38; constructed_curl_eq_selected_velocity, constructed_curl_axis_tendsto",
    },
    "NavierStokesReview/src/completions/SelectedCutStageCurlScope.lean": {
        "clusters": ["cartesian-assembly", "residual"],
        "finding": "Expands the curl of one selected cutoff stage into cutoff times curl plus the explicit cutoff-gradient commutator, including the first Cartesian component. It proves the commutator formula but does not prove that its radial or barMoment contribution is zero or nonzero.",
        "anchors": "21-59; selected_cut_stage_curl_expansion and selected_cut_stage_curl_component_zero",
    },
    "NavierStokesReview/src/completions/SelectedCylindricalComponentTransport.lean": {
        "clusters": ["axis", "cartesian-assembly"],
        "finding": "Proves the first component formula for the cylindrical frame and the positive-radius polar velocity chart. This is component-level chart transport only; it does not provide torus averaging, radial pullback, or barMoment transport.",
        "anchors": "17-35; frame_component_one, velocity_polar_component_one",
    },
    "NavierStokesReview/src/completions/SelectedDirectRadialMomentBridge.lean": {
        "clusters": ["moments", "cartesian-assembly"],
        "finding": "Composes the direct-stage first-component chart identity with the native angular scalar's zero order-two barMoment. The theorem is explicitly scoped to the direct scalar branch and does not identify it with the curl-generated or mixed endpoint velocity.",
        "anchors": "19-48; selected_direct_component_one_eq_native_scalar, selected_direct_native_scalar_barMoment_zero, selected_direct_native_scalar_radial_integral_zero",
    },
    "NavierStokesReview/src/completions/SelectedDirectStageMomentTransport.lean": {
        "clusters": ["moments", "corrections", "rank"],
        "finding": "Transports the selected cycle state's angular zero-moment invariant through native direct-stage differences. This is a correction/state invariant and not a field-level equality for the final mixed Cartesian selected field.",
        "anchors": "24-63; selected_angular_native_stage_moment_zero",
    },
    "NavierStokesReview/src/completions/SelectedPhysicalComponentTransport.lean": {
        "clusters": ["axis", "cartesian-assembly"],
        "finding": "Proves the first-component formula for the actual polar Cartesian map and a selected direct-stage scaled chart formula under explicit chart, band, and domain hypotheses. It stops before torus averaging and radial moment evaluation.",
        "anchors": "18-92; polar_velocity_map_component_one, selected_direct_stage_component_one_on_chart, selected_direct_stage_component_one_scaled",
    },
    "NavierStokesReview/src/completions/SelectedPhysicalPointTransport.lean": {
        "clusters": ["cartesian-assembly", "moments"],
        "finding": "Establishes definitional compatibility between the physical moment point and the PressureStream point, then rewrites barMoment for an explicitly supplied transport datum. The selected endpoint still does not supply the scalar profile and point map as exported fields.",
        "anchors": "18-34; physical_moment_point_defeq_pressure_stream_point, barMoment_transport_requires_selected_scalar",
    },
    "NavierStokesReview/src/completions/SelectedPotentialProductionRadialScalar.lean": {
        "clusters": ["cartesian-assembly", "moments", "residual"],
        "finding": "Defines the selected production scalar on the positive-radial section and proves the cutoff-times-curl plus commutator expansion under source differentiability and unit-cube hypotheses. The existential selected schedule is transported to this finite local formula, but no global radial integral identity is asserted.",
        "anchors": "25-133; selected_potential_production_radial_scalar_eq and selected_witness_production_radial_scalar_transport",
    },
    "NavierStokesReview/src/completions/SelectedPotentialStageChartTransport.lean": {
        "clusters": ["cartesian-assembly", "axis"],
        "finding": "Proves EqOn equality between the curl of a selected potential stage and the source chart potential parts on the Cartesian chart domain. This is genuine stage/chart transport, but not transport of the five radial observables through the full sum and localisation.",
        "anchors": "19-45; selected_potential_stage_curl_on_chart",
    },
    "NavierStokesReview/src/completions/SelectedStreamCurlChartTransport.lean": {
        "clusters": ["cartesian-assembly", "axis"],
        "finding": "Proves EqOn equality for the selected stream mean stage curl on the source Cartesian chart domain. It does not identify that vector field with the scalar torus-average input expected by barMoment.",
        "anchors": "18-41; selected_stream_stage_curl_on_chart",
    },
    "NavierStokesReview/src/completions/SelectedStreamRankScope.lean": {
        "clusters": ["rank", "moments", "cartesian-assembly"],
        "finding": "Shows that the selected successor stream is assembled from temporal and rank angular families and proves the upstream moving-field premise. It records upstream rank use but supplies no Cartesian curl-to-barMoment endpoint theorem.",
        "anchors": "18-41; selected_stream_successor_temporal_rank, selected_stream_successor_moving",
    },
    "NavierStokesReview/src/completions/SelectedSupportPredicateScope.lean": {
        "clusters": ["cartesian-assembly", "axis"],
        "finding": "Provides a zero-sorry interface countermodel showing that a shrinking radial-support predicate alone does not imply the cutoff plateau's axial-coordinate condition. This is a logical support-interface separation, not a countermodel to the selected smooth field.",
        "anchors": "21-48; axialSpike_shrinkingSupport and axialWitness_not_plateau",
    },
    "NavierStokesReview/src/completions/SelectedTorusLiftImageScope.lean": {
        "clusters": ["cartesian-assembly", "moments", "axis"],
        "finding": "Proves an image restriction for the physical lift: a linear auxiliary radial coordinate is nonnegative on lifted physical points, while an auxiliary point in the integration square lies outside that image. This identifies a sampling/overlap transport obligation; it does not prove a nonzero selected moment or False.",
        "anchors": "33-107; absoluteLift_auxiliary_radialCoordinate_nonnegative, unreachableAuxiliary_not_in_absoluteLift_image, unreachablePhysicalPoint_not_in_physicalPoint_image",
    },
    "NavierStokesReview/src/completions/SelectedScalarSamplingNonuniqueness.lean": {
        "clusters": ["cartesian-assembly", "moments"],
        "finding": "Constructs two scalar families agreeing on all sampled physicalPoint values but differing at an unreachable auxiliary point. This proves non-injectivity of the raw sampling map without proving that the selected family has a nonzero missed value or that the endpoint moments are wrong.",
        "anchors": "22-57; offImageFamily_sample_eq_zero, offImageFamily_at_unreachable_eq_one, physicalPoint_sampling_not_injective",
    },
    "NavierStokes/AxisSourceRegularity.lean": {
        "clusters": ["axis", "profiles", "pressure", "jets"],
        "finding": "Proves smooth and analytic finite lower-order quotient/pressure-source expressions, including an axis extension. These are reduced-source regularity results and do not transport the final selected Cartesian field's radial moments.",
        "anchors": "192-219; 522-636",
    },
    "NavierStokes/NativeBandExtension.lean": {
        "clusters": ["cartesian-assembly", "axis", "jets", "profiles"],
        "finding": "Proves support-endpoint jets, strict-cone continuity, phase velocity/pressure regularity, closed-band regularity, and zero germs. No barMoment or final five-observable endpoint identity is present in the reviewed declarations.",
        "anchors": "45-131; 179-265; 297-355; 501-580",
    },
    "NavierStokes/OutgoingProfile.lean": {
        "clusters": ["profiles", "moments", "pressure"],
        "finding": "Defines actual reduced-profile mass, angular, energy, pressure, and axis observables and proves exact reduced-profile integral/zero identities in Specification and profile existence theorems. It does not target the final selected Cartesian field.",
        "anchors": "24-75; 316-428; 555-590; 592-665",
    },
    "NavierStokes/PartitionedCovariance.lean": {
        "clusters": ["cartesian-assembly", "rank", "profiles"],
        "finding": "Proves compact grid-mask support and exact periodised pulse covariance under slot injectivity. This is covariance assembly, not transport of the final Cartesian field's five radial observables.",
        "anchors": "28-49; 62-82; 112-130",
    },
    "NavierStokes/ProfileHistories.lean": {
        "clusters": ["profiles", "moments", "pressure"],
        "finding": "Defines radial averages, primitives, actual history integrals, and pressure from a radial primitive plus axis data, with smoothness and fundamental-theorem derivative identities. No final Cartesian endpoint composition is asserted.",
        "anchors": "158-230; 303-350; 434-436",
    },
    "NavierStokes/ReferenceBounds.lean": {
        "clusters": ["profiles", "pressure", "jets", "moments"],
        "finding": "Provides reduced pressure/history bounds, five-coordinate bounded jet parameters, natural-coordinate models, and source/jet estimates. These are bound and parameter layers, not selected-field moment equality.",
        "anchors": "50-177; 394-399; 601-689",
    },
    "NavierStokes/PrimaryODE.lean": {
        "clusters": ["profiles", "residual", "jets", "cartesian-assembly"],
        "finding": "Defines moving-frame data, projected forcing, a finite-interval Volterra solution, ambient reconstruction, smoothness, and primary coefficient/energy bounds. It contains no final radial moment transport theorem.",
        "anchors": "31-111; 189-245; 254-342; 415-460",
    },
    "NavierStokes/GraphCalculus.lean": {
        "clusters": ["axis", "cartesian-assembly", "jets"],
        "finding": "Defines the auxiliary graph pullback and proves radial/time derivative and mixed-derivative identities using genuine Frechet derivatives. The radial formulas require a nonzero radius and do not evaluate barMoment or transport the selected field's five observables.",
        "anchors": "6-12; 22-51; 69-105; 181-209",
    },
    "NavierStokes/LocalizedMeanInteraction.lean": {
        "clusters": ["cartesian-assembly", "residual", "jets", "rank"],
        "finding": "Defines local mean/vector classes and proves localised mean-wave, wave-wave, interaction-block, and residual-difference rate estimates under support, frequency, and solenoidal hypotheses. These are local interaction/rate results; no final selected Cartesian radial-moment equality is exported.",
        "anchors": "25-40; 326-342; 378-398; 451-469",
    },
    "NavierStokes/NaturalAxisRange.lean": {
        "clusters": ["axis", "profiles", "pressure", "time"],
        "finding": "Packages small parameter bounds, proves a unique negative axis root, lower source margins, and existence of smooth cutoff parameters. This controls reduced axis geometry and cutoff choices, but does not transport those data through the selected Cartesian tsum field into barMoment.",
        "anchors": "12-23; 121-139; 212-229; 241-250",
    },
    "NavierStokes/PulseGrowth.lean": {
        "clusters": ["profiles", "time", "residual"],
        "finding": "Defines the scalar pulse net-growth rate after damping and proves its complete sign classification relative to the threshold. This is scalar pulse algebra, not a PDE residual theorem or a selected-field five-moment transport result.",
        "anchors": "18-35; 108-127",
    },
    "NavierStokes/TorusMeanRequestRebase.lean": {
        "clusters": ["cartesian-assembly", "moments", "pressure"],
        "finding": "Proves identity/rebase and freeze compatibility for signed-wave state requests, including reference-request equalities after coordinate swaps. The declarations bind request data across coordinate representations; they do not evaluate torus averages or identify the final field with the paper's five observables.",
        "anchors": "164-176; 267-291",
    },
    "NavierStokes/BaseStressClasses.lean": {
        "clusters": ["profiles", "moments", "rank", "jets", "cartesian-assembly"],
        "finding": "Builds weighted stress classes, chart composition bounds, edge-distance/growth controls, and leading/higher/virtual stress component classes for the slow base. These are substantive reduced stress and jet estimates; they do not provide selected Cartesian tsum-to-barMoment transport.",
        "anchors": "31-104; 147-233; 294-326; 455-524",
    },
    "NavierStokes/ChartScales.lean": {
        "clusters": ["profiles", "jets", "time"],
        "finding": "Source-reviewed: native chart scales, coefficient identities, carrier bounds, and asymptotic decay are substantive; no selected-field radial-moment transport theorem is stated here.",
        "anchors": "5-34; 122-208; 210-255; 257-307",
    },
    "NavierStokes/EndpointCoordinates.lean": {
        "clusters": ["cartesian-assembly", "axis", "jets"],
        "finding": "Source-reviewed: endpoint similarity-coordinate extensions and Cartesian smooth/jet agreement are substantive on their stated domains; no torus-average, barMoment, or five-moment selected-field theorem is stated here.",
        "anchors": "1-2; 23-40; 72-185; 228-326",
    },
    "NavierStokes/R3/CompactComparisonBounds.lean": {
        "clusters": ["energy", "cartesian-assembly"],
        "finding": "Source-reviewed: compact-slice, derivative, L3, cutoff-plateau, and compact-slab finite-energy estimates are substantive; no selected-field five-moment transport theorem is stated here.",
        "anchors": "1-3; 24-47; 49-98; 102-129; 133-155",
    },
    "NavierStokes/R3/ComparisonFiniteEnergy.lean": {
        "clusters": ["energy", "residual"],
        "finding": "Source-reviewed: finite-energy difference, tensor-difference integrability, and uniform Lp comparison bounds are substantive; no selected-field radial-moment or barMoment transport theorem is stated here.",
        "anchors": "1-2; 22-121; 124-172; 175-228",
    },
    "NavierStokes/R3/ComparisonSetup.lean": {
        "clusters": ["energy", "residual"],
        "finding": "Source-reviewed: comparison slabs, spatial derivatives, Lp/L2 energies, weighted energy/dissipation, and tensor differences are defined; no selected-field five-moment transport theorem is stated here.",
        "anchors": "22-53",
    },
    "NavierStokes/R3/LocalizedDifferenceEnergy.lean": {
        "clusters": ["energy", "residual", "pressure"],
        "finding": "Source-reviewed: cutoff-weighted difference energy integrability, continuity, derivative, and balance identities are substantive; no selected-field radial-moment or barMoment theorem is stated here.",
        "anchors": "34-101; 102-221",
    },
    "NavierStokes/R3/LocalizedLaplacian.lean": {
        "clusters": ["energy", "cartesian-assembly"],
        "finding": "Source-reviewed: weighted Laplacian integrability and integration-by-parts identities are substantive local analytic infrastructure; no selected-field five-moment transport theorem is stated here.",
        "anchors": "35-74; 85-153",
    },
    "NavierStokes/R3/SharpEnergyBound.lean": {
        "clusters": ["energy"],
        "finding": "Source-reviewed: scalar square-root and squared-energy inequalities are substantive; no field-level moment or selected endpoint transport theorem is stated here.",
        "anchors": "20-68",
    },
    "NavierStokes/R3/SpatialCauchySchwarz.lean": {
        "clusters": ["energy"],
        "finding": "Source-reviewed: spatial velocity-force work is bounded by L2 energies; no selected-field radial-moment or barMoment transport theorem is stated here.",
        "anchors": "22-46",
    },
    "NavierStokes/R3/WholeSpaceEnergyLimit.lean": {
        "clusters": ["energy", "endpoint"],
        "finding": "Source-reviewed: cutoff-weighted integrals converge to whole-space energy integrals and zero-field consequences are proved; no five-observable selected-field transport theorem is stated here.",
        "anchors": "25-38; 40-93",
    },
    "NavierStokes/SlotGeometry.lean": {
        "clusters": ["cartesian-assembly", "axis"],
        "finding": "Source-reviewed: plane-cover, lattice/torus-equivalence, slot-centre, lifted-support separation, and oriented-slot geometry are substantive; no torusAverage-to-barMoment selected-field theorem is stated here.",
        "anchors": "28-187; 208-282; 311-376; 387-477",
    },
    "NavierStokes/AnnularEndpoint.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "residual", "time"],
        "finding": "Source-reviewed: shrinking-support lemmas prove common terminal zero neighbourhoods, closure under tsum/potentialSum, curl support, local extensions, and eventual equality of the concrete Cartesian residual. These are germ/support and residual-localisation results, not a global radial-moment transport theorem or a nonzero defect.",
        "anchors": "1-12; 101-198; 207-278; 405-435; 440-520; 524-603",
    },
    "NavierStokes/AxisContraction.lean": {
        "clusters": ["axis", "profiles", "residual"],
        "finding": "Source-reviewed: defines controlled operator algebra, natural-axis data, fixed-point contraction thresholds, integrated coefficient equations, and angular/axial jet-error bounds. The result is reduced coefficient-space control; no selected Cartesian field five-moment equality, torus-average map, or endpoint Witness transport is stated here.",
        "anchors": "35-227; 287-400; 465-610; 618-753",
    },
    "NavierStokes/PhysicalCopyBounds.lean": {
        "clusters": ["cartesian-assembly", "jets", "time", "residual"],
        "finding": "Source-reviewed: defines copy-family periodisation, support cells, locally finite/germ reduction, smooth periodised sums, and native jet bounds. It proves local support and derivative control for copy sums, but does not evaluate barMoment or transport the paper's five radial observables through the periodised tsum.",
        "anchors": "1-18; 71-105; 116-218; 231-240; 266-336; 600-681",
    },
    "NavierStokes/R3/LocalizedFluxEstimates.lean": {
        "clusters": ["r3", "energy", "residual", "pressure"],
        "finding": "Source-reviewed: supplies integrability and bounds for nonlinear coupling, pressure, viscous, and cutoff-flux terms in the whole-space localized comparison energy argument. This is a comparison-energy layer and states no selected-field radial-moment or five-row transport theorem.",
        "anchors": "1-6; 19-43; 45-95; 97-166; 168-232",
    },
    "NavierStokes/ResetEnergyBounds.lean": {
        "clusters": ["energy", "profiles", "pressure"],
        "finding": "Source-reviewed: defines the scheduled angular-reset density/energy, support, smoothness, integrability, normalization, and small-energy bounds. It establishes intermediate tail-energy control, not transport of the five paper moments into the selected Cartesian field.",
        "anchors": "1-20; 22-116; 176-268; 270-307; 313-390; 420-450",
    },
    "NavierStokes/ScaledActualParticularControl.lean": {
        "clusters": ["profiles", "jets", "cartesian-assembly"],
        "finding": "Source-reviewed: records scaled particular-profile control and terminal-tail coefficient/stress bounds. The declarations are profile-scale estimates; no final Cartesian tsum-to-barMoment equality or selected Witness field transport is stated.",
        "anchors": "source declaration scan; verify full line anchors in the companion report",
    },
    "NavierStokes/TerminalCone.lean": {
        "clusters": ["profiles", "axis", "pressure", "time"],
        "finding": "Source-reviewed: constructs terminal-tail clocks, normalized radius/carrier quantities, mass and stress profiles, cone margins, and endpoint relations. These are reduced-profile/cone inequalities; no global Cartesian five-moment transport theorem is stated.",
        "anchors": "1-50; 53-110; 116-255; 259-308; 313-465; 477-566",
    },
    "NavierStokes/ViscousPropagator.lean": {
        "clusters": ["energy", "jets", "time"],
        "finding": "Source-reviewed: proves Hilbert-space norm/envelope estimates, finite-dimensional two-mode energy bounds, harmonic damping, and pulse propagator estimates. This is an analytic coefficient-energy layer; it is not a selected-field moment or pressure-semantics bridge.",
        "anchors": "1-14; 25-234; 254-353; 353-389; 419-483",
    },
    "NavierStokes/VolterraAnalyticBounds.lean": {
        "clusters": ["profiles", "jets", "energy"],
        "finding": "Source-reviewed: defines complex Volterra words, radial/analytic/matrix bounds, factorial majorants, summable word layers, and locally uniform series convergence for the reduced slow-axis recursion. It does not state selected Cartesian field radial-moment transport or a torusAverage-to-barMoment theorem.",
        "anchors": "1-12; 23-200; 208-373; 384-430; 440-524; 534-598",
    },
    "NavierStokes/ActivationBounds.lean": {
        "clusters": ["profiles", "jets", "residual", "pressure"],
        "finding": "Source-reviewed: defines smooth activation/error factors, transformed density/history terms, compact-parameter jet bounds, and continuation/independence results. This is reduced activation infrastructure; no selected Cartesian five-moment or barMoment transport theorem is stated.",
        "anchors": "1; 22-226; 241-324; 330-414; 453-464; 522-687",
    },
    "NavierStokes/ActualWaveRegularity.lean": {
        "clusters": ["cartesian-assembly", "jets", "time", "residual"],
        "finding": "Source-reviewed: proves native/common/corrected wave smoothness, zero germs, translation compatibility for cylindrical curls and tsum amplitudes, and finite cycle regularity. These are local regularity results, not the final Cartesian five-observable transport theorem.",
        "anchors": "1-15; 27-154; 172-279; 291-486; 510-555; 605-869",
    },
    "NavierStokes/CommonBaseContext.lean": {
        "clusters": ["profiles", "axis", "cartesian-assembly", "residual", "moments"],
        "finding": "Source-reviewed: proves chart/physical operator matching, cover-lift and pullback identities, periodicity, nominal-profile context bounds, stress classes, and primary coefficient matching. This is reduced context naturality, not a selected Cartesian torusAverage-to-barMoment theorem.",
        "anchors": "1-15; 25-103; 118-160; 165-373; 396-451; 463-625",
    },
    "NavierStokes/CopySolveCompatibility.lean": {
        "clusters": ["cartesian-assembly", "time", "jets", "residual"],
        "finding": "Source-reviewed: proves geometry/copy refinement, transported coefficients and forcing, source periodicity, time-clock transport, tsum congruence, physical-output smoothness, and compatible-family representation. It is generic copy-solve transport, not selected-field radial-moment transport.",
        "anchors": "1; 20-178; 181-327; 331-498; 507-588; 613-687",
    },
    "NavierStokes/LocalizedCurlRealization.lean": {
        "clusters": ["cartesian-assembly", "jets", "residual"],
        "finding": "Source-reviewed: proves patchwise cylindrical curl realization, divergence-zero identities, smoothness, tangency, zero-germ inheritance, and common-field assembly. This is local curl infrastructure, not a selected Cartesian torusAverage-to-barMoment or five-observable transport theorem.",
        "anchors": "1-10; 48-120; 124-167; 169-240; 244-257; 272-305",
    },
    "NavierStokes/MixedDiagonalExtensions.lean": {
        "clusters": ["cartesian-assembly", "endpoint", "residual", "time"],
        "finding": "Source-reviewed: proves potential-level shrinking support, eventual zero, stage-zero replacement, one-sided extension, and diagonal away-extension assembly for the natural sum. These are support/germ statements, not radial-moment evaluation or a nonzero selected-field defect.",
        "anchors": "1-3; 29-47; 50-95; 99-130; 134-154; 158-210",
    },
    "NavierStokes/ActualCarrierTransport.lean": {
        "clusters": ["cartesian-assembly", "profiles"],
        "finding": "Source-reviewed: identifies primitive carrier geometry, lengths, cutoffs, and fixed/canonical parameter records by definitional equalities and native-cutoff transport. No field, curl, radial observable, moment, or endpoint Witness theorem is stated.",
        "anchors": "1-10; 19-28; 32-64",
    },
    "NavierStokes/FiniteHeadClass.lean": {
        "clusters": ["jets", "profiles"],
        "finding": "Source-reviewed: transfers finite-prefix weighted jet bounds and class membership across exponents, with zero-tail derivative control. It does not evaluate radial observables or connect a class predicate to the selected Cartesian field.",
        "anchors": "1-8; 21-64; 65-93; 95-127",
    },
    "NavierStokes/CorrectedPulseAmplitude.lean": {
        "clusters": ["profiles", "moments", "energy"],
        "finding": "Source-reviewed: constructs the corrected angular energy integrand and proves smooth amplitude selection, zero corrected total energy, derivative bounds, uniqueness, and zero radial-energy integral. This is an energy-reset identity, not selected Cartesian five-observable transport.",
        "anchors": "1-2; 21-64; 404-422; 424-464",
    },
    "NavierStokes/PrimaryGeometryAssembly.lean": {
        "clusters": ["cartesian-assembly", "profiles", "axis"],
        "finding": "Source-reviewed: constructs open cells, carriers, phase/frequency/axial/shear data, chart geometry, angular modes, and normalized-stress identifications. This is reduced geometry and parameter binding, not a final Cartesian torusAverage-to-barMoment theorem.",
        "anchors": "1-2; 29-198; 225-239; 356-391; 498-595",
    },
    "NavierStokes/R3/ComparisonTimeAverages.lean": {
        "clusters": ["r3", "energy", "pressure"],
        "finding": "Source-reviewed: proves time-average integrability, finite-energy L2 bounds, componentwise square-integrability, and nonlinear tensor-difference integrability. It does not identify selected radial profiles or transport the five paper observables.",
        "anchors": "1-3; 25-134; 274-293; 295-344; 346-368",
    },
    "NavierStokes/SlowFirstOrderEdge.lean": {
        "clusters": ["profiles", "moments", "pressure", "axis"],
        "finding": "Source-reviewed: proves first-order radial source/stress factorisation, scaling, integrability, edge jets, and conditional forward-stress equality. The source explicitly delegates global moment closure to separate renormalized-moment and slow-order theorems; its scalar weighted-zero premise is not the final Cartesian five-observable transport theorem.",
        "anchors": "1; 21-239; 622-670; 679-725; 739-751",
    },
    "NavierStokes/ActualBaseVelocityBounds.lean": {
        "clusters": ["energy", "time", "cartesian-assembly", "profiles"],
        "finding": "Source-reviewed: derives actual exterior coefficient properties, leading-velocity agreement, finite-jet bounds, middle-region rates, and outer-region rates for the constructed slow-base velocity. The source notes that support and zero-mass identities come from coefficient construction, but it does not state the final Cartesian tsum-to-barMoment five-observable transport theorem.",
        "anchors": "415-449; 473-544; 546-557",
    },
    "NavierStokes/BaseContextAssembly.lean": {
        "clusters": ["axis", "moments", "residual", "cartesian-assembly"],
        "finding": "Source-reviewed: assembles scaled radial/frequency/axial base components, virtual stress, physical component identities, smoothness, native estimates, unweighted bounds, normalized stress, and inner stress vanishing. This is an intermediate reduced stress-realisation layer, not final selected Cartesian five-observable transport.",
        "anchors": "425-468; 470-544; 546-620",
    },
    "NavierStokes/PhaseEstimates.lean": {
        "clusters": ["axis", "time", "cartesian-assembly"],
        "finding": "Source-reviewed: proves representative normal-velocity, slope, phase, direction, angular-velocity, and uniform radial-slope bounds. These are quantitative phase/parameter estimates; no radial integral evaluator or selected-field five-moment transport theorem is stated.",
        "anchors": "440-475; 950-971; 985-1000",
    },
    "NavierStokes/PrimaryRepresentatives.lean": {
        "clusters": ["axis", "cartesian-assembly", "time"],
        "finding": "Source-reviewed: defines smooth supported native masks, grid boxes, active representatives, normalized physical masks, support-distance bounds, mesh convergence, and reference-cone parameters. This is representative geometry and covariance control, not final Cartesian tsum-to-barMoment transport.",
        "anchors": "53-118; 120-186; 188-220",
    },
    "NavierStokes/PositiveRepresentatives.lean": {
        "clusters": ["axis", "time", "cartesian-assembly"],
        "finding": "Source-reviewed: proves stable-branch coordinate bounds, positive-cell geometry, representative membership, and eventual fine-mesh containment. The inspected declarations do not state barMoment, torusAverage, or five-observable transport for the selected endpoint.",
        "anchors": "365-425; 452-487",
    },
    "NavierStokes/ReservedPatches.lean": {
        "clusters": ["moments", "rank", "profiles", "axis"],
        "finding": "Source-reviewed: constructs actual FiveProfileMoments patches, clean/heated fields, radial background identities, heat-increment support, and supported five-row updates. This confirms genuine upstream radial repair machinery, but does not prove its survival through the final Cartesian localization, periodization, tsum, and selected Witness boundary.",
        "anchors": "260-267; 288-357; 546-572; 576-590",
    },
    "NavierStokes/ActiveAnnulusWeight.lean": {
        "clusters": ["axis", "profiles", "jets", "time"],
        "finding": "Source-reviewed: defines logarithmic/radial edge distances, flat annulus weights, activation coefficients, radial pullbacks, weighted bounds, and terminal-edge factors. This is activation/collar machinery; no selected Cartesian radial-observable evaluator or five-moment transport theorem is stated.",
        "anchors": "23-76; 84-150; 247-310; 562-654; 957-1040; 1188-1234",
    },
    "NavierStokes/ActualParticularControl.lean": {
        "clusters": ["cartesian-assembly", "jets", "residual", "energy", "time"],
        "finding": "Source-reviewed: constructs selected moving-frame inputs, grouped source controls, phase patches, transported frames, coefficient/energy/kinematic bounds, and scaled selected-copy jets. These are particular-wave control results; no final Cartesian five-observable equality is stated.",
        "anchors": "36-112; 195-274; 564-609; 710-825; 868-1061",
    },
    "NavierStokes/EndpointExtension.lean": {
        "clusters": ["jets", "time"],
        "finding": "Source-reviewed: proves one-sided derivative-jet gluing, endpoint smoothness, and zero extension. This is generic regularity infrastructure and contains no physical radial observable or selected-Witness moment transport statement.",
        "anchors": "25-48; 62-113; 129-163",
    },
    "NavierStokes/FlatDyadicExtension.lean": {
        "clusters": ["jets", "axis", "time"],
        "finding": "Source-reviewed: proves little-o jet bounds, derivative/Taylor extension identities, smooth flat dyadic products, and face restrictions. These local extension results do not evaluate global radial integrals or prove five-moment preservation.",
        "anchors": "28-60; 115-210; 248-255",
    },
    "NavierStokes/LocalMeanPhysicalBounds.lean": {
        "clusters": ["cartesian-assembly", "jets", "axis", "residual"],
        "finding": "Source-reviewed: supplies local field and angular-field germs, smoothness, curl bounds, local-band jet bounds, and sublevel estimates on the normalized slow region. No barMoment/torusAverage composition or final selected-field five-moment theorem is stated.",
        "anchors": "25-107; 136-232; 250-320",
    },
    "NavierStokes/MovingFrameODE.lean": {
        "clusters": ["axis", "residual", "energy", "cartesian-assembly"],
        "finding": "Source-reviewed: defines the packed moving frame, normal/tangent motion, projected ODE, smooth frame reconstruction, modal equations, operator bounds, and modal energy estimates. This is frame kinematics/modal algebra, not radial observable transport to the selected Cartesian endpoint.",
        "anchors": "28-106; 158-227; 245-341; 368-469; 678-840",
    },
    "NavierStokes/NativeCutoffJets.lean": {
        "clusters": ["jets", "time", "axis"],
        "finding": "Source-reviewed: defines the literal transported native cutoff and proves reference-transport equality, core/germ identities, and uniform local iterated-jet bounds. This is local cutoff-jet control; no global selected-field radial-moment transport theorem is stated.",
        "anchors": "27-39; 51-82; 92-105",
    },
    "NavierStokes/NilpotentVolterra.lean": {
        "clusters": ["profiles", "jets", "residual", "cartesian-assembly"],
        "finding": "Source-reviewed: constructs weighted means, regular primitives, coefficient actions, holomorphic path words, analytic layers, summable solutionSeries, regular solutions, and uniqueness. This is genuine Volterra/infinite-series infrastructure, not a selected Cartesian barMoment/torusAverage five-observable theorem.",
        "anchors": "36-163; 173-237; 474-708; 796-905; 915-1058",
    },
    "NavierStokes/PhysicalWaveSum.lean": {
        "clusters": ["cartesian-assembly", "jets", "axis", "time"],
        "finding": "Source-reviewed: constructs chart/carrier lifts, supported masks, locally finite masked physical waves, smooth vector sums, support geometry, and jet bounds. It contains real local-finiteness and realised-curl infrastructure, but no equality between the full physical sum and the paper's five radial observables.",
        "anchors": "152-187; 227-378; 470-559; 585-720; 731-796; 825-976",
    },
    "NavierStokes/SmoothLoop.lean": {
        "clusters": ["moments", "profiles", "axis"],
        "finding": "Source-reviewed: defines angular means and proves cosine/exponential tilt mean, variance, projection, stress, rephasing, and positive circle-density identities. This is genuine angular-moment machinery, not transport of the five paper radial observables through the selected Cartesian assembly.",
        "anchors": "31-117; 127-222; 230-350; 360-590",
    },
    "NavierStokes/TailEnergyBounds.lean": {
        "clusters": ["energy", "profiles", "jets", "time"],
        "finding": "Source-reviewed: proves tail energy-density positivity, release/plateau bounds, integrability, split formulas, post-pulse energy control, smoothness, and parameter derivative estimates. This is substantive outgoing-tail energy control, not a selected-field five-observable equality.",
        "anchors": "22-120; 140-262; 271-410; 424-510; 512-707",
    },
    "NavierStokes/WaveInteractionBounds.lean": {
        "clusters": ["cartesian-assembly", "residual", "jets", "moments", "axis"],
        "finding": "Source-reviewed: proves wave-class closure, mean/wave products, harmonic bounds, finite sums, support-separated products, exact curl-interaction zero results under explicit hypotheses, Cartesian transport components, and realised stage bounds. These positive cancellations refute any claim that every curl interaction is necessarily nonzero, but do not establish the complete selected global five-observable transport theorem.",
        "anchors": "148-217; 233-337; 399-500; 629-697; 877-1029; 1035-1183",
    },
    "NavierStokes/ActualCurrentCarrierJets.lean": {
        "clusters": ["axis", "jets", "cartesian-assembly"],
        "finding": "Source-reviewed: proves actual carrier phase/character identities, smooth-neighbourhood results, positivity, and control-patch jets. This is native carrier regularity and does not evaluate global radial observables.",
        "anchors": "21-71; 75-127; 137-201",
    },
    "NavierStokes/AllBandBaseJets.lean": {
        "clusters": ["profiles", "jets", "axis", "cartesian-assembly"],
        "finding": "Source-reviewed: proves leading/zero cutoff identities, normalized error envelopes, actual estimates, polynomial normalized streams, reduced radial polynomial forms, radial envelopes/quotients, uniform radial jets and final weighted-bundle estimates. This is substantive reduced radial/base machinery, not the complete selected Cartesian five-observable equality.",
        "anchors": "27-91; 118-185; 221-366; 393-447",
    },
    "NavierStokes/AnalyticCoefficientBounds.lean": {
        "clusters": ["profiles", "jets", "axis"],
        "finding": "Source-reviewed: proves holomorphic tube/coefficient bounds, real jets, radius-loss summability, axis-space conversion, and normalized exponential estimates. These are analytic coefficient controls, not a physical radial-moment evaluator.",
        "anchors": "24-148; 174-243; 255-340",
    },
    "NavierStokes/BaseRadialJets.lean": {
        "clusters": ["profiles", "axis", "jets", "cartesian-assembly", "moments"],
        "finding": "Source-reviewed: constructs the averaged axial sequence, normalized stream, and literal normalized radial component of the constructed curl base, proving radial_eq, radial_eq_stream, reduced radial polynomial/envelope/jet results, and final_radial_eq. This is positive base-level radial realisation, but not the complete selected Cartesian five-observable transport theorem.",
        "anchors": "23-120; 144-177; 189-329; 363-386",
    },
    "NavierStokes/CurrentPhysicalChartJets.lean": {
        "clusters": ["axis", "jets", "cartesian-assembly"],
        "finding": "Source-reviewed: proves physical polar-chart smoothness and positive jets, composition/rotation jets, chart scaling/germ identities, and real-vector norm bounds. This is chart-lift regularity, not global radial-moment transport.",
        "anchors": "45-141; 159-235; 258-289",
    },
    "NavierStokes/FlatZeroExtension.lean": {
        "clusters": ["jets", "time"],
        "finding": "Source-reviewed: defines zero extension and proves local Gaussian bounds, flat edge derivatives, iterated-derivative identities, and joint smoothness. This endpoint regularity layer contains no global moment identity.",
        "anchors": "30-102; 141-237",
    },
    "NavierStokes/ParametricRephase.lean": {
        "clusters": ["profiles", "moments", "jets"],
        "finding": "Source-reviewed: constructs parameter-dependent phase maps and exact inverses, proving bijectivity, inverse-function smoothness, periodicity, rephased-family identities, and smooth parameter integrals. This is rephasing/integration infrastructure, not five-observable radial transport.",
        "anchors": "26-69; 106-179; 189-283",
    },
    "NavierStokes/RadialAlias.lean": {
        "clusters": ["moments", "profiles", "axis", "residual"],
        "finding": "Source-reviewed: defines translated and whole-line radial aliases using actual interval/Bochner integrals, radial support, directional derivatives, support-based endpoint cancellation, integration-by-parts/source-jet identities, and norm bounds. This is genuine radial integral infrastructure, but no connection to the selected Witness five-tuple is stated.",
        "anchors": "28-47; 50-132; 161-215; 226-260",
    },
    "NavierStokes/ScaledParticularFrameJets.lean": {
        "clusters": ["jets", "cartesian-assembly", "axis"],
        "finding": "Source-reviewed: proves scaled frame normal/motion/action jets, affine argument geometry, frame-field native jets, selected-frame identities, and native normal bounds. This is particular-frame jet control, not five-observable transport.",
        "anchors": "31-55; 96-152; 177-260",
    },
    "NavierStokes/SmoothParameterIntegral.lean": {
        "clusters": ["jets", "profiles", "moments"],
        "finding": "Source-reviewed: defines genuine parameter jets and proves differentiation, Taylor expansion, smoothness, and interval-integral regularity under local integrable majorants. This is general integration infrastructure and supplies no selected physical moment equality.",
        "anchors": "27-118; 127-214; 227-311",
    },
    "NavierStokes/SpacetimeEndpoint.lean": {
        "clusters": ["time", "jets", "cartesian-assembly"],
        "finding": "Source-reviewed: defines open/closed past sets and proves trace extension, boundary continuity, periodicity, mixed-jet extension, smooth Taylor families, and joint endpoint extension. This is spacetime boundary regularity, not radial-observable transport.",
        "anchors": "25-139; 175-262; 277-374",
    },
    "NavierStokes/NaturalCoefficientBridge.lean": {
        "clusters": ["profiles", "moments", "pressure", "axis"],
        "finding": "Transfers natural reduced equations to coefficient zeros, radial averages, histories, and zero inner radial stress primitives under explicit hypotheses. This is a reduced natural-to-radial bridge, not the final Cartesian tsum-to-moment bridge.",
        "anchors": "114-205; 296-320; 463-505",
    },
    "NavierStokes/GaugeDebtIncrement.lean": {
        "clusters": ["rank", "moments", "corrections", "pressure"],
        "finding": "Defines the actual three-coordinate debt and proves moment-change formulas and rate-class bounds for wave and temporal updates. The debt update is intermediate physical rank machinery and is not an endpoint five-observable equality.",
        "anchors": "5-10; 169-220; 323-423; 448-667",
    },
    "NavierStokes/GlobalStressSupport.lean": {
        "clusters": ["moments", "pressure", "rank", "profiles"],
        "finding": "Pulls slow profiles to signed radial histories and proves PositiveOrderMoments.moments = 0, conservative stress cancellations, exterior density/stress zeros, and nominal compact stress support. These are genuine upstream slow/radial results, not a final selected Cartesian endpoint theorem.",
        "anchors": "20-38; 119-180; 196-247; 428-473",
    },
    "NavierStokes/ActualCarrierGeometry.lean": {
        "clusters": ["cartesian-assembly", "axis"],
        "finding": "Builds signed-label carrier cells, phase/log bands, physical boxes, support lifting, injectivity, and disjointness under threshold hypotheses; no radial moment or Witness transport theorem is present.",
        "anchors": "50-342; cell_geometry, labelCarrier_*, geometry_liftedSupport, labelCarrier_disjoint",
    },
    "NavierStokes/ActualParticularBackground.lean": {
        "clusters": ["cartesian-assembly", "profiles"],
        "finding": "Proves reindexing/rescaling identities for actual wave-family normal, defect, and auxiliary data; this is intermediate coefficient construction, not selected Cartesian five-moment transport.",
        "anchors": "26-314; zeroRescale_*, backgroundFamily_eq, background_normal, background_defect",
    },
    "NavierStokes/ActualParticularGaussian.lean": {
        "clusters": ["profiles", "jets"],
        "finding": "Proves positive length/scale bounds and Gaussian envelope/gain bounds for active labels and cycle states; no barMoment or FiveRows endpoint export.",
        "anchors": "40-229; gaussianLength_*, envelope_gaussian, globalGaussian_all_gains, gaussianBlock_all_gains",
    },
    "NavierStokes/ActualSignedGaussian.lean": {
        "clusters": ["profiles", "jets"],
        "finding": "Constructs actual signed Gaussian local fields with zero regions, smooth jets, and gain bounds; no five-observable equality for the final selected field.",
        "anchors": "34-267; localGaussian_formula, localGaussian_zero_*, actual_gaussianBlock_jets",
    },
    "NavierStokes/AnalyticPrimitive.lean": {
        "clusters": ["profiles"],
        "finding": "Provides complex analytic primitive and smooth-factor machinery; it does not transport a fluid field or radial moment tuple to the endpoint.",
        "anchors": "26 onward; primitive, segment_mem, continuity and smooth-factor declarations",
    },
    "NavierStokes/CartesianCopySource.lean": {
        "clusters": ["cartesian-assembly", "axis"],
        "finding": "Pulls source profiles into Cartesian coordinates through rotation and annular jet bounds. rotationMap_smooth is explicitly off-axis, requiring y ≠ 0; no global moment bridge is supplied.",
        "anchors": "20 onward; pullStrip, rotationMap, rotationMap_smooth, rotationMap_jets, rotatedSource",
    },
    "NavierStokes/CauchyRestriction.lean": {
        "clusters": ["profiles"],
        "finding": "Develops bounded disk restrictions, Cauchy maps, derivative continuous linear maps, and complex integral identities; it is not a selected Navier-Stokes moment theorem.",
        "anchors": "24-296; restrictionLinear, cauchyMap, derivativeCLM, derivativeCLM_apply_integral",
    },
    "NavierStokes/Covariance.lean": {
        "clusters": ["profiles", "rank"],
        "finding": "Reconstructs finite-dimensional covariance coefficients and positive amplitudes under determinant hypotheses; no field-level endpoint moment equality.",
        "anchors": "29-207; signedMatrix, reconstruct, solution_unique, amplitudes_pos",
    },
    "NavierStokes/CurlGeometry.lean": {
        "clusters": ["cartesian-assembly", "axis"],
        "finding": "Proves algebraic cross-product/transversality and cylindrical curl/divergence identities; it supports solenoidal construction but does not evaluate selected radial integrals.",
        "anchors": "19-157; cross, curl_symbol_transverse, cylindrical_div_curl",
    },
    "NavierStokes/FlatPrimitive.lean": {
        "clusters": ["profiles", "jets"],
        "finding": "Builds flat primitives with derivative, recurrence, normalisation, positivity, and zero-limit results; no tsum-to-moment theorem.",
        "anchors": "25-291; primitive_hasDerivAt, primitive_recurrence, normalizedPrimitive_factorization",
    },
    "NavierStokes/FlatPrimitiveFactor.lean": {
        "clusters": ["profiles", "jets"],
        "finding": "Proves parameterised coordinate/factorisation, integrability, smoothness, and derivative bounds under positive-coordinate hypotheses; no global selected-field moment equality.",
        "anchors": "26-315; coordinate_image, factor_eq_normalized_primitive, exists_smooth_factor",
    },
    "NavierStokes/GaussianErrorNaturality.lean": {
        "clusters": ["profiles", "jets", "cartesian-assembly"],
        "finding": "Transports Gaussian error, cutoff, tail, source, amplitude, and reference-to-actual data under linear maps; the transported objects are not identified with the five selected radial observables.",
        "anchors": "23-455; fast_cutoff_transport, globalGaussian_transport, fromReference_*",
    },
    "NavierStokes/HolomorphicFamily.lean": {
        "clusters": ["profiles"],
        "finding": "Proves holomorphic/continuous parameter-family and Cauchy-integral regularity; no selected PDE endpoint or radial moment transport theorem.",
        "anchors": "21-359; contDiffOn_cauchyValue, cauchyValue_eq, hasFDerivAt_joint",
    },
    "NavierStokes/LocalAngularDiagonal.lean": {
        "clusters": ["cartesian-assembly", "moments", "jets"],
        "finding": "Relates a local angular series to potential/direct diagonal fields and proves smoothness, zero germs, and divergence under similarity-domain hypotheses; it stops before global five-moment endpoint evaluation.",
        "anchors": "30-183; rawSeries_eq, angularSum_eq_potentialSum, angularSum_divergence",
    },
    "NavierStokes/ParametricEvenDescent.lean": {
        "clusters": ["axis", "profiles"],
        "finding": "Provides even radial descent, localised smoothness, and axis-local derivative identities; no selected Cartesian moment transport.",
        "anchors": "47-367; radialReduce_integral, even_radialReduce, descend_localized_eventuallyEq",
    },
    "NavierStokes/ParametricFlatFactor.lean": {
        "clusters": ["profiles", "jets"],
        "finding": "Provides parameterised flat kernels, factors, primitives, factorisations, and smoothness; no endpoint observable identity.",
        "anchors": "53-259; kernel, factor, primitive, primitive_factorization, exists_joint_smooth_factor",
    },
    "NavierStokes/ParametricKernelBounds.lean": {
        "clusters": ["jets", "cartesian-assembly"],
        "finding": "Proves derivative and iterated-derivative bounds for parameterised coordinates, amplitudes, and kernels; these are rate estimates, not a five-moment payload.",
        "anchors": "29-324; coordinate_derivative_bound, amplitude_joint_derivative_bound, rawKernel_iteratedFDeriv_bound",
    },
    "NavierStokes/PrimaryMaterialDefect.lean": {
        "clusters": ["residual", "profiles", "jets"],
        "finding": "Defines native material coordinates, affine pullbacks, defect formulas/classes, and finite jet bounds; it is intermediate defect bookkeeping and does not state the final Witness moment equality.",
        "anchors": "27-450; NativeCoordinates, material_pullback, defect_formula, finite_jet_bounds",
    },
    "NavierStokes/R3/GradientOperator.lean": {
        "clusters": ["r3", "jets"],
        "finding": "Proves pointwise Cartesian derivative/operator-norm estimates and continuity of the gradient square; no radial moment transport.",
        "anchors": "20-57; gradientSq_*, fderiv_apply_eq_sum, norm_fderiv_le_three_mul_sqrt_gradientSq",
    },
    "NavierStokes/R3/WeightedSobolev.lean": {
        "clusters": ["r3", "energy", "jets"],
        "finding": "Proves compact-support integrability, cutoff-gradient amplitude bounds, and a weighted Sobolev inequality; it supports analytic estimates but does not identify selected moments.",
        "anchors": "32-237; memLp_of_compact, cutoffGradientAmplitude, weighted_sobolev",
    },
    "NavierStokes/Scaling.lean": {
        "clusters": ["profiles", "jets"],
        "finding": "Proves algebraic core/length/Reynolds scaling and carrier-frequency bounds under positivity assumptions; no physical-field moment transport.",
        "anchors": "24-230; coreVelocity, radialLength, wave_power_cancellation, carrier_frequency_sqrt_bounds",
    },
    "NavierStokes/SimilarityApproach.lean": {
        "clusters": ["jets", "time"],
        "finding": "Proves similarity-scale bounds, q → 0, and jet limits from explicit JetRate hypotheses; this is a limit route, not the five radial observables.",
        "anchors": "24-93; upperScale_*, physical_q_*, jet_tendsto_zero",
    },
    "NavierStokes/SlowDivergence.lean": {
        "clusters": ["moments", "axis", "residual"],
        "finding": "Proves reduced radial-flux identities, history/integral representations, axial balance, and slow-order divergence. Division-based smoothness is scoped away from the axis; later history identities remove that division. It is not a global selected Cartesian endpoint theorem.",
        "anchors": "21-170; radialFlux_*, physical_flux_axial_balance, slow_order_divergence",
    },
    "NavierStokes/SmoothCovariance.lean": {
        "clusters": ["profiles", "rank"],
        "finding": "Proves smooth finite-dimensional covariance reconstruction and compact perturbation stability margins; no endpoint moment transport.",
        "anchors": "27-346; StrictCone, reconstruct_amplitudes, compact_perturbation_stability",
    },
    "NavierStokes/SmoothPathFamily.lean": {
        "clusters": ["time", "profiles"],
        "finding": "Proves smooth parameter/path families and ODE-family derivative identities; no selected-field observable theorem.",
        "anchors": "34-263; continuousOn_pathFamily, contDiffOn_odeFamily_of_joint, odeFamily_hasDerivWithinAt",
    },
    "NavierStokes/UniformCone.lean": {
        "clusters": ["profiles", "rank"],
        "finding": "Proves compact cone margins, gaps, and perturbation stability; no selected radial moment equality.",
        "anchors": "29-268; compact_normalized_cone_gap, compact_trueCone_stable, compact_family_quadratic_stable",
    },
    "NavierStokes/ValidBandGluing.lean": {
        "clusters": ["cartesian-assembly", "jets"],
        "finding": "Compatible local representatives glue while preserving smoothness, germs, jets, and spatial curls; it does not state preservation of the five global moments.",
        "anchors": "20-172; Compatible, representative_jet_bound, representative_spatialCurl_*",
    },
    "NavierStokes/ValidDyadicBandCover.lean": {
        "clusters": ["cartesian-assembly", "jets", "time"],
        "finding": "Dyadic bands cover the sublevel region and compatible fields glue with smoothness, germs, and jet bounds. Endpoint extension requires an explicit one-sided extension premise; no five-moment transport is present.",
        "anchors": "32-168; sublevel_covered, Compatible, field_jet_bound, field_endpoint_extension",
    },
    "NavierStokes/WaveStateRegularity.lean": {
        "clusters": ["profiles", "jets"],
        "finding": "Proves angular-average/covariance regularity, local wave-state data, support, and field-sum regularity; no selected endpoint moment identity.",
        "anchors": "26-288; angularAverage_smooth, LocalData.fieldSum_smooth, fieldSum_covariance_regular",
    },
    "NavierStokes/ComparatorBridge.lean": {
        "clusters": ["endpoint", "r3", "force"],
        "finding": "Bridges the project's (time, space) operators to the comparator convention, proves viscosity rescaling, periodicity, support, decay-to-force-condition, and a GlobalSolutionOne packaging predicate. It transports differential operators and candidate regularity, not the paper's five radial moments.",
        "anchors": "5-10; 20-58; 60-134; 144-221",
    },
    "NavierStokes/CurrentParticularPhysicalCoherence.lean": {
        "clusters": ["cartesian-assembly", "profiles", "jets"],
        "finding": "Cancels native ratio-power scales to prove equality of current-band local potential and pressure modes under explicit native transformation hypotheses. The result is band coherence, not a global selected-field moment transport theorem.",
        "anchors": "5-10; 21-50; 52-68",
    },
    "NavierStokes/CurrentPhysicalModeGerms.lean": {
        "clusters": ["axis", "cartesian-assembly", "residual"],
        "finding": "Constructs common-lift charts, positive-radius mode germs, transported residual sources, support-zero results, and band amplitude/pressure equalities. Its BandCoherence comment explicitly limits the object to primitive field, phase, and operator identities; no final Cartesian five-observable equality is stated.",
        "anchors": "5-10; 23-70; 670-777",
    },
    "NavierStokes/ExtendedHeatDebts.lean": {
        "clusters": ["moments", "profiles", "jets"],
        "finding": "Defines heat-tail correction, pressure/energy/angular physical edits, weighted and normalised debt jets, integrability, derivative, smoothness, and band bounds. These are intermediate scalar/profile debt estimates; the module supplies no theorem transporting them through the selected Cartesian tsum/curl/localisation endpoint.",
        "anchors": "82-121; 283-378; 433-510; 736-812; 1022-1110; 1173-1191",
    },
    "NavierStokes/HarmonicStructurePreservation.lean": {
        "clusters": ["rank", "profiles", "cartesian-assembly"],
        "finding": "Proves harmonic block addition, carrier and mode smoothness, cylindrical divergence addition, solenoidal mode preservation, and zero-mode/zero-pressure addition. These are local harmonic-state invariants and contain no selected-field radial moment transport.",
        "anchors": "23-81; 83-131; 147-168",
    },
    "NavierStokes/PhysicalResidualNaturality.lean": {
        "clusters": ["residual", "cartesian-assembly", "profiles"],
        "finding": "Proves coefficient/frame/state naturality under linear charts, including scalar and vector residual transport, source transport, angular averaging, mean residuals, and coherent state pullback/addition. The transported quantities are local residual and state structures; no theorem identifies the final field with (M,I,J,S,Cp) or proves a nonzero defect.",
        "anchors": "56-199; 201-319; 532-553; 678-777; 1029-1158; 1162-1195",
    },
    "NavierStokes/ActualInitialExcluded.lean": {
        "clusters": ["profiles", "jets", "cartesian-assembly", "moments"],
        "finding": "Constructs actual initial excluded/base-error continuation, native approach filters, physical error jet/prefix bounds, copied and periodised Gaussian classes, support, zero germs, and initial alias bounds. These are concrete initial-stage and Gaussian estimates, not final selected-field five-observable transport.",
        "anchors": "299-411; 666-718; 728-758; 1153-1199; 1208-1371",
    },
    "NavierStokes/ComparatorDefinitions.lean": {
        "clusters": ["endpoint", "force", "r3"],
        "finding": "Defines the comparator-side divergence, periodic/decay initial conditions, force conditions, and Navier-Stokes existence/smoothness structures. It supplies formal comparator predicates, not a theorem identifying the constructed witness with the paper's five radial observables.",
        "anchors": "37-93; 95-189; 191-249",
    },
    "NavierStokes/ParametricHeatTail.lean": {
        "clusters": ["profiles", "moments", "jets"],
        "finding": "Proves differentiability, domination, integrability, smoothness, decay, and jet bounds for parametric heat-tail corrections and physical pressure/energy/angular debt functions. These are scalar tail/profile results and do not transport the final Cartesian field through tsum, curl, and localisation.",
        "anchors": "28-112; 185-260; 377-477; 489-562; 571-811; 903-1062",
    },
    "NavierStokes/SignedMeanGain.lean": {
        "clusters": ["moments", "rank", "residual", "profiles"],
        "finding": "Builds signed covariance changes, wave-stage residual changes, torus mean estimates, local native assembly, and a quantitative mean-gain theorem. The source comment explicitly says the excluded Gaussian is retained and the raw mean estimate does not set it or its average to zero; no final selected five-moment equality is supplied.",
        "anchors": "24-111; 168-244; 286-337; 382-434; 920-970; 1091-1190; 1321-1360",
    },
    "NavierStokes/CylindricalResidual.lean": {
        "clusters": ["axis", "residual", "cartesian-assembly"],
        "finding": "Defines the cylindrical chart/frame and proves the off-axis Cartesian-to-cylindrical Navier-Stokes residual, divergence, advection, Laplacian, and local-germ congruence identities. The hypotheses require positive radius; no radial integral or endpoint five-observable transport theorem is present.",
        "anchors": "29-88; 137-249; 451-512; 514-600",
    },
    "NavierStokes/HeatTailHistoryLimits.lean": {
        "clusters": ["profiles", "moments", "jets"],
        "finding": "Derives angular/energy history formulas, power-tail integral identities, pressure formulas, and limits of heat-tail quantities and derivatives as X tends to infinity. These are one-dimensional outgoing-tail limits, not the final activated Cartesian selected-field moment map.",
        "anchors": "343-443; 466-573; 709-729",
    },
    "NavierStokes/LinearWaveResidual.lean": {
        "clusters": ["residual", "axis", "cartesian-assembly"],
        "finding": "Defines the cylindrical linearised residual and proves its Cartesian/cylindrical conjugacy, including cross-advection, pressure, Laplacian, and local slice identities. This is an off-axis local operator theorem, not final selected-field moment transport.",
        "anchors": "498-569; 571-626",
    },
    "NavierStokes/PhysicalResidualBridge.lean": {
        "clusters": ["residual", "axis", "cartesian-assembly", "profiles"],
        "finding": "Defines scaled graph maps, physical cylindrical velocity/pressure, and proves scaled graph residual and viscosity-one Cartesian residual identities under positive-radius, smoothness, and local representation hypotheses. No global tsum/curl/localisation five-observable equality is stated.",
        "anchors": "314-391; 503-525; 663-770",
    },
    "NavierStokes/PhysicalResidualTZ.lean": {
        "clusters": ["residual", "axis", "cartesian-assembly"],
        "finding": "Reindexes the physical residual graph between coordinate layouts and proves residual/operator covariance and the full correction-state residual in (T,Z) coordinates. The theorem remains local and positive-radius; it does not transport the final selected field's radial moments.",
        "anchors": "24-157; 169-335; 385-475",
    },
    "NavierStokes/TransitionRamp.lean": {
        "clusters": ["profiles", "time", "jets", "moments"],
        "finding": "Defines smooth transition ramps, integrated slopes, logarithmic/axial fields, stock references, parameter jets, physical profiles, and local control bounds. It proves smoothness and natural-coordinate identities for the transition model, not final Cartesian five-moment transport.",
        "anchors": "23-184; 195-372; 702-820; 903-1081; 1152-1179",
    },
    "NavierStokes/CycleMeanEquation.lean": {
        "clusters": ["residual", "rank", "cartesian-assembly", "moments"],
        "finding": "Packages cycle-step inputs, periodic/zero-pressure/solenoidal block facts, next-state mean hypotheses, divergence propagation, and induction across the stored cycle. It propagates local mean-PDE hypotheses, not the final selected Cartesian five-observable tuple.",
        "anchors": "189-215; 216-255; 523-605",
    },
    "NavierStokes/FiveRowRank.lean": {
        "clusters": ["moments", "rank", "profiles"],
        "finding": "Defines the concrete 3-coordinate debt, compactly supported angular/axial repairs, exact radial moment equations, zero mass rows, and the FiveRows predicate. This is genuine intermediate rank/moment repair algebra; the file does not state that the final selected Cartesian field satisfies these rows.",
        "anchors": "19-24; 93-165; 189-246; 249-280; 311-560",
    },
    "NavierStokes/ResidualStability.lean": {
        "clusters": ["residual", "jets", "force"],
        "finding": "Defines exact nonlinear residual add/subtraction identities, residual-difference jet expressions, all-jets-flatness transfer, quantitative fixed-order jet bounds, and scale-filter flatness. This is substantive residual stability mathematics, but it does not transport the final selected field to the five paper observables.",
        "anchors": "355-389; 573-610; 687-712",
    },
    "NavierStokes/ParticularCopyBounds.lean": {
        "clusters": ["cartesian-assembly", "jets", "pressure"],
        "finding": "Defines finite-copy modal control, smooth copy solves, velocity and pressure coefficient LocalJets, localised copy/curl estimates, and forcing decks. These are genuine finite-stage and jet controls; no endpoint equality for (M,I,J,S,Cp) is exported.",
        "anchors": "28-100; 185-279; 563-660",
    },
    "NavierStokes/PastExtension.lean": {
        "clusters": ["time", "residual", "endpoint"],
        "finding": "Builds zero-before-time extensions of velocity, pressure, and residual, proving smoothness, periodicity, divergence-free preservation, speed-unbounded preservation, late-time agreement, and endpoint extension from residual limits. It contains no radial-moment transport theorem.",
        "anchors": "112-208; 217-264; 266-334",
    },
    "NavierStokes/LocalAxisymmetricResidual.lean": {
        "clusters": ["axis", "residual", "cartesian-assembly"],
        "finding": "Derives local axisymmetric Cartesian velocity derivatives, divergence, Laplacian, pressure gradient, temporal derivative, and the exact viscosity-one Navier-Stokes residual in profile components. This is a local PDE identity, not a global five-observable transport result.",
        "anchors": "228-368; 370-398",
    },
    "NavierStokes/PhysicalGraphBounds.lean": {
        "clusters": ["axis", "profiles", "jets", "cartesian-assembly"],
        "finding": "Constructs physical graph and polar-chart lifts with axis-free annular domains, nonzero-radius hypotheses, and uniform dyadic native-graph jet bounds. The explicit axis exclusion and geometric estimates do not establish final radial moment preservation.",
        "anchors": "113-176; 298-318; 388-418; 1017-1050; 1398-1468",
    },
    "NavierStokes/PrimaryPulseBounds.lean": {
        "clusters": ["profiles", "cartesian-assembly", "jets", "rank"],
        "finding": "Provides exact primary pulse curl-remainder wave classes and budgets, local radial/tangential profiles, phase-chart bounds, canonical pulse paths, covariance identities, and the uncut projected equation. These are substantive pulse and curl results, but no final Cartesian five-moment tuple is transported to Witness.",
        "anchors": "992-1026; 1699-1795; 1828-2025",
    },
    "NavierStokes/PrimaryFieldAssembly.lean": {
        "clusters": ["cartesian-assembly", "profiles", "moments", "rank"],
        "finding": "Assembles finite periodised vector modes, principal and corrected fields, source/amplitude identifications, torus averages, covariance expansions, periodicity, and outer-scale identities. This is genuine field assembly, but the inspected declarations do not identify the final field with the five paper observables.",
        "anchors": "60-174; 210-298; 395-478; 630-754; 791-873; 936-1081",
    },
    "NavierStokes/R3/ComparisonGronwall.lean": {
        "clusters": ["r3", "energy", "endpoint"],
        "finding": "Proves scalar comparison and Gronwall-style exponential/radius bounds, including uniform radius bounds and zero-from-large-radius consequences. This supports comparison analysis, not selected-field moment transport or the endpoint packaging predicate.",
        "anchors": "24-118; 119-163",
    },
    "NavierStokes/UniformHarmonicInteraction.lean": {
        "clusters": ["profiles", "rank", "residual", "cartesian-assembly"],
        "finding": "Proves uniform harmonic transport, divergence, ordered-kernel cancellation, block amplitudes, mixed and nonlinear coefficient bounds, and interaction-block structure. The uniform interaction layer has no final Cartesian `(M,I,J,S,Cp)` equality.",
        "anchors": "28-98; 172-245; 271-376; 420-434",
    },
    "NavierStokes/ActualCycleGeometry.lean": {
        "clusters": ["profiles", "axis", "time"],
        "finding": "Identifies the actual cycle geometry with initialization geometry, common gauge, strip, region, scales, operators, and base bounds, and proves index compatibility, positive radius, and positive strip time. These are parameter/geometry identifications, not global moment transport.",
        "anchors": "18-81; 97-111",
    },
    "NavierStokes/ActualPolarCoverage.lean": {
        "clusters": ["axis", "profiles", "jets", "cartesian-assembly"],
        "finding": "Provides actual polar coverage and physical residual jet-bound domains with inner-radius positivity and chart/annular coverage conditions. The inspected coverage declarations do not transport the selected field to the five paper observables.",
        "anchors": "21-39; 40-116; 117-298",
    },
    "NavierStokes/AxisSeries.lean": {
        "clusters": ["axis", "profiles", "moments"],
        "finding": "Defines and analyses the axis Bessel/profile series, derivative and ODE identities, tail bounds, positivity, and logarithmic slope estimates. This is explicit scalar series/profile mathematics, not a theorem that the final Cartesian field preserves the paper moment tuple.",
        "anchors": "56-210; 220-315; 329-385",
    },
    "NavierStokes/AxisCoefficientSpace.lean": {
        "clusters": ["axis", "profiles", "jets", "moments"],
        "finding": "Defines the interval coefficient window, compatible raw jets, coefficient subspace, smoothness, derivative, and norm-bound infrastructure. It provides genuine axis coefficient analysis but no selected-endpoint five-observable transport theorem.",
        "anchors": "28-102; 118-245; 260-450",
    },
    "NavierStokes/AxisEvaluation.lean": {
        "clusters": ["axis", "profiles", "jets", "cartesian-assembly", "moments"],
        "finding": "Defines polynomial jets, mixed coefficient series, profile evaluation, majorants, summability, uniform tsum evaluation, smoothness, and linear evaluation maps. The inspected declarations do not identify the final selected Cartesian field with the paper moment tuple.",
        "anchors": "29-54; 57-126; 135-488",
    },
    "NavierStokes/AxisResolvent.lean": {
        "clusters": ["axis", "profiles", "jets"],
        "finding": "Proves factorial majorants, vanishing-below-degree properties, radial inverses, alternating tsum resolvents, filtration powers, and resolvent equations/uniqueness. This is an analytic axis resolvent layer, not a physical selected-field moment transport theorem.",
        "anchors": "28-130; 139-190; 195-476",
    },
    "NavierStokes/BasePhaseGeometry.lean": {
        "clusters": ["axis", "jets", "residual", "energy", "cartesian-assembly"],
        "finding": "Defines reference scales, damping and normalisation bounds, local base/error/phase/frame estimates, family and modal jets, and phase-geometry ODE controls. These are substantive geometry and regularity results, but no global selected-field five-observable equality is stated.",
        "anchors": "28-137; 159-226; 524-1137",
    },
    "NavierStokes/LocalizedGaussianBounds.lean": {
        "clusters": ["jets", "residual", "axis", "cartesian-assembly"],
        "finding": "Proves zero/inactive germs, local and global Gaussian cutoff gains, indexed tails, uniform complement jets, and source/harmonic complement bounds. It controls localised regularity and tails but does not prove transport of the paper radial moment tuple.",
        "anchors": "29-45; 57-92; 149-245; 259-319; 351-557",
    },
    "NavierStokes/OutgoingDilation.lean": {
        "clusters": ["moments", "profiles", "axis", "pressure", "energy"],
        "finding": "Defines actual radial dilation and the reduced-profile observables M, I, J, S, totalS, renormalizedI, and axisDatum, then proves their scaling, integrability, zero identities, axis behaviour, and the reduced DilatedSpecification. This is strong positive evidence for upstream reduced moment mathematics; the inspected file does not transport these observables through the complete selected Cartesian field and Witness endpoint.",
        "anchors": "21-57; 61-78; 80-151; 294-609",
    },
    "NavierStokes/ParametricRadialExtension.lean": {
        "clusters": ["axis", "profiles", "jets"],
        "finding": "Constructs a smooth even radial extension with parameter cutoffs, squared-radius descent, half-plane lift, mixed jets, pullbacks, axis jets, zero exterior, and compact support. This supports axis regularity but does not state the final selected Cartesian five-moment transport equality.",
        "anchors": "24-113; 115-210; 214-362",
    },
    "NavierStokes/WeightedODEJets.lean": {
        "clusters": ["jets", "residual", "energy"],
        "finding": "Defines directional/list jets and proves smoothness, congruence, algebraic/product/cross-jet rules, ODE solution-jet identities, norm envelopes, and weighted finite-order estimates. This is parameter-ODE jet control, not a theorem transporting radial observables into the selected endpoint.",
        "anchors": "30-165; 194-260; 294-754",
    },
    "NavierStokes/ActualPhaseDefect.lean": {
        "clusters": ["axis", "jets", "cartesian-assembly", "residual"],
        "finding": "Defines actual chart-phase changes, slot/material coordinates, and radial/axial/temporal slow-change identities. This is a concrete phase comparison layer, not a global radial-observable map into Witness.",
        "anchors": "23-113; 169-190",
    },
    "NavierStokes/ActualPhaseJetBounds.lean": {
        "clusters": ["axis", "jets", "cartesian-assembly"],
        "finding": "Proves affine positive-jet bounds, phase-size constants, phase-cell containment/mapping, and native phase remainder infrastructure. These are actual phase regularity controls without a selected Cartesian five-observable equality.",
        "anchors": "27-122; 134-154",
    },
    "NavierStokes/ActualSignedControl.lean": {
        "clusters": ["axis", "jets", "cartesian-assembly"],
        "finding": "Identifies pulse matrices/vectors with actual phase constructions and proves geometric phase-jet/range bounds through ReferenceBounds. It does not transport reduced moments into the selected endpoint.",
        "anchors": "21-64; 85-107",
    },
    "NavierStokes/AxisEvaluationAlgebra.lean": {
        "clusters": ["axis", "profiles", "jets", "cartesian-assembly"],
        "finding": "Contains complex phase factors, carrier/mode differentiability, along-mode identities, cylindrical Laplacian and angular-independent identities, and three-component complex modes. This is cylindrical differential algebra, not a selected-field moment evaluator.",
        "anchors": "67-145; 199-284; 309-333",
    },
    "NavierStokes/AxisWeightEstimates.lean": {
        "clusters": ["axis", "jets", "profiles"],
        "finding": "Defines the exact coefficient weight, square-decay factors, radial/parameter shifts, product-weight sums, radial divisors, mixed-weight sums, and jet-product bounds. This is substantive coefficient convolution and radial-inverse control without a selected-field five-observable equality.",
        "anchors": "27-65; 77-125; 167-299; 336-473",
    },
    "NavierStokes/EdgeWeightJets.lean": {
        "clusters": ["axis", "jets", "profiles"],
        "finding": "Proves polynomial edge-jet masses, compact-coefficient jet bounds, weighted smoothness, edge division/vanishing identities, mixed derivative bounds, and weighted products/powers. This is substantive edge regularity without endpoint moment transport.",
        "anchors": "25-69; 106-227; 254-355; 430-515",
    },
    "NavierStokes/HarmonicCalculus.lean": {
        "clusters": ["axis", "jets", "residual"],
        "finding": "Proves actual complex harmonic carrier/mode calculus, scalar/vector cylindrical Laplacian identities, exact harmonic divergence and longitudinal identities, finite-jet contraction bounds, and graph derivative formulas. This is a strong local cylindrical differential layer without the complete selected-field five-observable equality.",
        "anchors": "30-137; 199-284; 309-367; 399-521; 643-689",
    },
    "NavierStokes/PhysicalClassBounds.lean": {
        "clusters": ["axis", "jets", "profiles"],
        "finding": "Defines flat geometry and proves edge-weight uniformity, moving-strip flatness, and absorption of edge growth into uniform coefficient classes. This is weighted local control, not a physical five-moment evaluator.",
        "anchors": "33-70; 76-104",
    },
    "NavierStokes/PolarCharts.lean": {
        "clusters": ["axis", "cartesian-assembly", "profiles"],
        "finding": "Defines four genuine polar chart rotations/inverses and proves norm/radius invariance, positivity, smoothness, and chart-offset identities. No selected-endpoint radial-moment transport theorem is stated.",
        "anchors": "29-118",
    },
    "NavierStokes/ReferenceJetBounds.lean": {
        "clusters": ["axis", "profiles", "jets"],
        "finding": "Proves reference parameter/radial derivative identities, coefficient-family jet constants/bounds, and natural U/log-coordinate value and derivative bounds. It does not identify the final selected field with the paper observables.",
        "anchors": "23-64; 72-133",
    },
    "NavierStokes/StressActivation.lean": {
        "clusters": ["moments", "profiles", "jets", "energy"],
        "finding": "Constructs smooth activation/damping, weighted fields, weighted primitives, derivative identities, and controlled fields from a flat primitive integral. This is positive primitive construction evidence, not complete selected-field five-moment transport.",
        "anchors": "24-85; 100-126",
    },
    "NavierStokes/VolterraRegularity.lean": {
        "clusters": ["moments", "profiles", "jets", "energy"],
        "finding": "Defines actual weighted radial means and regular Volterra primitives and proves continuity, differentiation under the actual integral, and smoothness including diagonal/scale families. It does not connect outputs to the paper tuple or Witness packaging.",
        "anchors": "28-238; 256-287",
    },
    "NavierStokes/WeightedClasses.lean": {
        "clusters": ["axis", "jets", "profiles"],
        "finding": "Defines strip data, growth, majorants, and polynomial/edge-weight domination. This is generic weighted local-jets infrastructure and carries no five cumulative radial observable payload.",
        "anchors": "31-94",
    },
    "NavierStokes/WeightedQuotients.lean": {
        "clusters": ["axis", "jets", "profiles"],
        "finding": "Proves iterated derivative bounds for powers, square-root/inverse-square-root bounds, composition jet bounds, and positive-power composition estimates. It is regularity infrastructure, not endpoint moment transport.",
        "anchors": "23-131",
    },
    "NavierStokes/AxisOperators.lean": {
        "clusters": ["axis", "jets", "profiles", "cartesian-assembly"],
        "finding": "Defines finite Leibniz jet sums, product families, bounded linear and bilinear jet operators, radial/parameter primitive and inverse rows, and continuous linear lifts. These are axis-operator and coefficient-jet infrastructure; no Cartesian field, torus-average, or selected-endpoint five-observable equality is stated.",
        "anchors": "27-124; 136-193; 197-339; 349-467",
    },
    "NavierStokes/BaseChartJets.lean": {
        "clusters": ["axis", "cartesian-assembly", "jets", "profiles", "moments"],
        "finding": "Defines actual normalised physical charts, chart jet/envelope estimates, base frequency and axial fields, and exact equalities with constructed normalised velocity and angular-moment components. It provides concrete chart-to-component identities and positive-cell estimates, but not the complete selected Cartesian `(M,I,J,S,C_p)` transport theorem.",
        "anchors": "65-239; 244-328; 358-446; 660-717; 744-923",
    },
    "NavierStokes/MatchingConeBounds.lean": {
        "clusters": ["profiles", "moments", "rank", "jets", "pressure"],
        "finding": "Defines shape-transition models, source thresholds, angular barriers, shaped profiles, radial derivative identities, seed/source jet bounds, and PreparedWitness cone controls. These are reduced-profile matching and cone estimates under explicit hypotheses; they do not evaluate the final selected Cartesian field or export its five observables.",
        "anchors": "22-129; 161-226; 238-296; 304-551; 563-673; 952-979",
    },
    "NavierStokes/PhysicalCoordinateBounds.lean": {
        "clusters": ["axis", "cartesian-assembly", "jets", "profiles", "time"],
        "finding": "Defines physical inverse coordinates, their differentials, homogeneous dilations, normalised compact regions, time reflection/shift, and derivative bounds for physical q/eta/x coordinates. This establishes chart regularity and scaling control, not a global radial observable map or selected Witness transport.",
        "anchors": "23-150; 161-302; 312-425; 434-538; 570-575",
    },
    "NavierStokes/SignedCovariance.lean": {
        "clusters": ["profiles", "rank", "jets", "cartesian-assembly", "moments"],
        "finding": "Defines signed covariance increments, exact inverse/cross reconstruction, finite and assembled radial/tangent waves, double-average covariance identities, signed-square identities, physical chart scaling, and weighted jet-class bounds. This is substantive local covariance and wave assembly; it does not transport the five paper observables to the selected Cartesian endpoint.",
        "anchors": "23-75; 107-212; 217-377; 385-425; 449-742; 752-844; 853-976",
    },
    "NavierStokes/WaveEdgeExtension.lean": {
        "clusters": ["profiles", "jets", "axis", "cartesian-assembly"],
        "finding": "Defines moving radial windows, smooth zero extensions, boundary controls, logarithmic coordinates, edge weights/growth, native radius and profile extensions, NativeJets zero-germ covers, and mean-coordinate extensions. These are strong edge regularity and extension results, but no final selected Cartesian barMoment or `(M,I,J,S,C_p)` equality is stated.",
        "anchors": "24-227; 276-434; 438-640; 684-825; 839-892",
    },
    "NavierStokes/BoundaryAxisJets.lean": {
        "clusters": ["axis", "jets", "profiles"],
        "finding": "Proves signed radial and squared-radius axis jet identities, even/localised descent, joint smoothness, holomorphic parameter versions, interior cutoff identities, and axis vanishing. This closes substantial local axis regularity cases but does not define a Cartesian field observable or transport the selected five moments.",
        "anchors": "21-99; 103-195; 226-320; 339-607; 631-714; 728-878",
    },
    "NavierStokes/GenericEndpointExtension.lean": {
        "clusters": ["time", "jets", "cartesian-assembly"],
        "finding": "Generalises smooth strip gluing, normal traces, closure jets, periodicity, and endpoint extensions across time boundaries. Theorems transfer regularity and additive periods to completed boundary values, but no radial observable, barMoment, FiveRows, or selected Witness transport is present.",
        "anchors": "23-413; 429-492; 612-854",
    },
    "NavierStokes/PhaseJetBounds.lean": {
        "clusters": ["jets", "profiles", "axis"],
        "finding": "Defines polynomial jet contracts, compact-range composition/inversion bounds, normal geometry jets, phase/frame families, and frequency/viscosity/epsilon rate bounds. This is quantitative phase regularity infrastructure; it contains no five-moment evaluator and no selected Cartesian endpoint theorem.",
        "anchors": "20-365; 371-445; 467-719; 755-1031",
    },
    "NavierStokes/RadialPullback.lean": {
        "clusters": ["moments", "profiles", "jets", "axis"],
        "finding": "Proves exact reduced radial integral identities for power-coordinate normalisation and physical compact pullbacks, with support, smoothness, derivative, finite-jet, and mean-class transport consequences. These are genuine reduced radial bridges under `RadialAlias` hypotheses, not a theorem identifying the selected 3D Cartesian field with `(M,I,J,S,C_p)` after curl, localisation, periodisation, or endpoint packaging.",
        "anchors": "15-224; 242-365; 382-485; 503-598; 605-715; 756-879; 810-856",
    },
    "NavierStokes/ReferencePath.lean": {
        "clusters": ["profiles", "moments", "time", "jets"],
        "finding": "Constructs the same-radius reference continuation, smooth damping, frozen continuation, log-radius reparameterisation, and reference error jet bounds. Its `histories` constructor explicitly rebuilds `f`, `U`, pressure0, and the ProfileHistories data from the reference path, so reduced moments are recomputed downstream; no selected Cartesian field, curl/tsum/localisation transport, or public Witness equality is supplied here.",
        "anchors": "17-217; 329-420; 447-601; 611-783; 804-820",
    },
    "NavierStokes/WeightedRadialPrimitive.lean": {
        "clusters": ["moments", "profiles", "jets", "energy"],
        "finding": "Proves uniform two-edge weighted bounds for compact radial primitives and transport inverses, exact left/right collar identities, finite-jet estimates, and canonical/support-preserving MeanClass transport. The result is a real reduced-profile integral/regularity bridge, but its generic vector-valued source and MeanClass target are not the selected Cartesian five-observable tuple or `Witness`.",
        "anchors": "31-206; 229-377; 451-565; 569-761; 814-988; 1029-1102",
    },
    "NavierStokes/R3CompactCandidate.lean": {
        "clusters": ["endpoint", "cartesian-assembly", "pressure", "force", "energy"],
        "finding": "Defines the compact whole-space candidate properties and proves transfer from the periodic local model to compact velocity, pressure, force, support, smoothness, and residual facts. `of_localized_fields` consumes the periodic `CandidateProperties` for the same raw sums, but no five-moment observable equality is added at this R3 packaging layer.",
        "anchors": "23-37; 39-99; 104-199; 201-252; 256-267",
    },
    "NavierStokes/ResidualRegularity.lean": {
        "clusters": ["residual", "force", "jets", "cartesian-assembly"],
        "finding": "Proves smoothness, spatial-period transfer, locality/congruence, and zero-residual consequences for the concrete Navier-Stokes residual. This supports exact local PDE reuse and zero extensions, but does not establish a radial observable or paper-moment transport theorem.",
        "anchors": "13-107; 113-194; 202-291",
    },
    "NavierStokes/GaugeRadialResidualBounds.lean": {
        "clusters": ["moments", "pressure", "residual", "axis", "jets"],
        "finding": "Defines the actual pressure-gauge radial residual and proves `pressureDefect_eq_mass`: the pressure defect is the actual zeroth radial moment of the radial source with the same auxiliary-torus average used by the gauge. It also proves reconstruction identities and debt-class/radial residual bounds under explicit fixed-pressure and primitive-data hypotheses; no full five-observable selected-field export is stated.",
        "anchors": "21-126; 151-193; 215-250",
    },
    "NavierStokes/MixedDiagonalResidual.lean": {
        "clusters": ["residual", "cartesian-assembly", "jets", "time", "force"],
        "finding": "Defines the mixed velocity, pressure, and residual from the actual potential sums, proves definitional equality with `MixedPeriodicAssembly.originalResidual`, establishes smoothness and residual jet rates, and derives physical joint zero jets from finite-stage inputs. These are concrete series/residual bridges, but the module exports no equality from the assembled field to the complete paper five-moment tuple.",
        "anchors": "21-50; 52-115; 125-198; 200-264",
    },
    "NavierStokes/ResidualCalculus.lean": {
        "clusters": ["residual", "force", "cartesian-assembly"],
        "finding": "Proves additivity and perturbation formulas for temporal and spatial derivatives, pressure gradients, divergence, Laplacian, advection, and the full Navier-Stokes residual, together with time-scalar multiplication and divergence-free consequences. This exposes residual path dependence algebraically but is not a CMI force-independence predicate or a five-moment endpoint transport theorem.",
        "anchors": "17-168; 178-268",
    },
    "NavierStokes/OutgoingSchedule.lean": {
        "clusters": ["moments", "profiles", "time", "axis"],
        "finding": "Constructs the outgoing radial/angular pulse and proves exact pulse moment identities, prefix closure, and endpoint cancellation. `massMoment_endpoint` and `angularMoment_endpoint` prove two combined log-coordinate moments vanish, with `exact_axial_moments` packaging them and post-pulse persistence. This is a genuine reduced-profile moment bridge, but it is not the complete five-observable Cartesian/torus/Witness transport theorem.",
        "anchors": "22-188; 289-318; 546-625; 633-715; 739-927; 929-994",
    },
    "NavierStokes/ActualIntermediateDebtBounds.lean": {
        "clusters": ["moments", "rank", "corrections", "physical-data", "jets"],
        "finding": "Derives actual three-component signed and temporal debt classes from checked correction-step data, including covariance and temporal increment bounds. This is a concrete intermediate rank/debt bridge, but it does not identify those components with the complete five paper observables or export them through the selected Cartesian Witness.",
        "anchors": "68-75; 136-177",
    },
    "NavierStokes/ActualMeanExterior.lean": {
        "clusters": ["cartesian-assembly", "moments", "profiles", "axis", "physical-data"],
        "finding": "Proves that actual moving mean fields, angular fields, pressure, temporal, rank, stream, and cycle families vanish outside the nominal active annulus under explicit support hypotheses. This is positive exterior/localisation control; it is not a global five-observable radial transport theorem for the selected whole-space field.",
        "anchors": "22-104; 121-144; 169-230",
    },
    "NavierStokes/R3/SpatialEnergyScaling.lean": {
        "clusters": ["r3", "energy"],
        "finding": "Proves exact kinetic-energy scaling under amplitude multiplication and nonzero spatial dilation, and transports uniform finite-energy bounds. This validates an R³ analytic scaling component but carries no radial-moment or selected-field correspondence payload.",
        "anchors": "16-23; 25-36; 38-48",
    },
    "NavierStokes/R3/SpatialSupportScaling.lean": {
        "clusters": ["r3", "energy", "cartesian-assembly"],
        "finding": "Proves compact-support transport under nonzero spatial dilation for spatial slices and positive-time spacetime force support. This is a concrete R³ support bridge, not a theorem preserving the paper's five radial observables through the selected assembly.",
        "anchors": "15-20; 22-32; 34-57",
    },
    "NavierStokes/R3ActualCandidate.lean": {
        "clusters": ["endpoint", "r3", "cartesian-assembly"],
        "finding": "Extracts `ActualCandidateAssembly.selected_witness` into a compact whole-space existential candidate through `R3CompactCandidate.of_localized_fields`. The wrapper retains the concrete assembled candidate properties, but its exported `Properties` type contains no complete five-observable equality.",
        "anchors": "1-9; 17-21",
    },
    "NavierStokes/NaturalEntrance.lean": {
        "clusters": ["profiles", "moments", "pressure", "axis", "jets"],
        "finding": "Constructs natural entrance profiles and proves exact reduced radial flux identities for angular and axial sources, including `angular_source_integral`, `Sn_eq_radial`, and `axial_source_integral`. These are substantive reduced PDE/entrance identities, but they are not composed with the final Cartesian curl, localisation, tsum, periodisation, and public Witness into the complete paper tuple.",
        "anchors": "933-1095; 1186-1233; 1235-1278; 1291-1303",
    },
    "NavierStokes/SquaredPartition.lean": {
        "clusters": ["cartesian-assembly", "time", "jets", "moments"],
        "finding": "Constructs smooth compactly supported line, grid, product, dyadic, and physical slow masks with local finiteness, finite jet support, and exact squared partition identities. The label-mask tail sums are exact, but the module does not prove preservation of the paper's radial observables after the full field assembly.",
        "anchors": "11-15; 80-93; 185-205; 548-568; 568-683; 768-801",
    },
    "NavierStokes/DirectAngularDiagonal.lean": {
        "clusters": ["cartesian-assembly", "axis", "residual", "jets", "time"],
        "finding": "Constructs the direct angular field, its locally finite sum, and the mixed velocity obtained by adding it to the solenoidal potential velocity sum. It proves smoothness, divergence-free composition, axis vanishing, spatial-cut transport, physical graph pullback, and all-order axis-germ results. These are genuine field-level identities, but no five-observable radial transport theorem reaches the public Witness.",
        "anchors": "64-117; 229-321; 336-370; 416-471; 527-621; 655-708",
    },
    "NavierStokes/GaussianTailFlat.lean": {
        "clusters": ["time", "jets", "profiles", "cartesian-assembly"],
        "finding": "Defines the actual smooth slot cutoff with plateau/support radii, proves derivative support and uniform jet bounds, derives Gaussian off-plateau decay, and proves Gaussian tails dominate every real power of the dyadic Q scale. This supplies rigorous tail/jet control, not a radial-moment equality for the assembled selected field.",
        "anchors": "25-104; 106-174; 176-215; 216-239",
    },
    "NavierStokes/LeadingStressWeights.lean": {
        "clusters": ["moments", "profiles", "axis", "jets", "cartesian-assembly"],
        "finding": "Defines nominal and modulated leading stress in logarithmic and physical radial charts, proves inner/outer exterior vanishing, strict cone nonvanishing, exact edge joins, weighted bounds, radial pullback identities, and physical jet bounds for the final profile witness. This is strong reduced profile/stress evidence, but it does not export the full selected Cartesian five-observable tuple.",
        "anchors": "23-121; 137-205; 429-532; 698-760; 1095-1148",
    },
    "NavierStokes/LocalSignedRequest.lean": {
        "clusters": ["moments", "pressure", "cartesian-assembly", "rank", "jets"],
        "finding": "Proves chart/profile pullback and inverse identities, MeanClass transport through compact signed primitives and torus averages, exact physical stress scaling, radial divergence formulas, compact support, and zero adjusted moments. These are genuine local physical radial bridges; they remain below the final selected Cartesian `Witness` composition.",
        "anchors": "122-178; 282-460; 531-565; 685-729; 855-920; 993-1008",
    },
    "NavierStokes/PulseCovariance.lean": {
        "clusters": ["moments", "rank", "profiles", "jets"],
        "finding": "Constructs Gaussian pulse weights and actual tangent/covariance columns, proves integrability, positive mass and moment bounds, directional concentration, exact covariance factorisation, signed strict-cone identities, and compact positive inverse results. This validates a real pulse covariance component, not the final Cartesian five-observable transport theorem.",
        "anchors": "40-105; 121-321; 361-454; 544-715; 744-829",
    },
    "NavierStokes/PositiveAxisExistence.lean": {
        "clusters": ["axis", "profiles", "moments", "jets"],
        "finding": "Connects the convergent six-component Volterra construction to the explicit positive-order axis system and proves squared-radius smoothness, parity, axis vanishing, axis jets, and real compatible profile systems. This is substantive reduced axis/profile existence evidence; it does not export a Cartesian selected-field five-observable equality.",
        "anchors": "1-13; 435-488; 543-661",
    },
    "NavierStokes/PulseLag.lean": {
        "clusters": ["moments", "time", "profiles", "jets"],
        "finding": "Defines the actual exponential convolution and pulse lag, proves positivity, integration-by-parts expansion, exact lag ODE/derivative identities, and quantitative second-order remainder and reset controls. This verifies a concrete outgoing pulse lag mechanism but does not compose its moments into the selected Cartesian Witness.",
        "anchors": "1-14; 16-120; 140-260; 289-395",
    },
    "NavierStokes/RadialHeatProfile.lean": {
        "clusters": ["moments", "profiles", "energy", "axis"],
        "finding": "Defines the radial heat profile and moments and proves the improper integration-by-parts moment ODE, profile jet ODE, endpoint/half-line identities, and radial heat-equation relations. These are exact reduced radial PDE identities, not transport of the final curl/localised/periodised selected field to the paper tuple.",
        "anchors": "300-345; 384-455; 600-650; 700-730",
    },
    "NavierStokes/ReleaseMoments.lean": {
        "clusters": ["moments", "profiles", "time", "axis"],
        "finding": "Constructs the corrected angular release history, proves smoothness, release/hold/tail regimes, renormalised radial integrability, and exact vanishing of the renormalised angular moment. `complete_release_moments` packages the scheduled reduced correction and eventual history. It is a strong positive reduced-moment bridge, not a final selected Cartesian five-observable transport theorem.",
        "anchors": "23-132; 140-225; 247-332; 340-395; 408-529; 531-540",
    },
    "NavierStokes/RenormalizedHeatMoment.lean": {
        "clusters": ["moments", "profiles", "axis", "energy", "jets"],
        "finding": "Proves renormalised heat/profile moment integrability, differentiation and scaling identities, axial viscosity moment cancellation, physical radial pullback formulas, and the heated nominal axial-viscosity zero theorem under explicit compensation hypotheses. This is concrete reduced/physical radial moment evidence, but no composition through final Cartesian curl, localisation, tsum, periodisation, and public Witness is exported.",
        "anchors": "109-182; 274-347; 367-496; 518-627; 699-788",
    },
    "NavierStokes/TorusAverages.lean": {
        "clusters": ["cartesian-assembly", "moments", "profiles", "rank"],
        "finding": "Defines the actual torus covering, Haar/square averages, lattice periodisation, native linear charts, determinant/Jacobian factors, transverse stretching, product-profile separation, pulse-column averages, and angular cosine covariance. These theorems establish genuine averaging and coordinate-change infrastructure, but do not by themselves identify the final selected Cartesian field with the complete paper five-moment tuple.",
        "anchors": "36-138; 140-207; 228-411; 419-555; 570-679",
    },
    "NavierStokes/LabelSumBounds.lean": {
        "clusters": ["cartesian-assembly", "jets", "rank", "moments"],
        "finding": "Proves finite active-label sum jet bounds, support-window consequences, covariance support, and harmonic covariance class transport for assembled oscillations. This is concrete finite-sum/covariance infrastructure; it does not state the final selected Cartesian five-observable equality.",
        "anchors": "157-372; 499-624; 745-818; 1004-1085",
    },
    "NavierStokes/CommonCoverClass.lean": {
        "clusters": ["cartesian-assembly", "jets", "profiles", "moments"],
        "finding": "Defines the actual common-cover path, affine argument maps, band ratios, chart costs, class and jet transport, profile slow strips, and native radial/temporal bases. This is geometric and regularity transport across overlapping bands, not final selected-field five-moment transport.",
        "anchors": "180-354; 414-565; 633-715; 857-971; 1016-1137; 1273-1300",
    },
    "NavierStokes/HeatSwitchCone.lean": {
        "clusters": ["moments", "profiles", "pressure", "rank", "jets"],
        "finding": "Constructs the compensated heat switch and proves smooth histories, exact pressure/future-integral identities, strict true-cone preservation, uniform compensation thresholds, and exact change-row integral relations. It is a substantive reduced heat/cone bridge; it does not export the final Cartesian selected-field tuple.",
        "anchors": "7-25; 67-175; 365-447; 616-768; 805-831; 1008-1092; 1104-1248",
    },
    "NavierStokes/ActualSignedGeometry.lean": {
        "clusters": ["cartesian-assembly", "profiles", "axis", "jets", "time"],
        "finding": "Defines the actual signed pulse geometry, common-cover charts, active pair indexing, phase cells, support cutoffs, and phase-normal/copy identities. These declarations connect actual profile labels and geometry to signed stage coordinates, but do not state a final radial observable transport theorem.",
        "anchors": "30-219; 249-372; 461-588; 806-946; 1143-1239; 1265-1433",
    },
    "NavierStokes/ActualSignedStageControls.lean": {
        "clusters": ["cartesian-assembly", "corrections", "rank", "jets", "moments"],
        "finding": "Instantiates actual signed correction-stage parameters, requests from residuals or invariants, native geometry/cutoffs, uniform cell jets, covariance records, and pulse/normal controls. This is concrete stage-data and covariance infrastructure; no complete selected Cartesian five-observable equality is exported.",
        "anchors": "1-199; 203-385; 444-525; 543-680; 704-777; 814-1010; 1042-1185",
    },
    "NavierStokes/RepairConeBounds.lean": {
        "clusters": ["moments", "profiles", "rank", "pressure", "jets"],
        "finding": "Contains a genuine five-coordinate reduced-profile bridge: `actual_moments` identifies normalized profile moments with `freeRows`, while `physical_rows`, `physical_stock_values`, `physical_transport`, `physical_lags`, and `physical_stocks` transport those rows and stock values through the physical chart under explicit hypotheses. This corrects any claim that five-moment transport is absent everywhere. The declarations remain reduced/profile-level and do not identify the final Cartesian curl/localised/tsum/periodised selected field with the public Witness tuple.",
        "anchors": "21-166; 328-377; 384-525; 786-924; 946-993; 1026-1163; 1223-1275",
    },
    "NavierStokes/ActualCycleExcluded.lean": {
        "clusters": ["corrections", "rank", "moments", "jets", "profiles"],
        "finding": "Propagates actual cycle primitive/cumulative data and covariance through particular, signed, temporal, and rank stages, then derives all-power bounds for the next axisymmetric aliases. This is concrete cycle-state preservation and alias control, not a final selected Cartesian five-observable equality.",
        "anchors": "20-71; 94-130; 153-210",
    },
    "NavierStokes/RankStateBounds.lean": {
        "clusters": ["rank", "moments", "profiles", "jets"],
        "finding": "Lifts actual three-component slow debt classes, defines normalized rank parameters, transports fixed-shell classes to moving support, and proves variable-gauge rank-increment bounds and support margins. This is concrete three-component rank-state control; it does not itself provide the final five-observable Cartesian endpoint equality.",
        "anchors": "25-87; 90-139; 143-225; 252-332",
    },
    "NavierStokes/BaseRankPatch.lean": {
        "clusters": ["rank", "moments", "cartesian-assembly", "profiles"],
        "finding": "Constructs the actual final-base angular and axial slices and proves background identities on the mean patch. `five_rows` explicitly proves `FiveRowRank.FiveRows` for the full final base with the original support radii and actual similarity scales. This is a genuine local physical rank bridge, but not the complete global selected Cartesian/curl/localisation/tsum/Witness transport theorem.",
        "anchors": "24-71; 87-190; 230-289; 333-358",
    },
    "NavierStokes/ParametricTerminalCompensation.lean": {
        "clusters": ["corrections", "rank", "moments", "profiles", "jets"],
        "finding": "Proves variable-debt coefficient compensation, derivative and compact-amplitude bounds, radius-ratio scaling, physical three-component debt identities, and existence of physical heat compensation. This is actual terminal correction data and parameter regularity, not final selected Cartesian five-observable transport.",
        "anchors": "20-124; 226-347; 365-471",
    },
    "NavierStokes/ActualMeanStageData.lean": {
        "clusters": ["cartesian-assembly", "axis", "time", "physical-data", "jets"],
        "finding": "Builds the actual radial section, coefficient/angular field, shrinking supports, zero germs, initial angular/temporal/rank/stream data, and iterated cycle mean-stage data. This is concrete physical stage ingestion and support control; it does not state the complete selected Cartesian five-observable equality.",
        "anchors": "22-65; 77-178; 190-281; 296-362; 368-462",
    },
    "NavierStokes/CorrectionAnalyticStep.lean": {
        "clusters": ["corrections", "rank", "moments", "cartesian-assembly", "jets"],
        "finding": "Defines the actual analytic correction step, proves signed/particular zero-germ and covariance-moving inputs, constructs step results, and proves invariant and result iteration preservation. This is a concrete induction layer; its outputs are correction invariants and estimates rather than the final selected Cartesian five-observable tuple.",
        "anchors": "25-149; 152-262; 467-632; 654-690",
    },
    "NavierStokes/AxisymmetricResidualGrouping.lean": {
        "clusters": ["residual", "axis", "jets"],
        "finding": "Provides explicit axisymmetric-mode alias bookkeeping, angular-average identities, and finite residual reconstruction/grouping. Adding or removing the axisymmetric alias changes the grouped good residual while leaving the nonconstant angular average unchanged under the stated integrability hypotheses. This is a valid zero-mode residual decomposition, not a final five-observable transport theorem.",
        "anchors": "23-65; 76-100; 104-188",
    },
    "NavierStokes/LocalResidualGrouping.lean": {
        "clusters": ["residual", "axis", "jets", "cartesian-assembly"],
        "finding": "Proves finite-sum nonlinear residual identities under disjoint-support and smoothness hypotheses, grouped good-residual formulas, and angular-mean extraction/reconstruction. This is a concrete local residual assembly result; it does not identify the final global selected Cartesian field with the five paper observables.",
        "anchors": "20-61; 70-143; 145-338",
    },
    "NavierStokes/DiagonalResidual.lean": {
        "clusters": ["residual", "jets", "cartesian-assembly", "time"],
        "finding": "Defines jet-rate and finite-jet-rate interfaces, proves residual difference and stage-to-limit power-rate transfer, diagonal potential-tail and spatial-curl estimates, and all-order residual flatness for the diagonal construction. The all-order statement is order-by-order with a possibly different finite stage; it is not a fixed-tail radial-moment theorem.",
        "anchors": "33-50; 165-224; 272-322; 341-410",
    },
    "NavierStokes/CompactForceDecay.lean": {
        "clusters": ["force", "jets", "time", "r3"],
        "finding": "Proves periodic spatial reduction and global weighted derivative decay in time for smooth fields with compact future-time support. This is a real force/regularity estimate on the periodic spatial model, not spatial radial decay or transport of the five cumulative moments.",
        "anchors": "20-65; 76-177; 193-213",
    },
    "NavierStokes/CompactSpatialForceDecay.lean": {
        "clusters": ["force", "jets", "cartesian-assembly"],
        "finding": "Defines fixed compact spatial support and proves derivative vanishing outside the support together with weighted spacetime jet decay, then packages the result into the comparator force condition. This supplies compact-force regularity semantics; it does not prove selected-field radial moment preservation or absolute pressure transport.",
        "anchors": "16-40; 44-76; 80-86",
    },
    "NavierStokes/R3/CompactForceBound.lean": {
        "clusters": ["r3", "force", "energy"],
        "finding": "Proves existence of a uniform spatial L2-square bound for a continuous force with compact spacetime support over the pre-singular time interval. This is a genuine R3 force-energy estimate, but it does not provide the selected Cartesian five-observable composition.",
        "anchors": "1-16; 25-36",
    },
    "NavierStokes/AlignedProfileSpectralCone.lean": {
        "clusters": ["profiles", "rank", "axis", "jets", "cartesian-assembly"],
        "finding": "Connects actual aligned modulation to profile spectral and target cones, proves radial germs, continuous/compact bounds, reference directions, and equality of actual reference frequency/shear with the constructed quantities. This is a substantive cone and representative bridge below the selected Cartesian observable boundary.",
        "anchors": "1-20; 26-110; 146-236; 424-469; 524-763",
    },
    "NavierStokes/AxisHolomorphic.lean": {
        "clusters": ["axis", "profiles", "jets", "time"],
        "finding": "Builds convergent geometric/factorial series, complex vertical extensions, derivative identities, analytic continuation on parameter tubes, and normalized jet bounds. This is genuine analytic regularity for the axis profile layer; it does not state a selected Cartesian moment or endpoint Witness theorem.",
        "anchors": "21-95; 117-181; 189-331; 341-569",
    },
    "NavierStokes/LocalPhysicalCopyBounds.lean": {
        "clusters": ["cartesian-assembly", "jets", "time", "axis"],
        "finding": "Proves smooth patch and germ extension lemmas, support geometry, local and weighted jet bounds, locally finite periodised copy sums, and vector-sum regularity. It is concrete physical copy/support infrastructure, not a five-observable transport theorem.",
        "anchors": "27-71; 83-150; 198-340; 401-499; 522-850",
    },
    "NavierStokes/NaturalProfile.lean": {
        "clusters": ["profiles", "moments", "axis", "jets"],
        "finding": "Defines natural radial/angle pullbacks and proves smoothness, derivative identities, transport-coefficient reconstruction, reconstructed angular/axial equations, average-integral reconstruction, and existence of natural profile families. These are reduced profile identities and do not export the final selected Cartesian five-observable equality.",
        "anchors": "21-186; 201-280; 284-417; 427-474; 552-690",
    },
    "NavierStokes/OutgoingCone.lean": {
        "clusters": ["profiles", "pressure", "rank", "jets", "time"],
        "finding": "Identifies actual outgoing cone components, proves hold/relaxed/true cone margins, pressure and stress bounds, compact pre-cone gaps, and ordered parameter choices. This is a positive outgoing-cone and stress-control layer, not the final Cartesian moment export.",
        "anchors": "24-120; 142-213; 227-367; 392-520; 550-700",
    },
    "NavierStokes/LoopMoments.lean": {
        "clusters": ["moments", "profiles", "rank"],
        "finding": "Provides exact finite-set mass, mean, variance, energy, rephasing, and two-point feasibility algebra for the loop construction. The results are finite reduced moment feasibility statements, not the five paper observables evaluated on the selected Cartesian field.",
        "anchors": "30-98; 100-199; 200-304",
    },
    "NavierStokes/OutgoingEntranceCone.lean": {
        "clusters": ["profiles", "pressure", "moments", "time", "jets"],
        "finding": "Constructs the outgoing entrance history, angular/axial lag and pressure histories, derives integral identities, positivity/barriers, envelope bounds, canonical pre-endpoint identities, and preliminary cone margins for actual reset data. This is a substantive reduced entrance/stress bridge below the final endpoint.",
        "anchors": "24-143; 229-477; 491-877; 1013-1252; 1385-1558; 1888-2178",
    },
    "NavierStokes/ProfileSpectralCone.lean": {
        "clusters": ["profiles", "rank", "moments", "axis"],
        "finding": "Derives primary and target spectral cones from the true profile cone, identifies the actual stress vector with integral-history stocks, and proves normalized-coordinate and shear identities with compact signed-shear bounds. This is a reduced cone/stress bridge, not final selected-field moment transport.",
        "anchors": "23-107; 137-238; 251-374; 449-502",
    },
    "NavierStokes/RadialModulation.lean": {
        "clusters": ["profiles", "moments", "jets", "time"],
        "finding": "Defines the logarithmic radial modulation, proves smoothness and exact shear derivative formulas, constructs periodic zero-mean primitives, and proves uniform eta-jet deviations of order O(1/n). This confirms modulation control at the reduced profile level; it does not prove preservation of the final Cartesian observables.",
        "anchors": "30-64; 66-165; 195-269; 278-419",
    },
    "NavierStokes/SimilarityHomogeneity.lean": {
        "clusters": ["profiles", "axis", "cartesian-assembly", "time"],
        "finding": "Proves anisotropic coordinate scaling, smooth physical/chart maps, transition identities and inverses, domain transport, and exact chart-weight/flat-factor transition. This is a genuine coordinate/homogeneity bridge, but no final radial-moment equality is exported.",
        "anchors": "25-133; 143-254; 275-371",
    },
    "NavierStokes/SimilarityProfile.lean": {
        "clusters": ["profiles", "axis", "jets", "cartesian-assembly"],
        "finding": "Defines the physical-to-inner similarity pullback and proves positivity, smoothness, complete time/space chain rules, higher derivative pullbacks, and physical-domain openness. These are coordinate regularity results below Cartesian field assembly, with no selected Witness moment transport.",
        "anchors": "27-92; 99-233; 242-327",
    },
    "NavierStokes/TemporalMeanUpdate.lean": {
        "clusters": ["moments", "time", "pressure", "cartesian-assembly", "jets"],
        "finding": "Proves Fourier differentiation and reconstruction for the actual covering map, zero-mean temporal inverse identities, support/periodicity, native pullback identities, desired mean increments, and smooth supported axial/radial updates. This is a real temporal mean-update bridge; it does not by itself compose to the final selected Cartesian five-observable tuple.",
        "anchors": "27-144; 145-276; 358-590; 617-805; 844-1114; 1130-1250",
    },
    "NavierStokes/AxisymmetricFields.lean": {
        "clusters": ["cartesian-assembly", "axis", "jets", "energy"],
        "finding": "Constructs an axisymmetric Cartesian potential and its actual spatial curl, proves explicit velocity components, smoothness, divergence freedom, axis values, and compact support/cylinder bounds. This is a genuine 3D curl lift and support bridge, but it does not transport the five paper moments through the selected global sums.",
        "anchors": "20-39; 41-95; 104-202; 216-300",
    },
    "NavierStokes/CommonCoverSolve.lean": {
        "clusters": ["cartesian-assembly", "time", "jets", "profiles"],
        "finding": "Builds the cover equivalence, deck transformations, copy/anchored solves, localised copy sums, torus descent, support preservation, smoothness, covering norm bounds, and affine path derivative estimates. This is substantial periodised-copy infrastructure; it does not prove final radial-moment transport into Witness.",
        "anchors": "22-68; 73-167; 179-329; 345-384; 528-731; 739-892",
    },
    "NavierStokes/HeatProfileExtension.lean": {
        "clusters": ["profiles", "axis", "moments", "jets"],
        "finding": "Constructs a globally smooth Borel/endpoint extension matching every actual right-hand heat-profile jet, proves equality with the original profile on the nonnegative half-line, compact vanishing on the negative tail, derivative bounds, positivity near the origin, and the scaled physical parameter composition. This is a genuine heat-profile extension bridge, not a selected Cartesian moment theorem.",
        "anchors": "1-38; 40-119; 121-206; 208-302; 304-380",
    },
    "NavierStokes/JetBounds.lean": {
        "clusters": ["jets", "cartesian-assembly"],
        "finding": "Defines finite and all-order Frechet jet bounds and proves monotonicity, derivative, addition, bilinear, multiplication, transport, second-derivative, and perturbation estimates. This is generic rate algebra used by later constructions; it does not encode radial moments or endpoint semantics.",
        "anchors": "31-62; 70-187; 193-280",
    },
    "NavierStokes/LocalizedMomentRepair.lean": {
        "clusters": ["moments", "profiles", "rank", "jets"],
        "finding": "Constructs smooth compactly supported bump repairs on fixed interior intervals, proves nonsingular generalized-power moment matrices, exact Lebesgue moment identities for arbitrary finite debt, linearity, support preservation, and derivative bounds. This is a genuine localized reduced-profile repair theorem, not transport to the selected Cartesian Witness.",
        "anchors": "21-68; 74-145; 147-191; 195-240; 251-342",
    },
    "NavierStokes/MomentRepair.lean": {
        "clusters": ["moments", "rank", "profiles"],
        "finding": "Defines abstract finite linear moment repair and proves exact matching, uniqueness, idempotence, support preservation, and contraction-side correction estimates under explicit nonsingularity hypotheses. It is generic finite-dimensional repair algebra; no selected-field composition is asserted.",
        "anchors": "29-85; 94-124; 130-173; 201-206",
    },
    "NavierStokes/SmoothFamilyTorusInverse.lean": {
        "clusters": ["time", "jets", "pressure", "moments"],
        "finding": "Defines smooth parameter families on the torus, means, Fourier inverses, zero-mean identities, support preservation, multiplier/jet bounds, nonbar decomposition, and finite/all-order inverse estimates. This is real torus inverse and mean machinery, not a final Cartesian radial-observable theorem.",
        "anchors": "20-69; 81-187; 218-266; 572-650; 689-805; 963-1082",
    },
    "NavierStokes/StressAlgebra.lean": {
        "clusters": ["moments", "pressure", "profiles", "residual"],
        "finding": "Defines explicit angular/axial radial source and primitive expressions and proves differentiated, integrated, lag, logarithmic, and stress-free substitution identities under stated moment and pressure balances. This is a substantive reduced stress calculus, not final selected Cartesian transport.",
        "anchors": "23-68; 79-126; 128-265; 272-338",
    },
    "NavierStokes/UniformFourierAlias.lean": {
        "clusters": ["moments", "time", "jets", "cartesian-assembly"],
        "finding": "Proves exact compact transport aliases, source and alias jet bounds, radial-slice and torus-mean identities, real centered/inverse constructions, support preservation, finite-jet and mean-class bounds, and superflat alias estimates. This is a genuine mean/alias transport layer, but no theorem here identifies the public selected Cartesian field with all five paper observables.",
        "anchors": "31-69; 116-281; 383-435; 484-626; 647-804; 893-1070; 1124-1322",
    },
    "NavierStokes/ZerothStressIdentity.lean": {
        "clusters": ["moments", "pressure", "profiles", "axis"],
        "finding": "Identifies leading angular/axial coefficients and weighted stresses, proves regularity through the axis, leading density formulas, scheme germs, raw stress identities, and equality of extended stress slots with literal leading stress. This is a reduced leading-stress bridge, not final endpoint transport.",
        "anchors": "24-68; 71-153; 167-225; 281-369",
    },
    "NavierStokes/AxisHolomorphicJoint.lean": {
        "clusters": ["axis", "profiles", "jets"],
        "finding": "Extends the axis holomorphic profile to joint parameter smoothness, proves compact-family derivative estimates, real agreement and common joint extensions, and uniform mean-value remainder control. This is analytic parameter regularity, not selected Cartesian moment transport.",
        "anchors": "25-61; 65-150; 158-223",
    },
    "NavierStokes/AxisProfile.lean": {
        "clusters": ["axis", "profiles", "jets"],
        "finding": "Defines radial operator/inverse coefficients and explicit low-order profile expansions, then proves coefficient inversion and leading axial derivative identities. This is local axis-profile algebra below the selected endpoint.",
        "anchors": "19-48; 80-168",
    },
    "NavierStokes/GaugeMassPreservation.lean": {
        "clusters": ["moments", "rank", "time", "pressure"],
        "finding": "Proves moving-gauge stream identities, torus-average congruence, zero radial moments for temporal increments, preservation of angular/axial torus means, and preservation of the two local `ZeroMassesOn` invariants on the valid slow region. This is a genuine local conservation bridge; it is not the complete global selected Cartesian five-observable theorem.",
        "anchors": "23-105; 111-160; 161-228; 229-299",
    },
    "NavierStokes/PhysicalCurlCovariance.lean": {
        "clusters": ["cartesian-assembly", "axis", "jets", "residual"],
        "finding": "Proves cylindrical/Cartesian curl covariance, moving-frame connection terms, pullback and cutoff identities, scaled-graph physical curl, Cartesian potential overlap/germ compatibility, global Cartesian potential and velocity smoothness, divergence freedom, axis zero, and constructed-wave curl identities. This is a strong physical curl bridge, but it does not prove the final five-observable radial transport into `Witness`.",
        "anchors": "28-101; 107-242; 271-376; 393-510; 521-610; 633-808; 820-1008; 1035-1063",
    },
    "NavierStokes/PowerMomentMatrix.lean": {
        "clusters": ["moments", "rank", "profiles"],
        "finding": "Proves nonsingularity of exponential and positive-power evaluation matrices, an interval zero-from-zero-integral lemma, exact power-sum integral expansion, and nonsingularity of interval and bump moment matrices under injectivity, positivity, separation, and nonzero-mass hypotheses. This is genuine general repair-matrix algebra, not the selected Cartesian endpoint theorem.",
        "anchors": "29-74; 120-175; 178-248; 252-309",
    },
    "NavierStokes/PreparedOutgoing.lean": {
        "clusters": ["profiles", "moments", "time"],
        "finding": "Defines `PreparedProfile`, proves existence from the scheduled family, proves arbitrarily late nominal matching while keeping the prepared profile and schedule fixed, and packages a fixed prepared profile. This is profile preparation, not selected Cartesian transport.",
        "anchors": "20-78; 82-116; 119-126",
    },
    "NavierStokes/R3/GaussianMoments.lean": {
        "clusters": ["r3", "energy", "moments"],
        "finding": "Proves whole-space integrability on R3 for Gaussian, first norm-weighted Gaussian, and second norm-weighted Gaussian functions using an explicit half-decay estimate. This supports analytic estimates but is not a selected radial moment identity or pressure representation.",
        "anchors": "21-34; 36-65; 67-81",
    },
    "NavierStokes/ScheduledProfileChoice.lean": {
        "clusters": ["profiles", "time", "moments"],
        "finding": "Constructs scheduled cores and profiles below caller-supplied positive bounds, proves height-cap positivity and bounds, and packages an additional terminal small-tail condition. This is genuine schedule/profile existence, not the public endpoint composition.",
        "anchors": "20-58; 60-78; 80-101; 105-129",
    },
    "NavierStokes/SmoothMomentRepair.lean": {
        "clusters": ["moments", "rank", "profiles", "jets"],
        "finding": "Defines a quadratic repair equation on a normed space and proves local analytic/smooth solution branches, norm bounds, correction-ball uniqueness, compact-parameter inverse bounds, and uniform small-correction existence. This is a strong abstract nonlinear repair theorem, but its variables are generic operators and debt vectors rather than the selected Cartesian radial observables.",
        "anchors": "27-77; 80-110; 114-208; 211-231; 234-265; 271-337",
    },
    "NavierStokes/ParametricTorusInverse.lean": {
        "clusters": ["moments", "time", "jets", "profiles"],
        "finding": "Defines a smooth real-parameter/torus source, proves parameter and torus derivative regularity, periodicity and zero-mean preservation, coefficient and multiplier bounds, Fourier inverse representations, rapid-decay and finite-jet estimates, and smooth inverse-multiplier application. This is a substantial parametric torus inverse layer, not the final selected Cartesian five-observable theorem.",
        "anchors": "20-112; 116-185; 208-240; 247-330; 347-434; 474-591; 598-682",
    },
    "NavierStokes/PeriodicPhaseAssembly.lean": {
        "clusters": ["cartesian-assembly", "time", "jets", "moments", "profiles"],
        "finding": "Defines compact clock windows and smooth cutoffs, proves local finiteness and periodicity of tsum-based scalar periodisation, clock germs and path identities, phase/angular-lift periodicity, native-phase germ and jet equality, geometry refinement/transport, physical block construction, and carrier adapter periodicity/germ/jet facts. This is genuine phase/common-cover transport, not the public selected-field five-observable export.",
        "anchors": "24-116; 127-201; 208-251; 260-404; 408-456; 458-591; 598-684; 692-749; 763-884",
    },
    "NavierStokes/R3/ForceL2Norm.lean": {
        "clusters": ["r3", "energy", "force"],
        "finding": "Defines the R3 force L2 norm and cumulative force norm, proves continuity, interval integrability, differentiability, nonnegativity, monotonicity, and the square-integral identity. This supplies whole-space force-energy accounting, not selected-field moment transport.",
        "anchors": "20-24; 26-80",
    },
    "NavierStokes/R3/IntegratedDissipation.lean": {
        "clusters": ["r3", "energy", "force"],
        "finding": "Derives the integrated viscous energy balance, force-work bound, candidate dissipation integrability, L2 control by cumulative force, uniform kinetic-energy control, finite-time dissipation estimates, and the bundled candidate energy estimates. These are genuine selected CandidateProperties energy consequences, but they do not encode the paper's five radial observables.",
        "anchors": "27-48; 52-69; 73-141; 143-181; 183-200; 203-246; 248-277; 279-292",
    },
    "NavierStokes/R3/PositiveTimeForce.lean": {
        "clusters": ["r3", "force", "time"],
        "finding": "Defines a smooth time cutoff, proves it is one on [3/8,1] and zero outside [1/16,21/16], and defines the positive-time force with smoothness and compact-positive-time support. This confirms a smooth temporal cutoff and does not support a discontinuous-cutoff objection.",
        "anchors": "21-44; 46-80",
    },
    "NavierStokes/R3/ScalarEnergyBound.lean": {
        "clusters": ["r3", "energy"],
        "finding": "Proves weighted, unweighted, and uniform forced Gronwall inequalities for a scalar energy with zero initial value. This is an abstract scalar energy estimate and is not a field-level moment or pressure theorem.",
        "anchors": "21-78",
    },
    "NavierStokes/R3/ViscousEnergyBalance.lean": {
        "clusters": ["r3", "energy", "force"],
        "finding": "Proves the exact compact-support viscous energy identity retaining viscosity and force work, its time derivative form, continuity of force work, and continuity of spatial partials on smooth slabs. This confirms a real Newtonian energy layer under explicit compact-support and residual hypotheses; it does not establish selected Cartesian five-moment transport.",
        "anchors": "21-53; 55-71; 73-81; 83-114",
    },
    "NavierStokes/ResidualPolarGraph.lean": {
        "clusters": ["axis", "cartesian-assembly", "residual", "jets"],
        "finding": "Defines the scaled physical radial projection, local angle, cylindrical point, and proves positivity, chart-angle identities, polar reconstruction, chart/cylindrical and spacetime reconstruction, and eventual chart-domain membership. This is an off-axis coordinate bridge for residual analysis; it does not evaluate a global radial moment tuple or close the origin-to-global endpoint transport.",
        "anchors": "21-46; 48-105; 112-177",
    },
    "NavierStokes/UniformPrimaryWeights.lean": {
        "clusters": ["cartesian-assembly", "jets", "profiles", "time", "moments"],
        "finding": "Propagates uniform weighted classes through square roots, quotients, derivatives, products, covariance weights, primary coefficients, cylindrical curls, curl remainders, actual phase data, cutoff coefficients, and wave corrections. It is a substantial uniform regularity/curl-rate layer, but its output is a rate class and not a selected whole-space barMoment equality.",
        "anchors": "54-152; 159-251; 263-313; 316-368; 370-489; 491-620; 625-650; 652-701; 705-736",
    },
    "NavierStokes/ModulatedHistories.lean": {
        "clusters": ["moments", "profiles", "rank", "jets", "time"],
        "finding": "Defines five-coordinate density/history fields, smooth periodic localisations, axis histories, profile rows, repair debt, edited fields, and repaired histories, with exact support, integrability, and restoration identities. This is strong reduced-profile history/repair evidence, not a final selected Cartesian barMoment transport theorem.",
        "anchors": "20-153; 188-313; 355-468; 574-683; 747-988; 1185-1425",
    },
    "NavierStokes/ActualInitialMean.lean": {
        "clusters": ["physical-data", "moments", "rank", "cartesian-assembly", "time"],
        "finding": "Assembles initial base/primary/temporal/ranked states and proves phase/cutoff, mean-zero, covariance, matched-flux, primary-data, cumulative, mean, debt, and zeroMasses results. This is concrete initial-stage physical data below the final endpoint, not global selected five-observable transport.",
        "anchors": "36-146; 186-309; 352-411; 422-477; 503-670",
    },
    "NavierStokes/HarmonicSourceSupport.lean": {
        "clusters": ["residual", "pressure", "cartesian-assembly", "jets", "profiles"],
        "finding": "Proves harmonic coefficient/source support under differentiation, angular operations, Laplacians, transport, gradients, nonlinear residuals, real projections, native unions, and source-family coverage, including complement germs/jets and native support. This is support infrastructure, not final radial-observable evaluation or pressure Poisson transport.",
        "anchors": "23-184; 208-342; 372-396; 429-620; 678-959",
    },
    "NavierStokes/HarmonicFields.lean": {
        "clusters": ["profiles", "moments", "cartesian-assembly", "jets"],
        "finding": "Defines finite harmonic coefficient algebra, angular characters/means, convolution, conjugate symmetry, band limitation, quadratic iterates, waves, coefficient differentiation, and angular differentiation with support and regularity identities. This is analytic harmonic calculus, not selected Cartesian five-observable or absolute pressure transport.",
        "anchors": "21-203; 228-312; 332-418; 438-610; 626-667",
    },
    "NavierStokes/ActualExteriorPrefix.lean": {
        "clusters": ["cartesian-assembly", "residual", "pressure", "profiles"],
        "finding": "Defines the exterior domain and exterior-stage proposition, then proves potential/direct/pressure prefix agreement, germs, velocity prefix agreement, and exterior prefix/germ results. This is positive finite-prefix exterior matching, not the global selected endpoint moment composition.",
        "anchors": "23-56; 71-127; 142-161",
    },
    "NavierStokes/ActualParticularMeanGain.lean": {
        "clusters": ["physical-data", "moments", "rank"],
        "finding": "Defines particular-mean input/result propositions and proves a covariance class, moving-field covariance, and the post-particular gain under the stated parameter bound. This is a local cycle-level covariance result, not a public Witness or global radial-observable theorem.",
        "anchors": "20-69; 104-138",
    },
    "NavierStokes/ActualSignedFamilySupport.lean": {
        "clusters": ["force", "pressure", "cartesian-assembly", "profiles"],
        "finding": "Defines potential and pressure copy families and proves their support, smoothness, and source-domain properties. This is concrete signed-family support evidence, not pressure Poisson semantics or final selected five-observable transport.",
        "anchors": "76-183",
    },
    "NavierStokes/JointResidualLimits.lean": {
        "clusters": ["endpoint", "residual", "jets", "time"],
        "finding": "Builds genuine one-sided smooth extensions, joint boundary limits, locally uniform and compact-uniform convergence, compatible derivative recurrences, and an extended residual that agrees on the past and is flat at the spacetime origin. This strengthens endpoint regularity and boundary-limit infrastructure, but it does not evaluate or transport the five selected Cartesian radial observables.",
        "anchors": "30-65; 73-116; 120-175; 181-256; 257-308",
    },
    "NavierStokes/MatchingDebtBounds.lean": {
        "clusters": ["moments", "rank", "profiles", "jets", "time"],
        "finding": "Defines five-coordinate debt extensions, reset vectors, jet bounds, vanishing sums, matching budgets, and existence of ordered nominal/assembled witnesses with small coefficients. This is substantive reduced-profile debt and matching control; it does not identify those debt coordinates with the final selected Cartesian barMoment tuple or public Witness.",
        "anchors": "19-43; 68-128; 136-206; 244-340; 385-429; 433-477; 510-559; 578-652; 753-928",
    },
    "NavierStokes/MaximalLifespan.lean": {
        "clusters": ["endpoint", "energy", "force", "time"],
        "finding": "Defines classical solutions, overlap agreement, admissible/maximal lifespans, periodic slab bounds, and the candidate's non-extension past time one under the supplied candidate hypotheses. This is a whole-space lifespan consequence relative to the formal candidate and force; it does not prove the paper's five-moment transport or an autonomous-force criterion.",
        "anchors": "21-58; 79-124; 130-190; 198-237; 260-292",
    },
    "NavierStokes/MeanBoundsReindex.lean": {
        "clusters": ["residual", "jets", "cartesian-assembly", "profiles"],
        "finding": "Proves pullback and return equivalences for strip, mean, cumulative, operator, residual-block, and uniform-velocity bounds under linear isometric reindexing. This is exact rate-class chart invariance, not a value-level radial-moment transport theorem for the selected field.",
        "anchors": "23-124; 127-170; 182-288",
    },
    "NavierStokes/PulseEnergyHistory.lean": {
        "clusters": ["energy", "force", "profiles", "time"],
        "finding": "Derives explicit pulse energy weights, parameter derivatives, incoming prefix history, source and ratio bounds, and corrected pulse-history bounds from the actual pulse data. This is concrete intermediate energy/history control; it does not export the five selected Cartesian observables or alter the endpoint correspondence classification.",
        "anchors": "21-137; 147-204; 227-365; 370-434; 439-490",
    },
    "NavierStokes/RadialFluxResidual.lean": {
        "clusters": ["axis", "residual", "profiles", "cartesian-assembly"],
        "finding": "Defines the radial quotient B = -V/(2s), proves its regularity and derivative formulas off the axis, derives the weighted radial flux residual, and identifies it with the physical Cartesian residual projection. This is a genuine local axisymmetric residual bridge with an explicit positive-radius condition, not a global barMoment or endpoint Witness theorem.",
        "anchors": "23-149; 170-205; 209-249",
    },
    "NavierStokes/NormalScaling.lean": {
        "clusters": ["cartesian-assembly", "residual", "profiles"],
        "finding": "Proves tangent-projection, projected-RHS, pressure-coefficient, and projected-operator rescaling identities in a finite-dimensional inner-product setting. This is algebraic normal/tangent scaling, not selected-field or radial-observable transport.",
        "anchors": "1-12; 22-86",
    },
    "NavierStokes/R3/ActualPressureFlux.lean": {
        "clusters": ["pressure", "endpoint", "energy"],
        "finding": "For comparison hypotheses, proves smoothness and integrability of the pressure-difference flux against a compact cutoff and identifies it with a canonical Riesz pairing. The quantified objects are u, v, p, q and the integrand uses p-q, so this is relative comparison rather than an absolute selected-pressure representative.",
        "anchors": "23-34; 36-58",
    },
    "NavierStokes/R3/ComparisonFourierSetup.lean": {
        "clusters": ["pressure", "r3"],
        "finding": "Defines Schwartz complex tests, the Riesz symbol, Riesz test operator, pressure pairing, and Fourier H-norm. This supplies Fourier test vocabulary only; it does not transport a selected field to radial moments.",
        "anchors": "1-30",
    },
    "NavierStokes/R3/LocalizedTransport.lean": {
        "clusters": ["energy", "pressure", "residual"],
        "finding": "Proves divergence, derivative integration, transport, and pressure integration identities for compactly weighted difference fields. This is localised difference-energy calculus, not a global absolute pressure-Poisson realization.",
        "anchors": "26-91",
    },
    "NavierStokes/R3/PressureFluxIdentity.lean": {
        "clusters": ["pressure", "energy", "r3"],
        "finding": "Builds smooth compactly supported cutoff-gradient flux functions, weighted components, canonical pressure linear functionals, and a gradient-identification flux identity. Compact support belongs to the test/cutoff and the result remains comparative.",
        "anchors": "26-45; 49-114; 114-176",
    },
    "NavierStokes/R3/PressureFunctionals.lean": {
        "clusters": ["pressure", "r3", "energy"],
        "finding": "Defines time-averaged pressure-difference functionals from velocity and tensor coefficients, proves integrability and Fourier-H3 bounds, and exposes a complex-linear pairing. This is a bounded functional on tests, not an absolute pressure field or selected Cartesian moment theorem.",
        "anchors": "122-140; 142-192; 244-287",
    },
    "NavierStokes/R3/PressureRecoveryHelpers.lean": {
        "clusters": ["pressure", "r3", "residual"],
        "finding": "Defines compact real tests and proves the differentiated pressure-Poisson comparison identity against compact tests. gradient_poisson_test explicitly has p-q, u-v, equal-residual hypotheses, and compact test support; it does not recover p alone on all of R3.",
        "anchors": "32-109; 114-160; 162-189",
    },
    "NavierStokes/R3/PressureTemporalIdentity.lean": {
        "clusters": ["pressure", "time", "residual"],
        "finding": "Proves temporal integration by parts and pressure-gradient identities against compact spatial and temporal tests supported in the interior time interval. This is a distributional comparison identity, not absolute endpoint pressure semantics.",
        "anchors": "34-109; 120-178; 187-209",
    },
    "NavierStokes/R3/RieszHeatRepresentation.lean": {
        "clusters": ["pressure", "r3"],
        "finding": "Defines heat-weighted second-order Fourier symbols and proves integrability and an integral representation of Riesz tests. This is an analytic representation layer, not selected-field moment evaluation.",
        "anchors": "26-69; 71-144",
    },
    "NavierStokes/R3/RieszL2Bounds.lean": {
        "clusters": ["pressure", "energy", "r3"],
        "finding": "Proves L2 pairing, MemLp 2, and integral-square bounds for Riesz test operators. These are functional estimates only and contain no selected radial-observable transport.",
        "anchors": "26-121; 123-179",
    },
    "NavierStokes/R3/RieszLinearityDecay.lean": {
        "clusters": ["pressure", "r3", "jets"],
        "finding": "Proves additivity, scalar and finite-sum linearity, and Riemann-Lebesgue decay of Riesz tests. This is test-operator regularity/decay only.",
        "anchors": "21-83",
    },
    "NavierStokes/R3/RieszPairing.lean": {
        "clusters": ["pressure", "r3"],
        "finding": "Proves integrability, Fourier pairing, conjugate pairing, and self-adjointness identities for Riesz test operators. This is a weak Fourier comparison layer, not an absolute pressure representative.",
        "anchors": "24-109",
    },
    "NavierStokes/R3/RieszSymbolRegularity.lean": {
        "clusters": ["pressure", "r3", "jets"],
        "finding": "Proves boundedness, measurability, integrability, smoothness, and bounds for Riesz multipliers and tests. It supplies symbol regularity, not physical-field transport.",
        "anchors": "21-120",
    },
    "NavierStokes/R3/SmoothSobolevL6.lean": {
        "clusters": ["energy", "jets", "r3"],
        "finding": "Proves cutoff derivative bounds, Sobolev L6 estimates, and smooth MemLp 6 consequences. This is functional regularity and estimation, not radial-moment transport.",
        "anchors": "26-152",
    },
    "NavierStokes/R3/ViscosityScaling.lean": {
        "clusters": ["residual", "energy", "endpoint", "cartesian-assembly"],
        "finding": "Defines velocity and pressure rescaling and proves derivative, divergence, advection, gradient, Laplacian, residual, speed-unboundedness, candidate, and global-solution scaling identities. This is a genuine PDE scaling layer, but it transports residual/candidate predicates rather than the five paper observables.",
        "anchors": "24-91; 93-139; 141-197",
    },
    "NavierStokes/R3/WholeSpaceComparisonClosure.lean": {
        "clusters": ["pressure", "energy", "endpoint", "r3"],
        "finding": "eq_of_pressure_flux_bound combines compact weighted estimates and a pressure-flux bound to prove equality of two solutions on a closed pre-singular slab. Its hypotheses compare u,v,p,q under equal residuals; it is a strong relative uniqueness consequence, not an absolute pressure or five-moment theorem.",
        "anchors": "25-53; 54-69; 70-157",
    },
    "NavierStokes/ScalarParticularSupport.lean": {
        "clusters": ["profiles", "pressure", "cartesian-assembly"],
        "finding": "Defines scalar particular copy data/cells and proves cutoff support, a native-zero alternative, and zero germs. This is support bookkeeping, not selected endpoint transport.",
        "anchors": "31-73; 75-132",
    },
    "NavierStokes/TangentProjection.lean": {
        "clusters": ["cartesian-assembly", "profiles", "residual"],
        "finding": "Proves algebraic tangent projection, idempotence, projected balance, pressure cancellation, differentiated tangency, preservation, and coefficient sign facts. This is finite-dimensional constraint algebra, not a global field realization.",
        "anchors": "27-82; 84-153",
    },
    "NavierStokes/ActualCoreSupport.lean": {
        "clusters": ["axis", "cartesian-assembly", "profiles", "time"],
        "finding": "Defines the concrete radial/core carrier used by the actual initialisation path and proves support, continuity, germ, initial-support, and invariant properties for primary velocity, pressure, and Gaussian pieces. This is concrete support geometry, not transport of the five selected-field observables.",
        "anchors": "23-51; 56-145; 184-308",
    },
    "NavierStokes/ActualSignedUnmaskedBinding.lean": {
        "clusters": ["cartesian-assembly", "profiles", "time"],
        "finding": "Binds signed unmasked branch states, labels, masks, amplitudes, pressure, potentials, and wave factors. The declarations establish branch/layout algebra but expose no selected Cartesian moment equality or endpoint pressure representation.",
        "anchors": "1-25; declaration and binding blocks",
    },
    "NavierStokes/ActualSignedUnmaskedBounds.lean": {
        "clusters": ["cartesian-assembly", "jets", "profiles", "time"],
        "finding": "Proves dyadic/grid-mask, localised potential, amplitude, pressure, and jet/support bounds for the signed unmasked family. These are local rate and support contracts; they do not evaluate barMoment or transport the paper tuple.",
        "anchors": "1-20; declaration and bound blocks",
    },
    "NavierStokes/AxisTailRegularity.lean": {
        "clusters": ["axis", "jets", "profiles"],
        "finding": "Axis/tail regularity layer for reduced fields and their limiting behaviour. It supplies regularity estimates, not a global Cartesian radial-moment transport theorem.",
        "anchors": "source-indexed declaration review",
    },
    "NavierStokes/GaugeExcludedBounds.lean": {
        "clusters": ["cartesian-assembly", "jets", "profiles"],
        "finding": "Bounds the gauge-excluded pieces and their derivatives on the selected local geometry. This controls rates after a gauge choice; no five-moment equality reaches the endpoint.",
        "anchors": "source-indexed declaration review",
    },
    "NavierStokes/GermEndpointInputs.lean": {
        "clusters": ["endpoint", "jets", "cartesian-assembly"],
        "finding": "Packages germ and endpoint input data used by later candidate assembly. It supplies boundary/regularity inputs, not a theorem identifying the assembled field with the five paper observables.",
        "anchors": "source-indexed declaration review",
    },
    "NavierStokes/HeatSwitchHistoryDerivatives.lean": {
        "clusters": ["energy", "jets", "time", "profiles"],
        "finding": "Differentiates heat-switch histories and proves the associated rate/support estimates. It is an intermediate history/rate layer and does not prove selected-field moment preservation.",
        "anchors": "source-indexed declaration review",
    },
    "NavierStokes/MixedDiagonalSchedule.lean": {
        "clusters": ["cartesian-assembly", "profiles", "time"],
        "finding": "Defines mixed diagonal schedule data and proves its schedule/support relationships. It is scheduling infrastructure, not a value-level Cartesian-to-radial bridge.",
        "anchors": "source-indexed declaration review",
    },
    "NavierStokes/OffplaneJetExtensions.lean": {
        "clusters": ["axis", "jets", "cartesian-assembly"],
        "finding": "Extends off-plane jet estimates across the relevant geometric regions. This addresses regularity and extension bounds, not the global radial observables of the selected field.",
        "anchors": "source-indexed declaration review",
    },
    "NavierStokes/OscillatoryCurl.lean": {
        "clusters": ["cartesian-assembly", "jets", "residual"],
        "finding": "Controls oscillatory curl constructions and their derivative/rate behaviour. The file does not by itself prove that curl, localisation, and summation preserve the five moments.",
        "anchors": "source-indexed declaration review",
    },
    "NavierStokes/PhysicalStageSupport.lean": {
        "clusters": ["cartesian-assembly", "profiles", "time"],
        "finding": "Provides support and germ facts for physical stage pieces. Support preservation is not a theorem of radial-moment preservation after global assembly.",
        "anchors": "source-indexed declaration review",
    },
    "NavierStokes/R3/ConservativeDifference.lean": {
        "clusters": ["pressure", "energy", "residual", "r3"],
        "finding": "Derives conservative difference equations, integration-by-parts identities, weak pressure-gradient identities, and a compact-test Poisson identity for p-q under equal residuals. This is a rigorous comparative weak PDE layer; it does not recover an absolute selected pressure or five Cartesian moments.",
        "anchors": "1-19; 137-158; 428-468",
    },
    "NavierStokes/R3/PressureFluxTest.lean": {
        "clusters": ["pressure", "energy", "r3"],
        "finding": "Constructs smooth compact pressure-flux test functions and proves support, Lp, derivative, and cutoff-flux bounds. The compactness belongs to the test, not to an absolute pressure representative or selected-field moment theorem.",
        "anchors": "22-61; 284-331",
    },
    "NavierStokes/R3/PressureRecovery.lean": {
        "clusters": ["pressure", "energy", "residual", "r3"],
        "finding": "Defines comparison hypotheses for u,v,p,q and proves pressure-gradient recovery against compact tests from equal residuals and finite energy. Every recovery conclusion is comparative and uses p-q and u-v; it is not an absolute global pressure-Poisson theorem for the selected witness.",
        "anchors": "31-44; 388-438",
    },
    "NavierStokes/R3/RieszTestOperators.lean": {
        "clusters": ["pressure", "jets", "r3"],
        "finding": "Proves differentiability, integrability, Lp, Sobolev, and Laplacian identities for Riesz test operators and the pressure pairing. This supplies analytic test machinery only, not selected-field radial-moment evaluation.",
        "anchors": "27-123; 166-243; 277-284",
    },
    "NavierStokes/SchedulePressure.lean": {
        "clusters": ["pressure", "profiles", "time", "axis"],
        "finding": "Defines the reduced outgoing schedule's axis pressure from an angular profile and proves smoothness, sign, derivative, integrability, and natural-axis profile facts. This is reduced schedule pressure, not an absolute whole-space pressure representative.",
        "anchors": "22-69; 123-226; 244-267",
    },
    "NavierStokes/TailCone.lean": {
        "clusters": ["energy", "profiles", "time", "jets"],
        "finding": "Provides extensive reduced tail/cone, release, angular-suppression, energy, mass, ratio, and future-bound estimates. These are upstream asymptotic controls; they do not establish endpoint transport of the five named paper moments.",
        "anchors": "source-indexed declaration review; 1714-line tail/cone module",
    },
    "NavierStokes/TimeLocalization.lean": {
        "clusters": ["endpoint", "force", "residual", "time", "cartesian-assembly"],
        "finding": "Defines activatedVelocity and activatedPressure using the smooth time switch. It proves smoothness, periodicity, zero initial data, divergence preservation, the exact switched residual formula, late-time equality, and equivalence of speed blow-up. The residual formula explicitly contains switch and temporal/advection terms; no five-moment transport is asserted.",
        "anchors": "1-16; 27-32; 57-91; 110-138; 166-223",
    },
    "NavierStokes/UniformBlockBounds.lean": {
        "clusters": ["jets", "profiles", "cartesian-assembly", "time"],
        "finding": "Proves uniformity under reindexing, slicing, pairing, signed/product blocks, native assembly, and state reindexing for wave coefficients and pressure/amplitude blocks. These are uniform rate contracts, not value-level radial-moment transport.",
        "anchors": "29-89; 111-239; 255-348",
    },
    "NavierStokes/ActivationContinuation.lean": {
        "clusters": ["profiles", "moments", "axis", "time"],
        "finding": "Defines relaxed continuation, shear/projection/transverse coordinates, hold models, stock and field jets, density histories, and transfer/bound lemmas. This is substantial reduced activation and profile-control algebra; it does not identify the final selected Cartesian observables.",
        "anchors": "23-126; 144-239; 500-698; 779-977",
    },
    "NavierStokes/ActualMeanPotentialRealization.lean": {
        "clusters": ["cartesian-assembly", "axis", "residual", "profiles"],
        "finding": "Provides a genuine local Cartesian potential/curl realization: componentPotential_realCurl and cartesianPotential_curl_forward identify the real Cartesian curl with the meridional velocity on valid cylindrical domains, and coherent_angularField_curl propagates this identity to coherent physical mean fields. This is positive local transport, but it is chart/local-field level and does not establish the final selected global five-observable equality.",
        "anchors": "24-40; 103-190; 318-440",
    },
    "NavierStokes/CurlClassBounds.lean": {
        "clusters": ["cartesian-assembly", "jets", "residual"],
        "finding": "Bounds curl classes and derivative/rate behaviour for assembled fields. These bounds support smooth Cartesian construction but do not evaluate the five radial observables after global localisation and summation.",
        "anchors": "source-indexed declaration review",
    },
    "NavierStokes/SmoothFourierData.lean": {
        "clusters": ["profiles", "jets", "cartesian-assembly"],
        "finding": "Defines smooth Fourier-side data and proves the associated regularity and decay facts. It is harmonic/Fourier infrastructure, not selected-field radial-moment transport.",
        "anchors": "source-indexed declaration review",
    },
    "NavierStokes/FourierAlias.lean": {
        "clusters": ["profiles", "cartesian-assembly", "jets"],
        "finding": "Provides Fourier aliases and conversion identities used by the wave/field layers. The aliases do not themselves identify the final Cartesian field with the five paper observables.",
        "anchors": "source-indexed declaration review",
    },
    "NavierStokes/MixedAxisPreservation.lean": {
        "clusters": ["axis", "cartesian-assembly", "profiles"],
        "finding": "Proves preservation facts for mixed axis/copy data and associated geometric pieces. This is a local axis-preservation result, not a global radial-observable theorem.",
        "anchors": "source-indexed declaration review",
    },
    "NavierStokes/NaturalCore.lean": {
        "clusters": ["axis", "profiles", "endpoint"],
        "finding": "Defines the natural core and proves origin/axis values, regularity, and speed-unboundedness consequences for the reduced core. It is a core-level construction result, not the complete selected Cartesian field transport.",
        "anchors": "source-indexed declaration review; 420-504",
    },
    "NavierStokes/ActivationHolomorphic.lean": {
        "clusters": ["profiles", "time", "jets", "axis"],
        "finding": "Defines joint smooth/holomorphic activation families, averages, primitives, continuation, controlled activation, and real/complex regularity. This proves parameter regularity, not the selected Cartesian five-moment equality.",
        "anchors": "24-148; 232-342; 443-677",
    },
    "NavierStokes/ActualWaveRegularityData.lean": {
        "clusters": ["cartesian-assembly", "jets", "profiles", "time"],
        "finding": "Constructs concrete wave regularity data, deck/phase/radius maps, ordered-band and zero-germ alternatives, signed copies, smoothness, support, and tsum-zero consequences. This is genuine stage-wave support/regularity; no final radial observable equality is exposed.",
        "anchors": "24-146; 194-292; 692-910",
    },
    "NavierStokes/NominalConeAssembly.lean": {
        "clusters": ["moments", "profiles", "axis", "cartesian-assembly"],
        "finding": "Contains real reduced profile moment identities: history_eq_moment, moments_eq_profile_moments, and chart identities for outgoing/heated M, I, J, and S moments. These are positive reduced/chart transport results. They stop short of a theorem for the final selected Cartesian field after all global assembly stages.",
        "anchors": "185-214; 305-321; 327-445",
    },
    "NavierStokes/TailGaugePotential.lean": {
        "clusters": ["cartesian-assembly", "profiles", "axis", "residual"],
        "finding": "Defines the anchored/gauged summed swirl potential and proves spatialCurl_potential, including the spatial axis, together with heat-exterior potential identification and finalPotential_sameCurl. This is a strong local/global-potential curl component. It still does not prove that the selected endpoint's full localised/periodised field has the five radial observables.",
        "anchors": "58-100; 228-267; 433-470",
    },
    "NavierStokes/ActualSignedNativeRegularity.lean": {
        "clusters": ["jets", "profiles", "cartesian-assembly", "residual"],
        "finding": "Proves signed radial/dyadic pullback regularity, zero-outside jets, native potential/pressure smoothness and flatness, and request jets derived from residual classes. This is positive stage regularity evidence, not the final selected Cartesian five-observable equality.",
        "anchors": "65-190; 197-255; 309-325; 398-524",
    },
    "NavierStokes/ExponentLedger.lean": {
        "clusters": ["jets", "residual", "profiles"],
        "finding": "Defines wave/mean/particular/signed residual exponents and proves exact identities and lower-margin inequalities. This validates rate arithmetic but contains no field-level radial observable transport.",
        "anchors": "23-164; 170-321",
    },
    "NavierStokes/GaugeAliasDecay.lean": {
        "clusters": ["jets", "axis", "pressure", "time"],
        "finding": "Proves finite-jet fibre and local alias bounds, pressure mass localisation, compact-alias gains, superflat mean classes, frequency bounds, and zero-mass source/pressure alias facts. These are genuine gauge/alias controls, not final selected Cartesian moment evaluation.",
        "anchors": "29-246; 283-365; 392-579; 607-757",
    },
    "NavierStokes/GaugeStateCoherence.lean": {
        "clusters": ["pressure", "axis", "cartesian-assembly", "profiles"],
        "finding": "Proves fibre-local pressure aliases, endpoint congruence, gauge reconstruction, supported aliases, band scaling, radial-frequency transport, and similarity reconstruction. These are reduced/gauge coherence results, not an absolute selected pressure representative or final five-observable equality.",
        "anchors": "56-219; 271-421; 453-504",
    },
    "NavierStokes/IntervalCopyTransport.lean": {
        "clusters": ["time", "cartesian-assembly", "pressure", "force"],
        "finding": "Proves anchored/copy solve uniqueness and time-data transport, transported velocity/pressure identities, forcing continuity, zero entries, and common-solve transport. This is real copy-path transport but does not carry the paper's five radial moments into Witness.",
        "anchors": "29-192; 223-353; 394-495",
    },
    "NavierStokes/LabelSupportPreservation.lean": {
        "clusters": ["cartesian-assembly", "time", "profiles"],
        "finding": "Proves zero germs and support preservation for raw, corrected, native, particular, signed, block-summed, and transported-mask data. This controls localisation support but does not prove complete selected-field moment preservation.",
        "anchors": "28-225; 256-340; 394-499; 531-590",
    },
    "NavierStokes/ModulatedExterior.lean": {
        "clusters": ["profiles", "moments", "residual", "axis"],
        "finding": "Proves reduced exterior integral/pressure matching, heat-exterior identities, residual and residual-jet vanishing, and terminal extension. This is substantive reduced exterior evidence, not the selected Cartesian/localised/periodised five-moment theorem.",
        "anchors": "28-126; 144-307; 325-370; 444-513",
    },
    "NavierStokes/NaturalAxisData.lean": {
        "clusters": ["axis", "pressure", "profiles"],
        "finding": "Defines reduced axis quantities and proves parameter bounds, root existence/uniqueness, pressure-related positivity and derivative facts, and cutoff-parameter existence. This is reduced axis pressure data, not global Cartesian pressure semantics.",
        "anchors": "27-178; 192-315; 325-370",
    },
    "NavierStokes/PositiveTimeSignedData.lean": {
        "clusters": ["time", "cartesian-assembly", "pressure", "jets"],
        "finding": "Defines positive-time signed potential/pressure copies, cells, carriers, support, smoothness, wave data, germs, and physical bounds. It supplies concrete stage data but does not expose the final selected Cartesian five-observable equality.",
        "anchors": "29-177; 222-373; 397-523; 540-579",
    },
    "NavierStokes/PressureDatum.lean": {
        "clusters": ["pressure", "profiles", "axis"],
        "finding": "Defines a weighted pressure kernel and proves integrability, sign, smoothness, complex analytic continuation, derivative signs, prefix-mass inequalities, and ideal-prefix bounds. This is a reduced pressure datum, not an absolute whole-space selected pressure Poisson/Leray representation.",
        "anchors": "28-96; 116-243; 267-390; 401-450",
    },
    "NavierStokes/ScaledTangentTransport.lean": {
        "clusters": ["time", "cartesian-assembly", "pressure", "force"],
        "finding": "Proves coordinate/path/slot transport, finite transported copy cutoffs, tangent normal scaling, compatible copy solves, real/complex pressure and velocity transport, and finite transported periodisation. This is strong intermediate transport infrastructure but not the final selected five-observable composition.",
        "anchors": "22-83; 85-218; 218-286",
    },
    "NavierStokes/ActualCurrentWaveSupport.lean": {
        "clusters": ["cartesian-assembly", "profiles", "pressure", "residual"],
        "finding": "Proves current-band Cartesian-radius and native-point identities, native and local zero germs, carrier/annulus support, current-mode support, active-field support, and axis-zero behaviour. These are concrete local support and coordinate results, not a final barMoment or (M,I,J,S,Cp) equality.",
        "anchors": "273-345; 356-601; 657-706",
    },
    "NavierStokes/ActualIterationLedger.lean": {
        "clusters": ["jets", "residual", "time"],
        "finding": "Proves sigma/gain schedule arithmetic, physical gaps, residual exponents, rate inequalities, and eventual residual-rate growth. It is exponent bookkeeping and carries no selected-field moment observable.",
        "anchors": "36-110; 145-198; 228-315",
    },
    "NavierStokes/ActualSignedCoherence.lean": {
        "clusters": ["cartesian-assembly", "pressure", "time", "jets"],
        "finding": "Proves signed chart/scale/request transport and pushes amplitude and pressure scaling through tsum_congr and scalar extraction, with corresponding germ and exact-block transport. This is genuine local value-level transport but does not evaluate the final field with barMoment.",
        "anchors": "64-327; 331-426; 428-559",
    },
    "NavierStokes/CopyAngularInvariance.lean": {
        "clusters": ["cartesian-assembly", "axis", "residual"],
        "finding": "Proves angular/phase invariance through maps, derivatives, tsum, copy and pressure solves, cutoffs, cylindrical curl, curl remainders, and realised coefficients. This corrects any claim that all curl-level invariance is absent; it is not a five-observable radial evaluation.",
        "anchors": "33-105; 128-289; 304-370; 491-509",
    },
    "NavierStokes/CycleStateCoherence.lean": {
        "clusters": ["corrections", "cartesian-assembly", "pressure", "rank"],
        "finding": "Packages primitive particular/signed/temporal/ranked stages and constructs CycleTransport for state bands and temporal/pressure aliases across a correction cycle. The certificate is local StateBand/ErrorBand transport, not a selected whole-space barMoment equality.",
        "anchors": "279-310; 323-356; 377-452; 481-656",
    },
    "NavierStokes/DependentSignedPhysicalFamily.lean": {
        "clusters": ["cartesian-assembly", "pressure", "jets"],
        "finding": "Constructs dependent signed physical families, proves inactive-label zeros, diagonal support/smoothness, active periodised potential and pressure identities, identity-chart jet bounds, and physical scalar bounds. It stops before applying a final radial observable.",
        "anchors": "23-272; 321-365; 382-475; 551-562",
    },
    "NavierStokes/FuturePressureBounds.lean": {
        "clusters": ["pressure", "profiles", "moments"],
        "finding": "Proves future-tail clock/square-integral estimates, reduced future mass and pressure identities, derivative bounds, and invariance of future integrals under zero-total-integral corrections. These are reduced pressure-history results, not absolute selected pressure semantics or final five-moment transport.",
        "anchors": "36-219; 226-301; 316-489; 508-566",
    },
    "NavierStokes/NaturalAxisBridge.lean": {
        "clusters": ["axis", "pressure", "profiles", "moments"],
        "finding": "Defines reduced radial evaluation, parameter/source data, reconstructed profiles and remainders, and proves reduced pressure and integrated-solution identities. This is a genuine reduced-axis bridge, not a theorem for the selected Cartesian tsum field.",
        "anchors": "28-210; 221-321; 344-521; 621-716",
    },
    "NavierStokes/NaturalAxisCoefficients.lean": {
        "clusters": ["axis", "pressure", "profiles"],
        "finding": "Constructs analytic complex/real coefficient fields, coefficient families, ideal-prefix coefficients, phase derivatives, and amplitude bounds from PressureDatum. It contains analytic coefficient infrastructure but no selected endpoint or barMoment composition.",
        "anchors": "27-190; 299-429; 445-577",
    },
    "NavierStokes/PhysicalStageBounds.lean": {
        "clusters": ["stage-interface", "jets", "cartesian-assembly", "pressure"],
        "finding": "Packages native WaveData and MeanData, constructs potential/direct/pressure stages, and proves smoothness and RawStageBounds for joint inputs. These are local physical stage estimates and do not export the selected field's five-observable equality.",
        "anchors": "51-213; 286-369; 398-518; 528-571",
    },
    "NavierStokes/R3/PressureFlux.lean": {
        "clusters": ["pressure", "r3", "energy"],
        "finding": "Defines canonical compact-test pressure fluxes, proves commutator decompositions and bounds, and derives uniform actual flux bounds under comparative PressureRecovery.Hypotheses for p-q and u-v. It is not an absolute selected-pressure Poisson theorem or radial five-moment evaluation.",
        "anchors": "125-232; 235-376; 576-600",
    },
    "NavierStokes/SignedCopyBounds.lean": {
        "clusters": ["jets", "cartesian-assembly", "pressure"],
        "finding": "Proves local jet closure for signed quotients, native covariance invertibility, signed amplitude/vector jets, projected pressure jets, and uniformised/localised coefficient bounds. It supplies periodisation-ready rates but no final barMoment or (M,I,J,S,Cp) identity.",
        "anchors": "54-240; 386-483; 494-648; 711-828",
    },
    "NavierStokes/ActualCycleCoherence.lean": {
        "clusters": ["cartesian-assembly", "stage-interface", "rank", "jets"],
        "finding": "Defines state/block/axis coherence and proves initial coherence, support-induced zero fields, particular-source identities, wave transport, coherent cycle steps, and indexed coherent iteration. This is a genuine cycle bridge but does not evaluate barMoment or export (M,I,J,S,Cp).",
        "anchors": "36-116; 120-250; 253-304; 321-735; 786-861",
    },
    "NavierStokes/ActualInitialCoherence.lean": {
        "clusters": ["cartesian-assembly", "jets", "rank", "time"],
        "finding": "Constructs seed, primary, temporal, ranked, and initialized states and proves band coordinate identities, primitive reconstruction, debt regularity, smoothness, support, covariance regularity, periodicity, and overlap transport. It contains no final selected Cartesian barMoment or five-observable equality.",
        "anchors": "27-250; 266-325; 417-653; 700-752",
    },
    "NavierStokes/ActualParticularCycleData.lean": {
        "clusters": ["cartesian-assembly", "stage-interface", "pressure", "jets"],
        "finding": "Packages particular-cycle Data and nativeData, then proves source/pressure/Gaussian boundary identities, residual transport, native classes, smoothness, support, periodicity, coefficient bounds, solenoidality, cancellation, and actual data/input outputs. It stops at local stage data and does not prove the global selected barMoment tuple.",
        "anchors": "34-72; 102-286; 286-563; 573-731; 731-814",
    },
    "NavierStokes/CorrectedPressureBounds.lean": {
        "clusters": ["pressure", "profiles", "moments"],
        "finding": "Constructs a reduced corrected pressure from a finite partial reset, proving before/after matching, joint smoothness, derivative and size bounds, endpoint estimates, and an axisPressure-plus-correction identity. This is reduced pressure evidence, not an absolute whole-space pressure-Poisson theorem or final selected five-moment transport.",
        "anchors": "23-235; 236-298; 301-426; 434-681",
    },
    "NavierStokes/ActualCyclePreservation.lean": {
        "clusters": ["cartesian-assembly", "stage-interface", "rank", "jets"],
        "finding": "Preserves actual cycle states and labels and proves rank/debt regularity, primary and signed-field smoothness, periodicity, support, particular inputs, curl fields, and indexed run invariants. This is substantive stage-level transport, but the inspected output contains no final barMoment or (M,I,J,S,Cp) equality for the selected Cartesian field.",
        "anchors": "1-16; 42-96; 149-191; 259-389; 453-526; 538-726; 730-914",
    },
    "NavierStokes/ActualParticularRealization.lean": {
        "clusters": ["cartesian-assembly", "pressure", "jets"],
        "finding": "Proves reindexing and germ transport for curl-corrected coefficients, cylindrical and Cartesian SpatialCurl realization, cycle velocity and pressure realization, differentiated covariance, smoothness, and current-input EqOn transport. This is a genuine local field bridge, not a final selected global radial-moment theorem.",
        "anchors": "36-71; 432-433; 523-673; 731-867; 996-1034; 1067-1085",
    },
    "NavierStokes/ActualParticularCoherence.lean": {
        "clusters": ["cartesian-assembly", "stage-interface", "jets", "time"],
        "finding": "Transports current-state particular data to target charts through amplitude/phase germs, the complete curl correction, smooth and supported cutoffs, source records, and particular data. The inspected declarations do not evaluate the final selected Cartesian field through barMoment or identify it with (M,I,J,S,Cp).",
        "anchors": "1-8; 55-146; 176-286; 501-543; 591-936",
    },
    "NavierStokes/ActivationStocks.lean": {
        "clusters": ["profiles", "moments", "pressure", "jets"],
        "finding": "Defines reduced activation/profile stock quantities and proves stock, eta/log, pressure, derivative, history, and uniform jet identities and bounds for the activation layer. The inspected declarations do not construct the final Cartesian field or prove a selected-field barMoment/(M,I,J,S,Cp) equality.",
        "anchors": "20-72; 93-99; 174-219; 239-312; 334-500; 522-711; 747-785; 868-1027",
    },
    "NavierStokes/DiagonalJetBounds.lean": {
        "clusters": ["cartesian-assembly", "jets", "time"],
        "finding": "Proves locally finite tsum derivative identities, finite-prefix/tail decompositions, scalar and norm tail bounds, potential tail jet bounds, and uncut prefix/tail orders. This is genuine series/jet control, but it does not provide weighted radial-integral convergence or final barMoment transport.",
        "anchors": "1-24; 29-190; 196-307",
    },
    "NavierStokes/ExtendedHeatedOutgoing.lean": {
        "clusters": ["profiles", "moments", "pressure", "jets"],
        "finding": "Constructs a compensated outgoing reduced profile on an open parameter neighbourhood. Its Witness carries a three-component reduced physical-moment equation, coefficient/derivative/first-jet bounds and positivity; downstream theorems prove heat/change-row integral cancellation, canonical pressure and energy identities, zero mass/angular/renormalised moments, smoothness, and the reduced Specification. This is substantial profile-level moment transport, but it remains in (X,eta) variables and does not prove final Cartesian torus/radial barMoment transport.",
        "anchors": "1-17; 23-115; 266-362; 443-507; 846-919",
    },
    "NavierStokes/HeatedOutgoing.lean": {
        "clusters": ["profiles", "moments", "pressure", "jets"],
        "finding": "Defines the physical-band outgoing heat profile, compensation patch, reduced pressure kernel, energy and moment rows, and proves smoothness, support, positivity, row decomposition, integrability, and exact three-row compensation cancellation. It supplies real reduced-profile moment infrastructure but no final Cartesian torus/radial barMoment transport.",
        "anchors": "1-56; 57-162; 167-286; 300-390; 472-508; 793-862",
    },
    "NavierStokes/ModeSolenoidalReindex.lean": {
        "clusters": ["cartesian-assembly", "rank", "jets"],
        "finding": "Proves linear-equivalence reindexing identities for harmonic amplitudes, single modes, lift and angular directions, cylindrical divergence, and mode-solenoidal structure. This preserves a local mode-level divergence-free property under reindexing, not a global selected-field radial observable identity.",
        "anchors": "1-20; 22-63; 92-97",
    },
    "NavierStokes/ShapedWaitBounds.lean": {
        "clusters": ["time", "pressure", "jets", "profiles"],
        "finding": "Proves shaped temporal hold/wait formulas, pressure-source and axial/angular lag bounds, smoothness and derivative bounds, initial energy/axial constants, and exponential-to-power decay estimates. This is temporal/reduced estimate infrastructure and contains no Cartesian curl, barMoment, or five-observable endpoint transport.",
        "anchors": "1-43; 45-168; 188-313; 354-423; 432-575; 582-800; 839-915; 980-1038; 1072-1304",
    },
    "NavierStokes/SignedWaveUpdate.lean": {
        "clusters": ["cartesian-assembly", "moments", "rank", "jets"],
        "finding": "Defines signed radial stress primitives, covariance inversion, local curl realisation, tsum assembly, radial/tangential component identities, double-average stress identities, and signed-square identities. These are genuine reduced and local transport results, but no final selected Cartesian barMoment or (M,I,J,S,Cp) theorem is exported.",
        "anchors": "36-116; 580-668; 984-1090; 1170-1473",
    },
    "NavierStokes/EntranceAlignedBase.lean": {
        "clusters": ["profiles", "moments", "pressure", "rank"],
        "finding": "Builds aligned and modulated slow bases and proves reduced positive-order moment, mass-primitive, pressure-coefficient, support, smoothness, and finite-identity theorems. The moments remain in reduced (X,eta) profile variables; no final Cartesian radial-observable transport is proved.",
        "anchors": "25-132; 355-689; 800-1056",
    },
    "NavierStokes/InitializedPhysicalBackground.lean": {
        "clusters": ["cartesian-assembly", "jets", "rank"],
        "finding": "Constructs initialized curl-lifted potential and velocity fields and proves smoothness, decomposition, native rate bounds, finite rates, local representation, and uncut/represented rate transport. It contains no final selected Cartesian barMoment or five-observable equality.",
        "anchors": "51-174; 216-321",
    },
    "NavierStokes/MeanStageRegularity.lean": {
        "clusters": ["rank", "moments", "stage-interface", "time"],
        "finding": "Proves smooth moving fields, actual debt smoothness, moving rank geometry, rank increments, reconstruction, and temporal preservation. This is substantive state/rank transport, not a theorem evaluating the final selected Cartesian field through barMoment.",
        "anchors": "28-102; 111-186; 217-318",
    },
    "NavierStokes/PeriodicIntegration.lean": {
        "clusters": ["cartesian-assembly", "energy"],
        "finding": "Defines periodic cube coordinates and integration, proves periodic derivative integrals vanish, product-rule identities, and parameter-dependent cube-integral calculus. These are cube-periodic identities, not radial barMoment transport for the selected field.",
        "anchors": "24-123; 141-203; 223-329",
    },
    "NavierStokes/PeriodicLocalization.lean": {
        "clusters": ["cartesian-assembly", "jets", "time"],
        "finding": "Defines lattice periodisation and proves local finiteness, smoothness, periodicity, inner-cube equality, origin equality, and time-support preservation. It does not prove preservation of weighted radial moments under periodisation.",
        "anchors": "28-62; 79-207; 237-290",
    },
    "NavierStokes/PeriodicSobolev.lean": {
        "clusters": ["energy", "endpoint", "cartesian-assembly"],
        "finding": "Defines periodic energy and derivative-H3 norms, proves the periodic pointwise bound, and derives derivative-H3 blow-up from candidate speed blow-up. This is an endpoint functional-analytic consequence and contains no moment construction or transport theorem.",
        "anchors": "31-122; 147-244; 314-351",
    },
    "NavierStokes/PrimaryCopyBounds.lean": {
        "clusters": ["jets", "cartesian-assembly", "profiles", "time"],
        "finding": "Defines native jets, affine copies, locally finite copy sums, outer cutoffs, periodised native fields, support, and uniform jet bounds. It supplies strong local/copy-sum control but no weighted radial-integral convergence or final (M,I,J,S,Cp) equality.",
        "anchors": "30-242; 252-462; 665-842; 844-900; 1000-1246; 1269-1509",
    },
    "NavierStokesReview/src/external-semantic/ClaySpec.lean": {
        "clusters": ["external-semantics", "cmi", "specification", "periodic", "energy"],
        "finding": "Direct review finds an explicit audit-side specification of R3 and periodic fields, within-half-space derivatives, equations, admissible data, bounded energy, and alternatives C/D. It is a review specification layer, not the OpenAI selected Navier-Stokes endpoint; fidelity to the frozen CMI source remains a separate validation obligation.",
        "anchors": "28-32; 53-114; 117-171; 174-226",
    },
    "NavierStokesReview/src/external-semantic/Gap.lean": {
        "clusters": ["external-semantics", "cmi", "comparator", "translation"],
        "finding": "Direct review finds comparator-to-ClaySpec data and solution translations and statement-level implications. The bridge is audit infrastructure and contains no selected_witness, CandidateProperties, barMoment, or five-observable transport theorem.",
        "anchors": "274-303; 525-597; 602-642",
    },
    "Euler/AllOrderDriftEquation.lean": {
        "clusters": ["euler", "correction", "pressure", "residual", "existence"],
        "finding": "Direct review finds corrected Euler field and pressure towers, initial/divergence/gradient/energy/derivative identities, and an existential exact lifted solution under Budget and ApproximationResidual hypotheses. It is not the selected Navier-Stokes endpoint and carries no five-observable transport theorem.",
        "anchors": "33-68; 71-137; 141-166",
    },
    "Euler/AllOrderDriftFieldDecomposition.lean": {
        "clusters": ["euler", "correction", "field-decomposition"],
        "finding": "Direct review finds exact corrected tower and packet point-field decompositions in the Euler branch. No selected Navier-Stokes field, CandidateProperties, barMoment, or five-observable equality is stated.",
        "anchors": "18-43",
    },
    "Euler/AllOrderDriftResidualBounds.lean": {
        "clusters": ["euler", "residual", "bounds", "weighted-norm", "pressure"],
        "finding": "Direct review finds residual-envelope, weighted field/derivative, pressure, and time-derivative estimates. These are genuine quantitative bounds, but they are not radial five-observable identities or selected Navier-Stokes transport.",
        "anchors": "17-36; 39-72; 75-105; 109-151",
    },
    "Euler/CorrectionResidualCancellation.lean": {
        "clusters": ["euler", "correction", "residual", "pressure"],
        "finding": "Direct review finds exact nonlinear residual-increment and cancellation identities plus initial, divergence-free, gradient-space, and derivative closure for corrected Euler paths. It does not connect to the selected Navier-Stokes witness.",
        "anchors": "22-53; 55-86",
    },
    "Euler/MeanPressureRepresentative.lean": {
        "clusters": ["euler", "pressure", "representative", "functional-analysis"],
        "finding": "Direct review finds continuous L2 pressure representatives, smoothness/AE/continuity results, physical-gradient recovery, and a scalar equation in the Euler mean-pressure branch. It does not prove an absolute selected Navier-Stokes pressure-Poisson representative or five-observable transport.",
        "anchors": "29-90; 96-156",
    },
    "Euler/PacketAngularPressureStepBound.lean": {
        "clusters": ["euler", "pressure", "packet", "bounds"],
        "finding": "Direct review finds an angular pressure step construction under explicit packet budget hypotheses. It is scoped Euler pressure infrastructure, not the selected Navier-Stokes endpoint.",
        "anchors": "15-95",
    },
    "Euler/PacketFiniteParity.lean": {
        "clusters": ["euler", "parity", "packet", "residual"],
        "finding": "Direct review finds joint oddness propagated through finite sums, assembly, pressure, nonlinear grades, velocity, and residual tails. This is a genuine Euler packet symmetry result, not a selected Navier-Stokes radial-moment bridge.",
        "anchors": "19-143",
    },
    "Euler/PacketForwardPressureBudgets.lean": {
        "clusters": ["euler", "pressure", "packet", "budgets"],
        "finding": "Direct review finds forward angular and initialized pressure budget constructions under explicit hypotheses. No selected Navier-Stokes pressure or five-observable transport theorem is stated.",
        "anchors": "17-214",
    },
    "Euler/PacketForwardPressureRemainder.lean": {
        "clusters": ["euler", "pressure", "packet", "remainder", "bounds"],
        "finding": "Direct review finds forward initialized pressure and covector remainders with gradient decomposition and bounds. These are scoped Euler packet results, not an absolute selected Navier-Stokes pressure-Poisson theorem.",
        "anchors": "37-155",
    },
    "Euler/PacketInitializedPressureRemainder.lean": {
        "clusters": ["euler", "pressure", "packet", "remainder", "bounds"],
        "finding": "Direct review finds initialized pressure and covector remainders with gradient decomposition and bounds. It contains no selected Navier-Stokes field-level five-observable transport theorem.",
        "anchors": "37-157",
    },
    "NavierStokesReview/src/audit/priority_147_external_semantic_euler_drift_pressure_source_review_2026-09-29.md": {
        "clusters": ["external-semantics", "euler", "pressure", "methodology", "repository-root"],
        "finding": "Human-readable Priority 147 direct review of the audit semantic bridge and ten Euler correction/pressure/parity/residual modules, with source anchors, positive results, semantic limits, and explicit tranche-level absence boundaries.",
        "anchors": "1-118",
    },
    "NavierStokesReview/evidence/source_tranche_external_semantic_euler_drift_pressure_2026-09-29.json": {
        "clusters": ["external-semantics", "euler", "pressure", "methodology", "repository-root"],
        "finding": "Machine-readable Priority 147 evidence for twelve directly reviewed audit and Euler modules, including the endpoint-symbol absence boundary and classification limits.",
        "anchors": "generated JSON; 12 source records",
    },
    "Euler/CylinderGraphRealization.lean": {
        "clusters": ["euler", "cylinder", "lp", "graph"],
        "finding": "Direct review finds an L2 graph representative on a prescribed phase graph, with almost-everywhere representative and norm bound. No selected Navier-Stokes endpoint or radial five-observable transport.",
        "anchors": "18-24; 26-38; 41-65",
    },
    "Euler/CylinderHeatEquation.lean": {
        "clusters": ["euler", "cylinder", "heat", "regularity"],
        "finding": "Direct review finds finite real heat products with linearity, continuity, strong derivative, and generator identities. No selected Navier-Stokes field or five-observable transport.",
        "anchors": "17-75; 78-135",
    },
    "Euler/CylinderLocalSupport.lean": {
        "clusters": ["euler", "cylinder", "support", "curl"],
        "finding": "Direct review finds support preservation for primitives, derivatives, potential paths, and slow curls, plus derivative vanishing outside closed support. Support control does not prove radial moment cancellation.",
        "anchors": "25-43; 47-58; 64-97",
    },
    "Euler/CylinderMeasureDescent.lean": {
        "clusters": ["euler", "cylinder", "measure", "periodic"],
        "finding": "Direct review finds a fundamental strip, covering-map measure preservation, quotient measure, and deck-equivariant descent. No torus-average or barMoment identity.",
        "anchors": "32-48; 50-79; 81-89",
    },
    "Euler/CylinderPathAdvection.lean": {
        "clusters": ["euler", "cylinder", "advection", "bounds"],
        "finding": "Direct review finds p dot grad q path construction, orbit smoothness, almost-everywhere and pointwise representation, and a majorant. No selected endpoint transport.",
        "anchors": "17-30; 32-43; 62-82",
    },
    "Euler/CylinderPathBilinear.lean": {
        "clusters": ["euler", "cylinder", "bilinear", "cartesian"],
        "finding": "Direct review finds generic bilinear products reconstructed by three component decomposition with almost-everywhere and pointwise identities. No paper observable equality.",
        "anchors": "15-32; 39-66; 80-90",
    },
    "Euler/CylinderPathBilinearBounds.lean": {
        "clusters": ["euler", "cylinder", "bilinear", "bounds"],
        "finding": "Direct review finds block and majorant bounds for bilinear paths. Rate control is not radial moment transport.",
        "anchors": "23-44",
    },
    "Euler/CylinderPathDerivativeProduct.lean": {
        "clusters": ["euler", "cylinder", "derivative", "product"],
        "finding": "Direct review finds derivative-product path smoothness, pointwise product representation, and derivative-shift majorants. No selected endpoint bridge.",
        "anchors": "21-56",
    },
    "Euler/CylinderPathIntegral.lean": {
        "clusters": ["euler", "cylinder", "integral", "translation"],
        "finding": "Direct review finds translation commuting with time integration and smooth translated paths from derivative data. No CMI endpoint result.",
        "anchors": "18-30; 32-49",
    },
    "Euler/CylinderPathProduct.lean": {
        "clusters": ["euler", "cylinder", "product", "regularity"],
        "finding": "Direct review finds bounded bilinear path application with norm, smoothness, almost-everywhere, and pointwise product realization. No five-observable transport.",
        "anchors": "42-58; 68-116",
    },
    "Euler/CylinderPathProductBounds.lean": {
        "clusters": ["euler", "cylinder", "product", "bounds"],
        "finding": "Direct review finds Sobolev, block, and majorant bounds for products. Quantitative bounds do not imply global radial identities.",
        "anchors": "34-46; 48-58; 62-109",
    },
    "Euler/CylinderPathProductSupport.lean": {
        "clusters": ["euler", "cylinder", "product", "support"],
        "finding": "Direct review finds scalar, bilinear, derivative-product, and advection support preservation. No integrated radial moment or pressure-Poisson conclusion.",
        "anchors": "19-35; 46-82",
    },
    "Euler/CylinderPathWords.lean": {
        "clusters": ["euler", "cylinder", "operator-path", "translation", "bounds"],
        "finding": "Direct review finds finite translation-word and derivative paths with orbit, ae, pointwise, Sobolev, block, majorant, and time-derivative results. No selected field or five-observable equality.",
        "anchors": "1; 19-65; 72-126",
    },
    "Euler/CylinderPhysicalTensor.lean": {
        "clusters": ["euler", "cylinder", "tensor", "graph", "regularity"],
        "finding": "Direct review finds graph-coordinate pullback, smoothness, and iterated physical derivative bounds. No radial moment or pressure-Poisson transport.",
        "anchors": "1-2; 17-46; 50-72",
    },
    "Euler/CylinderPhysicalTensorDifference.lean": {
        "clusters": ["euler", "cylinder", "tensor", "bounds"],
        "finding": "Direct review finds pointwise and difference bounds for physical tensors from almost-everywhere hypotheses. No selected endpoint or moment observable.",
        "anchors": "1; 14-30",
    },
    "Euler/CylinderPhysicalTensorLp.lean": {
        "clusters": ["euler", "cylinder", "tensor", "lp", "bounds"],
        "finding": "Direct review finds graph-word and physical-tensor Lp membership and norm bounds. Lp control does not imply global radial identities.",
        "anchors": "1; 14-49",
    },
    "Euler/CylinderRawSupport.lean": {
        "clusters": ["euler", "cylinder", "support"],
        "finding": "Direct review finds representative support containment and compact support under compactness hypotheses. No moment cancellation.",
        "anchors": "1-2; 13-39",
    },
    "Euler/CylinderReflection.lean": {
        "clusters": ["euler", "cylinder", "reflection", "symmetry"],
        "finding": "Direct review finds measure-preserving reflection, isometry, translation, derivative, test, and gradient identities. No selected Cartesian transport.",
        "anchors": "1; 12-61; 77-98",
    },
    "Euler/CylinderRetractRepresentative.lean": {
        "clusters": ["euler", "cylinder", "representative", "regularity"],
        "finding": "Direct review finds retract-based pointwise representatives with continuity, smoothness, ae equality, and time derivatives. No selected candidate or five-moment tuple.",
        "anchors": "1-2; 19-56; 62-80",
    },
    "Euler/CylinderScalarAverage.lean": {
        "clusters": ["euler", "cylinder", "mean-zero", "scalar"],
        "finding": "Direct review finds scalar angular mean-zero for the scalar primitive construction. This is not the paper's five cumulative radial identity.",
        "anchors": "1-2; 15-19",
    },
    "Euler/CylinderScalarClassical.lean": {
        "clusters": ["euler", "cylinder", "scalar", "regularity", "mean-zero"],
        "finding": "Direct review finds classical scalar angular primitive cover, mean-zero, smoothness, continuity, and zero-input identities. No selected pressure endpoint.",
        "anchors": "1-2; 13-79",
    },
    "Euler/CylinderScalarParity.lean": {
        "clusters": ["euler", "cylinder", "scalar", "parity", "symmetry"],
        "finding": "Direct review finds joint-even parity of the classical scalar primitive. Parity does not identify selected-field radial observables.",
        "anchors": "1-2; 12-15",
    },
    "Euler/CylinderScalarPrimitive.lean": {
        "clusters": ["euler", "cylinder", "scalar", "operator-path", "bounds"],
        "finding": "Direct review finds scalar embedding, projection, primitive operators, norm and translation bounds, path smoothness, and block bounds. No selected-field bridge.",
        "anchors": "1-2; 20-51; 66-116",
    },
    "Euler/CylinderScalarRepresentative.lean": {
        "clusters": ["euler", "cylinder", "scalar", "representative", "regularity"],
        "finding": "Direct review finds smooth embedding and ae/constructed-field agreement for the scalar primitive. Exact representative agreement is not selected Navier-Stokes transport.",
        "anchors": "1-4; 22-67",
    },
    "NavierStokesReview/src/audit/priority_148_euler_cylinder_graph_path_support_source_review_2026-09-29.md": {
        "clusters": ["euler", "cylinder", "support", "methodology", "repository-root"],
        "finding": "Human-readable Priority 148 direct review of twelve Euler cylinder graph, path, product, heat, measure, and support modules, with source anchors and tranche-level absence boundaries.",
        "anchors": "1-92",
    },
    "NavierStokesReview/evidence/source_tranche_euler_cylinder_graph_path_support_2026-09-29.json": {
        "clusters": ["euler", "cylinder", "support", "methodology", "repository-root"],
        "finding": "Machine-readable Priority 148 evidence for twelve directly reviewed Euler cylinder modules, including source-hygiene and endpoint-transport classification fields.",
        "anchors": "generated JSON; 12 source records",
    },
    "NavierStokesReview/src/audit/priority_149_euler_cylinder_tensor_scalar_source_review_2026-09-29.md": {
        "clusters": ["euler", "cylinder", "tensor", "scalar", "methodology", "repository-root"],
        "finding": "Human-readable Priority 149 direct review of twelve Euler cylinder tensor, scalar, reflection, support, path, and representative modules, with source anchors and tranche-level absence boundaries.",
        "anchors": "1-86",
    },
    "NavierStokesReview/evidence/source_tranche_euler_cylinder_tensor_scalar_2026-09-29.json": {
        "clusters": ["euler", "cylinder", "tensor", "scalar", "methodology", "repository-root"],
        "finding": "Machine-readable Priority 149 evidence for twelve directly reviewed Euler cylinder modules, including source-hygiene and endpoint-transport classification fields.",
        "anchors": "generated JSON; 12 source records",
    },
    "Euler/CylinderSliceRepresentatives.lean": {
        "clusters": ["euler", "cylinder", "representative", "slice"],
        "finding": "Direct review finds continuous cylinder path representatives from equal slice data, including scalar representatives. No selected-field moment transport.",
        "anchors": "1; 17-34",
    },
    "Euler/CylinderSlowCurl.lean": {
        "clusters": ["euler", "cylinder", "curl", "cartesian", "path"],
        "finding": "Direct review finds three curl terms, a finite path sum, ae reconstruction, a classical field, and equality with the lifted slow-curl operator. No five-observable or selected endpoint equality.",
        "anchors": "1-3; 38-47; 55-77; 80-107",
    },
    "Euler/CylinderSlowCurlBounds.lean": {
        "clusters": ["euler", "cylinder", "curl", "bounds"],
        "finding": "Direct review finds a block bound where one spatial derivative consumes one shift while the external radius is unchanged. This is not radial moment transport.",
        "anchors": "1; 39-72",
    },
    "Euler/CylinderSlowCurlWeight.lean": {
        "clusters": ["euler", "cylinder", "curl", "weight", "time"],
        "finding": "Direct review finds weight commutation, path normalisation, normalised block bounds, and time-derivative normalisation/bounds. No selected-field observable equality.",
        "anchors": "1-2; 30-59; 74-101",
    },
    "Euler/CylinderSobolevDensity.lean": {
        "clusters": ["euler", "cylinder", "sobolev", "density"],
        "finding": "Direct review finds Sobolev mollifiers, boundedness, convergence, representative compatibility, ae word identities, and smooth density. No endpoint transport.",
        "anchors": "1; 16-63",
    },
    "Euler/CylinderSobolevDerivatives.lean": {
        "clusters": ["euler", "cylinder", "sobolev", "derivative"],
        "finding": "Direct review finds truncation and derivative operators with bounds, value recovery, derivative existence, and translation compatibility. No five-moment conclusion.",
        "anchors": "1; 13-103",
    },
    "Euler/CylinderSobolevEmbedding.lean": {
        "clusters": ["euler", "cylinder", "sobolev", "embedding", "bounds"],
        "finding": "Direct review finds embedding constants and pointwise value bounds from high-order Sobolev control. No radial integral bridge.",
        "anchors": "1-2; 18-67",
    },
    "Euler/CylinderSobolevOperators.lean": {
        "clusters": ["euler", "cylinder", "sobolev", "operator", "translation"],
        "finding": "Direct review finds array/value/word operators, derivative-sum norms, lifted translation-commuting operators, and continuity. No selected-field or pressure semantics.",
        "anchors": "1; 16-53; 68-145",
    },
    "Euler/CylinderSobolevOrbit.lean": {
        "clusters": ["euler", "cylinder", "sobolev", "orbit", "path"],
        "finding": "Direct review finds Sobolev translation orbits and assembled paths with coordinate and smoothness results. No endpoint transport.",
        "anchors": "1-2; 23-71",
    },
    "Euler/CylinderSobolevWordBounds.lean": {
        "clusters": ["euler", "cylinder", "sobolev", "bounds", "orbit"],
        "finding": "Direct review finds word-level, summed-level, and block-level Sobolev bounds for the orbit. No five-observable equality.",
        "anchors": "1-2; 23-89",
    },
    "Euler/CylinderSpatialEmbedding.lean": {
        "clusters": ["euler", "cylinder", "embedding", "lp", "spatial"],
        "finding": "Direct review finds the spatial-to-cylinder L2 embedding, linearity, norm scaling, continuity, and inner-product identities. No radial moment or pressure-Poisson theorem.",
        "anchors": "1-3; 23-61; 79-109",
    },
    "Euler/CylinderSpatialMean.lean": {
        "clusters": ["euler", "cylinder", "mean", "average", "spatial"],
        "finding": "Direct review finds a bounded cylinder-to-spatial mean as an adjoint with translation covariance, constant-embedding retraction, and angular-average invariance. This is not barMoment or selected-field transport.",
        "anchors": "1-3; 18-44; 51-86",
    },
    "NavierStokesReview/src/audit/priority_150_euler_cylinder_slow_curl_sobolev_source_review_2026-09-29.md": {
        "clusters": ["euler", "cylinder", "curl", "sobolev", "mean", "methodology", "repository-root"],
        "finding": "Human-readable Priority 150 direct review of twelve Euler cylinder slow-curl, Sobolev, embedding, representative, and spatial-mean modules, with source anchors and tranche-level absence boundaries.",
        "anchors": "1-78",
    },
    "NavierStokesReview/evidence/source_tranche_euler_cylinder_slow_curl_sobolev_2026-09-29.json": {
        "clusters": ["euler", "cylinder", "curl", "sobolev", "mean", "methodology", "repository-root"],
        "finding": "Machine-readable Priority 150 evidence for twelve directly reviewed Euler cylinder modules, including source-hygiene and endpoint-transport classification fields.",
        "anchors": "generated JSON; 12 source records",
    },
    "Euler/CylinderSpatialMeanPath.lean": {
        "clusters": ["euler", "cylinder", "mean", "path", "translation"],
        "finding": "Direct review finds a bounded cylinder spatial path mean with translation covariance, norm, differentiability, and block majorants. It is not selected-field radial moment transport.",
        "anchors": "8; 25-70",
    },
    "Euler/CylinderSpatialMeanRepresentative.lean": {
        "clusters": ["euler", "cylinder", "mean", "representative", "lp"],
        "finding": "Direct review finds continuity, MemLp, and almost-everywhere representative identities for lifted raw means. It does not identify the CMI observables.",
        "anchors": "17-64",
    },
    "Euler/CylinderTerminalAmplitude.lean": {
        "clusters": ["euler", "cylinder", "endpoint", "bounds"],
        "finding": "Direct review finds constant-path block and terminal-amplitude bounds. It is not a selected Navier-Stokes endpoint theorem.",
        "anchors": "24-47",
    },
    "Euler/DevelopmentBridge.lean": {
        "clusters": ["euler", "bridge", "initial-data", "integrability"],
        "finding": "Direct review finds divergence/development identities and a velocity-field conversion guarded by explicit all-order spatial integrability. The source states that the Comparator does not provide that hypothesis.",
        "anchors": "20-55",
    },
    "Euler/DivergenceFreeHeat.lean": {
        "clusters": ["euler", "heat", "invariant", "regularity"],
        "finding": "Direct review finds heat, convolution, and mild-solution preservation of a projected zero-gradient invariant. It is not five-moment or pressure-Poisson transport.",
        "anchors": "17-132",
    },
    "Euler/DriftGlobalInviscidGevrey.lean": {
        "clusters": ["euler", "drift", "gevrey", "pde"],
        "finding": "Direct review finds a global inviscid Gevrey PDE construction under explicit hypotheses. It is Euler drift infrastructure, not the selected Navier-Stokes Witness.",
        "anchors": "9-21",
    },
    "Euler/DriftMetricForcing.lean": {
        "clusters": ["euler", "drift", "force", "metric"],
        "finding": "Direct review finds metric correction-forcing bounds using drift, pressure, transport, and coefficient estimates. It is not a CMI force-provenance theorem.",
        "anchors": "8-19",
    },
    "Euler/DriftNonlinearEstimate.lean": {
        "clusters": ["euler", "drift", "force", "nonlinear", "bounds"],
        "finding": "Direct review finds drift-loss absorption, polynomial assembly, and correction-forcing bounds. It has no five-observable equality.",
        "anchors": "8-45",
    },
    "Euler/DuhamelDifferentiation.lean": {
        "clusters": ["euler", "duhamel", "heat", "differentiation"],
        "finding": "Direct review finds heat/Duhamel flows with continuity, measurability, Lipschitz, and derivative identities. It has no selected-field moment transport.",
        "anchors": "9-114",
    },
    "Euler/DuhamelEquation.lean": {
        "clusters": ["euler", "duhamel", "heat", "equation"],
        "finding": "Direct review finds Duhamel decomposition, source-tail differentiation, and inhomogeneous heat derivative identities. It is not the exported Navier-Stokes endpoint.",
        "anchors": "7-90",
    },
    "Euler/DuhamelPasting.lean": {
        "clusters": ["euler", "duhamel", "pasting", "gluing"],
        "finding": "Direct review finds restart, shifted-source, source-integral, and mild-solution gluing identities. It has no global CMI correspondence theorem.",
        "anchors": "8-55",
    },
    "Euler/ExternalScalarCommutator.lean": {
        "clusters": ["euler", "commutator", "regularity", "lp", "bounds"],
        "finding": "Direct review finds scalar commutator smoothness, MemLp, positivity, successor, and convolution bounds. It has no computed nonzero selected-field defect.",
        "anchors": "8-120",
    },
    "NavierStokesReview/src/audit/priority_151_euler_mean_development_heat_duhamel_source_review_2026-09-29.md": {
        "clusters": ["euler", "mean", "development", "heat", "duhamel", "methodology", "repository-root"],
        "finding": "Human-readable Priority 151 direct source review of twelve Euler mean, development-bridge, heat, drift, Duhamel, and scalar-commutator modules, including the explicit conditional-integrability boundary.",
        "anchors": "1-78",
    },
    "NavierStokesReview/evidence/source_tranche_euler_mean_development_heat_duhamel_2026-09-29.json": {
        "clusters": ["euler", "mean", "development", "heat", "duhamel", "methodology", "repository-root"],
        "finding": "Machine-readable Priority 151 evidence for twelve directly reviewed Euler modules, including source hygiene and the explicit conditional bridge record.",
        "anchors": "generated JSON; 12 source records",
    },
    "Euler/PacketMeanPressureStepBound.lean": {
        "clusters": ["euler", "packet", "pressure", "bounds"],
        "finding": "Direct review finds mean-pressure step existence and a field bound under supplied Field hypotheses. It is not selected pressure or five-observable transport.",
        "anchors": "1; 29-65",
    },
    "Euler/PacketProfileCoarseBounds.lean": {
        "clusters": ["euler", "packet", "profiles", "bounds", "pressure"],
        "finding": "Direct review finds packet word, scale, high, mean, corrector, derivative, and pressure coarse majorants. It has no selected Cartesian observable equality.",
        "anchors": "1-3; 16-87",
    },
    "Euler/PacketRecursiveBase.lean": {
        "clusters": ["euler", "packet", "recursion", "residual"],
        "finding": "Direct review finds primary profiles and zero/one recursive-grade identities with a first nonlinear grade estimate. This is Euler packet algebra only.",
        "anchors": "1; 11-54",
    },
    "Euler/PacketRecursiveCancellation.lean": {
        "clusters": ["euler", "packet", "recursion", "cancellation", "residual"],
        "finding": "Direct review finds assembled velocity/pressure and recursive-grade identities, including zero-grade cancellation under hypotheses. It has no global moment transport.",
        "anchors": "1-3; 13-67",
    },
    "Euler/ParentNormalizedEuler.lean": {
        "clusters": ["euler", "parent-data", "coordinates", "normalisation"],
        "finding": "Direct review finds normalized Euler parent-frame velocity/pressure, differentiability, zero normalized momentum, and restoration identities. It is not selected Witness.",
        "anchors": "1-2; 16-75",
    },
    "NavierStokesReview/src/probes/StageEstimatesMomentBlindnessProbe.lean": {
        "clusters": ["endpoint", "stage-interface", "moments", "methodology", "probe"],
        "finding": "Direct review finds a zero StageEstimates inhabitant, no zero-stage blowup, and no inference of PositiveOrderMoments.Debt from StageEstimates alone. The source explicitly says it does not attack selected_witness.",
        "anchors": "1; 21-173",
    },
    "Euler/PacketProfileRecursion.lean": {
        "clusters": ["euler", "packet", "profiles", "recursion", "pressure"],
        "finding": "Direct review finds actual Profile/operators, angular mean, jet/force maps, one-step and strong-recursion profiles, prefix dependence, and recursive equations. No selected endpoint bridge.",
        "anchors": "1-2; 20-143",
    },
    "Euler/PacketJoinedSourceResidual.lean": {
        "clusters": ["euler", "packet", "residual", "pressure", "profiles"],
        "finding": "Direct review finds joined primary profiles and finite packet residual equality to an uncancelled recursive tail sum under explicit hypotheses. It is not CandidateProperties.",
        "anchors": "1-2; 24-76",
    },
    "Euler/PacketRecursiveForcing.lean": {
        "clusters": ["euler", "packet", "force", "residual", "recursion"],
        "finding": "Direct review finds assembled jets/full force, primary and nonlinear-grade identities, known-force subtraction, and recursive force sums. It is not CMI force provenance.",
        "anchors": "1-2; 18-95",
    },
    "Euler/PacketRecursiveResidual.lean": {
        "clusters": ["euler", "packet", "residual", "recursion"],
        "finding": "Direct review finds the recursive residual-tail theorem consumed by packet base and joined-source modules. It has no whole-space endpoint semantics.",
        "anchors": "1; 13",
    },
    "Euler/PacketResidualTailActual.lean": {
        "clusters": ["euler", "packet", "residual", "tails", "regularity"],
        "finding": "Direct review finds finite assembled velocity jets and sliced momentum grades identified with recursive tails, then packaged as literal tail-grade fields. This is conditional and packet-local.",
        "anchors": "1-2; 16-96",
    },
    "Euler/PacketResidualTailDecomposition.lean": {
        "clusters": ["euler", "packet", "residual", "tails", "algebra"],
        "finding": "Direct review finds convolution shift, coefficient-tail, and recursive-grade tail identities. It is algebraic decomposition, not five-moment selected-field transport.",
        "anchors": "1; 14-77",
    },
    "NavierStokesReview/src/audit/priority_152_euler_packet_recursive_source_review_2026-09-29.md": {
        "clusters": ["euler", "packet", "recursion", "residual", "methodology", "repository-root"],
        "finding": "Human-readable Priority 152 direct source review of twelve Euler packet/profile recursion, forcing, cancellation, residual-tail, and StageEstimates interface modules.",
        "anchors": "1-78",
    },
    "NavierStokesReview/evidence/source_tranche_euler_packet_recursive_2026-09-29.json": {
        "clusters": ["euler", "packet", "recursion", "residual", "methodology", "repository-root"],
        "finding": "Machine-readable Priority 152 evidence for twelve directly reviewed Euler packet and review-probe modules, including the narrow probe boundary.",
        "anchors": "generated JSON; 12 source records",
    },
    "Euler/FixedEvolutionRegularity.lean": {
        "clusters": ["euler", "fixed-frame", "regularity", "transport"],
        "finding": "Direct review finds smooth parameter dependence of fixed-frame velocity, acceleration, physical velocity, and derivative paths under explicit coercivity, regularity, and smallness hypotheses. No selected endpoint bridge.",
        "anchors": "1-5; 24-43; 45-92",
    },
    "Euler/FixedFrameNaturality.lean": {
        "clusters": ["euler", "fixed-frame", "naturality", "operator"],
        "finding": "Direct review finds norm control and intertwining for fixed-frame operators. No selected Cartesian moment transport.",
        "anchors": "1-2; 28-39; 45-96",
    },
    "Euler/FlowEscapeBound.lean": {
        "clusters": ["euler", "flow", "escape", "bounds"],
        "finding": "Direct review finds action bounds for curve displacement, flow escape, and escape measure under explicit hypotheses. Euler flow estimate only.",
        "anchors": "1-4; 26-70; 99-180",
    },
    "Euler/FlowL2Transport.lean": {
        "clusters": ["euler", "flow", "transport", "lp"],
        "finding": "Direct review finds determinant-one inverse-flow measure preservation and exact continuous spatial L2 path transport. No five radial observable transport.",
        "anchors": "1-2; 13-29; 43-69",
    },
    "Euler/FrameEndpointUniqueness.lean": {
        "clusters": ["euler", "frame", "uniqueness", "energy"],
        "finding": "Direct review finds conditional moving-frame projected-equation zero and uniqueness from energy coercivity and endpoint conditions. Not whole-space selected Navier-Stokes uniqueness.",
        "anchors": "1-2; 21-40; 40-99; 100-130",
    },
    "Euler/FrameWronskian.lean": {
        "clusters": ["euler", "frame", "wronskian", "strain"],
        "finding": "Direct review finds constant frame Wronskian and induced strain symmetry. Local frame algebra only.",
        "anchors": "1-4; 19-65",
    },
    "Euler/FrozenEvolutionGevrey.lean": {
        "clusters": ["euler", "gevrey", "evolution", "recurrence"],
        "finding": "Direct review finds a frozen-evolution Gevrey derivative recurrence. No selected endpoint transport.",
        "anchors": "1; 23 onward",
    },
    "Euler/FunctionalVelocity.lean": {
        "clusters": ["euler", "velocity", "assembly", "sobolev"],
        "finding": "Direct review finds four lifted velocity coefficients assembled as a bounded linear map with coordinate Sobolev and dimension-factor bounds. No selected witness or five-moment equality.",
        "anchors": "1-2; 15-19; 24-57",
    },
    "Euler/GainedMildFormula.lean": {
        "clusters": ["euler", "mild", "duhamel", "heat"],
        "finding": "Direct review finds a high-order heat-plus-Duhamel path, truncation identity, and gained-mild equivalence. Euler cylinder/Sobolev layer only.",
        "anchors": "1; 16-69",
    },
    "Euler/GainedMildPasting.lean": {
        "clusters": ["euler", "mild", "pasting", "duhamel"],
        "finding": "Direct review finds bounded-map endpoint gluing and gained-mild solution pasting under explicit source hypotheses. No global selected-field bridge.",
        "anchors": "1-2; 15-25; 30-50",
    },
    "Euler/GaussianCylinderHeat.lean": {
        "clusters": ["euler", "gaussian", "heat", "cylinder"],
        "finding": "Direct review finds Gaussian line heat orbit/operator continuity, integrability, contraction, translation, semigroup, commutation, and representation results. No selected pressure or moment equality.",
        "anchors": "1-2; 17-73; 85-144",
    },
    "Euler/GaussianHeatSmoothing.lean": {
        "clusters": ["euler", "gaussian", "heat", "smoothing"],
        "finding": "Direct review finds a Gaussian moment derivative operator, differentiability, derivative bounds, and translation compatibility. Heat smoothing only.",
        "anchors": "1; 16-91",
    },
    "NavierStokesReview/src/audit/priority_154_euler_transport_frame_heat_source_review_2026-09-29.md": {
        "clusters": ["euler", "transport", "frame", "heat", "methodology", "repository-root"],
        "finding": "Human-readable Priority 154 direct source review of twelve Euler transport, frame, flow, mild-evolution, and Gaussian-heat modules.",
        "anchors": "1-78",
    },
    "NavierStokesReview/evidence/source_tranche_euler_transport_frame_heat_2026-09-29.json": {
        "clusters": ["euler", "transport", "frame", "heat", "methodology", "repository-root"],
        "finding": "Machine-readable Priority 154 evidence for twelve directly reviewed Euler support modules, with bounded absence and source-hygiene boundaries.",
        "anchors": "generated JSON; 12 source records",
    },
    "Euler/GaussianHeatTotal.lean": {
        "clusters": ["euler", "gaussian", "heat", "cylinder"],
        "finding": "Direct review finds finite line-heat assembly with contraction, semigroup, translation, continuity, commutation, and one-derivative estimates. Heat-operator support only.",
        "anchors": "1; 16-111; 130-154",
    },
    "Euler/GeneralCylinderAlgebra.lean": {
        "clusters": ["euler", "sobolev", "algebra", "product"],
        "finding": "Direct review finds fixed-order complex cylinder Sobolev multiplication for q >= 6 with explicit product envelopes, MemLp hypotheses, and finite algebra constants. No selected endpoint or radial observable.",
        "anchors": "1; 22-82; 84-228; 240-263",
    },
    "Euler/GeneralRealCylinderAlgebra.lean": {
        "clusters": ["euler", "sobolev", "algebra", "real", "vector"],
        "finding": "Direct review finds real and scalar-vector fixed-order cylinder algebra and L2 product estimates. No selected Cartesian moment transport.",
        "anchors": "1-2; 17-34; 36-77; 79-107",
    },
    "Euler/GevreyBaseTransport.lean": {
        "clusters": ["euler", "gevrey", "transport", "commutator"],
        "finding": "Direct review finds weighted base-word identities and commutator forcing bounds with the explicit 5461 factor under bounded coefficient-map and Sobolev hypotheses. No five-moment statement.",
        "anchors": "1-2; 18-47; 49-94",
    },
    "Euler/GevreyCompactProduct.lean": {
        "clusters": ["euler", "gevrey", "compact-support", "product"],
        "finding": "Direct review finds factorial derivative product bounds when one factor has compact support. No selected witness, pressure, or radial-moment target.",
        "anchors": "1-3; 16-65",
    },
    "Euler/GevreyComposition.lean": {
        "clusters": ["euler", "gevrey", "composition", "faà-di-bruno"],
        "finding": "Direct review finds ordered-partition and Faà di Bruno factorial-square composition bounds under explicit pointwise jet hypotheses. Composition regularity only.",
        "anchors": "1-5; 24-41; 73-104",
    },
    "Euler/GevreyCompositionLp.lean": {
        "clusters": ["euler", "gevrey", "composition", "lp"],
        "finding": "Direct review finds Gevrey composition bounds with outer derivatives in L2 under measure preservation, measurability, MemLp, and pointwise jet hypotheses. No selected observable equality.",
        "anchors": "1-4; 22-54; 57-130",
    },
    "Euler/GevreyCompositionPartitions.lean": {
        "clusters": ["euler", "gevrey", "composition", "partitions"],
        "finding": "Direct review finds finite partition weights and nonnegative, successor, and total-sum bounds. No PDE endpoint or physical moment construction.",
        "anchors": "1; 21-128",
    },
    "Euler/GevreyContinuationNorm.lean": {
        "clusters": ["euler", "gevrey", "continuation", "sobolev"],
        "finding": "Direct review finds positive-radius Gevrey-to-Sobolev norm control, optionally via coercivity. Continuation estimate under explicit norm hypotheses, not selected-field realization.",
        "anchors": "1-3; 13-44; 47-76",
    },
    "Euler/GevreyFamilyCompactness.lean": {
        "clusters": ["euler", "gevrey", "compactness", "correction-family"],
        "finding": "Direct review finds a strong lower-order limit for a bounded viscous correction family under explicit correction-data, Cauchy-viscosity, Duhamel, endpoint, and divergence-free hypotheses. No CMI endpoint bridge.",
        "anchors": "1-4; 17-44",
    },
    "Euler/GevreyFlowBootstrap.lean": {
        "clusters": ["euler", "gevrey", "flow", "bootstrap"],
        "finding": "Direct review finds a first-hitting barrier and rational integral bootstrap under B*R*T <= 1/8 and an explicit integral inequality. No selected witness or radial moment claim.",
        "anchors": "1-9; 18-55; 57-108",
    },
    "Euler/GevreyFlowFinite.lean": {
        "clusters": ["euler", "gevrey", "flow", "jet-bounds"],
        "finding": "Direct review finds finite flow derivative bounds from a genuine within-time jet equation, continuity, factorial-square spatial bounds, and B*R*T <= 1/8. Finite-order flow estimate only.",
        "anchors": "1-7; 23-60; 64-117; 151-198",
    },
    "NavierStokesReview/src/audit/priority_155_euler_gaussian_gevrey_source_review_2026-09-29.md": {
        "clusters": ["euler", "gaussian", "gevrey", "methodology", "repository-root"],
        "finding": "Human-readable Priority 155 direct source review of twelve Euler Gaussian heat, cylinder algebra, Gevrey, continuation, flow, and compactness modules.",
        "anchors": "1-58",
    },
    "NavierStokesReview/evidence/source_tranche_euler_gaussian_gevrey_2026-09-29.json": {
        "clusters": ["euler", "gaussian", "gevrey", "methodology", "repository-root"],
        "finding": "Machine-readable Priority 155 evidence for twelve directly reviewed Euler Gaussian/Gevrey support modules with bounded absence and source-hygiene boundaries.",
        "anchors": "generated JSON; 12 source records",
    },
    "Euler/ExternalTransportCommutator.lean": {
        "clusters": ["euler", "transport", "commutator", "gevrey", "bounds"],
        "finding": "Direct review finds the literal external transport commutator, scalar decomposition, H6 bound, and weighted Gevrey radius-loss estimate under smoothness and all-order MemLp hypotheses. No selected-field transport.",
        "anchors": "1-12; 17-28; 30-51; 53-107; 109-139",
    },
    "Euler/FiniteGradeAlgebra.lean": {
        "clusters": ["euler", "packet", "algebra", "residual", "recursion"],
        "finding": "Direct review finds finite evaluation, truncation, bilinear convolution, exact grade expansion, vanishing above degree, inverse evaluation, and finite tail extraction.",
        "anchors": "1-22; 24-35; 61-100",
    },
    "Euler/FiniteGradeAssembly.lean": {
        "clusters": ["euler", "packet", "algebra", "assembly"],
        "finding": "Direct review finds primary/corrector coefficient reindexing with exact shift and finite assembly identities, including the retained final corrector.",
        "anchors": "1-18; 20-49; 51-74",
    },
    "Euler/FiniteGradeDiagonal.lean": {
        "clusters": ["euler", "packet", "algebra", "recursion"],
        "finding": "Direct review finds finite convolution equal to antidiagonal/range sums and dependence only on coefficients through the target grade.",
        "anchors": "1-4; 15-44",
    },
    "Euler/FiniteGradeSupport.lean": {
        "clusters": ["euler", "packet", "support", "algebra"],
        "finding": "Direct review finds truncation/support, finite evaluation extension, and fast-derivative inverse shift identities.",
        "anchors": "1-3; 13-61",
    },
    "Euler/FiniteGradeTriangular.lean": {
        "clusters": ["euler", "packet", "algebra", "recursion"],
        "finding": "Direct review finds strict lower-grade slow dependence and the two new-grade contributions in the fast convolution.",
        "anchors": "1-3; 14-59",
    },
    "Euler/FinitePathTensor.lean": {
        "clusters": ["euler", "tensor", "functional-analysis", "continuity", "derivatives"],
        "finding": "Direct review finds continuous finite-dimensional multilinear tensor paths, pointwise evaluation, norm control, linearity, and iterated-derivative commutation.",
        "anchors": "1-7; 16-69; 71-106",
    },
    "Euler/FinitePathTensorIntegral.lean": {
        "clusters": ["euler", "tensor", "integral", "functional-analysis"],
        "finding": "Direct review finds tensor-path commutation with constant paths and Bochner time integration under compactness and finite-dimensional hypotheses.",
        "anchors": "1-5; 18-40",
    },
    "Euler/FiniteQuadraticCauchy.lean": {
        "clusters": ["euler", "functional-analysis", "bounds", "continuity"],
        "finding": "Direct review finds a finite quadratic-observation criterion forcing a sequence to be Cauchy. Abstract convergence result only.",
        "anchors": "1-10; 10-30",
    },
    "Euler/FixedEndpointStrong.lean": {
        "clusters": ["euler", "endpoint", "coordinates", "evolution", "regularity"],
        "finding": "Direct review finds a conditional fixed-coordinate endpoint inverse, coordinate equation, H1/reconstruction, derivative, and forward-history identities.",
        "anchors": "1-10; 40-113; 157-203",
    },
    "Euler/FixedEndpointClassical.lean": {
        "clusters": ["euler", "endpoint", "coordinates", "evolution", "uniqueness"],
        "finding": "Direct review finds conditional classical displacement/acceleration, endpoint values, differentiability, projected equation, and coordinate-path uniqueness.",
        "anchors": "1-19; 21-31; 40-124",
    },
    "Euler/FixedEvolutionNaturality.lean": {
        "clusters": ["euler", "endpoint", "operator-intertwining", "evolution", "functional-analysis"],
        "finding": "Direct review finds adjoint/Gram/solver and velocity/acceleration/path intertwining for compatible operators with explicit coercivity and regularity hypotheses.",
        "anchors": "1-20; 22-71; 73-127",
    },
    "NavierStokesReview/src/audit/priority_153_euler_finite_grade_endpoint_source_review_2026-09-29.md": {
        "clusters": ["euler", "endpoint", "packet", "methodology", "repository-root"],
        "finding": "Human-readable Priority 153 direct source review of twelve Euler finite-grade, tensor-path, quadratic-Cauchy, and fixed-endpoint modules.",
        "anchors": "1-95",
    },
    "NavierStokesReview/evidence/source_tranche_euler_finite_grade_endpoint_2026-09-29.json": {
        "clusters": ["euler", "endpoint", "packet", "methodology", "repository-root"],
        "finding": "Machine-readable Priority 153 evidence for twelve directly reviewed Euler finite-grade, tensor-path, quadratic-Cauchy, and fixed-evolution modules.",
        "anchors": "generated JSON; 12 source records",
    },
    "NavierStokes/LocalPaperTheorem.lean": {
        "clusters": ["endpoint", "profiles", "residual", "pressure", "cartesian-assembly"],
        "finding": "Direct review finds local selected schedule properties, smooth fields, pressure and residual flatness, exterior agreement, and local chart assembly. It does not export the selected Cartesian (M,I,J,S,C_p) observable equality.",
        "anchors": "53-83; 100-124; 128-186",
    },
    "NavierStokes/LocalResidualFlatness.lean": {
        "clusters": ["residual", "jets", "stage-interface", "endpoint"],
        "finding": "Direct review finds selected concrete estimates producing a common schedule and all residual jet rates. This is a real rate derivation, not a free NativeBounds premise, but it does not identify those rates with the paper's final five observables.",
        "anchors": "19-75; 80-125",
    },
    "NavierStokes/PaperLocalization.lean": {
        "clusters": ["endpoint", "pressure", "time", "cartesian-assembly"],
        "finding": "Direct review finds late-time compact-pressure/local-field agreement and a local theorem with a compact candidate. It does not prove selected-field five-moment transport or absolute pressure-Poisson semantics.",
        "anchors": "20-50",
    },
    "NavierStokes/PeriodizePDE.lean": {
        "clusters": ["cartesian-assembly", "residual", "pressure", "time"],
        "finding": "Direct review finds translation, derivative, divergence, pressure, Laplacian, advection, and residual periodisation identities. These transport the PDE operator, not the paper's radial five-moment observables.",
        "anchors": "32-40; 46-114; 117-150",
    },
    "NavierStokes/MomentRepairPicard.lean": {
        "clusters": ["moments", "corrections", "rank", "profiles"],
        "finding": "Direct review finds abstract compatible moment-repair iteration, limit compatibility, and small-solution existence. It does not identify the selected mixed Cartesian endpoint with the five paper observables.",
        "anchors": "inverse_compatible; iteration_compatible; iterates_compatible; limits_compatible; exists_compatible_small_solutions",
    },
    "NavierStokes/MomentRepairPicardConvergence.lean": {
        "clusters": ["moments", "corrections", "profiles"],
        "finding": "Direct review finds contraction and convergent abstract moment-repair iterates under stated hypotheses. It does not supply the final selected-field transport theorem.",
        "anchors": "21-; exists_small_solution_with_iterates",
    },
    "NavierStokes/CandidateFromLimits.lean": {
        "clusters": ["force", "residual", "jets", "endpoint"],
        "finding": "Direct review finds force smoothness derived from full residual derivative limits, activated-residual agreement before t=1, support, and derivative decay. This is not a proof that the manuscript's five-moment explanation has been transported.",
        "anchors": "35-57; 80-148; 167-218",
    },
    "NavierStokes/MixedPeriodicAssembly.lean": {
        "clusters": ["force", "residual", "endpoint", "cartesian-assembly"],
        "finding": "Direct review finds the candidate force assembled from residual limits, smooth extensions, divergence, periodicity, and the axis-growth premise. It does not make the force smoothness equivalent to a final five-moment equality.",
        "anchors": "338-365",
    },
    "NavierStokes/ActualCandidateAssembly.lean": {
        "clusters": ["endpoint", "physical-data", "moments", "force", "jets"],
        "finding": "Direct review confirms actual physical data and actualStageEstimates feed the selected endpoint. Witness exports force, consequences, blow-up, and limits but no named final (M,I,J,S,C_p) equality.",
        "anchors": "1079-1098; 1121-1151",
    },
    "NavierStokesReview/src/audit/priority_161_rebuttal_force_smoothness_moment_boundary_adjudication_2026-09-29.md": {
        "clusters": ["methodology", "endpoint", "moments", "force", "residual"],
        "finding": "Human-readable adverse adjudication of the supplied rebuttal: confirms the endpoint correspondence gap, rejects the unsupported sole-Fredholm/iff escalation, and distinguishes derived force smoothness from unclosed paper-mechanism transport.",
        "anchors": "1-150",
    },
    "NavierStokesReview/evidence/source_tranche_rebuttal_force_smoothness_moment_boundary_2026-09-29.json": {
        "clusters": ["methodology", "endpoint", "moments", "force", "residual"],
        "finding": "Machine-readable Priority 161 source adjudication with exact Lean/manuscript anchors and explicit confirmed/not-established boundaries.",
        "anchors": "generated JSON; 9 source records",
    },
    "NavierStokesReview/src/audit/priority_162_barmoment_correction_state_vs_selected_field_source_review_2026-09-29.md": {
        "clusters": ["moments", "rank", "cartesian-assembly", "endpoint"],
        "finding": "Direct review separates genuine correction-state barMoment/FiveRows identities from the still-unclosed equality identifying those observables with the final activated Cartesian field.",
        "anchors": "source review; DefectIncrementBounds 214-220, 621-658; StateMomentBalances 956-978; CorrectionStep 1469-1498; NominalProfile 2078-2140",
    },
    "NavierStokesReview/evidence/source_tranche_barmoment_correction_state_vs_selected_field_2026-09-29.json": {
        "clusters": ["moments", "rank", "cartesian-assembly", "endpoint"],
        "finding": "Machine-readable Priority 162 source review records the correction-state versus final selected-field type boundary without claiming a nonzero defect or impossibility.",
        "anchors": "generated JSON; direct declaration review",
    },
}


CLUSTER_RULES = [
    ("endpoint", ("ActualCandidate", "CandidateConsequences", "Theorem", "ProblemStatement", "GermCandidate")),
    ("moments", ("Moment", "Profile", "barMoment", "GlobalStress")),
    ("rank", ("Rank", "Debt", "Correction", "DefectIncrement")),
    ("pressure", ("Pressure", "Riesz", "Poisson", "pressure")),
    ("energy", ("Energy", "Dissipation", "energy")),
    ("force", ("Force", "Residual", "force")),
    ("jets", ("Jet", "Residual", "Germ", "Taylor")),
    ("time", ("Time", "Schedule", "Glued", "Interval", "Cutoff")),
    ("axis", ("Axis", "Origin", "Chart", "radius")),
    ("cartesian-assembly", ("ActualPrimary", "StateRealization", "Solenoidal", "Potential", "Period")),
    ("euler", ("Euler/", "Packet", "IntervalPath", "Vorticity")),
]

CLUSTER_PRIORITY = {
    "endpoint": 100,
    "moments": 95,
    "cartesian-assembly": 90,
    "pressure": 85,
    "force": 80,
    "rank": 78,
    "residual": 75,
    "jets": 72,
    "energy": 68,
    "axis": 66,
    "time": 60,
    "stage-interface": 58,
    "global-assembly": 56,
    "physical-data": 52,
    "profiles": 50,
    "r3": 45,
    "euler": 40,
}


def inferred_clusters(module: str, declarations: list[dict[str, Any]]) -> list[str]:
    text = module + " " + " ".join(d["name"] for d in declarations)
    return [name for name, needles in CLUSTER_RULES if any(needle in text for needle in needles)]


def normalise_modules(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Accept both the legacy module-dictionary map and the current list map."""
    raw = data.get("modules", {})
    if isinstance(raw, dict):
        return raw
    return {record["module"]: record for record in raw}


def reachable_modules(data: dict[str, Any], modules: dict[str, dict[str, Any]]) -> set[str]:
    """Recover module reachability from either map-generation format.

    The current repository map stores declaration routes rather than a flat
    dependency_subgraph.  Route source strings contain a stable
    ``module=...`` field, while declaration names provide a second check.
    """
    subgraph = data.get("dependency_subgraph")
    if isinstance(subgraph, dict):
        return set(subgraph.get("reachable_modules", []))

    declaration_modules: dict[str, str] = {}
    for module, record in modules.items():
        for declaration in record.get("declarations", []):
            name = declaration.get("name")
            if name:
                declaration_modules[name] = module

    reachable: set[str] = set()
    for route in data.get("routes", []):
        if not route.get("reachable", False):
            continue
        for node in route.get("path", []):
            name = node.get("name")
            if name in declaration_modules:
                reachable.add(declaration_modules[name])
            source = node.get("source", "")
            if isinstance(source, dict):
                module_name = source.get("module")
                if module_name:
                    reachable.add(module_name)
            elif isinstance(source, str):
                match = re.search(r"module=([^;}]*)", source)
                if match:
                    reachable.add(match.group(1))
    return reachable


def review_priority(clusters: list[str], declarations: int, lines: int) -> int:
    """Rank unresolved modules for human review; never infer a mathematical result."""
    base = max((CLUSTER_PRIORITY.get(cluster, 0) for cluster in clusters), default=0)
    load_bearing = sum(CLUSTER_PRIORITY.get(cluster, 0) for cluster in clusters if cluster in {
        "endpoint", "moments", "cartesian-assembly", "pressure", "force", "rank", "residual"
    })
    return min(999, base + min(load_bearing // 4, 60) + min(declarations // 20, 20) + min(lines // 500, 10))


def make_rows(data: dict[str, Any]) -> list[dict[str, Any]]:
    modules = normalise_modules(data)
    reachable = reachable_modules(data, modules)
    rows = []
    for module, record in sorted(modules.items()):
        explicit = EVIDENCE.get(record["path"])
        if explicit:
            status = "evidence_inspected"
            finding = explicit["finding"]
            anchors = explicit["anchors"]
        elif module in reachable:
            status = "reachable_not_semantically_inspected"
            finding = "Import-reachable from a captured root; declaration use and paper-level transport have not been independently classified."
            anchors = ""
        elif record.get("source_flags", {}).get("sorry_token"):
            status = "source_indexed_sorry_token"
            finding = "Source-indexed file contains a `sorry` token; endpoint contamination is not inferred from this row alone."
            anchors = ""
        else:
            status = "source_indexed_review_queued"
            finding = "Source-indexed path; no declaration-level semantic review record yet."
            anchors = ""
        clusters = sorted(set(inferred_clusters(module, record.get("declarations", [])) + (explicit or {}).get("clusters", [])))
        resolution = record.get("import_resolution", {})
        if not resolution:
            resolution = {
                "resolved": record.get("resolved_imports", []),
                "external": record.get("external_imports", []),
                "missing_project": record.get("missing_project_imports", []),
            }
        rows.append({
            "module": module,
            "path": record["path"],
            "sha256": record["sha256"],
            "lines": record["line_count"],
            "declarations": len(record.get("declarations", [])),
            "imports_resolved": len(resolution.get("resolved", [])),
            "imports_external": len(resolution.get("external", [])),
            "imports_missing": len(resolution.get("missing_project", [])),
            "reachable": module in reachable,
            "clusters": clusters,
            "priority": review_priority(clusters, len(record.get("declarations", [])), record["line_count"]),
            "status": status,
            "finding": finding,
            "anchors": anchors,
            "source_flags": record.get("source_flags", {}),
        })
    return rows


def count_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "modules": len(rows),
        "reachable": sum(r["reachable"] for r in rows),
        "not_reachable": sum(not r["reachable"] for r in rows),
        "status": dict(sorted(Counter(r["status"] for r in rows).items())),
        "cluster": dict(sorted(Counter(c for r in rows for c in r["clusters"]).items())),
        "missing_project_import_edges": sum(r["imports_missing"] for r in rows),
        "source_rows_with_sorry_token": sum(r["source_flags"].get("sorry_token", False) for r in rows),
    }


def supplemental_evidence(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Return explicit evidence artifacts that are not Lean module rows."""
    module_paths = {record["path"] for record in normalise_modules(data).values()}
    return [
        {"path": path, **record}
        for path, record in sorted(EVIDENCE.items())
        if path not in module_paths
    ]


def render_markdown(data: dict[str, Any], rows: list[dict[str, Any]]) -> str:
    c = count_rows(rows)
    supplemental = supplemental_evidence(data)
    out = [
        "# Semantic Coverage Register for the Lean Repository", "",
        "Generated from the hardened source map. This is a review register, not a proof certificate.", "",
        "## Reading rule", "",
        "`reachable` means that the source import graph reaches the module from captured roots. `evidence_inspected` means that an explicit source-and-line review record exists in this register. Neither status alone proves that a paper-level mathematical identity is transported to the exported endpoint.", "",
        f"- Modules: **{c['modules']}**; endpoint-graph reachable: **{c['reachable']}**; outside that graph: **{c['not_reachable']}**.",
        f"- Explicitly inspected source records: **{c['status'].get('evidence_inspected', 0)}**.",
        f"- Supplemental review artifacts (not Lean module rows): **{len(supplemental)}**.",
        f"- Reachable but not semantically inspected: **{c['status'].get('reachable_not_semantically_inspected', 0)}**.",
        f"- Source rows with a `sorry` token: **{c['source_rows_with_sorry_token']}**. This is a census flag, not endpoint contamination proof.",
        f"- Missing project import edges recorded by the map: **{c['missing_project_import_edges']}**.", "",
        "## Status meanings", "",
        "| Status | Meaning |", "|---|---|",
        "| `evidence_inspected` | Explicit source locations and a bounded mathematical finding are recorded. |",
        "| `reachable_not_semantically_inspected` | The source import graph reaches the module, but no semantic transport conclusion is asserted. |",
        "| `source_indexed_review_queued` | The file is present and indexed, but not yet reviewed at declaration level. |",
        "| `source_indexed_sorry_token` | The source census found a `sorry` token; this does not prove endpoint use. |", "",
        "## Current controlled conclusions", "",
        "1. Upstream five-moment/profile machinery is real and locally consumed.",
        "2. Inspected selected-endpoint predicates do not require equality transporting the five named paper moments onto the final activated Cartesian field.",
        "3. The generic stage interface is rate/smoothness based and moment-blind by type. That proves interface non-entailment, not a nonzero moment leak in the concrete selected field.",
        "4. Pressure comparison identities and energy identities are real; they must not be reported as an absolute selected-pressure transport theorem or as evidence of a missing energy identity.",
        "5. An unconditional `False` requires a concrete contradiction, such as a verified nonzero selected-field remainder against a verified zero invariant. This register does not manufacture that result.", "",
        "## Supplemental review artifacts", "",
        "These files are explicit audit evidence but are not counted as Lean modules or endpoint reachability rows.", "",
        "| Artifact | Finding |", "|---|---|",
    ]
    for artifact in supplemental:
        out.append(f"| `{artifact['path']}` | {artifact['finding']} |")
    out += [
        "",
        "## Cluster coverage", "", "| Cluster | Modules tagged |", "|---|---:|",
    ]
    for cluster, total in c["cluster"].items():
        out.append(f"| `{cluster}` | {total} |")
    out += ["", "## Prioritised unresolved reachable queue", "", "This queue is an order of inspection, not a negative finding. A high score means that the path is reachable and named by load-bearing clusters such as endpoint, moments, pressure, force, rank, residual, or Cartesian assembly.", "", "| Priority | Module | Source path | Lines | Decls | Clusters | Current state |", "|---:|---|---|---:|---:|---|---|"]
    for row in sorted((r for r in rows if r["status"] == "reachable_not_semantically_inspected"), key=lambda r: (-r["priority"], r["module"])):
        clusters = ", ".join(row["clusters"]) or "unclassified"
        out.append(f"| {row['priority']} | `{row['module']}` | `{row['path']}` | {row['lines']} | {row['declarations']} | {clusters} | `{row['status']}` |")
    out += ["", "## Full path-qualified module register", "", "| Module | Source path | Lines | Decls | Reachable | Priority | Clusters | Status | Evidence / current finding |", "|---|---|---:|---:|:---:|---:|---|---|---|"]
    for row in rows:
        def esc(value: Any) -> str:
            return str(value).replace("|", "\\|").replace("\n", " ")
        clusters = ", ".join(row["clusters"]) or "unclassified"
        evidence = (row["anchors"] + ": " if row["anchors"] else "") + row["finding"]
        out.append(f"| `{esc(row['module'])}` | `{esc(row['path'])}` | {row['lines']} | {row['declarations']} | {str(row['reachable']).lower()} | {row['priority']} | {esc(clusters)} | `{row['status']}` | {esc(evidence)} |")
    out += ["", "## Required next review order", "", "1. Complete declaration-level classification for every endpoint-reachable module, using path-qualified names.", "2. For each paper load-bearing identity, record the exact source theorem that transports it through summation, curl, cutoffs, periodisation, and endpoint packaging.", "3. Mark a bridge `transported` only after inspecting its theorem statement and proof term, not because an import or similarly named declaration exists.", "4. Keep unresolved rows visible; do not convert them to negative findings without a source-backed contradiction.", ""]
    return "\n".join(out)


def render_html(rows: list[dict[str, Any]], c: dict[str, Any]) -> str:
    body = []
    for row in rows:
        text = (row["anchors"] + ": " if row["anchors"] else "") + row["finding"]
        body.append("<tr><td>{}</td><td><code>{}</code></td><td><code>{}</code></td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td><code>{}</code></td><td>{}</td></tr>".format(row["priority"], html.escape(row["module"]), html.escape(row["path"]), row["lines"], row["declarations"], str(row["reachable"]).lower(), html.escape(", ".join(row["clusters"])), html.escape(row["status"]), html.escape(text)))
    template = """<!doctype html><html><head><meta charset='utf-8'><title>Lean semantic coverage register</title><style>body{{font-family:system-ui,sans-serif;margin:2rem;color:#17202a}} .cards{{display:flex;gap:1rem;flex-wrap:wrap}}.card{{border:1px solid #ccd;padding:.7rem;border-radius:.4rem;background:#f7f9fb}}input,select{{padding:.5rem;margin:.3rem 0}}.wrap{{overflow:auto;max-height:75vh;border:1px solid #ccd}}table{{border-collapse:collapse;width:100%;font-size:.86rem}}th,td{{border-bottom:1px solid #dde;padding:.45rem;text-align:left;vertical-align:top}}th{{position:sticky;top:0;background:#eaf0f6}}</style></head><body><h1>Lean semantic coverage register</h1><p>Structural reachability is not semantic transport. This register keeps those states separate.</p><div class='cards'><div class='card'>modules: <b>{modules}</b></div><div class='card'>reachable: <b>{reachable}</b></div><div class='card'>inspected: <b>{inspected}</b></div><div class='card'>reachable-open: <b>{open}</b></div></div><p><input id='q' placeholder='filter module, path, finding'><select id='s'><option value=''>all statuses</option><option>evidence_inspected</option><option>reachable_not_semantically_inspected</option><option>source_indexed_review_queued</option><option>source_indexed_sorry_token</option></select></p><div class='wrap'><table id='t'><thead><tr><th>Priority</th><th>Module</th><th>Path</th><th>Lines</th><th>Decls</th><th>Reachable</th><th>Clusters</th><th>Status</th><th>Finding</th></tr></thead><tbody>{rows}</tbody></table></div><script>const q=document.querySelector('#q'),s=document.querySelector('#s');function f(){{const x=q.value.toLowerCase(),y=s.value;for(const r of document.querySelectorAll('#t tbody tr'))r.style.display=(!y||r.cells[7].innerText.trim()===y)&&(!x||r.innerText.toLowerCase().includes(x))?'':'none'}}q.oninput=f;s.onchange=f;</script></body></html>"""
    return template.format(modules=c["modules"], reachable=c["reachable"], inspected=c["status"].get("evidence_inspected", 0), open=c["status"].get("reachable_not_semantically_inspected", 0), rows="".join(body))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-map", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    parser.add_argument("--html", type=Path, required=True)
    args = parser.parse_args()
    data = json.loads(args.source_map.read_text(encoding="utf-8"))
    rows = make_rows(data)
    counts = count_rows(rows)
    artifacts = supplemental_evidence(data)
    counts["supplemental_evidence_records"] = len(artifacts)
    payload = {
        "schema": "navier-stokes-semantic-coverage-register/v2",
        "source_map": str(args.source_map),
        "counts": counts,
        "supplemental_evidence": artifacts,
        "rows": rows,
    }
    for path in (args.json, args.markdown, args.html):
        path.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.markdown.write_text(render_markdown(data, rows), encoding="utf-8")
    args.html.write_text(render_html(rows, payload["counts"]), encoding="utf-8")
    print(json.dumps({"json": str(args.json), "markdown": str(args.markdown), "html": str(args.html), "counts": payload["counts"]}, indent=2))


if __name__ == "__main__":
    main()
