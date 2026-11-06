# 外部工具

浏览器、浏览器驱动、FFmpeg 和 Tesseract 安装程序都**没有放进包里**，各目录下只有同名 `.url` 占位文件，内含官方下载链接、版本、大小、SHA256 与许可说明。

| 目录 | 内容 | 用途 |
| --- | --- | --- |
| `chrome/` | Chrome for Testing 157（浏览器、无头版） | Selenium / 爬虫 |
| `chromedriver/` | ChromeDriver 157 | Selenium 驱动 Chrome |
| `msedgedriver/` | Edge WebDriver 156 | Selenium 驱动 Edge（版本需与本机 Edge 一致） |
| `ffmpeg/` | FFmpeg 9.0.2 essentials | moviepy / pydub 等音视频处理 |
| `tesseract/` | Tesseract OCR 5.4.0 安装程序 | OCR |
| `tessdata/` | eng、chi_sim、chi_sim_vert、osd 语言数据（**已包含**，Apache-2.0） | Tesseract 识别中英文 |
| `playwright/` | 说明 | Playwright 浏览器需在联网机器上用 `playwright install` 获取 |

下载后可用 PowerShell 核对：`Get-FileHash <文件> -Algorithm SHA256`，与 `.url` 中的 `SHA256=` 比较。标为 `unverified` 的两个 Chrome 压缩包超过 100 MiB，未下载核对。
