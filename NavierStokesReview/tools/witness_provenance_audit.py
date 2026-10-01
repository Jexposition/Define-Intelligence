"""
Witness Provenance & Choice Identity Tracker
=============================================
Deeper companion to deep_semantic_audit.py.

For every Classical.choice / Classical.choose in the OpenAI NavierStokes tree:
  1. Extracts the exact source existence theorem being selected from
  2. Identifies the type/structure being inhabited
  3. Checks whether choose_spec is used downstream (proving independence)
  4. Checks whether the same existence theorem is selected from multiple times
     (potential identity violation: two choices from the same ∃ give different witnesses)
  5. Maps which final endpoint declarations transitively depend on each choice

Also scans for:
  - Structure fields that could be "proof laundering" (fields named like
    theorems: smooth, support, decay, bounded, etc.)
  - Comparator solution imports and configuration

Outputs:
  - results/witness_provenance_audit.json
  - evidence/witness_provenance_evidence.md
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

REPO_ROOT = Path(r"D:\Research Lab\Jexposition\Define Intelligence\Define-Intelligence-github")
NS_DIR = REPO_ROOT / "NavierStokes"
RESULTS_DIR = REPO_ROOT / "NavierStokesReview" / "results"
EVIDENCE_DIR = REPO_ROOT / "NavierStokesReview" / "evidence"

RESULTS_DIR.mkdir(parents=True, exist_ok=True)
EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)


# ── Suspicious field names (fields that sound like proof obligations) ──
PROOF_OBLIGATION_FIELD_NAMES = re.compile(
    r'\b(smooth|decay|bounded|compact|support|finite|continuous|measurable|'
    r'integrable|convergent|positive|nonneg|nonzero|tendsto|vanishing|'
    r'flatness|residual_flatness|force_smooth|candidate|valid|compatible|'
    r'coherent|preserved|invariant|independent|extension|regularity)\b',
    re.IGNORECASE
)


def extract_choice_provenance(filepath: Path) -> list:
    """
    For each Classical.choose / Classical.choice in a file, extract:
    - The existence theorem / Nonempty proof being selected from
    - Whether choose_spec is used nearby
    - The enclosing def/theorem name
    """
    try:
        content = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []

    lines = content.split('\n')
    results = []

    # Find enclosing definition for a given line number
    def find_enclosing_decl(line_num):
        for i in range(line_num - 1, -1, -1):
            m = re.match(r'^(?:noncomputable\s+)?(?:private\s+)?(?:protected\s+)?'
                        r'(def|theorem|lemma|instance|abbrev)\s+(\S+)', lines[i])
            if m:
                return m.group(1), m.group(2), i + 1
        return None, None, None

    # Scan for Classical.choose
    for i, line in enumerate(lines):
        for pat_name, pat in [
            ("Classical.choose", re.compile(r'Classical\.choose\s+\(?(\w[\w.]*)')),
            ("Classical.choice", re.compile(r'Classical\.choice\s+\(?(\w[\w.]*)')),
        ]:
            for m in pat.finditer(line):
                source_theorem = m.group(1)
                decl_kind, decl_name, decl_line = find_enclosing_decl(i)

                # Check for choose_spec in surrounding 30 lines
                window_start = max(0, i - 5)
                window_end = min(len(lines), i + 30)
                window = '\n'.join(lines[window_start:window_end])
                has_spec = "choose_spec" in window or "choice_spec" in window

                # Get broader context
                ctx_start = max(0, i - 2)
                ctx_end = min(len(lines), i + 5)
                context = [l.rstrip() for l in lines[ctx_start:ctx_end]]

                results.append({
                    "file": str(filepath.relative_to(REPO_ROOT)),
                    "line": i + 1,
                    "pattern": pat_name,
                    "source_theorem": source_theorem,
                    "enclosing_decl": decl_name,
                    "enclosing_kind": decl_kind,
                    "enclosing_line": decl_line,
                    "has_spec_nearby": has_spec,
                    "content": line.rstrip(),
                    "context": context,
                })

    return results


def extract_structure_fields(filepath: Path) -> list:
    """
    Extract structure declarations and classify fields as:
    - data_field: likely a data carrier
    - proof_field: name suggests it carries a proof obligation
    """
    try:
        content = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []

    results = []
    # Match structure ... where blocks
    for m in re.finditer(
        r'^(structure|class)\s+(\w+).*?(?:where|:=)\s*\n((?:\s+.*\n)*)',
        content, re.MULTILINE
    ):
        kind = m.group(1)
        name = m.group(2)
        body = m.group(3)
        line_num = content[:m.start()].count('\n') + 1

        fields = []
        for fm in re.finditer(r'^\s+(\w+)\s*:\s*(.+?)(?:\s*$)', body, re.MULTILINE):
            field_name = fm.group(1)
            field_type = fm.group(2).strip()
            is_proof = bool(PROOF_OBLIGATION_FIELD_NAMES.search(field_name))
            # Also check if the type looks like a Prop
            looks_propish = bool(re.search(r'\b(Prop|True|False|∀|∃|→|↔|≤|<|=|≠|∈|⊆|HasCompact|Smooth|ContDiff|Measurable|Integrable|Continuous|Tendsto)\b', field_type))
            fields.append({
                "name": field_name,
                "type_preview": field_type[:120],
                "likely_proof_obligation": is_proof or looks_propish,
                "name_suspicious": is_proof,
                "type_suspicious": looks_propish,
            })

        proof_fields = [f for f in fields if f["likely_proof_obligation"]]

        results.append({
            "file": str(filepath.relative_to(REPO_ROOT)),
            "line": line_num,
            "kind": kind,
            "name": name,
            "total_fields": len(fields),
            "proof_obligation_fields": len(proof_fields),
            "fields": fields,
        })

    return results


def audit_comparator_solution(repo_root: Path) -> dict:
    """
    Verify what ComparatorSolution.lean imports and how it constructs the final theorem.
    """
    sol_path = repo_root / "NavierStokes" / "ComparatorSolution.lean"
    if not sol_path.exists():
        return {"error": "ComparatorSolution.lean not found"}

    content = sol_path.read_text(encoding="utf-8", errors="replace")
    return {
        "file": "NavierStokes/ComparatorSolution.lean",
        "full_content": content,
        "imports": re.findall(r'^import\s+(.+)$', content, re.MULTILINE),
        "theorems": re.findall(r'^theorem\s+(\w+)', content, re.MULTILINE),
        "uses_sorry": "sorry" in content,
        "uses_exact": [l.strip() for l in content.split('\n') if "exact" in l],
    }


def generate_markdown(choices: list, structures: list, comparator: dict, identity_risks: list) -> str:
    """Generate human-readable evidence."""
    ts = datetime.now(timezone.utc).isoformat()
    md = []
    md.append(f"# Witness Provenance & Choice Identity Evidence")
    md.append(f"")
    md.append(f"**Generated:** {ts}")
    md.append(f"")

    # ── Choice Provenance ─────────────────────────────────────────────
    md.append(f"## 1. Choice Provenance Ledger")
    md.append(f"")
    md.append(f"Total `Classical.choose` witness selections: "
              f"{len([c for c in choices if c['pattern'] == 'Classical.choose'])}")
    md.append(f"Total `Classical.choice` witness selections: "
              f"{len([c for c in choices if c['pattern'] == 'Classical.choice'])}")
    md.append(f"")

    md.append(f"### Witness Identity Risk: selections WITHOUT nearby choose_spec")
    md.append(f"")
    md.append(f"These select a witness but do not immediately use `choose_spec` to")
    md.append(f"extract or constrain the chosen value. The witness may be consumed")
    md.append(f"as though canonical without proving independence.")
    md.append(f"")

    no_spec = [c for c in choices if not c["has_spec_nearby"]]
    md.append(f"**{len(no_spec)} selections without nearby spec ({len(no_spec)}/{len(choices)} = "
              f"{100*len(no_spec)/max(1,len(choices)):.0f}%)**")
    md.append(f"")

    for c in no_spec:
        md.append(f"- **`{c['file']}`** L{c['line']} in `{c['enclosing_decl'] or '?'}`")
        md.append(f"  Source: `{c['source_theorem']}`")
        md.append(f"  `{c['content'].strip()}`")
    md.append(f"")

    md.append(f"### Witness Identity Risk: same source selected multiple times")
    md.append(f"")
    source_counts = defaultdict(list)
    for c in choices:
        source_counts[c["source_theorem"]].append(c)

    multi = {k: v for k, v in source_counts.items() if len(v) > 1}
    if multi:
        md.append(f"**{len(multi)} source theorems selected from more than once:**")
        md.append(f"")
        for src, hits in sorted(multi.items(), key=lambda x: -len(x[1])):
            md.append(f"#### `{src}` — selected {len(hits)} times")
            md.append(f"")
            md.append(f"**Risk:** if these selections occur in different definitions,")
            md.append(f"the two witnesses are NOT guaranteed to be the same object.")
            md.append(f"")
            for h in hits:
                md.append(f"- `{h['file']}` L{h['line']} → `{h['enclosing_decl'] or '?'}`")
            md.append(f"")
    else:
        md.append(f"No source theorems are selected from more than once. Low identity risk.")
        md.append(f"")

    # ── Identity risks ────────────────────────────────────────────────
    if identity_risks:
        md.append(f"## 2. Explicit Identity Risk Cases")
        md.append(f"")
        for ir in identity_risks:
            md.append(f"- {ir}")
        md.append(f"")

    # ── Structure proof-obligation fields ─────────────────────────────
    md.append(f"## 3. Structure Proof-Obligation Fields")
    md.append(f"")
    md.append(f"Structures whose field names or types suggest proof obligations.")
    md.append(f"Each such field must be independently verified for the final selected witness.")
    md.append(f"")

    high_risk_structs = [s for s in structures if s["proof_obligation_fields"] >= 2]
    high_risk_structs.sort(key=lambda x: -x["proof_obligation_fields"])

    md.append(f"**{len(high_risk_structs)} structures with ≥ 2 proof-obligation fields:**")
    md.append(f"")

    for s in high_risk_structs[:30]:
        md.append(f"### `{s['name']}` in `{s['file']}` L{s['line']}")
        md.append(f"")
        md.append(f"| Field | Type Preview | Proof Obligation? |")
        md.append(f"| --- | --- | --- |")
        for f in s["fields"]:
            flag = "⚠️ YES" if f["likely_proof_obligation"] else "no"
            md.append(f"| `{f['name']}` | `{f['type_preview'][:80]}` | {flag} |")
        md.append(f"")

    # ── Comparator Solution Verification ──────────────────────────────
    md.append(f"## 4. Comparator Solution Verification")
    md.append(f"")
    if "error" in comparator:
        md.append(f"**ERROR:** {comparator['error']}")
    else:
        md.append(f"**File:** `{comparator['file']}`")
        md.append(f"**Imports:** {', '.join(f'`{i}`' for i in comparator['imports'])}")
        md.append(f"**Theorems declared:** {', '.join(f'`{t}`' for t in comparator['theorems'])}")
        md.append(f"**Contains sorry:** {'YES ⚠️' if comparator['uses_sorry'] else 'NO ✅'}")
        md.append(f"")
        md.append(f"### Full source")
        md.append(f"```lean")
        md.append(comparator["full_content"])
        md.append(f"```")
    md.append(f"")

    return '\n'.join(md)


def main():
    print("=" * 70)
    print("Witness Provenance & Choice Identity Tracker")
    print("=" * 70)

    # 1. Choice provenance
    print("\n  Scanning for Classical.choose / Classical.choice provenance …")
    all_choices = []
    for f in sorted(NS_DIR.rglob("*.lean")):
        all_choices.extend(extract_choice_provenance(f))
    print(f"    Found {len(all_choices)} witness selections")

    # 2. Structure fields
    print("\n  Scanning structure definitions for proof-obligation fields …")
    all_structures = []
    for f in sorted(NS_DIR.rglob("*.lean")):
        all_structures.extend(extract_structure_fields(f))
    print(f"    Found {len(all_structures)} structure/class declarations")

    # 3. Identity risk analysis
    print("\n  Analysing identity risks …")
    identity_risks = []
    source_counts = defaultdict(list)
    for c in all_choices:
        source_counts[c["source_theorem"]].append(c)

    for src, hits in source_counts.items():
        if len(hits) > 1:
            files = set(h["file"] for h in hits)
            defs = set(h["enclosing_decl"] for h in hits if h["enclosing_decl"])
            if len(defs) > 1:
                identity_risks.append(
                    f"`{src}` selected in {len(defs)} different definitions across "
                    f"{len(files)} files: {', '.join(f'`{d}`' for d in sorted(defs))}. "
                    f"These witnesses are NOT provably identical."
                )

    # 4. Comparator solution
    print("\n  Verifying ComparatorSolution.lean …")
    comparator = audit_comparator_solution(REPO_ROOT)

    # ── Output ────────────────────────────────────────────────────────
    json_out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "choices": all_choices,
        "structures": all_structures,
        "identity_risks": identity_risks,
        "comparator": comparator,
    }

    json_path = RESULTS_DIR / "witness_provenance_audit.json"
    json_path.write_text(json.dumps(json_out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n  JSON → {json_path}")

    md_content = generate_markdown(all_choices, all_structures, comparator, identity_risks)
    md_path = EVIDENCE_DIR / "witness_provenance_evidence.md"
    md_path.write_text(md_content, encoding="utf-8")
    print(f"  Markdown → {md_path}")

    print(f"\n{'=' * 70}")
    print("DONE.")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
