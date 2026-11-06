# Windows 安装步骤

1. 把需要的 tar 包全部解压到同一个目录，例如 `D:\wpo\`（Windows 10/11 自带 `tar -xf <包>.tar`，7-Zip 也可以）。解压后得到 `D:\wpo\windows_python_offline_resources\`。
2. 安装 Python：运行 `python310_amd64\runtime\python-3.10.11-amd64.exe` 或 `python312_amd64\runtime\python-3.12.10-amd64.exe`。可在安装界面取消 “Add python.exe to PATH”，脚本会按默认安装路径找 Python。
3. 打开 PowerShell，进入环境组目录，例如：

   ```powershell
   cd D:\wpo\windows_python_offline_resources\python312_amd64\environments\01_base_scientific_py312
   powershell -ExecutionPolicy Bypass -File .\install_offline_en.ps1
   ```

4. 脚本会创建 `.venv`，离线安装锁定清单中的所有包，然后运行 `check_environment_en.py`。输出 `result: all ok` 即完成。
5. 使用：`.\.venv\Scripts\Activate.ps1`，或直接调用 `.\.venv\Scripts\python.exe`。

## 需要另外下载的文件

torch、tensorflow、pyside6_addons 的 wheel 超过 100 MiB，包里只有 `.url` 占位文件。用到这些包的组（04、05、07、07b、08、09、15、17b、24c）在安装前需把对应 wheel 下载到该组的 `wheelhouse\`，或在联网时运行 `install_offline_en.ps1 -DownloadPlaceholders`，脚本会下载并核对 SHA256。完整列表见库根 `placeholders_cn.csv`。

## 常见问题

- **执行策略报错**：用 `powershell -ExecutionPolicy Bypass -File ...` 运行，或 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`。
- **路径过长**：解压目录尽量短（如 `D:\wpo\`）。
- **DLL 缺失**：安装 Microsoft VC++ 运行库，链接见 `installers\vc_redist.x64.exe.url`。
- **校验文件**：在库根运行 `powershell -ExecutionPolicy Bypass -File .\tools\verify_sha256_en.ps1`。
