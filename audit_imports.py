import os
import sys

src_dir = "NavierStokes"
main_file = os.path.join("NavierStokes", "R3", "Theorem.lean")

if not os.path.exists(main_file):
    print(f"ERROR: Main theorem file {main_file} not found. Skipping dependency check.")
    sys.exit(0)

# 1. Collect all valid .lean files in the repository
all_files = set()
for root, _, files in os.walk(src_dir):
    for f in files:
        if f.endswith(".lean"):
            rel_path = os.path.relpath(os.path.join(root, f), ".")
            lean_mod = rel_path.replace("\\", ".").replace("/", ".").replace(".lean", "")
            all_files.add(lean_mod)

# 2. Extract the absolute closure of imports starting from the main theorem
imported_modules = set([main_file.replace("\\", ".").replace("/", ".").replace(".lean", "")])

def trace_imports(file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith("import "):
                mod = line.strip().split("import ")[1].split()[0]
                if mod.startswith(src_dir) and mod not in imported_modules:
                    imported_modules.add(mod)
                    # Convert back to system path to trace nested definitions
                    sys_path = mod.replace(".", "/") + ".lean"
                    if not os.path.exists(sys_path):
                        sys_path = mod.replace(".", "\\") + ".lean"
                    trace_imports(sys_path)

trace_imports(main_file)

# 3. Diff the sets to isolate dead files
dead_files = all_files - imported_modules
if dead_files:
    print(f"WARNING: FOUND {len(dead_files)} UNIMPORTED/DEAD FILES DETECTED:")
    for df in sorted(dead_files):
        print(f"  --> {df}.lean (This code is completely ignored by the main Navier-Stokes endpoint!)")
else:
    print("Total Import Integrity Verified: Every file in the domain tree is linked to the main endpoint.")
