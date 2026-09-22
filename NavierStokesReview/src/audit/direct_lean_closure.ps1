param(
    [string]$Target = 'Euler.Solution',
    [int]$Workers = 8
)

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
$Lean = 'C:\Users\Admin\.elan\toolchains\leanprover--lean4---v4.34.0-rc2\bin\lean.exe'
$ProjectPrefixes = @('Euler', 'NavierStokes')

$packagePaths = Get-ChildItem (Join-Path $Root '.lake\packages') -Directory |
    ForEach-Object { Join-Path $_.FullName '.lake\build\lib\lean' } |
    Where-Object { Test-Path -LiteralPath $_ }
$env:LEAN_PATH = (($packagePaths + (Join-Path $Root '.lake\build\lib\lean')) -join [IO.Path]::PathSeparator)

$moduleSources = @{}
$moduleImports = @{}

function Get-Source([string]$Module) {
    if(-not ($ProjectPrefixes | Where-Object {$Module -eq $_ -or $Module.StartsWith("$_.")})) { return $null }
    $relative = ($Module -replace '\.', '\') + '.lean'
    $path = Join-Path $Root $relative
    if(Test-Path -LiteralPath $path) { return (Resolve-Path -LiteralPath $path).Path }
    throw "Project module source not found: $Module"
}

function Get-Imports([string]$Source) {
    $result = @()
    foreach($line in Get-Content -LiteralPath $Source) {
        if($line -match '^\s*import\s+([A-Za-z0-9_.]+)') { $result += $Matches[1] }
    }
    return $result
}

function Visit([string]$Module) {
    if($moduleSources.ContainsKey($Module)) { return }
    $source = Get-Source $Module
    $moduleSources[$Module] = $source
    $deps = @(Get-Imports $source | Where-Object {
        $m = $_
        ($ProjectPrefixes | Where-Object {$m -eq $_ -or $m.StartsWith("$_.")})
    })
    $moduleImports[$Module] = $deps
    foreach($dep in $deps) { Visit $dep }
}

Visit $Target
$remaining = [Collections.Generic.HashSet[string]]::new([string[]]$moduleSources.Keys)
$groups = @()
while($remaining.Count -gt 0) {
    $ready = @($remaining | Where-Object {
        $module = $_
        $unresolved = @($moduleImports[$module] | Where-Object {$remaining.Contains($_)})
        $unresolved.Count -eq 0
    } | Sort-Object)
    if($ready.Count -eq 0) {
        $diagnostic = foreach($module in ($remaining | Sort-Object | Select-Object -First 12)) {
            $deps = @($moduleImports[$module]) -join ','
            "${module}=>${deps}"
        }
        throw ("Import cycle or unresolved dependency: " + (($remaining | Sort-Object) -join ', ') + " | " + ($diagnostic -join ' ; '))
    }
    $groups += ,$ready
    foreach($module in $ready) { [void]$remaining.Remove($module) }
}

Write-Output ("target={0} project_modules={1} groups={2}" -f $Target,$moduleSources.Count,$groups.Count)
$completed = 0
foreach($group in $groups) {
    $results = @($group | ForEach-Object -Parallel {
        $module = $_
        $root = $using:Root
        $lean = $using:Lean
        $sources = $using:moduleSources
        $source = $sources[$module]
        $relative = ($module -replace '\.', '\')
        $output = Join-Path $root ('.lake\build\lib\lean\' + $relative + '.olean')
        $interface = Join-Path $root ('.lake\build\lib\lean\' + $relative + '.ilean')
        $parent = Split-Path -Parent $output
        New-Item -ItemType Directory -Force -Path $parent | Out-Null
        if((Test-Path -LiteralPath $output) -and
           ((Get-Item -LiteralPath $output).LastWriteTime -ge (Get-Item -LiteralPath $source).LastWriteTime)) {
            [pscustomobject]@{Module=$module;Status='cached';Code=0;Output=''}
        } else {
            $text = @(& $lean $source -o $output -i $interface 2>&1 | ForEach-Object {$_.ToString()}) -join "`n"
            [pscustomobject]@{Module=$module;Status=($(if($LASTEXITCODE -eq 0){'compiled'}else{'failed'}));Code=$LASTEXITCODE;Output=$text}
        }
    } -ThrottleLimit $Workers)
    foreach($result in $results) {
        $completed++
        Write-Output ("[{0}/{1}] {2}: {3}" -f $completed,$moduleSources.Count,$result.Status,$result.Module)
        if($result.Status -eq 'failed') {
            Write-Output $result.Output
            exit ([Math]::Max(1,[int]$result.Code))
        }
    }
}
