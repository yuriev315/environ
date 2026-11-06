# Verify extracted files against package_inventory_cn.csv (run from the library root, e.g. D:\wpo\windows_python_offline_resources).
param([string]$Root = (Split-Path -Parent $PSScriptRoot))
$ErrorActionPreference = "Stop"
$rows = Import-Csv (Join-Path $Root "package_inventory_cn.csv") -Encoding UTF8
$bad = 0; $ok = 0; $skip = 0
foreach ($r in $rows) {
  if ($r.status -ne "included") { $skip++; continue }
  $p = Join-Path $Root ($r.file -replace "/", "\")
  if (-not (Test-Path $p)) { Write-Host "MISSING $($r.file)"; $bad++; continue }
  if ((Get-FileHash $p -Algorithm SHA256).Hash.ToLower() -ne $r.sha256) { Write-Host "BAD     $($r.file)"; $bad++ } else { $ok++ }
}
Write-Host "ok=$ok bad=$bad placeholders=$skip"
if ($bad) { exit 1 }
