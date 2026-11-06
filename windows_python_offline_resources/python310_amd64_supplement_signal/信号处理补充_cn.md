# Windows Python 3.10.11 信号处理补充

在 `python310_amd64\environments\03_signal_image_audio_py310` 环境上追加安装，不修改该环境的 `requirements_lock_en.txt`。

## 覆盖范围

| 能力 | 包 | 说明 |
| --- | --- | --- |
| 傅里叶 / 频谱 | NumPy、SciPy | 已在 03 组，本包不重复存放 |
| 小波分解与重构 | PyWavelets | 已在 03 组 |
| EMD / EEMD / CEEMDAN | **EMD-signal** 1.10.0 | pip 名 `EMD-signal`，**导入名 `PyEMD`** |
| Kalman 实时滤波 | filterpy 2.0.0 | `predict` / `update`，因果 |
| Kalman 离线平滑 | pykalman 0.11.2 | `filter` 因果；`smooth` 使用未来观测，仅离线 |

`packages_wheel/` 只放 03 组之外新增的 wheel（EMD-signal、filterpy、pykalman 及 pathos、pox、ppft、dill、multiprocess、scikit-base、tqdm、colorama）。清单见 `inventory_cn.csv`，复用 03 组的文件见 `reused_from_original_cn.csv`。带 SHA256 的完整锁定清单（03 组 + 本补充）见 `requirements_supplement_lock_en.txt`。

## 安装

先按 `python310_amd64\environments\03_signal_image_audio_py310\README_cn.md` 装好 03 环境（会在该目录下生成 `.venv`），然后在库根目录（例如 `D:\wpo\windows_python_offline_resources`）下进入本目录运行：

```powershell
cd python310_amd64_supplement_signal
powershell -ExecutionPolicy Bypass -File .\install_supplement_en.ps1
```

脚本只安装 `requirements_supplement_en.txt` 中的新增包，依赖从 `packages_wheel/` 和 03 组的 `wheelhouse/` 解析。必须使用 CPython 3.10.11。

## 实时滤波 vs 离线平滑

- **实时 / 因果**：`filterpy.kalman.KalmanFilter.predict` + `update`，或 `pykalman.KalmanFilter.filter`。时刻 t 的输出只依赖 `z[0]..z[t]`。
- **离线平滑**：`pykalman.KalmanFilter.smooth`（RTS）。时刻 t 的输出依赖 `z[0]..z[N-1]`，含未来观测。滞后更小、误差通常更低，**不能**接到必须在采样时刻给出估计的控制回路。

## 示例

`examples/` 下 4 个脚本仅作最小调用示意，**未执行验证**。
