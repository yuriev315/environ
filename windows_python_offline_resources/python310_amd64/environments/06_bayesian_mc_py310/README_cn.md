# 06_bayesian_mc（Python 3.10.11，Windows x64）

用途：贝叶斯推断与蒙特卡洛

## 直接依赖

| 包 | 版本 |
| --- | --- |
| `pymc` | 5.25.1 |
| `arviz` | 0.23.4 |
| `emcee` | 3.1.6 |
| `corner` | 2.3.0 |
| `numpy` | 2.2.6 |
| `scipy` | 1.15.3 |
| `pandas` | 2.3.3 |
| `matplotlib` | 3.10.9 |

锁定清单共 41 个分发包（含传递依赖），本目录内含 41 个，约 91 MiB。全部来自 PyPI，并与锁定清单中的 SHA256 一致。

## 安装

先安装 `python310_amd64\runtime\python-3.10.11-amd64.exe`，然后在 PowerShell 中：

```powershell
cd D:\wpo\python310_amd64\environments\06_bayesian_mc_py310
powershell -ExecutionPolicy Bypass -File .\install_offline_en.ps1
```

脚本在本目录下创建 `.venv`，先用随包的 pip 26.2 升级 pip，再按锁定清单（`--require-hashes`）离线安装，最后运行 `check_environment_en.py` 检查导入与版本。

激活：`.\.venv\Scripts\Activate.ps1`

## 状态

只做了静态检查：wheel 平台标签与 Python 版本、锁定清单 SHA256、`pip install --dry-run --platform win_amd64` 通过。**没有在 Windows 上实际安装验证。**
