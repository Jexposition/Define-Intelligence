#!/usr/bin/env python3
"""Validate the review claim register against the current mapping evidence.

This validator checks only structural prerequisites: exact source names,
compiled endpoint routes, and evidence-file presence.  It deliberately does
not turn reachability into a mathematical correspondence theorem.  Open
semantic claims therefore remain visible in the generated report.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ALLOWED_STATUS = {"supported", "open", "conditional", "rejected", "retracted"}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_names(source_map: dict[str, Any]) -> set[str]:
    return {
        declaration["name"]
        for record in source_map.get("modules", {}).values()
        for declaration in record.get("declarations", [])
    }


def validate(repo: Path, claims: dict[str, Any], source_map: dict[str, Any], joined: dict[str, Any], bundle: dict[str, Any]) -> dict[str, Any]:
    failures: list[str] = []
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    available_sources = source_names(source_map)
    routes = joined.get("routes", {})

    if claims.get("schema") != "navier-stokes-review-claim-register/v1":
        failures.append("unsupported claim-register schema")
    if not bundle.get("validation", {}).get("passed", False):
        failures.append("the hardened audit bundle did not pass")

    for claim in claims.get("claims", []):
        claim_id = claim.get("id", "")
        if claim_id in seen:
            failures.append(f"duplicate claim id: {claim_id}")
        seen.add(claim_id)
        status = claim.get("status")
        if status not in ALLOWED_STATUS:
            failures.append(f"{claim_id}: unsupported status {status!r}")

        missing_sources = sorted(set(claim.get("required_source_names", [])) - available_sources)
        missing_routes = sorted(
            name for name in claim.get("required_routes", [])
            if not routes.get(name, {}).get("reachable", False)
        )
        missing_evidence = sorted(
            path for path in claim.get("evidence", [])
            if not (repo / path).is_file()
        )
        if missing_sources:
            failures.append(f"{claim_id}: missing source declarations: {', '.join(missing_sources)}")
        if missing_routes:
            failures.append(f"{claim_id}: missing compiled routes: {', '.join(missing_routes)}")
        if missing_evidence:
            failures.append(f"{claim_id}: missing evidence files: {', '.join(missing_evidence)}")
        rows.append({
            "id": claim_id,
            "title": claim.get("title", ""),
            "status": status,
            "level": claim.get("level", ""),
            "structural_prerequisites": {
                "source_names_present": not missing_sources,
                "compiled_routes_reachable": not missing_routes,
                "evidence_files_present": not missing_evidence,
            },
            "open_semantic_obligation": status in {"open", "conditional"},
            "interpretation": claim.get("interpretation", ""),
        })

    return {
        "schema": "navier-stokes-review-claim-register-report/v1",
        "validation": {"passed": not failures, "failures": failures},
        "claims": rows,
        "counts": {
            "claims": len(rows),
            "open_or_conditional": sum(row["open_semantic_obligation"] for row in rows),
            "structural_failures": len(failures),
        },
    }


def markdown(report: dict[str, Any]) -> str:
    validation = report["validation"]
    lines = [
        "# Review claim register",
        "",
        "This report validates structural prerequisites for review claims. It does not infer a mathematical theorem from a reachable declaration.",
        "",
        f"- Structural validation: **{'passed' if validation['passed'] else 'failed'}**",
        f"- Claims: `{report['counts']['claims']}`",
        f"- Open or conditional semantic claims: `{report['counts']['open_or_conditional']}`",
        "",
        "| ID | Level | Status | Source names | Compiled routes | Evidence files |",
        "|---|---|---|:---:|:---:|:---:|",
    ]
    for row in report["claims"]:
        checks = row["structural_prerequisites"]
        lines.append(
            f"| `{row['id']}` | `{row['level']}` | `{row['status']}` | "
            f"{'yes' if checks['source_names_present'] else 'no'} | "
            f"{'yes' if checks['compiled_routes_reachable'] else 'no'} | "
            f"{'yes' if checks['evidence_files_present'] else 'no'} |"
        )
    lines += ["", "## Interpretation", ""]
    for row in report["claims"]:
        lines += [f"### {row['id']}: {row['title']}", "", row["interpretation"], ""]
    if validation["failures"]:
        lines += ["## Failures", ""]
        lines.extend(f"- {failure}" for failure in validation["failures"])
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--claims", type=Path, required=True)
    parser.add_argument("--source-map", type=Path, required=True)
    parser.add_argument("--joined", type=Path, required=True)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()
    report = validate(
        args.repo.resolve(),
        load(args.claims.resolve()),
        load(args.source_map.resolve()),
        load(args.joined.resolve()),
        load(args.bundle.resolve()),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.markdown.write_text(markdown(report), encoding="utf-8")
    print(json.dumps(report["validation"], sort_keys=True))
    if not report["validation"]["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
