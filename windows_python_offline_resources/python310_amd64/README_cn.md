# Python 3.10.11 版本树（Windows x64）

- `runtime/python-3.10.11-amd64.exe`：官方安装程序，附 `.asc`、`.sigstore` 签名。
- `environments/`：31 个环境组，每组有 `requirements_direct_en.txt`（直接依赖）、`requirements_lock_en.txt`（带 SHA256 的完整锁定清单）、`wheelhouse/`、`install_offline_en.ps1`、`check_environment_en.py`、`wheel_manifest_cn.csv` 和 `README_cn.md`。
- 同级目录 `python310_amd64_supplement/`（akshare、lime、ta、jieba、odfpy 等，含源码包）与 `python310_amd64_supplement_signal/`（EMD / 小波 / 卡尔曼）。

本树（含两个补充目录）共 487 个不同的分发文件；同一个 wheel 在多个组中各存一份完整文件，不使用链接。

## 安装

1. 运行 `runtime\python-3.10.11-amd64.exe`，默认装到 `%LOCALAPPDATA%\Programs\Python\Python310`。
2. 进入要用的环境组目录，运行 `powershell -ExecutionPolicy Bypass -File .\install_offline_en.ps1`。Python 装在别处时加 `-Python <python.exe 路径>`。
3. 脚本结束时会运行 `check_environment_en.py`，逐个检查直接依赖的版本与导入。

各组之间互不依赖，可以只装需要的组。不同组的包版本可能互斥（例如 TensorFlow 组与 PyTorch 组），请分别用各自的 `.venv`。
