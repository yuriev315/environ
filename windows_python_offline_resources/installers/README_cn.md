# 安装程序

- Python 安装程序在各版本树的 `runtime/` 中：`python310_amd64\runtime\python-3.10.11-amd64.exe`、`python312_amd64\runtime\python-3.12.10-amd64.exe`，同目录有官方 `.asc` 与 `.sigstore` 签名文件。两者都已用 python.org 发布签名密钥核对 GPG 签名。
- 3.10.11 与 3.12.10 是这两个版本线最后提供 Windows 二进制安装程序的版本。
- `vc_redist.x64.exe.url`：Microsoft VC++ 运行库（微软专有，只给官方链接）。Python 安装程序已自带所需运行库，一般无需另装；个别带 C++ 扩展的包报 DLL 缺失时再装。
- `Git-2.56.0.4-64-bit.exe.url`：Git for Windows（GPL 捆绑包，只给官方链接，SHA256 与官方发布值一致）。
- `python-3.13.17-amd64.exe.url`：本库不使用 3.13，仅留链接。

明细见 `installer_inventory_cn.csv`。
