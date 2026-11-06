# Offline install of python312_amd64/environments/03_signal_image_audio_py312 into a virtual environment.
# Usage (PowerShell, from any folder):
#   powershell -ExecutionPolicy Bypass -File install_offline_en.ps1 [-Python C:\path\python.exe] [-DownloadPlaceholders]
param(
  [string]$Python = "",
  [string]$VenvDir = (Join-Path $PSScriptRoot ".venv"),
  [switch]$DownloadPlaceholders
)
$ErrorActionPreference = "Stop"
$Wheelhouse = Join-Path $PSScriptRoot "wheelhouse"
$Lock = Join-Path $PSScriptRoot "requirements_lock_en.txt"
if (-not $Python) { $Python = Join-Path $env:LOCALAPPDATA "Programs\Python\Python312\python.exe" }
if (-not (Test-Path $Python)) { throw "Python 3.12.10 not found at $Python. Install python312_amd64\runtime\python-3.12.10-amd64.exe first, or pass -Python." }
$ver = & $Python -c "import platform; print(platform.python_version())"
if ($ver -ne "3.12.10") { Write-Warning "This environment was locked for Python 3.12.10; found $ver." }

# Wheels kept as .url placeholders (files over 100 MiB) must be downloaded first.
$missing = @()
foreach ($u in Get-ChildItem $Wheelhouse -Filter *.url) {
  $ini = Get-Content $u.FullName
  $name = (($ini | Where-Object { $_ -like "Name=*" }) -replace "^Name=", "")
  $url = (($ini | Where-Object { $_ -like "URL=*" }) -replace "^URL=", "")
  $sha = (($ini | Where-Object { $_ -like "SHA256=*" }) -replace "^SHA256=", "")
  $target = Join-Path $Wheelhouse $name
  if (Test-Path $target) {
    if ((Get-FileHash $target -Algorithm SHA256).Hash.ToLower() -ne $sha) { throw "SHA256 mismatch: $target" }
    continue
  }
  if ($DownloadPlaceholders) {
    Write-Host "Downloading $name"
    Invoke-WebRequest -Uri $url -OutFile $target
    if ((Get-FileHash $target -Algorithm SHA256).Hash.ToLower() -ne $sha) { Remove-Item $target; throw "SHA256 mismatch: $name" }
  } else {
    $missing += "$name  <-  $url"
  }
}
if ($missing.Count) {
  Write-Host "These wheels are not in the package (over 100 MiB). Download them into $Wheelhouse, or rerun with -DownloadPlaceholders:"
  $missing | ForEach-Object { Write-Host "  $_" }
  exit 1
}

& $Python -m venv $VenvDir
$VPy = Join-Path $VenvDir "Scripts\python.exe"
& $VPy -m pip install --no-index --find-links $Wheelhouse --require-hashes -r (Join-Path $PSScriptRoot "requirements_pip_en.txt")
if ($LASTEXITCODE) { throw "pip upgrade failed" }
& $VPy -m pip install --no-index --find-links $Wheelhouse --require-hashes -r $Lock
if ($LASTEXITCODE) { throw "pip install failed" }
& $VPy (Join-Path $PSScriptRoot "check_environment_en.py")
