$ErrorActionPreference = "Stop"

$BUILD_DIR = ".lake\build"
$SRC_DIR = "NavierStokes"
$REVIEW_DIR = "NavierStokesReview"

Write-Host "======================================================================"
Write-Host "LEAN 4 COMPILER OVERRIDE & BUILD ARTIFACT AUDIT TRACKER"
Write-Host "======================================================================"

if (-not (Test-Path $BUILD_DIR)) {
    Write-Host "Build directory not found. Running 'lake build' to generate artifacts..."
    & $env:USERPROFILE\.elan\bin\lake build
}

Write-Host "`n[STEP 1/4] Scanning Source & Build Metadata for Hidden Axioms/Constants..."
Write-Host "Checking for unsafe declarations..."
$unsafe = Select-String -Path "$SRC_DIR\*.lean", "$SRC_DIR\*\*.lean" -Pattern "axiom", "constant", "opaque", "unsafe" -List
if ($unsafe) {
    Write-Host "ALERT: Explicit unsafe keyword overrides found in source code:"
    $unsafe | ForEach-Object { Write-Host $_.Path }
} else {
    Write-Host "No explicit unsafe keyword overrides found in source code."
}

Write-Host "`n[STEP 2/4] Scanning for Unresolved Directives and Bypasses..."
$bypasses = Select-String -Path "$SRC_DIR\*.lean", "$SRC_DIR\*\*.lean" -Pattern "sorryAx", "no_compute", "implemented_by" -List
if ($bypasses) {
    Write-Host "ALERT: Runtime replacement or structural proof bypasses found:"
    $bypasses | ForEach-Object { Write-Host $_.Path }
} else {
    Write-Host "No runtime replacement or structural proof bypasses found."
}

Write-Host "`n[STEP 3/4] Running Dead-Code Dependency Tracking..."
python3 .\audit_imports.py

Write-Host "`n[STEP 4/4] Automated Binary Analysis of Compiled Olean Fingerprints..."
if (Test-Path "$BUILD_DIR\lib") {
    Write-Host "Analyzing compiled library files for unexpected low-level definitions..."
    $sorryAx = Get-ChildItem -Path "$BUILD_DIR\lib" -Recurse -Filter "*.olean" | Select-String -Pattern "sorryAx" -List
    if ($sorryAx) {
        Write-Host "ALERT: Compiled binary objects contain active 'sorryAx' instructions!"
        $sorryAx | ForEach-Object { Write-Host $_.Path }
    } else {
        Write-Host "Binary Validation Passed: No hidden 'sorry' macros detected inside compiled library elements."
    }
} else {
    Write-Host "Compiled library artifacts path missing. Make sure your Lake target is configured properly."
}

Write-Host "`n======================================================================"
Write-Host "Audit completed. Cross-reference results with agent_audit_ledger.md."
Write-Host "======================================================================"
