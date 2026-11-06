# 下载与解压说明（Windows 通用科研 Python 离线环境库）

本 Release 的包都是**不压缩 tar**（wheel 和安装程序本身已压缩）。所有包解压到**同一个目录**，例如 `D:\wpo\`，得到 `D:\wpo\windows_python_offline_resources\`。

## 按需下载

| 包 | 内容 | 大小 |
| --- | --- | ---: |
| `windows_python_offline_01_docs_required_cn_en.tar` | 必下：全部说明、登记表、锁定清单、安装/检查脚本、`.url` 占位文件 | 约 7 MiB |
| `windows_python_offline_02_installers_cn_en.tar` | 安装程序：Python 3.10.11 / 3.12.10 官方 Windows x64 安装程序 | 53 MiB |
| `windows_python_offline_03_py310_part1_cn_en.tar` | Python 3.10 环境组：`01_base_scientific`、`02_ml_stats`、`03_signal_image_audio`、`04_pytorch_cpu`、`05_gpr_bo_pytorch`、`06_bayesian_mc`、`07_tensorflow_cpu`、`07b_gpflow_tf`、`08_rl_basic`、`09_huggingface_llm_cpu`、`10_onnx_api_app` | 1.32 GiB |
| `windows_python_offline_04_py310_part2_cn_en.tar` | Python 3.10 环境组：`11_optimization_control`、`12_scientific_extra`、`13_stats_optimize_extra`、`14_ml_extra`、`15_dl_pytorch_extra`、`16_timeseries_quant`、`17_nlp_classic`、`17b_nlp_sentence_transformers`、`18_vision_extra`、`19_av_extra`、`20_web_api_extra`、`21_database`、`22_crawler` | 1.36 GiB |
| `windows_python_offline_05_py310_part3_cn_en.tar` | Python 3.10 环境组：`22b_playwright`、`23_office_pdf`、`24_gui_tk`、`24b_gui_pyqt6`、`24c_gui_pyside6`、`24d_gui_wx`、`25_devtools`、`supplement`、`supplement_signal` | 525 MiB |
| `windows_python_offline_06_py312_part1_cn_en.tar` | Python 3.12 环境组：`01_base_scientific`、`02_ml_stats`、`03_signal_image_audio`、`04_pytorch_cpu`、`05_gpr_bo_pytorch`、`06_bayesian_mc`、`07_tensorflow_cpu`、`07b_gpflow_tf`、`08_rl_basic`、`09_huggingface_llm_cpu`、`10_onnx_api_app` | 1.30 GiB |
| `windows_python_offline_07_py312_part2_cn_en.tar` | Python 3.12 环境组：`11_optimization_control`、`12_scientific_extra`、`13_stats_optimize_extra`、`14_ml_extra`、`15_dl_pytorch_extra`、`16_timeseries_quant`、`17_nlp_classic`、`17b_nlp_sentence_transformers`、`18_vision_extra`、`19_av_extra`、`20_web_api_extra`、`21_database`、`22_crawler`、`22b_playwright` | 1.38 GiB |
| `windows_python_offline_08_py312_part3_cn_en.tar` | Python 3.12 环境组：`23_office_pdf`、`24_gui_tk`、`24b_gui_pyqt6`、`24c_gui_pyside6`、`24d_gui_wx`、`25_devtools`、`supplement`、`supplement_signal` | 468 MiB |
| `windows_python_offline_09_external_tessdata_cn_en.tar` | Tesseract 语言数据 eng、chi_sim、chi_sim_vert、osd | 18 MiB |

- 01（说明与清单）必下；02（Python 安装程序）首次使用时必下。
- 只用一个 Python 版本时，下载该版本的 3 个 part 即可（3.10 为 03–05，3.12 为 06–08）。每个 part 只含完整的环境组，只要某几组时也可以只下对应的 part。
- 09 是 Tesseract 语言数据，用 OCR 时再下。

## 解压

Windows 10/11 自带 `tar`：

```powershell
mkdir D:\wpo
cd D:\wpo
tar -xf "$env:USERPROFILE\Downloads\windows_python_offline_01_docs_required_cn_en.tar"
tar -xf "$env:USERPROFILE\Downloads\windows_python_offline_02_installers_cn_en.tar"
tar -xf "$env:USERPROFILE\Downloads\windows_python_offline_06_py312_part1_cn_en.tar"
# … 其余包同样解压到 D:\wpo
```

7-Zip 也可以解压。包内没有符号链接和硬链接：同一个 wheel 在多个环境组中各存一份完整文件。

## 校验

- 各包的 SHA256 见 Release 中的 `SHA256SUMS.txt`：`Get-FileHash <包>.tar -Algorithm SHA256`。
- `archive_index_cn.csv` 列出每个文件所在的包、大小和 SHA256。
- 解压后在库根运行 `powershell -ExecutionPolicy Bypass -File .\tools\verify_sha256_en.ps1`，按 `package_inventory_cn.csv` 逐个核对 wheel。

## 安装

见 `guides/windows_install_steps_cn.md`。本库**只做了静态检查，没有在 Windows 上实际安装验证**。
