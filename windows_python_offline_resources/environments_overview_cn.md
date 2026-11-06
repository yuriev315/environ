# 环境组总览

每组在两棵版本树中各有一份：`python310_amd64/environments/<组>_py310` 与 `python312_amd64/environments/<组>_py312`。每组自带完整 `wheelhouse/`，可单独安装。

| 组 | 用途 | 3.10 分发包数 / 大小 | 3.12 分发包数 / 大小 | 需另下的大文件 |
| --- | --- | --- | --- | --- |
| `01_base_scientific` | 科学计算基础：数组、数据表、绘图、Jupyter | 116 / 142 MiB | 113 / 138 MiB | — |
| `02_ml_stats` | 机器学习与统计建模 | 30 / 304 MiB | 30 / 270 MiB | — |
| `03_signal_image_audio` | 信号、图像、音频处理 | 41 / 184 MiB | 41 / 180 MiB | — |
| `04_pytorch_cpu` | PyTorch CPU 版 | 25 / 44 MiB | 25 / 46 MiB | torch |
| `05_gpr_bo_pytorch` | 高斯过程回归与贝叶斯优化（PyTorch） | 45 / 96 MiB | 42 / 95 MiB | torch |
| `06_bayesian_mc` | 贝叶斯推断与蒙特卡洛 | 42 / 93 MiB | 44 / 132 MiB | — |
| `07_tensorflow_cpu` | TensorFlow CPU 版 | 48 / 88 MiB | 43 / 83 MiB | tensorflow |
| `07b_gpflow_tf` | GPflow 高斯过程（TensorFlow） | 59 / 124 MiB | 54 / 116 MiB | tensorflow |
| `08_rl_basic` | 强化学习基础 | 33 / 63 MiB | 33 / 64 MiB | torch |
| `09_huggingface_llm_cpu` | Hugging Face 大模型 CPU 推理与微调 | 63 / 88 MiB | 61 / 88 MiB | torch |
| `10_onnx_api_app` | ONNX 推理与 API / Web 应用 | 62 / 123 MiB | 56 / 115 MiB | — |
| `11_optimization_control` | 优化与控制 | 27 / 153 MiB | 30 / 150 MiB | — |
| `12_scientific_extra` | 科学计算扩展 | 34 / 187 MiB | 32 / 187 MiB | — |
| `13_stats_optimize_extra` | 统计与调参扩展 | 53 / 110 MiB | 52 / 107 MiB | — |
| `14_ml_extra` | 机器学习扩展与可解释性 | 43 / 150 MiB | 42 / 146 MiB | — |
| `15_dl_pytorch_extra` | PyTorch 深度学习扩展 | 51 / 56 MiB | 49 / 57 MiB | torch |
| `16_timeseries_quant` | 时间序列与量化 | 51 / 158 MiB | 51 / 154 MiB | — |
| `17_nlp_classic` | 经典自然语言处理 | 65 / 134 MiB | 64 / 130 MiB | — |
| `17b_nlp_sentence_transformers` | 句向量与向量检索 | 42 / 109 MiB | 41 / 104 MiB | torch |
| `18_vision_extra` | 计算机视觉扩展 | 30 / 172 MiB | 30 / 168 MiB | — |
| `19_av_extra` | 音视频处理 | 16 / 78 MiB | 16 / 77 MiB | — |
| `20_web_api_extra` | Web 与 API 开发 | 35 / 17 MiB | 34 / 17 MiB | — |
| `21_database` | 数据库访问 | 22 / 46 MiB | 20 / 46 MiB | — |
| `22_crawler` | 网页抓取 | 52 / 25 MiB | 50 / 24 MiB | — |
| `22b_playwright` | Playwright 浏览器自动化（浏览器本体需另行下载） | 22 / 41 MiB | 20 / 41 MiB | — |
| `23_office_pdf` | Office 与 PDF 文档处理 | 19 / 49 MiB | 19 / 48 MiB | — |
| `24_gui_tk` | Tkinter 图形界面 | 15 / 32 MiB | 15 / 33 MiB | — |
| `24b_gui_pyqt6` | PyQt6 图形界面 | 7 / 97 MiB | 7 / 97 MiB | — |
| `24c_gui_pyside6` | PySide6 图形界面 | 5 / 77 MiB | 4 / 77 MiB | pyside6-addons |
| `24d_gui_wx` | wxPython 图形界面 | 4 / 32 MiB | 2 / 19 MiB | — |
| `25_devtools` | 开发、测试与打包工具 | 82 / 48 MiB | 78 / 48 MiB | — |
| 补充包 `python3xx_amd64_supplement` | 补充：金融数据与常用工具（另含源码包） | 55 / 149 MiB | 55 / 144 MiB | — |
| 信号补充 `python3xx_amd64_supplement_signal` | 补充：EMD / 小波 / 卡尔曼滤波 | 11 / 1 MiB | 11 / 1 MiB | — |

分发包数含每组随附的 pip 26.2 wheel（补充包另含构建源码包用的 setuptools、wheel）；信号补充只计新增 wheel。需另下的大文件见各组 `README_cn.md` 与库根 `placeholders_cn.csv`。
