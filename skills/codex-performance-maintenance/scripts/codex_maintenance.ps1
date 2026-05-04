param(
    [switch]$Apply,
    [int]$ArchiveSessionsOlderThanDays = 7,
    [int]$LargeSessionMB = 10,
    [string]$BackupRoot = "$env:USERPROFILE\CodexArchives"
)

$ErrorActionPreference = "Stop"
$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

$codexRoot = Join-Path $env:USERPROFILE ".codex"
if (-not (Test-Path -LiteralPath $codexRoot)) {
    throw "Codex root not found: $codexRoot"
}

$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$runRoot = Join-Path $BackupRoot "maintenance-$stamp"
$report = [ordered]@{
    Timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    CodexRoot = $codexRoot
    Apply = [bool]$Apply
    Actions = @()
    Warnings = @()
}

function Add-Action {
    param([string]$Type, [string]$Path, [double]$SizeMB, [string]$Target = "")
    $script:report.Actions += [ordered]@{
        Type = $Type
        Path = $Path
        SizeMB = [math]::Round($SizeMB, 2)
        Target = $Target
    }
}

function Dir-SizeMB {
    param([string]$Path)
    $sum = (Get-ChildItem -LiteralPath $Path -Recurse -Force -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum
    return [math]::Round(($sum / 1MB), 2)
}

$codexProcs = Get-Process -ErrorAction SilentlyContinue | Where-Object {
    $_.ProcessName -match '^(Codex|codex|Codex Accounts Desktop|CodexAccountsDesktop)$'
}

if ($codexProcs) {
    $report.Warnings += "Codex processes are running. This script will not rotate sqlite logs or move active sessions while Codex is open."
}

$sessionsRoot = Join-Path $codexRoot "sessions"
if (Test-Path -LiteralPath $sessionsRoot) {
    $cutoff = (Get-Date).AddDays(-1 * $ArchiveSessionsOlderThanDays)
    $sessionArchive = Join-Path $runRoot "sessions"
    $sessionFiles = Get-ChildItem -LiteralPath $sessionsRoot -Recurse -Force -File -ErrorAction SilentlyContinue |
        Where-Object { $_.Length -ge ($LargeSessionMB * 1MB) -and $_.LastWriteTime -lt $cutoff }
    foreach ($file in $sessionFiles) {
        $src = (Resolve-Path -LiteralPath $file.FullName).Path
        $sessionResolved = (Resolve-Path -LiteralPath $sessionsRoot).Path
        $rel = $src.Substring($sessionResolved.Length).TrimStart('\')
        $dst = Join-Path $sessionArchive $rel
        Add-Action -Type "archive-session" -Path $src -SizeMB ($file.Length / 1MB) -Target $dst
        if ($Apply -and -not $codexProcs) {
            $dstDir = Split-Path -Parent $dst
            New-Item -ItemType Directory -Force -Path $dstDir | Out-Null
            $dstParentResolved = (Resolve-Path -LiteralPath $dstDir).Path
            if (-not $dstParentResolved.StartsWith((Resolve-Path -LiteralPath $runRoot).Path, [StringComparison]::OrdinalIgnoreCase)) {
                throw "Archive target escaped backup root: $dst"
            }
            Move-Item -LiteralPath $src -Destination $dst
        }
    }
}

$tmpRoot = Join-Path $codexRoot ".tmp"
if (Test-Path -LiteralPath $tmpRoot) {
    foreach ($name in @("bundled-marketplaces", "plugins", "marketplaces")) {
        $p = Join-Path $tmpRoot $name
        if (Test-Path -LiteralPath $p) {
            Add-Action -Type "archive-temp-cache" -Path $p -SizeMB (Dir-SizeMB $p) -Target (Join-Path $runRoot ".tmp\$name")
            if ($Apply -and -not $codexProcs) {
                $target = Join-Path $runRoot ".tmp\$name"
                New-Item -ItemType Directory -Force -Path (Split-Path -Parent $target) | Out-Null
                Move-Item -LiteralPath $p -Destination $target
            }
        }
    }
}

foreach ($name in @("logs_2.sqlite", "logs_2.sqlite-wal", "logs_2.sqlite-shm")) {
    $p = Join-Path $codexRoot $name
    if (Test-Path -LiteralPath $p) {
        $file = Get-Item -LiteralPath $p
        Add-Action -Type "rotate-log-after-close" -Path $p -SizeMB ($file.Length / 1MB) -Target (Join-Path $runRoot "logs\$name")
        if ($Apply -and -not $codexProcs) {
            $target = Join-Path $runRoot "logs\$name"
            New-Item -ItemType Directory -Force -Path (Split-Path -Parent $target) | Out-Null
            Move-Item -LiteralPath $p -Destination $target
        }
    }
}

New-Item -ItemType Directory -Force -Path $runRoot | Out-Null
$reportPath = Join-Path $runRoot "codex-maintenance-report.json"
($report | ConvertTo-Json -Depth 6) | Set-Content -Encoding UTF8 -Path $reportPath

[pscustomobject]@{
    Report = $reportPath
    Apply = [bool]$Apply
    CodexRunning = [bool]$codexProcs
    PlannedActions = $report.Actions.Count
    PlannedMB = [math]::Round((($report.Actions | ForEach-Object { [double]$_["SizeMB"] } | Measure-Object -Sum).Sum), 2)
    Warnings = ($report.Warnings -join " | ")
}

