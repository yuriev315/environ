# 12_scientific_extra（Python 3.10.11，Windows x64）

用途：科学计算扩展

## 直接依赖

| 包 | 版本 |
| --- | --- |
| `numba` | 0.66.0 |
| `xarray` | 2025.6.1 |
| `netcdf4` | 1.7.4 |
| `dask` | 2026.7.1 |
| `polars` | 1.43.2 |
| `pyarrow` | 25.0.0 |
| `networkx` | 3.4.2 |
| `sympy` | 1.14.0 |
| `astropy` | 6.1.7 |

锁定清单共 33 个分发包（含传递依赖），本目录内含 33 个，约 185 MiB。全部来自 PyPI，并与锁定清单中的 SHA256 一致。

## 安装

先安装 `python310_amd64\runtime\python-3.10.11-amd64.exe`，然后在 PowerShell 中：

```powershell
cd D:\wpo\python310_amd64\environments\12_scientific_extra_py310
powershell -ExecutionPolicy Bypass -File .\install_offline_en.ps1
```

脚本在本目录下创建 `.venv`，先用随包的 pip 26.2 升级 pip，再按锁定清单（`--require-hashes`）离线安装，最后运行 `check_environment_en.py` 检查导入与版本。

激活：`.\.venv\Scripts\Activate.ps1`

## 状态

只做了静态检查：wheel 平台标签与 Python 版本、锁定清单 SHA256、`pip install --dry-run --platform win_amd64` 通过。**没有在 Windows 上实际安装验证。**
