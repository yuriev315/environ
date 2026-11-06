# 14_ml_extra（Python 3.12.10，Windows x64）

用途：机器学习扩展与可解释性

## 直接依赖

| 包 | 版本 |
| --- | --- |
| `shap` | 0.52.0 |
| `umap-learn` | 0.5.12 |
| `hdbscan` | 0.8.44 |
| `mlxtend` | 0.23.4 |
| `category-encoders` | 2.10.0 |
| `optuna` | 4.9.0 |
| `scikit-learn` | 1.7.2 |

锁定清单共 41 个分发包（含传递依赖），本目录内含 41 个，约 144 MiB。全部来自 PyPI，并与锁定清单中的 SHA256 一致。

## 安装

先安装 `python312_amd64\runtime\python-3.12.10-amd64.exe`，然后在 PowerShell 中：

```powershell
cd D:\wpo\python312_amd64\environments\14_ml_extra_py312
powershell -ExecutionPolicy Bypass -File .\install_offline_en.ps1
```

脚本在本目录下创建 `.venv`，先用随包的 pip 26.2 升级 pip，再按锁定清单（`--require-hashes`）离线安装，最后运行 `check_environment_en.py` 检查导入与版本。

激活：`.\.venv\Scripts\Activate.ps1`

## 状态

只做了静态检查：wheel 平台标签与 Python 版本、锁定清单 SHA256、`pip install --dry-run --platform win_amd64` 通过。**没有在 Windows 上实际安装验证。**
