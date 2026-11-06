# 25_devtools（Python 3.10.11，Windows x64）

用途：开发、测试与打包工具

## 直接依赖

| 包 | 版本 |
| --- | --- |
| `pytest` | 9.1.1 |
| `black` | 26.5.1 |
| `ruff` | 0.16.1 |
| `mypy` | 2.3.0 |
| `pre-commit` | 4.6.1 |
| `ipython` | 8.39.0 |
| `pylint` | 4.0.6 |
| `isort` | 8.0.1 |
| `flake8` | 7.3.0 |
| `pyinstaller` | 6.21.0 |
| `build` | 1.5.0 |
| `twine` | 7.0.0 |
| `setuptools` | 83.0.0 |
| `wheel` | 0.47.0 |

锁定清单共 81 个分发包（含传递依赖），本目录内含 81 个，约 46 MiB。全部来自 PyPI，并与锁定清单中的 SHA256 一致。

## 安装

先安装 `python310_amd64\runtime\python-3.10.11-amd64.exe`，然后在 PowerShell 中：

```powershell
cd D:\wpo\python310_amd64\environments\25_devtools_py310
powershell -ExecutionPolicy Bypass -File .\install_offline_en.ps1
```

脚本在本目录下创建 `.venv`，先用随包的 pip 26.2 升级 pip，再按锁定清单（`--require-hashes`）离线安装，最后运行 `check_environment_en.py` 检查导入与版本。

激活：`.\.venv\Scripts\Activate.ps1`

## 状态

只做了静态检查：wheel 平台标签与 Python 版本、锁定清单 SHA256、`pip install --dry-run --platform win_amd64` 通过。**没有在 Windows 上实际安装验证。**
