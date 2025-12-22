# YouTube 视频下载与格式转换工具

这是一个使用 Python 编写的工具，可以从 YouTube 下载视频并自动将其转换为 mp4 格式。该工具结合了 `yt-dlp` 和 `ffmpeg` 的强大功能。

## 功能特点

- **自动下载**：只需提供 YouTube 链接即可自动下载视频
- **批量转换**：下载完成后自动将 webm 格式转换为 mp4 格式
- **高质量**：使用最佳视频和音频质量下载
- **自动覆盖**：转换时自动覆盖已存在的文件
- **错误处理**：完善的错误处理和用户反馈机制
- **命令行界面**：简单易用的命令行参数

## 技术依赖

该工具需要以下外部依赖：

1. **Python 3**：推荐 Python 3.7 或更高版本
2. **yt-dlp**：用于下载 YouTube 视频
3. **ffmpeg**：用于视频格式转换

## 安装说明

### 1. 安装 Python 3

请从 [Python 官网](https://www.python.org/downloads/) 下载并安装最新版本的 Python 3。

### 2. 安装 yt-dlp

使用 pip 安装 yt-dlp：
```bash
pip3 install yt-dlp
```

### 3. 安装 ffmpeg

- **macOS (Homebrew)**：
  ```bash
  brew install ffmpeg
  ```

- **Ubuntu/Debian**：
  ```bash
  sudo apt-get install ffmpeg
  ```

- **Windows**：
  从 [ffmpeg 官网](https://ffmpeg.org/download.html) 下载，并将 ffmpeg.exe 所在目录添加到系统环境变量 Path 中。

## 使用方法

### 基本用法

```bash
python3 main.py "YOUTUBE_URL"
```

### 示例

```bash
python3 main.py "https://www.youtube.com/watch?v=CbZgAvfrYX8"
```

### 注意事项

- **URL 必须加引号**：由于 YouTube 链接包含特殊字符（如 `?` 和 `&`），必须使用引号将 URL 括起来
- **下载位置**：下载和转换后的文件将保存在当前目录中
- **转换后文件**：mp4 文件将与原文件名相同，仅扩展名不同
- **原文件保留**：默认会保留下载的 webm 文件，可以在脚本中取消注释相关代码以自动删除原文件

## 脚本结构

```python
main.py
├── download_youtube_video(): 使用yt-dlp下载视频
├── convert_webm_to_mp4(): 转换webm到mp4
└── main(): 主函数，处理命令行参数和流程控制
```

## 配置选项

你可以根据需要修改脚本中的以下参数：

1. **视频质量**：修改 `yt-dlp` 命令中的 `-f` 参数
2. **转换格式**：修改 ffmpeg 命令中的编码参数
3. **自动删除原文件**：取消注释 `os.remove(webm_file)` 行

## 许可证

这个项目采用 MIT 许可证，你可以自由使用和修改。

## 反馈

如有任何问题或建议，欢迎提出！
