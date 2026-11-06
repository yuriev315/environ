# 03_signal_image_audio（Python 3.10.11，Windows x64）

用途：信号、图像、音频处理

## 直接依赖

| 包 | 版本 |
| --- | --- |
| `numpy` | 2.2.6 |
| `scipy` | 1.15.3 |
| `pywavelets` | 1.8.0 |
| `scikit-image` | 0.25.2 |
| `opencv-python-headless` | 5.0.0.93 |
| `pillow` | 11.3.0 |
| `librosa` | 0.11.0 |
| `soundfile` | 0.14.0 |
| `imageio` | 2.37.4 |
| `matplotlib` | 3.10.9 |

锁定清单共 40 个分发包（含传递依赖），本目录内含 40 个，约 182 MiB。全部来自 PyPI，并与锁定清单中的 SHA256 一致。

## 安装

先安装 `python310_amd64\runtime\python-3.10.11-amd64.exe`，然后在 PowerShell 中：

```powershell
cd D:\wpo\python310_amd64\environments\03_signal_image_audio_py310
powershell -ExecutionPolicy Bypass -File .\install_offline_en.ps1
```

脚本在本目录下创建 `.venv`，先用随包的 pip 26.2 升级 pip，再按锁定清单（`--require-hashes`）离线安装，最后运行 `check_environment_en.py` 检查导入与版本。

激活：`.\.venv\Scripts\Activate.ps1`

## 状态

只做了静态检查：wheel 平台标签与 Python 版本、锁定清单 SHA256、`pip install --dry-run --platform win_amd64` 通过。**没有在 Windows 上实际安装验证。**
