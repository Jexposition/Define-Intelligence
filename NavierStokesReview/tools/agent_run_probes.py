import os
import subprocess

def run_probes(probes_dir):
    """
    Finds all .lean probes and compiles them using the canonical elan/lake environment.
    """
    elan_path = r"C:\Users\Admin\.elan\bin\lake.exe"
    lean_path = r"C:\Users\Admin\.elan\bin\lean.exe"
    
    if not os.path.exists(probes_dir):
        print(f"Probes directory {probes_dir} not found.")
        return

    success_count = 0
    failure_count = 0
    
    for root, _, files in os.walk(probes_dir):
        for file in files:
            if file.endswith(".lean"):
                probe_path = os.path.join(root, file)
                print(f"Running probe: {probe_path}")
                
                cmd = [elan_path, "env", lean_path, probe_path]
                result = subprocess.run(cmd, capture_output=True, text=True)
                
                if result.returncode == 0:
                    print(f"[SUCCESS] {file} compiled mathematically sound without errors.\n")
                    success_count += 1
                else:
                    print(f"[FAILED] {file} failed to compile.")
                    print(result.stderr)
                    print("\n")
                    failure_count += 1
                    
    print(f"Probe Execution Complete. {success_count} succeeded, {failure_count} failed.")

if __name__ == "__main__":
    workspace_root = r"D:\Research Lab\Jexposition\Define Intelligence\Define-Intelligence-github"
    probes_directory = os.path.join(workspace_root, r"NavierStokesReview\src\probes")
    
    # Ensure script is run from the workspace root for Lake context
    os.chdir(workspace_root)
    run_probes(probes_directory)
