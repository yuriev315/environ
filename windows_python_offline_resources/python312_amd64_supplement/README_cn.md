# 补充包（Python 3.12.10，Windows x64）

用途：补充：金融数据与常用工具（另含源码包）

## 直接依赖

| 包 | 版本 |
| --- | --- |
| `akshare` | 1.18.88 |
| `lime` | 0.2.0.1 |
| `ta` | 0.11.0 |
| `jieba` | 0.42.1 |
| `odfpy` | 1.4.1 |
| `numpy` | 2.4.6 |
| `pandas` | 2.3.3 |
| `scikit-learn` | 1.7.2 |
| `matplotlib` | 3.11.1 |

锁定清单共 52 个分发包（含传递依赖），本目录内含 52 个，约 142 MiB。全部来自 PyPI，并与锁定清单中的 SHA256 一致。

## 源码包

下列包在 PyPI 上没有 wheel，`packages_sdist/` 中是源码包，安装时由 pip 用 `packages_wheel/` 中的 setuptools 离线构建（纯 Python）。在 Linux 上用同一版本 setuptools 离线构建通过，Windows 上未实际构建。

- `jieba-0.42.1.tar.gz`
- `jsonpath-0.82.2.tar.gz`
- `lime-0.2.0.1.tar.gz`
- `odfpy-1.4.1.tar.gz`
- `ta-0.11.0.tar.gz`

## 安装

先安装 `python312_amd64\runtime\python-3.12.10-amd64.exe`，然后在 PowerShell 中：

```powershell
cd D:\wpo\python312_amd64_supplement
powershell -ExecutionPolicy Bypass -File .\install_supplement_en.ps1
```

脚本在本目录下创建 `.venv`，先用随包的 pip 26.2 升级 pip，再按锁定清单（`--require-hashes`）离线安装，最后运行 `check_environment_en.py` 检查导入与版本。

激活：`.\.venv\Scripts\Activate.ps1`

## 状态

只做了静态检查：wheel 平台标签与 Python 版本、锁定清单 SHA256、`pip install --dry-run --platform win_amd64` 通过。**没有在 Windows 上实际安装验证。**
