# Windows 通用科研 Python 离线环境库

面向无网络的 Windows 10/11 x64 机器：两棵独立版本树（CPython **3.10.11** 与 **3.12.10**），各 31 个环境组，外加补充包和信号处理补充。每组带直接依赖清单、带 SHA256 的完整锁定清单、全部 `win_amd64` / 纯 Python wheel、离线安装脚本和检查脚本。

## 目录

| 路径 | 内容 |
| --- | --- |
| `python310_amd64/`、`python312_amd64/` | `runtime/`（官方安装程序与签名）和 `environments/`（31 个环境组，每组自带 `wheelhouse/`） |
| `python3xx_amd64_supplement/` | 补充包：akshare 1.18.88、lime、ta、jieba、odfpy、jsonpath 等（后 5 个只有源码包，安装时离线构建） |
| `python3xx_amd64_supplement_signal/` | 信号处理补充：EMD-signal（PyEMD）、filterpy、pykalman，追加到 03 组环境上；含 4 个示例 |
| `installers/` | 安装程序登记表；VC++ 运行库、Git for Windows 等为 `.url` 占位 |
| `external/` | 浏览器、驱动、FFmpeg、Tesseract 的 `.url` 占位，Tesseract 语言数据 |
| `guides/` | Windows 安装步骤、Python 版本选择 |
| `tools/` | `verify_sha256_en.ps1`（校验）、`download_installers.sh`（Linux 上下载安装程序） |
| `environments_overview_cn.md` | 各组用途、分发包数量与大小 |
| `package_inventory_cn.csv` | 每个文件的包名、版本、大小、SHA256、许可证、来源 |
| `placeholders_cn.csv` | 全部 `.url` 占位文件及原因 |
| `external_dependencies_cn.csv`、`licenses_cn.md` | 外部工具与许可说明 |

## 快速开始

1. 从 Release 下载 `windows_python_offline_01_docs_required_cn_en.tar`、`windows_python_offline_02_installers_cn_en.tar` 和所需版本的 part，全部解压到 `D:\wpo\`（详见 `download_restore_cn.md`）。
2. 安装 `python312_amd64\runtime\python-3.12.10-amd64.exe`（或 3.10.11）。
3. 进入环境组目录，运行 `powershell -ExecutionPolicy Bypass -File .\install_offline_en.ps1`。

## 需另行下载的文件

下列文件没有放进包里，对应位置是同名 `.url` 文件（官方链接、大小、SHA256），共 27 个，见 `placeholders_cn.csv`：

- 超过 100 MiB 的 wheel（5 个文件）：`torch` 2.13.0、`tensorflow`（3.10 为 2.20.0，3.12 为 2.21.0）、`pyside6_addons` 6.11.1。涉及 04、05、07、07b、08、09、15、17b、24c 组。安装脚本加 `-DownloadPlaceholders` 可在联网时自动下载并核对。
- 专有或 GPL 捆绑的外部程序：VC++ 运行库、Git for Windows、Chrome for Testing 与 ChromeDriver、Edge WebDriver、FFmpeg、Tesseract 安装程序，以及不使用的 Python 3.13.17 安装程序。

## 版本与来源

- 3.10 树共 487 个不同的分发文件，3.12 树共 480 个，全部来自 PyPI，SHA256 与锁定清单一致。
- 每棵树内，同一个包在所有组中只用一个版本（唯一例外是 `scikit-base`，见 `guides/python_version_policy_cn.md`）。版本取 2026-08-01 之前发布的稳定版，补充包取 2026-10-31 之前。
- Python 安装程序来自 python.org，GPG 签名已核对。

## 状态

只做了静态检查：每个锁定清单都用 `pip install --dry-run --platform win_amd64 --only-binary=:all: --no-index --require-hashes` 对本地 wheel 检查通过；补充包的 5 个源码包在 Linux 上用随包 setuptools 离线构建通过。**没有在 Windows 上实际安装或运行验证。**
