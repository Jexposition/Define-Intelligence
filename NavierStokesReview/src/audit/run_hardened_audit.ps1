param(
  [string]$Stamp = (Get-Date -Format 'yyyy-MM-dd')
)

$ErrorActionPreference = 'Stop'

$repo = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
$python = (Get-Command python).Source
$elan = 'C:\Users\Admin\.elan\bin\elan.exe'
$toolchain = 'leanprover/lean4:v4.34.0-rc2'

Push-Location $repo
try {
  $tree = 'D:\Research Lab\Jexposition\tree-maker\Define inteligence tree.md'
  $json = Join-Path $repo "NavierStokesReview/evidence/hardened_source_map_$Stamp.json"
  $markdown = Join-Path $repo "NavierStokesReview/evidence/hardened_source_map_$Stamp.md"
  & $python 'NavierStokesReview/src/audit/hardened_source_map.py' `
    --repo $repo `
    --tree $tree `
    --output $json `
    --markdown $markdown
  if ($LASTEXITCODE -ne 0) { throw "hardened_source_map.py failed with exit code $LASTEXITCODE" }

  & cmd /c "`"$elan`" run $toolchain lake env lean NavierStokesReview/src/audit/EnvironmentDependencyExport.lean"
  if ($LASTEXITCODE -ne 0) { throw "EnvironmentDependencyExport.lean failed with exit code $LASTEXITCODE" }

  $environment = Join-Path $repo "NavierStokesReview/evidence/lean_environment_closure_$Stamp.json"
  $joinedJson = Join-Path $repo "NavierStokesReview/evidence/joined_environment_source_map_$Stamp.json"
  $joinedMarkdown = Join-Path $repo "NavierStokesReview/evidence/joined_environment_source_map_$Stamp.md"
  $routesMarkdown = Join-Path $repo "NavierStokesReview/evidence/selected_endpoint_routes_$Stamp.md"
  & $python 'NavierStokesReview/src/audit/join_environment_source_map.py' `
    --source-map $json `
    --environment $environment `
    --output $joinedJson `
    --markdown $joinedMarkdown `
    --routes-markdown $routesMarkdown
  if ($LASTEXITCODE -ne 0) { throw "join_environment_source_map.py failed with exit code $LASTEXITCODE" }

  $reconciliation = Join-Path $repo "NavierStokesReview/evidence/tree_reconciliation_$Stamp.json"
  $reconciliationMarkdown = Join-Path $repo "NavierStokesReview/evidence/tree_reconciliation_$Stamp.md"
  & $python 'NavierStokesReview/src/audit/tree_reconciliation.py' `
    --repo $repo `
    --tree $tree `
    --output $reconciliation `
    --markdown $reconciliationMarkdown
  if ($LASTEXITCODE -ne 0) { throw "tree_reconciliation.py failed with exit code $LASTEXITCODE" }

  $bundleJson = Join-Path $repo "NavierStokesReview/evidence/hardened_audit_bundle_$Stamp.json"
  $bundleMarkdown = Join-Path $repo "NavierStokesReview/evidence/hardened_audit_bundle_$Stamp.md"
  & $python 'NavierStokesReview/src/audit/audit_bundle.py' `
    --repo $repo `
    --tree $tree `
    --source-map $json `
    --joined $joinedJson `
    --reconciliation $reconciliation `
    --output $bundleJson `
    --markdown $bundleMarkdown
  if ($LASTEXITCODE -ne 0) { throw "audit_bundle.py failed with exit code $LASTEXITCODE" }

  $claims = Join-Path $repo 'NavierStokesReview/config/review_claims.json'
  $claimRegister = Join-Path $repo "NavierStokesReview/evidence/review_claim_register_$Stamp.json"
  $claimRegisterMarkdown = Join-Path $repo "NavierStokesReview/evidence/review_claim_register_$Stamp.md"
  & $python 'NavierStokesReview/src/audit/claim_register.py' `
    --repo $repo `
    --claims $claims `
    --source-map $json `
    --joined $joinedJson `
    --bundle $bundleJson `
    --output $claimRegister `
    --markdown $claimRegisterMarkdown
  if ($LASTEXITCODE -ne 0) { throw "claim_register.py failed with exit code $LASTEXITCODE" }

  $repositoryMapJson = Join-Path $repo "NavierStokesReview/evidence/repository_map_$Stamp.json"
  $repositoryMapMarkdown = Join-Path $repo "NavierStokesReview/evidence/repository_map_$Stamp.md"
  $repositoryMapDot = Join-Path $repo "NavierStokesReview/evidence/repository_map_$Stamp.dot"
  $repositoryMapTex = Join-Path $repo "NavierStokesReview/evidence/repository_map_$Stamp.tex"
  & $python 'NavierStokesReview/src/audit/repository_map.py' `
    --repo $repo `
    --tree $tree `
    --source-map $json `
    --joined $joinedJson `
    --claims $claims `
    --json-output $repositoryMapJson `
    --markdown-output $repositoryMapMarkdown `
    --dot-output $repositoryMapDot `
    --tex-output $repositoryMapTex
  if ($LASTEXITCODE -ne 0) { throw "repository_map.py failed with exit code $LASTEXITCODE" }

  $humanArchitecture = Join-Path $repo 'docs/REPOSITORY_ARCHITECTURE_MAP.md'
  $humanAtlas = Join-Path $repo 'docs/REPOSITORY_MODULE_ATLAS.md'
  $humanDot = Join-Path $repo 'docs/REPOSITORY_ARCHITECTURE_MAP.dot'
  $humanTex = Join-Path $repo 'docs/REPOSITORY_ARCHITECTURE_MAP.tex'
  $humanHtml = Join-Path $repo 'docs/REPOSITORY_ARCHITECTURE_MAP.html'
  $humanExplanations = Join-Path $repo 'docs/LEAN_MODULE_EXPLANATIONS.md'
$humanDeclarationIndex = Join-Path $repo 'docs/LEAN_DECLARATION_INDEX.md'
  $auditGraph = Join-Path $repo "NavierStokesReview/evidence/repository_audit_graph_$Stamp.json"
$mathematicalSpec = Join-Path $repo 'docs/MATHEMATICAL_SPECIFICATION.md'
  $routes = Join-Path $repo "NavierStokesReview/evidence/selected_endpoint_routes_$Stamp.md"
  & $python 'NavierStokesReview/src/audit/human_readable_map.py' `
    --repo $repo `
    --map $repositoryMapJson `
    --routes $routes `
    --architecture $humanArchitecture `
    --atlas $humanAtlas `
    --dot $humanDot `
    --tex $humanTex `
    --explanations $humanExplanations `
    --html $humanHtml `
  --claims $claims `
  --declaration-index $humanDeclarationIndex `
  --audit-graph $auditGraph `
  --mathematical-spec $mathematicalSpec
  if ($LASTEXITCODE -ne 0) { throw "human_readable_map.py failed with exit code $LASTEXITCODE" }
}
finally {
  Pop-Location
}
