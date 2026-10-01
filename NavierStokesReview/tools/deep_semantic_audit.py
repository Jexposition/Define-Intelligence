"""
Deep Semantic Audit of OpenAI Navier-Stokes Repository
=======================================================
Scans the OpenAI Lean source tree for:
  1. Kernel trust-escape keywords (sorry, unsafe, native_decide, etc.)
  2. Classical.choose / Classical.choice witness selection
  3. Fallback totalization patterns (if h then X else 0)
  4. Structure definitions and their fields (semantic laundering boundaries)
  5. Noncomputable defs with witness/choice patterns
  6. Custom metaprogramming (syntax, macro, elab, etc.)
  7. Function.extend / arbitrary extension
  8. Build file audit (lakefile, lake-manifest, git deps)
  9. Comparator configuration verification

Outputs:
  - results/deep_semantic_audit.json   (machine-readable)
  - evidence/deep_semantic_audit_evidence.md  (human-readable)
"""

import os
import re
import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

# ── Paths ──────────────────────────────────────────────────────────────
REPO_ROOT = Path(r"D:\Research Lab\Jexposition\Define Intelligence\Define-Intelligence-github")
NS_DIR = REPO_ROOT / "NavierStokes"
EULER_DIR = REPO_ROOT / "Euler"
CHALLENGE_DIR = REPO_ROOT / "ComparatorChallenges"
REVIEW_DIR = REPO_ROOT / "NavierStokesReview"
RESULTS_DIR = REVIEW_DIR / "results"
EVIDENCE_DIR = REVIEW_DIR / "evidence"

RESULTS_DIR.mkdir(parents=True, exist_ok=True)
EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

# ── 1. Trust-escape keyword patterns ──────────────────────────────────
TRUST_ESCAPE_PATTERNS = {
    "sorry": re.compile(r'\bsorry\b'),
    "sorryAx": re.compile(r'\bsorryAx\b'),
    "unsafe_def": re.compile(r'\bunsafe\s+def\b'),
    "unsafe_theorem": re.compile(r'\bunsafe\s+theorem\b'),
    "unsafe_abbrev": re.compile(r'\bunsafe\s+abbrev\b'),
    "partial_def": re.compile(r'\bpartial\s+def\b'),
    "partial_theorem": re.compile(r'\bpartial\s+theorem\b'),
    "opaque_decl": re.compile(r'^opaque\s+', re.MULTILINE),
    "implemented_by": re.compile(r'@\[implemented_by'),
    "extern_attr": re.compile(r'@\[extern'),
    "trusted_attr": re.compile(r'@\[trusted'),
    "run_tac": re.compile(r'\brun_tac\b'),
    "native_decide": re.compile(r'\bnative_decide\b'),
    "decide_native": re.compile(r'\bdecide\s*\+\s*native\b'),
    "ofReduceBool": re.compile(r'\bLean\.ofReduceBool\b'),
    "ofReduceNat": re.compile(r'\bLean\.ofReduceNat\b'),
    "custom_axiom": re.compile(r'^axiom\s+\w', re.MULTILINE),
}

# ── 2. Semantic risk patterns ─────────────────────────────────────────
SEMANTIC_PATTERNS = {
    "Classical.choose": re.compile(r'Classical\.choose\b'),
    "Classical.choose_spec": re.compile(r'Classical\.choose_spec\b'),
    "Classical.choice": re.compile(r'Classical\.choice\b'),
    "Exists.choose": re.compile(r'Exists\.choose\b'),
    "Exists.choose_spec": re.compile(r'Exists\.choose_spec\b'),
    "Classical.epsilon": re.compile(r'Classical\.epsilon\b'),
    "Nonempty.some": re.compile(r'Nonempty\.some\b'),
    "Function.extend": re.compile(r'Function\.extend\b'),
    "Subsingleton.elim": re.compile(r'Subsingleton\.elim\b'),
    "Filter.bot": re.compile(r'Filter\.bot\b'),
    # Fallback totalization: if h : P then X else 0
    "fallback_else_0": re.compile(r'if\s+\w+\s*:.*then.*else\s+0\b'),
    # dite usage
    "dite": re.compile(r'\bdite\b'),
    # autoImplicit (accidental free-variable generalization)
    "autoImplicit_true": re.compile(r'set_option\s+autoImplicit\s+true'),
}

# ── 3. Structure / metaprogramming / notation patterns ────────────────
STRUCTURE_PATTERNS = {
    "structure_decl": re.compile(r'^structure\s+(\w+)', re.MULTILINE),
    "class_decl": re.compile(r'^class\s+(\w+)', re.MULTILINE),
    "syntax_decl": re.compile(r'^syntax\b', re.MULTILINE),
    "macro_decl": re.compile(r'^macro\s', re.MULTILINE),
    "elab_decl": re.compile(r'^elab\s', re.MULTILINE),
    "elab_rules_decl": re.compile(r'^elab_rules\b', re.MULTILINE),
    "macro_rules_decl": re.compile(r'^macro_rules\b', re.MULTILINE),
    "register_option": re.compile(r'\bregister_option\b'),
    "scoped_notation": re.compile(r'\bscoped\s+notation\b'),
    "local_notation": re.compile(r'\blocal\s+notation\b'),
    "custom_Coe": re.compile(r'\binstance\b.*\bCoe\b'),
    "custom_CoeFun": re.compile(r'\binstance\b.*\bCoeFun\b'),
    "simp_attr": re.compile(r'@\[simp\b'),
    "Fact_typeclass": re.compile(r'\bFact\s*\('),
    "letI": re.compile(r'\bletI\b'),
    "haveI": re.compile(r'\bhaveI\b'),
    "abbrev_decl": re.compile(r'^(?:noncomputable\s+)?abbrev\s+(\w+)', re.MULTILINE),
}

# ── 4. Noncomputable classification ──────────────────────────────────
NONCOMPUTABLE_PATTERNS = {
    "noncomputable_def": re.compile(r'noncomputable\s+def\s+(\w+)'),
    "noncomputable_instance": re.compile(r'noncomputable\s+instance\b'),
    "noncomputable_section": re.compile(r'noncomputable\s+section\b'),
}


def scan_file(filepath: Path) -> dict:
    """Scan a single .lean file for all patterns, returning structured hits."""
    try:
        content = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return {"error": str(e)}

    lines = content.split('\n')

    # Mask Lean line/block comments while preserving line boundaries.  The
    # earlier line-prefix test treated words inside `/- ... -/` documentation
    # as declarations, which made the trust scan over-report challenge sorries.
    masked_chars = []
    block_depth = 0
    i = 0
    while i < len(content):
        if block_depth:
            if content.startswith('/-', i):
                block_depth += 1
                masked_chars.extend('  ')
                i += 2
            elif content.startswith('-/', i):
                block_depth -= 1
                masked_chars.extend('  ')
                i += 2
            else:
                ch = content[i]
                masked_chars.append('\n' if ch == '\n' else ' ')
                i += 1
        elif content.startswith('--', i):
            while i < len(content) and content[i] != '\n':
                masked_chars.append(' ')
                i += 1
        elif content.startswith('/-', i):
            block_depth = 1
            masked_chars.extend('  ')
            i += 2
        else:
            masked_chars.append(content[i])
            i += 1
    masked_lines = ''.join(masked_chars).split('\n')
    result = {
        "file": str(filepath.relative_to(REPO_ROOT)),
        "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
        "line_count": len(lines),
        "byte_count": len(content.encode("utf-8")),
        "trust_escapes": [],
        "semantic_risks": [],
        "structures": [],
        "metaprogramming": [],
        "noncomputable": [],
    }

    # Helper: find hits with context
    def find_hits(patterns_dict, category_key):
        for name, pat in patterns_dict.items():
            for i, line in enumerate(lines, 1):
                search_line = masked_lines[i - 1]
                is_comment = not search_line.strip()
                if pat.search(search_line):
                    ctx_start = max(0, i - 3)
                    ctx_end = min(len(lines), i + 2)
                    context_lines = lines[ctx_start:ctx_end]
                    result[category_key].append({
                        "pattern": name,
                        "line": i,
                        "content": line.rstrip(),
                        "in_comment": is_comment,
                        "context": [l.rstrip() for l in context_lines],
                    })

    find_hits(TRUST_ESCAPE_PATTERNS, "trust_escapes")
    find_hits(SEMANTIC_PATTERNS, "semantic_risks")

    # Structure definitions with fields
    for m in re.finditer(r'^structure\s+(\w+).*?where\s*\n((?:\s+.*\n)*)', content, re.MULTILINE):
        name = m.group(1)
        body = m.group(2)
        fields = []
        for fm in re.finditer(r'^\s+(\w+)\s*:', body, re.MULTILINE):
            fields.append(fm.group(1))
        line_num = content[:m.start()].count('\n') + 1
        result["structures"].append({
            "name": name,
            "line": line_num,
            "fields": fields,
            "field_count": len(fields),
        })

    # Metaprogramming and notation
    find_hits(STRUCTURE_PATTERNS, "metaprogramming")

    # Noncomputable defs with classification
    for name, pat in NONCOMPUTABLE_PATTERNS.items():
        for m in pat.finditer(content):
            line_num = content[:m.start()].count('\n') + 1
            # Get context for classification
            line_content = lines[line_num - 1] if line_num <= len(lines) else ""
            # Look at next few lines for choice/fallback patterns
            downstream = '\n'.join(lines[line_num - 1:min(line_num + 5, len(lines))])
            classification = "analytic"  # default
            if "Classical.choice" in downstream:
                classification = "existential_witness_selection"
            elif "Classical.choose" in downstream:
                classification = "existential_witness_selection"
            elif re.search(r'if\s+\w+\s*:.*then.*else\s+0', downstream):
                classification = "conditional_fallback"
            elif "Function.extend" in downstream:
                classification = "arbitrary_extension"
            elif "sInf" in downstream or "sSup" in downstream:
                classification = "suprema_infima_selection"
            elif "choose_spec" in downstream:
                classification = "choice_with_spec"

            result["noncomputable"].append({
                "pattern": name,
                "line": line_num,
                "def_name": m.group(1) if m.lastindex and m.lastindex >= 1 else "(section/instance)",
                "content": line_content.rstrip(),
                "classification": classification,
                "downstream_snippet": downstream[:300],
            })

    return result


def scan_build_files() -> dict:
    """Audit build configuration files."""
    build_audit = {
        "lakefile": None,
        "lake_manifest": None,
        "lean_toolchain": None,
        "comparator_configs": [],
    }

    # lakefile.lean or lakefile.toml
    for name in ["lakefile.lean", "lakefile.toml"]:
        p = REPO_ROOT / name
        if p.exists():
            content = p.read_text(encoding="utf-8", errors="replace")
            build_audit["lakefile"] = {
                "file": name,
                "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
                "content": content[:5000],  # first 5KB
            }

    # lake-manifest.json
    manifest = REPO_ROOT / "lake-manifest.json"
    if manifest.exists():
        content = manifest.read_text(encoding="utf-8", errors="replace")
        build_audit["lake_manifest"] = {
            "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
            "content_preview": content[:3000],
        }
        try:
            mdata = json.loads(content)
            if "packages" in mdata:
                build_audit["lake_manifest"]["packages"] = [
                    {
                        "name": p.get("name", "?"),
                        "type": p.get("type", "?"),
                        "url": p.get("url", p.get("path", "?")),
                        "rev": p.get("rev", "?"),
                    }
                    for p in mdata["packages"]
                ]
        except json.JSONDecodeError:
            pass

    # lean-toolchain
    tc = REPO_ROOT / "lean-toolchain"
    if tc.exists():
        build_audit["lean_toolchain"] = tc.read_text(encoding="utf-8").strip()

    # Comparator JSON configs
    for jf in CHALLENGE_DIR.glob("*.json"):
        content = jf.read_text(encoding="utf-8", errors="replace")
        build_audit["comparator_configs"].append({
            "file": jf.name,
            "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
            "content": content,
        })

    return build_audit


def count_noncomputable_sections(directory: Path) -> int:
    """Count noncomputable section declarations across a directory."""
    count = 0
    for f in directory.rglob("*.lean"):
        try:
            content = f.read_text(encoding="utf-8", errors="replace")
            count += len(re.findall(r'noncomputable\s+section', content))
        except Exception:
            pass
    return count


def generate_markdown_report(all_results: list, build_audit: dict, stats: dict) -> str:
    """Generate human-readable Markdown evidence report."""
    timestamp = datetime.now(timezone.utc).isoformat()
    md = []
    md.append(f"# Deep Semantic Audit Evidence — OpenAI Navier-Stokes Repository")
    md.append(f"")
    md.append(f"**Generated:** {timestamp}")
    md.append(f"**Scope:** `NavierStokes/`, `Euler/`, `ComparatorChallenges/`")
    md.append(f"**Script:** `NavierStokesReview/tools/deep_semantic_audit.py`")
    md.append(f"")

    # ── Summary statistics ────────────────────────────────────────────
    md.append(f"## Summary Statistics")
    md.append(f"")
    md.append(f"| Metric | Count |")
    md.append(f"| --- | ---: |")
    for k, v in stats.items():
        md.append(f"| {k} | {v} |")
    md.append(f"")

    # ── 1. Trust Escapes ──────────────────────────────────────────────
    md.append(f"## 1. Kernel Trust-Escape Scan")
    md.append(f"")
    trust_hits = []
    for r in all_results:
        for h in r.get("trust_escapes", []):
            if not h["in_comment"]:
                trust_hits.append((r["file"], h))

    if not trust_hits:
        md.append(f"**RESULT: No non-comment trust-escape keywords found in NavierStokes/ or Euler/.**")
        md.append(f"")
    else:
        md.append(f"**WARNING: {len(trust_hits)} trust-escape hits found (excluding comments):**")
        md.append(f"")
        for fpath, h in trust_hits:
            md.append(f"### `{h['pattern']}` in `{fpath}` line {h['line']}")
            md.append(f"```lean")
            for cl in h["context"]:
                md.append(cl)
            md.append(f"```")
            md.append(f"")

    # ComparatorChallenges sorry (expected)
    challenge_sorries = [
        (r["file"], h) for r in all_results
        for h in r.get("trust_escapes", [])
        if h["pattern"] == "sorry" and "ComparatorChallenges" in r["file"]
    ]
    if challenge_sorries:
        md.append(f"### ComparatorChallenges `sorry` (expected by design)")
        md.append(f"")
        md.append(f"{len(challenge_sorries)} `sorry` occurrences in ComparatorChallenges/ — these are intentional challenge placeholders per Comparator protocol.")
        md.append(f"")
        for fpath, h in challenge_sorries:
            md.append(f"- `{fpath}` line {h['line']}: `{h['content'].strip()}`")
        md.append(f"")

    # ── 2. Classical.choose / Classical.choice Provenance ─────────────
    md.append(f"## 2. Witness Selection Provenance (Classical.choose / Classical.choice)")
    md.append(f"")

    choose_hits = []
    choice_hits = []
    for r in all_results:
        for h in r.get("semantic_risks", []):
            if h["pattern"] == "Classical.choose" and not h["in_comment"]:
                choose_hits.append((r["file"], h))
            elif h["pattern"] == "Classical.choice" and not h["in_comment"]:
                choice_hits.append((r["file"], h))

    md.append(f"| Category | Count |")
    md.append(f"| --- | ---: |")
    md.append(f"| `Classical.choose` occurrences | {len(choose_hits)} |")
    md.append(f"| `Classical.choice` occurrences | {len(choice_hits)} |")
    md.append(f"")

    md.append(f"### Classical.choice witness selections (HIGH PRIORITY)")
    md.append(f"")
    md.append(f"Each `Classical.choice` selects an arbitrary inhabitant of a `Nonempty` type.")
    md.append(f"Audit question: is the selected witness later proved independent of the choice,")
    md.append(f"or is it consumed as though canonical?")
    md.append(f"")

    for fpath, h in choice_hits[:50]:  # Cap output
        md.append(f"- **`{fpath}`** L{h['line']}: `{h['content'].strip()}`")
    md.append(f"")

    md.append(f"### Classical.choose witness selections")
    md.append(f"")
    # Group by file
    choose_by_file = defaultdict(list)
    for fpath, h in choose_hits:
        choose_by_file[fpath].append(h)

    for fpath, hits in sorted(choose_by_file.items()):
        md.append(f"#### `{fpath}` ({len(hits)} occurrences)")
        for h in hits:
            md.append(f"- L{h['line']}: `{h['content'].strip()}`")
        md.append(f"")

    # ── 3. Fallback Totalization ──────────────────────────────────────
    md.append(f"## 3. Fallback Totalization Patterns")
    md.append(f"")
    md.append(f"Definitions of the form `if h : P then intendedObject else 0`.")
    md.append(f"Each must be audited: is the intended branch always selected on the proof path?")
    md.append(f"")

    fallback_hits = []
    for r in all_results:
        for h in r.get("semantic_risks", []):
            if h["pattern"] == "fallback_else_0" and not h["in_comment"]:
                fallback_hits.append((r["file"], h))

    md.append(f"**Total fallback-to-zero patterns found: {len(fallback_hits)}**")
    md.append(f"")

    for fpath, h in fallback_hits:
        md.append(f"### `{fpath}` line {h['line']}")
        md.append(f"```lean")
        for cl in h["context"]:
            md.append(cl)
        md.append(f"```")
        md.append(f"**Audit obligation:** Locate the theorem proving `h` holds for every point consumed by the final endpoint.")
        md.append(f"")

    # ── 4. Noncomputable Classification ───────────────────────────────
    md.append(f"## 4. Noncomputable Definition Classification")
    md.append(f"")

    nc_by_class = defaultdict(list)
    for r in all_results:
        for h in r.get("noncomputable", []):
            if h["pattern"] == "noncomputable_def":
                nc_by_class[h["classification"]].append((r["file"], h))

    md.append(f"| Classification | Count | Audit Priority |")
    md.append(f"| --- | ---: | --- |")
    priority_map = {
        "existential_witness_selection": "HIGH",
        "conditional_fallback": "VERY HIGH",
        "arbitrary_extension": "VERY HIGH",
        "suprema_infima_selection": "MEDIUM-HIGH",
        "choice_with_spec": "MEDIUM (lower if spec checked)",
        "analytic": "LOW",
    }
    for cls in ["conditional_fallback", "existential_witness_selection", "arbitrary_extension",
                "suprema_infima_selection", "choice_with_spec", "analytic"]:
        items = nc_by_class.get(cls, [])
        pri = priority_map.get(cls, "?")
        md.append(f"| {cls} | {len(items)} | {pri} |")
    md.append(f"")

    # Detail high-priority ones
    for cls in ["conditional_fallback", "existential_witness_selection", "arbitrary_extension"]:
        items = nc_by_class.get(cls, [])
        if items:
            md.append(f"### {cls} ({len(items)} defs)")
            md.append(f"")
            for fpath, h in items[:30]:
                md.append(f"- **`{fpath}`** L{h['line']} `{h['def_name']}`: `{h['content'].strip()}`")
            if len(items) > 30:
                md.append(f"- … and {len(items) - 30} more")
            md.append(f"")

    # ── 5. Structure Definitions (Semantic Laundering Boundaries) ─────
    md.append(f"## 5. Structure Definitions")
    md.append(f"")
    md.append(f"Structures can act as semantic laundering boundaries: a field stored")
    md.append(f"as a constructor parameter may never be independently proved for the")
    md.append(f"final selected witness.")
    md.append(f"")

    all_structures = []
    for r in all_results:
        for s in r.get("structures", []):
            all_structures.append((r["file"], s))

    md.append(f"**Total structure declarations: {len(all_structures)}**")
    md.append(f"")

    # Show structures with many fields (most likely to hide obligations)
    big_structures = [(f, s) for f, s in all_structures if s["field_count"] >= 3]
    big_structures.sort(key=lambda x: -x[1]["field_count"])

    md.append(f"### Structures with ≥ 3 fields ({len(big_structures)} total, showing top 40)")
    md.append(f"")
    md.append(f"| File | Structure | Fields | Field Names |")
    md.append(f"| --- | --- | ---: | --- |")
    for fpath, s in big_structures[:40]:
        fields_str = ", ".join(s["fields"][:8])
        if len(s["fields"]) > 8:
            fields_str += f" … (+{len(s['fields']) - 8})"
        md.append(f"| `{fpath}` | `{s['name']}` | {s['field_count']} | {fields_str} |")
    md.append(f"")

    # ── 6. Metaprogramming ────────────────────────────────────────────
    md.append(f"## 6. Custom Metaprogramming and Notation")
    md.append(f"")

    meta_hits = defaultdict(list)
    for r in all_results:
        for h in r.get("metaprogramming", []):
            if not h["in_comment"]:
                meta_hits[h["pattern"]].append((r["file"], h))

    if not any(meta_hits.get(k) for k in ["syntax_decl", "macro_decl", "elab_decl",
                                           "elab_rules_decl", "macro_rules_decl"]):
        md.append(f"**No custom syntax/macro/elab declarations found.** This is positive evidence.")
        md.append(f"")
    else:
        for pat in ["syntax_decl", "macro_decl", "elab_decl", "elab_rules_decl", "macro_rules_decl"]:
            hits = meta_hits.get(pat, [])
            if hits:
                md.append(f"### `{pat}` ({len(hits)} occurrences)")
                for fpath, h in hits:
                    md.append(f"- `{fpath}` L{h['line']}: `{h['content'].strip()}`")
                md.append(f"")

    # letI / haveI
    leti_count = sum(len(meta_hits.get(k, [])) for k in ["letI", "haveI"])
    md.append(f"**`letI`/`haveI` instance overrides:** {leti_count} (review for hidden typeclass manipulation)")
    md.append(f"")

    # @[simp]
    simp_count = len(meta_hits.get("simp_attr", []))
    md.append(f"**`@[simp]` lemma registrations:** {simp_count}")
    md.append(f"")

    # abbrev
    abbrev_hits = meta_hits.get("abbrev_decl", [])
    md.append(f"**`abbrev` declarations:** {len(abbrev_hits)} (abbreviations are definitionally transparent)")
    md.append(f"")

    # ── 7. Build File Audit ───────────────────────────────────────────
    md.append(f"## 7. Build Configuration Audit")
    md.append(f"")

    if build_audit.get("lean_toolchain"):
        md.append(f"**Lean toolchain:** `{build_audit['lean_toolchain']}`")
        md.append(f"")

    if build_audit.get("lakefile"):
        lf = build_audit["lakefile"]
        md.append(f"### `{lf['file']}` (SHA256: `{lf['sha256'][:16]}…`)")
        md.append(f"```")
        md.append(lf["content"][:3000])
        md.append(f"```")
        md.append(f"")

    if build_audit.get("lake_manifest") and "packages" in build_audit["lake_manifest"]:
        md.append(f"### Dependencies (lake-manifest.json)")
        md.append(f"")
        md.append(f"| Package | Type | URL/Path | Rev |")
        md.append(f"| --- | --- | --- | --- |")
        for p in build_audit["lake_manifest"]["packages"]:
            rev_short = str(p["rev"])[:12] if p["rev"] != "?" else "?"
            md.append(f"| `{p['name']}` | {p['type']} | `{p['url']}` | `{rev_short}…` |")
        md.append(f"")

    if build_audit.get("comparator_configs"):
        md.append(f"### Comparator Configurations")
        md.append(f"")
        for cfg in build_audit["comparator_configs"]:
            md.append(f"#### `{cfg['file']}`")
            md.append(f"```json")
            md.append(cfg["content"])
            md.append(f"```")
            md.append(f"")

    # ── 8. Function.extend ────────────────────────────────────────────
    md.append(f"## 8. Function.extend / Arbitrary Extension Patterns")
    md.append(f"")

    extend_hits = []
    for r in all_results:
        for h in r.get("semantic_risks", []):
            if h["pattern"] == "Function.extend" and not h["in_comment"]:
                extend_hits.append((r["file"], h))

    if not extend_hits:
        md.append(f"**No `Function.extend` usage found.** Low risk for arbitrary-extension hiding.")
        md.append(f"")
    else:
        md.append(f"**{len(extend_hits)} `Function.extend` occurrences:**")
        md.append(f"")
        for fpath, h in extend_hits:
            md.append(f"- `{fpath}` L{h['line']}: `{h['content'].strip()}`")
            md.append(f"  ```lean")
            for cl in h["context"]:
                md.append(f"  {cl}")
            md.append(f"  ```")
        md.append(f"")

    # ── 9. Filter.bot (vacuity risk) ──────────────────────────────────
    md.append(f"## 9. Filter.bot Occurrences (Vacuity Risk)")
    md.append(f"")

    bot_hits = []
    for r in all_results:
        for h in r.get("semantic_risks", []):
            if h["pattern"] == "Filter.bot" and not h["in_comment"]:
                bot_hits.append((r["file"], h))

    md.append(f"**{len(bot_hits)} `Filter.bot` references (each could make a limit statement vacuous)**")
    md.append(f"")
    for fpath, h in bot_hits[:20]:
        md.append(f"- `{fpath}` L{h['line']}: `{h['content'].strip()}`")
    md.append(f"")

    # ── Conclusion ────────────────────────────────────────────────────
    md.append(f"## Conclusion")
    md.append(f"")
    md.append(f"This scan is a regex-level pre-audit. It identifies locations for deeper")
    md.append(f"semantic inspection but cannot distinguish benign from load-bearing uses.")
    md.append(f"Each high-priority item requires manual or Lean-level verification that:")
    md.append(f"")
    md.append(f"1. Every `Classical.choice`/`choose` witness is either proved independent")
    md.append(f"   of the selection or consumed with the correct identity.")
    md.append(f"2. Every fallback-to-zero definition has its good branch selected on the")
    md.append(f"   complete endpoint path.")
    md.append(f"3. Every structure field is independently proved (not just stored as a")
    md.append(f"   constructor parameter) for the final selected witness.")
    md.append(f"4. No build-level plugin, generated file, or patched dependency injects")
    md.append(f"   trust outside the audited source.")
    md.append(f"")

    return '\n'.join(md)


def main():
    print("=" * 70)
    print("Deep Semantic Audit — OpenAI Navier-Stokes Repository")
    print("=" * 70)

    # Collect all .lean files
    scan_dirs = [
        ("NavierStokes", NS_DIR),
        ("Euler", EULER_DIR),
        ("ComparatorChallenges", CHALLENGE_DIR),
    ]

    all_results = []
    total_files = 0
    total_lines = 0
    total_bytes = 0

    for label, directory in scan_dirs:
        if not directory.exists():
            print(f"  SKIP: {directory} does not exist")
            continue
        lean_files = sorted(directory.rglob("*.lean"))
        print(f"\n  Scanning {label}/: {len(lean_files)} .lean files …")
        for f in lean_files:
            r = scan_file(f)
            all_results.append(r)
            total_files += 1
            total_lines += r.get("line_count", 0)
            total_bytes += r.get("byte_count", 0)

    # Build file audit
    print("\n  Auditing build files …")
    build_audit = scan_build_files()

    # Compute statistics
    nc_section_count = 0
    for _, d in scan_dirs:
        if d.exists():
            nc_section_count += count_noncomputable_sections(d)

    trust_total = sum(
        len([h for h in r.get("trust_escapes", []) if not h["in_comment"]])
        for r in all_results
    )
    trust_in_ns = sum(
        len([h for h in r.get("trust_escapes", []) if not h["in_comment"]])
        for r in all_results if "NavierStokes" in r.get("file", "") and "ComparatorChallenges" not in r.get("file", "")
    )
    choose_total = sum(
        len([h for h in r.get("semantic_risks", [])
             if h["pattern"] in ("Classical.choose",) and not h["in_comment"]])
        for r in all_results
    )
    choice_total = sum(
        len([h for h in r.get("semantic_risks", [])
             if h["pattern"] in ("Classical.choice",) and not h["in_comment"]])
        for r in all_results
    )
    fallback_total = sum(
        len([h for h in r.get("semantic_risks", [])
             if h["pattern"] == "fallback_else_0" and not h["in_comment"]])
        for r in all_results
    )
    structure_total = sum(len(r.get("structures", [])) for r in all_results)
    nc_def_total = sum(
        len([h for h in r.get("noncomputable", []) if h["pattern"] == "noncomputable_def"])
        for r in all_results
    )

    stats = {
        "Total .lean files scanned": total_files,
        "Total lines of Lean": total_lines,
        "Total bytes": total_bytes,
        "Trust-escape hits (non-comment, all dirs)": trust_total,
        "Trust-escape hits (NavierStokes/ only)": trust_in_ns,
        "`Classical.choose` occurrences": choose_total,
        "`Classical.choice` occurrences": choice_total,
        "Fallback-to-zero patterns": fallback_total,
        "Structure declarations": structure_total,
        "`noncomputable def` declarations": nc_def_total,
        "`noncomputable section` declarations": nc_section_count,
    }

    print(f"\n  Statistics:")
    for k, v in stats.items():
        print(f"    {k}: {v}")

    # ── Write JSON evidence ──────────────────────────────────────────
    json_path = RESULTS_DIR / "deep_semantic_audit.json"
    output = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "statistics": stats,
        "build_audit": build_audit,
        "file_results": all_results,
    }
    json_path.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n  JSON evidence → {json_path}")

    # ── Write Markdown evidence ──────────────────────────────────────
    md_content = generate_markdown_report(all_results, build_audit, stats)
    md_path = EVIDENCE_DIR / "deep_semantic_audit_evidence.md"
    md_path.write_text(md_content, encoding="utf-8")
    print(f"  Markdown evidence → {md_path}")

    print(f"\n{'=' * 70}")
    print(f"DONE. Review the evidence files for detailed findings.")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
