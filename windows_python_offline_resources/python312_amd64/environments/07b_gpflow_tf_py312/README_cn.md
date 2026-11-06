# 07b_gpflow_tf（Python 3.12.10，Windows x64）

用途：GPflow 高斯过程（TensorFlow）

## 直接依赖

| 包 | 版本 |
| --- | --- |
| `gpflow` | 2.9.2 |
| `tensorflow` | 2.21.0 |
| `tensorflow-probability` | 0.25.0 |
| `tf-keras` | 2.21.0 |
| `numpy` | 2.4.6 |
| `matplotlib` | 3.11.1 |

锁定清单共 54 个分发包（含传递依赖），本目录内含 53 个，约 114 MiB。全部来自 PyPI，并与锁定清单中的 SHA256 一致。

## 需要另行下载的文件

下列文件超过 100 MiB，目录里只有同名 `.url` 占位文件（含官方链接、大小和 SHA256）。安装前下载到 `wheelhouse/`，或运行安装脚本时加 `-DownloadPlaceholders`（需要联网）。

- `tensorflow-2.21.0-cp312-cp312-win_amd64.whl`（335 MiB）

## 安装

先安装 `python312_amd64\runtime\python-3.12.10-amd64.exe`，然后在 PowerShell 中：

```powershell
cd D:\wpo\python312_amd64\environments\07b_gpflow_tf_py312
powershell -ExecutionPolicy Bypass -File .\install_offline_en.ps1
```

脚本在本目录下创建 `.venv`，先用随包的 pip 26.2 升级 pip，再按锁定清单（`--require-hashes`）离线安装，最后运行 `check_environment_en.py` 检查导入与版本。

激活：`.\.venv\Scripts\Activate.ps1`

## 状态

只做了静态检查：wheel 平台标签与 Python 版本、锁定清单 SHA256、`pip install --dry-run --platform win_amd64` 通过。**没有在 Windows 上实际安装验证。**
