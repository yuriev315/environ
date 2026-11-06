# 15_dl_pytorch_extra（Python 3.10.11，Windows x64）

用途：PyTorch 深度学习扩展

## 直接依赖

| 包 | 版本 |
| --- | --- |
| `torch` | 2.13.0 |
| `lightning` | 2.6.5 |
| `torchmetrics` | 1.9.0 |
| `timm` | 1.0.28 |
| `einops` | 0.8.2 |
| `tensorboard` | 2.20.0 |
| `torchinfo` | 1.8.0 |

锁定清单共 51 个分发包（含传递依赖），本目录内含 50 个，约 55 MiB。全部来自 PyPI，并与锁定清单中的 SHA256 一致。

## 需要另行下载的文件

下列文件超过 100 MiB，目录里只有同名 `.url` 占位文件（含官方链接、大小和 SHA256）。安装前下载到 `wheelhouse/`，或运行安装脚本时加 `-DownloadPlaceholders`（需要联网）。

- `torch-2.13.0-cp310-cp310-win_amd64.whl`（116 MiB）

## 安装

先安装 `python310_amd64\runtime\python-3.10.11-amd64.exe`，然后在 PowerShell 中：

```powershell
cd D:\wpo\python310_amd64\environments\15_dl_pytorch_extra_py310
powershell -ExecutionPolicy Bypass -File .\install_offline_en.ps1
```

脚本在本目录下创建 `.venv`，先用随包的 pip 26.2 升级 pip，再按锁定清单（`--require-hashes`）离线安装，最后运行 `check_environment_en.py` 检查导入与版本。

激活：`.\.venv\Scripts\Activate.ps1`

## 状态

只做了静态检查：wheel 平台标签与 Python 版本、锁定清单 SHA256、`pip install --dry-run --platform win_amd64` 通过。**没有在 Windows 上实际安装验证。**
