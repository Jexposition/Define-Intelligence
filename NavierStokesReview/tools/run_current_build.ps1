$ErrorActionPreference = 'Continue'
$repo = 'D:\Research Lab\Jexposition\Define Intelligence\NavierStokesReview\src\upstream-current'
$log = 'D:\Research Lab\Jexposition\Define Intelligence\NavierStokesReview\results\BUILD_CURRENT_4_34_RC2.txt'
Set-Location -LiteralPath $repo
& 'C:\Users\Admin\.elan\bin\elan.exe' run leanprover/lean4:v4.34.0-rc2 lake build *>> $log
$code = $LASTEXITCODE
Add-Content -LiteralPath $log -Value "`nEXIT_CODE=$code"
exit $code
