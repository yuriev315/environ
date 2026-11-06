# 许可说明

- 所有 wheel 与源码包均原样来自 PyPI，各自遵循其许可证（见 `package_inventory_cn.csv` 的 `license` 列及 wheel 内的许可文件）。
- 以下 PyPI wheel 内含 GPL / LGPL 或第三方二进制，按其许可证可再分发，源码可从各项目或 PyPI 源码包获得：
  - `av`（PyAV）：捆绑 FFmpeg 及 x264 / x265（GPL）。
  - `imageio-ffmpeg`：捆绑 FFmpeg 可执行文件。
  - `opencv-python`、`opencv-python-headless`：捆绑 FFmpeg（LGPL）视频后端。
  - `pyqt6`（GPL-3.0）、`pyqt6-qt6`、`pyside6-essentials`（LGPL-3.0，Qt）。
  - `pymupdf`：AGPL-3.0（或 Artifex 商业许可）。
  - `pyinstaller`：GPL-2.0（带引导程序例外）。
- Python 安装程序：PSF License 2.0。
- `external/tessdata/`：Apache-2.0（tesseract-ocr/tessdata_fast）。
- 微软、谷歌的专有二进制，以及 Git for Windows、FFmpeg、Tesseract 安装程序未放入本库，只提供 `.url` 占位文件（官方链接、大小、SHA256）。清单见 `placeholders_cn.csv`。
