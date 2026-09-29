"""Hardened selected-endpoint transport audit.

This tool is deliberately stricter than a grep scan.  It performs two
independent passes:

1. a source pass that records declaration blocks, their source spans, and
   whether the *same declaration* mentions the selected field, the moment
   operator, and the transformations that must be transported; and
2. an optional Lean-environment pass over the exported declaration closure,
   using the exact declaration type and environment references emitted by
   ``EnvironmentDependencyExport.lean``.

The result is triage evidence, not a theorem.  In particular, absence of a
candidate is never upgraded to an impossibility claim, and a declaration that
mentions ``barMoment`` is not treated as a transport theorem unless its type
or body also binds the selected expression and an equality/iff/transport
conclusion.  The tool records unresolved candidates for manual Lean review.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DECL_RE = re.compile(
    r"^\s*(?:(?:private|protected|noncomputable|unsafe|partial|opaque)\s+)*"
    r"(?:@\[[^\]]*\]\s*)*"
    r"(theorem|lemma|def|abbrev|structure|class|inductive|opaque|axiom|example|instance)\s+"
    r"([A-Za-z_][A-Za-z0-9_'.]*)"
)
NAMESPACE_RE = re.compile(r"^\s*namespace\s+([A-Za-z_][A-Za-z0-9_'.]*)\s*$")
END_RE = re.compile(r"^\s*end(?:\s+[A-Za-z_][A-Za-z0-9_'.]*)?\s*$")
IMPORT_RE = re.compile(r"^\s*import\s+([A-Za-z0-9_.]+)")

FIELD_TERMS = (
    "selected_witness", "selectedPotentialSum", "potentialSum", "ASum",
    "BSum", "PSum", "selectedPotentialStages", "selectedDirectSum",
    "selectedDirectPrefix", "selectedMixed", "selectedMixedRadialPullback",
    "physicalFields_all", "cutPotential", "cutVelocity", "periodicVelocity",
    "activatedVelocity", "selectedPotentialComponent", "VelocityField",
)
MOMENT_TERMS = (
    "barMoment", "FiveRows", "FiveRowRank", "PositiveOrderMoments",
    "FiveProfileMoments", "physicalMoments", "five_moments", "Debt",
)
TRANSFORM_TERMS = (
    "tsum", "curl", "spatialCurl", "SpatialLocalization", "periodize",
    "torusAverage", "radial", "Radial", "CylPoint", "chartIdentity",
)
EQUALITY_TERMS = ("=", "↔", "Iff", "Eq", "transport", "preserv", "identity")
TARGET_TUPLE_TERMS = ("M", "I", "J", "S", "Cp", "C_p")


@dataclass(frozen=True)
class SourceDecl:
    module: str
    path: str
    line: int
    end_line: int
    kind: str
    name: str
    text: str
    header: str
    body: str


def module_name(repo_root: Path, path: Path) -> str:
    return ".".join(path.relative_to(repo_root).with_suffix("").parts)


def terms_present(text: str, terms: Iterable[str]) -> list[str]:
    return [term for term in terms if re.search(rf"(?<![A-Za-z0-9_']){re.escape(term)}(?![A-Za-z0-9_'])", text)]


def strip_lean_comments(text: str) -> str:
    """Remove nested Lean comments before interpreting declaration evidence.

    Declaration windows extend to the next declaration, so trailing module
    prose must not count as a term in the declaration being classified.
    Strings are retained; this keeps the pass conservative rather than
    pretending to be a full Lean lexer.
    """
    out: list[str] = []
    depth = 0
    i = 0
    while i < len(text):
        if depth == 0 and text.startswith("--", i):
            newline = text.find("\n", i)
            if newline < 0:
                break
            out.append("\n")
            i = newline + 1
            continue
        if text.startswith("/-", i):
            depth += 1
            i += 2
            continue
        if depth and text.startswith("-/", i):
            depth -= 1
            i += 2
            continue
        if depth == 0:
            out.append(text[i])
        elif text[i] == "\n":
            out.append("\n")
        i += 1
    return "".join(out)


def decl_blocks(repo_root: Path, source_root: Path) -> list[SourceDecl]:
    rows: list[SourceDecl] = []
    file_terms = FIELD_TERMS + MOMENT_TERMS + TRANSFORM_TERMS
    for path in sorted(source_root.rglob("*.lean")):
        if ".lake" in path.parts or ".git" in path.parts:
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        # The repository-wide source census already records every file.  This
        # declaration pass only expands files that can participate in the
        # selected transport question, which keeps the expensive namespace
        # and block parsing bounded without turning the result into a sample.
        if not any(term in raw for term in file_terms):
            continue
        # Use a comment-stripped copy for declaration and namespace detection.
        # This prevents prose examples inside nested Lean comments from being
        # mistaken for source declarations.  The original lines remain the
        # source of excerpts and line spans.
        structural_lines = strip_lean_comments(raw).splitlines()
        lines = raw.splitlines()
        starts: list[tuple[int, str, str]] = []
        namespace_stack: list[str] = []
        for index, line in enumerate(structural_lines):
            namespace = NAMESPACE_RE.match(line)
            if namespace:
                namespace_stack.append(namespace.group(1))
                continue
            if END_RE.match(line) and namespace_stack:
                namespace_stack.pop()
                continue
            match = DECL_RE.match(line)
            if match:
                local = match.group(2)
                qualified = ".".join([*namespace_stack, local])
                starts.append((index, match.group(1), qualified))
        for position, (start, kind, name) in enumerate(starts):
            stop = starts[position + 1][0] if position + 1 < len(starts) else len(lines)
            text = "\n".join(lines[start:stop])
            # Lean permits `:= by` on the declaration line, so do not require
            # a preceding newline or a word-boundary after `:=` (there is no
            # word boundary between `=` and whitespace).
            split = re.search(r"(?::=|where)(?=\s|$)", strip_lean_comments(text))
            if split:
                structural_text = strip_lean_comments(text)
                header = structural_text[:split.start()]
                body = structural_text[split.end():]
            else:
                header, body = strip_lean_comments(text), ""
            rows.append(SourceDecl(
                module=module_name(repo_root, path),
                path=path.relative_to(repo_root).as_posix(),
                line=start + 1,
                end_line=stop,
                kind=kind,
                name=name,
                text=strip_lean_comments(text),
                header=header,
                body=body,
            ))
    return rows


def source_classification(decl: SourceDecl) -> dict[str, object]:
    code = strip_lean_comments(decl.text)
    body_code = strip_lean_comments(decl.body)
    field = terms_present(code, FIELD_TERMS)
    moment = terms_present(code, MOMENT_TERMS)
    transform = terms_present(code, TRANSFORM_TERMS)
    equality = terms_present(code, EQUALITY_TERMS)
    tuple_terms = terms_present(code, TARGET_TUPLE_TERMS)
    body_field = terms_present(body_code, FIELD_TERMS)
    body_moment = terms_present(body_code, MOMENT_TERMS)
    body_transform = terms_present(body_code, TRANSFORM_TERMS)
    negative_marker_terms = (
        "does_not", "not_", "not_entail", "compatible", "coexists",
        "obstruction", "ignores", "unconstrained", "countermodel",
    )
    negative_markers = [term for term in negative_marker_terms if term in code]
    gate_markers = [term for term in ("hpositive", "hsupport", "hnonzero", "hperiodic") if term in code]
    is_proposition = decl.kind in {"theorem", "lemma", "example"}
    body_present = bool(body_code.strip())
    has_selected_expression = any(
        term in field
        for term in (
            "selected_witness",
            "selectedMixedRadialPullback",
            "selectedPotentialSum",
            "selectedPotentialStages",
            "selectedPotentialComponent",
        )
    )
    if not field or not moment:
        category = "not_a_joint_candidate"
    elif "False" in code or "\u22a5" in code or negative_markers or gate_markers:
        category = "conditional_or_obstruction_candidate"
    elif is_proposition and body_present and has_selected_expression and transform and equality:
        category = "manual_transport_candidate"
    elif field and moment and equality:
        category = "moment_field_equality_candidate"
    else:
        category = "cooccurrence_only"
    return {
        "module": decl.module,
        "path": decl.path,
        "origin": (
            "review_completion"
            if decl.path.startswith("NavierStokesReview/")
            else "source_tree"
        ),
        "line": decl.line,
        "end_line": decl.end_line,
        "kind": decl.kind,
        "name": decl.name,
        "category": category,
        "field_terms": field,
        "moment_terms": moment,
        "transform_terms": transform,
        "equality_terms": equality,
        "tuple_terms": tuple_terms,
        "negative_markers": negative_markers,
        "gate_markers": gate_markers,
        "is_proposition": is_proposition,
        "has_selected_expression": has_selected_expression,
        "body_field_terms": body_field,
        "body_moment_terms": body_moment,
        "body_transform_terms": body_transform,
        "body_present": body_present,
        "header_field_terms": terms_present(decl.header, FIELD_TERMS),
        "header_moment_terms": terms_present(decl.header, MOMENT_TERMS),
        "header_transform_terms": terms_present(decl.header, TRANSFORM_TERMS),
        "source_excerpt": "\n".join(decl.text.splitlines()[:28]),
    }


def load_environment(path: Path) -> dict[str, dict[str, object]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {row["name"]: row for row in payload.get("nodes", []) if "name" in row}


def environment_closure(nodes: dict[str, dict[str, object]], roots: list[str]) -> set[str]:
    seen: set[str] = set()
    queue: deque[str] = deque(roots)
    while queue:
        current = queue.popleft()
        if current in seen:
            continue
        seen.add(current)
        for target in nodes.get(current, {}).get("uses", []):
            if target in nodes:
                queue.append(target)
    return seen


def environment_rows(
    nodes: dict[str, dict[str, object]], roots: list[str]
) -> tuple[list[dict[str, object]], list[str]]:
    closure = environment_closure(nodes, roots)
    rows: list[dict[str, object]] = []
    for name in sorted(closure):
        # A stale export can mention a root or dependency that is not present
        # in its node table.  Keep that condition explicit instead of raising
        # or silently interpreting it as source absence.
        node = nodes.get(name)
        if node is None:
            continue
        type_text = str(node.get("type", ""))
        type_field = terms_present(type_text, FIELD_TERMS)
        type_moment = terms_present(type_text, MOMENT_TERMS)
        type_transform = terms_present(type_text, TRANSFORM_TERMS)
        if type_field or type_moment or type_transform or name in roots:
            rows.append({
                "name": name,
                "type": type_text,
                "uses_sorry_ax": bool(node.get("usesSorryAx", False)),
                "field_terms_in_type": type_field,
                "moment_terms_in_type": type_moment,
                "transform_terms_in_type": type_transform,
                "uses_count": len(node.get("uses", [])),
            })
    missing_roots = sorted({root for root in roots if root not in nodes})
    return rows, missing_roots


def markdown(payload: dict[str, object]) -> str:
    lines = [
        "# Hardened selected-endpoint transport audit",
        "",
        "This report separates source declaration triage from Lean-environment evidence.",
        "A co-occurrence is not a transport proof. No absence result is promoted to an impossibility theorem.",
        "",
        "## Audit contract",
        "",
        "A declaration is a transport candidate only when the same declaration binds selected-field terms and moment terms, and also contains an equality/transport conclusion. A `manual_transport_candidate` is a positive theorem/lemma/example whose declaration body also binds the selected expression and transformation terms. Negative, compatibility, countermodel, and conditional-gate declarations are separated before this category. All candidates remain review targets until compiled and manually checked.",
        "",
        f"- Source declarations indexed: **{payload['source_declarations']}**",
        f"- Joint source candidates: **{payload['source_joint_candidates']}**",
        f"- Full manual candidates: **{payload['source_manual_candidates']}**",
        f"- Joint candidates by origin: **{payload['source_joint_candidates_by_origin']}**",
        f"- Manual candidates by origin: **{payload['source_manual_candidates_by_origin']}**",
        f"- Environment closure supplied: **{payload['environment_supplied']}**",
        f"- Environment status: **{payload['environment_status']}**",
        f"- Missing environment roots: **{', '.join(payload['missing_environment_roots']) or 'none'}**",
        f"- Environment declarations with endpoint/moment/transform terms in their type: **{payload['environment_rows']}**",
        "",
        "## Source candidates",
        "",
        "| Origin | Category | File | Lines | Declaration | Field terms | Moment terms | Transform terms |",
        "|---|---|---|---:|---|---|---|---|",
    ]
    for row in payload["source_candidates"]:
        lines.append(
            f"| {row['origin']} | {row['category']} | `{row['path']}` | {row['line']}-{row['end_line']} | `{row['name']}` | "
            f"{', '.join(row['field_terms'])} | {', '.join(row['moment_terms'])} | {', '.join(row['transform_terms'])} |"
        )
    lines.extend([
        "",
        "## Interpretation boundary",
        "",
        "`manual_transport_candidate` means only that a declaration deserves direct Lean review. It does not prove that the equality is the paper's equality, that its domain is the selected whole-space field, or that its premises are inhabited. A conditional `False` theorem is not an endpoint contradiction until every hypothesis is derived on the selected branch. `conditional_or_obstruction_candidate` includes useful adversarial probes, but never counts as a selected-field impossibility theorem by itself.",
        "",
        "The report therefore cannot by itself justify `FORMALLY REFUTED`, `False`, `Delta m != 0`, or `zero percent formalised`. Those labels require a compiled zero-sorry theorem or a complete source-backed proof with all concrete premises.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--source-root", type=Path, action="append", help="Repeat for additional source roots; defaults to the repository root.")
    parser.add_argument("--environment", type=Path)
    parser.add_argument("--json", type=Path)
    parser.add_argument("--markdown", type=Path)
    parser.add_argument(
        "--root",
        action="append",
        default=None,
        help="Endpoint declaration root; repeat for multiple roots. Defaults to the selected NS endpoints.",
    )
    args = parser.parse_args()
    if args.root is None:
        args.root = [
            "NavierStokesR3.theorem_1_1",
            "NavierStokes.ActualCandidateAssembly.selected_witness",
        ]
    repo_root = args.repo_root.resolve()
    source_roots = [path.resolve() for path in args.source_root] if args.source_root else [repo_root]
    declarations = []
    for source_root in source_roots:
        declarations.extend(decl_blocks(repo_root, source_root))
    source_candidates = [source_classification(row) for row in declarations]
    source_candidates = [
        row for row in source_candidates
        if row["category"] != "not_a_joint_candidate"
    ]
    env_rows: list[dict[str, object]] = []
    missing_environment_roots: list[str] = []
    if args.environment:
        nodes = load_environment(args.environment.resolve())
        env_rows, missing_environment_roots = environment_rows(nodes, args.root)
    payload: dict[str, object] = {
        "instrument": "selected_transport_audit",
        "status": "conservative source and optional Lean-environment triage; not a theorem",
        "repo_root": repo_root.as_posix(),
        "source_roots": [path.as_posix() for path in source_roots],
        "roots": args.root,
        "environment": args.environment.resolve().as_posix() if args.environment else None,
        "environment_supplied": bool(args.environment),
        "environment_status": (
            "not_supplied"
            if not args.environment
            else "supplied_with_missing_roots"
            if missing_environment_roots
            else "historical_snapshot_freshness_not_asserted"
        ),
        "missing_environment_roots": missing_environment_roots,
        "source_files_with_audit_terms": len({row.path for row in declarations}),
        "source_declarations": len(declarations),
        "source_joint_candidates": len(source_candidates),
        "source_manual_candidates": sum(row["category"] == "manual_transport_candidate" for row in source_candidates),
        "source_joint_candidates_by_origin": {
            origin: sum(row["origin"] == origin for row in source_candidates)
            for origin in sorted({str(row["origin"]) for row in source_candidates})
        },
        "source_manual_candidates_by_origin": {
            origin: sum(
                row["origin"] == origin
                and row["category"] == "manual_transport_candidate"
                for row in source_candidates
            )
            for origin in sorted({str(row["origin"]) for row in source_candidates})
        },
        "environment_rows": len(env_rows),
        "source_candidates": source_candidates,
        "environment_rows_detail": env_rows,
        "verdict": {
            "selected_transport_proved": False,
            "selected_transport_disproved": False,
            "selected_delta_m_proved": False,
            "kernel_false_proved": False,
            "absence_claim_permitted": False,
        },
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    print(json.dumps({k: payload[k] for k in (
        "source_declarations", "source_joint_candidates", "source_manual_candidates",
        "environment_supplied", "environment_rows", "verdict",
    )}, indent=2))
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(encoded, encoding="utf-8")
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text(markdown(payload), encoding="utf-8")


if __name__ == "__main__":
    main()
