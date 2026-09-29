"""Audit the logical scope of review-authored Lean probes.

This is a provenance and contract checker, not a Lean theorem prover.  It is
designed to catch the most dangerous audit mistake: treating a conditional,
interface-level, or review-completion theorem as a theorem about the exported
OpenAI endpoint.  It reports the declaration location, source origin, selected
endpoint binding, explicit premise markers, and conclusion-strength markers.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


DECL_RE = re.compile(
    r"(?m)^(?P<indent>\s*)(?P<kind>theorem|lemma|def|example)\s+"
    r"(?P<name>[A-Za-z0-9_'.]+)"
)

AUDIT_TERMS = (
    "selected",
    "moment",
    "barMoment",
    "Debt",
    "FiveRows",
    "periodic",
    "support",
    "fixed_force",
    "False",
    "nonzero",
    "neq",
)

SELECTED_TERMS = (
    "selected_witness",
    "selectedWitness",
    "selectedPotential",
    "selectedMixed",
    "selectedDirect",
    "selected_r3",
)

PREMISE_MARKERS = (
    "hsupport",
    "hnonzero",
    "hpositive",
    "htransport",
    "hbridge",
    "hidentity",
    "hperiodic",
    "hfinite",
    "hscalar",
    "hcutoff",
    "hselected",
)

INTERFACE_MARKERS = (
    "StageEstimates",
    "interface_does_not",
    "zero_stage",
    "witnessDebt",
    "arbitrary",
    "ghost",
    "FiveRows",
    "Debt",
)

CONCLUSION_MARKERS = (
    "False",
    "≠",
    "neq",
    "not_",
    "¬",
    "does_not",
    "obstruction",
)


def strip_comments(text: str) -> str:
    """Remove nested Lean comments while preserving line positions."""
    out: list[str] = []
    i = 0
    depth = 0
    while i < len(text):
        if text.startswith("/-", i):
            depth += 1
            out.append("  ")
            i += 2
            continue
        if depth and text.startswith("-/", i):
            depth -= 1
            out.append("  ")
            i += 2
            continue
        if depth:
            out.append("\n" if text[i] == "\n" else " ")
        elif text.startswith("--", i):
            while i < len(text) and text[i] != "\n":
                out.append(" ")
                i += 1
            continue
        else:
            out.append(text[i])
        i += 1
    return "".join(out)


def declaration_windows(path: Path, repo_root: Path) -> list[dict[str, object]]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    text = strip_comments(raw)
    matches = list(DECL_RE.finditer(text))
    rows: list[dict[str, object]] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[start:end]
        if not any(term in block for term in AUDIT_TERMS):
            continue
        line = text.count("\n", 0, start) + 1
        end_line = text.count("\n", 0, end) + 1
        header = block.split(":=", 1)[0].strip()
        path_text = path.relative_to(repo_root).as_posix()
        selected = [term for term in SELECTED_TERMS if term in block]
        premises = [term for term in PREMISE_MARKERS if re.search(rf"\b{re.escape(term)}\b", block)]
        interfaces = [term for term in INTERFACE_MARKERS if term in block]
        conclusions = [term for term in CONCLUSION_MARKERS if term in block]
        if path_text.startswith("NavierStokesReview/src/completions/"):
            origin = "review_completion"
        elif path_text.startswith("NavierStokesReview/src/"):
            origin = "review_probe_or_extension"
        else:
            origin = "other_workspace_source"

        if "StageEstimates" in block or "interface_does_not" in block:
            scope = "interface_level"
        elif premises and ("False" in block or "≠" in block or "neq" in block):
            scope = "conditional_conclusion"
        elif "witnessDebt" in block or "Debt" in block and "selected_witness" in block:
            scope = "type_boundary_or_ghost_payload"
        elif "fixed_force" in block:
            scope = "fixed_force_path_dependence"
        elif origin == "review_completion":
            scope = "review_completion_identity"
        else:
            scope = "requires_manual_scope_review"

        rows.append(
            {
                "path": path_text,
                "line": line,
                "end_line": end_line,
                "kind": match.group("kind"),
                "name": match.group("name"),
                "origin": origin,
                "scope": scope,
                "selected_terms": selected,
                "premise_markers": premises,
                "interface_markers": interfaces,
                "conclusion_markers": conclusions,
                "header": " ".join(header.split()),
            }
        )
    return rows


def classify(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "declarations_reviewed": len(rows),
        "by_origin": dict(Counter(str(row["origin"]) for row in rows)),
        "by_scope": dict(Counter(str(row["scope"]) for row in rows)),
        "conditional_rows": sum(bool(row["premise_markers"]) for row in rows),
        "selected_rows": sum(bool(row["selected_terms"]) for row in rows),
        "strong_conclusion_rows": sum(bool(row["conclusion_markers"]) for row in rows),
        "unconditional_endpoint_claims": 0,
    }


def render(payload: dict[str, object]) -> str:
    counts = payload["counts"]
    lines = [
        "# Adversarial probe-contract audit",
        "",
        "This report audits the logical scope of auditor-authored Lean probes. It",
        "does not replace Lean compilation and does not infer mathematical truth",
        "from names or lexical co-occurrence.",
        "",
        "## Machine summary",
        "",
        f"- Declarations reviewed: **{counts['declarations_reviewed']}**",
        f"- Selected-term declarations: **{counts['selected_rows']}**",
        f"- Declarations with explicit premise markers: **{counts['conditional_rows']}**",
        f"- Declarations with strong-conclusion markers: **{counts['strong_conclusion_rows']}**",
        "- Unconditional endpoint claims authorised by this instrument: **0**",
        f"- Origins: `{counts['by_origin']}`",
        f"- Scope classes: `{counts['by_scope']}`",
        "",
        "## Contract rules",
        "",
        "1. A conditional theorem remains conditional until every premise is",
        "   derived from the selected construction.",
        "2. A ghost `Debt` or interface countermodel is not the selected field's",
        "   physical observable.",
        "3. A review completion is not OpenAI source evidence.",
        "4. A pointwise inequality is not a nonzero integrated moment.",
        "5. A finite-prefix identity is not an infinite-`tsum` identity without",
        "   convergence, interchange, and domain proofs.",
        "6. No declaration-level scan authorises `False`, `Delta m != 0`, or",
        "   formal refutation.",
        "",
        "## Declaration matrix",
        "",
        "| Origin | Scope | File | Lines | Declaration | Premises | Conclusion markers |",
        "|---|---|---|---:|---|---|---|",
    ]
    for row in payload["rows"]:
        lines.append(
            f"| {row['origin']} | {row['scope']} | `{row['path']}` | "
            f"{row['line']}-{row['end_line']} | `{row['name']}` | "
            f"{', '.join(row['premise_markers']) or 'none'} | "
            f"{', '.join(row['conclusion_markers']) or 'none'} |"
        )
    lines.extend(
        [
            "",
            "## Audit status",
            "",
            "This instrument is a blindside detector for the review apparatus. It",
            "does not assert that a hidden source theorem is absent. The selected",
            "field still requires a source-backed, compiled theorem for the exact",
            "Cartesian-to-radial composition and its five observables.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--source-root", type=Path, default=None)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()
    repo_root = args.repo_root.resolve()
    source_root = (args.source_root or repo_root / "NavierStokesReview" / "src").resolve()
    rows: list[dict[str, object]] = []
    for path in sorted(source_root.rglob("*.lean")):
        rows.extend(declaration_windows(path, repo_root))
    payload = {
        "instrument": "probe_logic_contract_audit",
        "status": "static logical-scope triage; not a theorem",
        "repo_root": repo_root.as_posix(),
        "source_root": source_root.as_posix(),
        "counts": classify(rows),
        "rows": rows,
    }
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.markdown.write_text(render(payload), encoding="utf-8")


if __name__ == "__main__":
    main()
