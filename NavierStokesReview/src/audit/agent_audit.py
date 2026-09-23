import os
import re

def audit_lean_files(directory):
    issues = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.lean'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Check for sorry
                    if 'sorry' in content:
                        issues.append(f"SORRY FOUND: {filepath}")
                        
                    # Check for Filter.bot
                    if re.search(r'\b(bot|⊥)\b', content) and 'Filter' in content:
                        issues.append(f"FILTER.BOT FOUND: {filepath}")
                        
    return issues

if __name__ == '__main__':
    target_dir = r"D:\Research Lab\Jexposition\Define Intelligence\Define-Intelligence-github\NavierStokes"
    results = audit_lean_files(target_dir)
    
    output_path = r"D:\Research Lab\Jexposition\Define Intelligence\Define-Intelligence-github\NavierStokesReview\evidence\agent_evidence_python_audit.md"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Python Audit Script Results\n\n")
        if results:
            for r in results:
                f.write(f"- {r}\n")
        else:
            f.write("No instances of 'sorry' or 'Filter.bot' found in the NavierStokes directory.\n")
