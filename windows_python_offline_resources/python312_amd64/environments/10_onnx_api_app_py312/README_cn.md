# 10_onnx_api_app（Python 3.12.10，Windows x64）

用途：ONNX 推理与 API / Web 应用

## 直接依赖

| 包 | 版本 |
| --- | --- |
| `onnx` | 1.22.0 |
| `onnxruntime` | 1.28.0 |
| `fastapi` | 0.141.1 |
| `uvicorn` | 0.52.1 |
| `pydantic` | 2.13.4 |
| `streamlit` | 1.59.1 |
| `numpy` | 2.4.6 |
| `requests` | 2.34.2 |

锁定清单共 55 个分发包（含传递依赖），本目录内含 55 个，约 114 MiB。全部来自 PyPI，并与锁定清单中的 SHA256 一致。

## 安装

先安装 `python312_amd64\runtime\python-3.12.10-amd64.exe`，然后在 PowerShell 中：

```powershell
cd D:\wpo\python312_amd64\environments\10_onnx_api_app_py312
powershell -ExecutionPolicy Bypass -File .\install_offline_en.ps1
```

脚本在本目录下创建 `.venv`，先用随包的 pip 26.2 升级 pip，再按锁定清单（`--require-hashes`）离线安装，最后运行 `check_environment_en.py` 检查导入与版本。

激活：`.\.venv\Scripts\Activate.ps1`

## 状态

只做了静态检查：wheel 平台标签与 Python 版本、锁定清单 SHA256、`pip install --dry-run --platform win_amd64` 通过。**没有在 Windows 上实际安装验证。**
