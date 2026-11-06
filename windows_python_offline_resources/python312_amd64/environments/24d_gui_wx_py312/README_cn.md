# 24d_gui_wx（Python 3.12.10，Windows x64）

用途：wxPython 图形界面

## 直接依赖

| 包 | 版本 |
| --- | --- |
| `wxpython` | 4.3.1 |

锁定清单共 1 个分发包（含传递依赖），本目录内含 1 个，约 18 MiB。全部来自 PyPI，并与锁定清单中的 SHA256 一致。

## 安装

先安装 `python312_amd64\runtime\python-3.12.10-amd64.exe`，然后在 PowerShell 中：

```powershell
cd D:\wpo\python312_amd64\environments\24d_gui_wx_py312
powershell -ExecutionPolicy Bypass -File .\install_offline_en.ps1
```

脚本在本目录下创建 `.venv`，先用随包的 pip 26.2 升级 pip，再按锁定清单（`--require-hashes`）离线安装，最后运行 `check_environment_en.py` 检查导入与版本。

激活：`.\.venv\Scripts\Activate.ps1`

## 状态

只做了静态检查：wheel 平台标签与 Python 版本、锁定清单 SHA256、`pip install --dry-run --platform win_amd64` 通过。**没有在 Windows 上实际安装验证。**
