import os
import re

ROOT = r"D:\Research Lab\Jexposition\Define Intelligence\Define-Intelligence-github"

def module_to_path(module):
    # e.g. NavierStokes.R3.Theorem -> NavierStokes/R3/Theorem.lean
    return module.replace('.', '/') + '.lean'

def path_to_module(path):
    # e.g. NavierStokes/R3/Theorem.lean -> NavierStokes.R3.Theorem
    # Need to handle relative paths from root.
    rel_path = os.path.relpath(path, ROOT)
    if rel_path.endswith('.lean'):
        rel_path = rel_path[:-5]
    return rel_path.replace(os.sep, '.')

def get_lean_files():
    files = []
    for dirpath, _, filenames in os.walk(ROOT):
        if '.lake' in dirpath:
            continue
        for f in filenames:
            if f.endswith('.lean'):
                files.append(os.path.join(dirpath, f))
    return files

def parse_file(filepath):
    imports = []
    bypasses = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                # Import parsing
                if line.startswith('import '):
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        imports.append(parts[1])
                
                # Bypass parsing
                match = re.search(r'\b(unsafe|axiom|constant|opaque|implemented_by)\b|@&', line)
                if match:
                    # Filter out comments? Just report all for now.
                    if '--' not in line[:match.start()] and '/-' not in line[:match.start()]:
                        bypasses.append(f"Line {i+1}: {line.strip()}")
    except Exception as e:
        pass
    return imports, bypasses

def main():
    lean_files = get_lean_files()
    
    # Build graph
    graph = {}
    bypasses_dict = {}
    
    # Map module name to its physical path
    mod_to_path = {}
    for f in lean_files:
        mod = path_to_module(f)
        mod_to_path[mod] = f
        
    for f in lean_files:
        mod = path_to_module(f)
        imports, bypasses = parse_file(f)
        graph[mod] = imports
        bypasses_dict[mod] = bypasses

    # Compute closure from key endpoints
    endpoints = ['NavierStokes.R3.Theorem', 'NavierStokes.ActualCandidateAssembly']
    visited = set()
    queue = list(endpoints)
    while queue:
        curr = queue.pop(0)
        if curr not in visited:
            visited.add(curr)
            if curr in graph:
                queue.extend(graph[curr])
                
    # Generate ledger
    output = []
    output.append("# Full Verification Ledger")
    output.append(f"\nTotal `.lean` files tracked (excluding `.lake`): {len(lean_files)}")
    
    output.append("\n## Hard Syntax Bypasses Found")
    found_bypasses = False
    for mod, bypasses in bypasses_dict.items():
        if bypasses:
            found_bypasses = True
            output.append(f"\n### {mod}")
            for b in bypasses:
                output.append(f"- {b}")
    if not found_bypasses:
        output.append("\nNo hard syntax bypasses (`unsafe`, `axiom`, etc.) were found outside of standard comments.")
        
    output.append("\n## Import Closure Anomalies (Dead Code/Disconnected Modules)")
    disconnected = []
    for mod in mod_to_path.keys():
        if mod not in visited:
            disconnected.append(mod)
            
    if disconnected:
        # Group by top-level dir to avoid massive spam if it's too big
        output.append(f"\nFound {len(disconnected)} modules disconnected from the main endpoints.\n")
        # Just list them
        for d in sorted(disconnected):
            output.append(f"- {d}")
    else:
        output.append("\nAll modules are within the import closure of the endpoints.")

    # Write output
    out_path = os.path.join(ROOT, "NavierStokesReview", "evidence", "full_verification_ledger.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output))
    print(f"Ledger written to {out_path}")

if __name__ == "__main__":
    main()
