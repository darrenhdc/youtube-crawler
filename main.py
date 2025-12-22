import subprocess
import os
import glob
import sys

def download_youtube_video(url):
    """使用yt-dlp下载YouTube视频"""
    try:
        print(f"正在从YouTube下载视频：{url}")

        # 构建yt-dlp命令，下载webm格式
        cmd = [
            "yt-dlp",
            "-f", "bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]",  # 下载webm格式
            "--merge-output-format", "webm",
            url
        ]

        subprocess.run(cmd, check=True)
        print(f"✓ 视频下载成功")

    except subprocess.CalledProcessError as e:
        print(f"✗ 视频下载失败")
        print(f"错误信息：{e.stderr.decode('utf-8') if e.stderr else str(e)}")
        return False
    except KeyboardInterrupt:
        print("\n用户中断了下载")
        return False

    return True

def convert_webm_to_mp4():
    """将当前目录下的webm文件转换为mp4格式"""
    webm_files = glob.glob("*.webm")

    if not webm_files:
        print("当前目录下没有找到webm格式的视频文件")
        return False

    print(f"\n找到 {len(webm_files)} 个webm文件，开始转换为mp4格式：")

    success_count = 0

    for webm_file in webm_files:
        mp4_file = os.path.splitext(webm_file)[0] + ".mp4"

        try:
            print(f"\n正在转换：{webm_file} -> {mp4_file}")

            cmd = [
                "ffmpeg",
                "-i", webm_file,
                "-c:v", "libx264",
                "-c:a", "aac",
                "-strict", "experimental",
                "-y",  # 自动覆盖已存在的文件
                mp4_file
            ]

            subprocess.run(cmd, check=True, capture_output=True)
            print(f"✓ 转换成功：{mp4_file}")
            success_count += 1

            # 转换完成后可以选择删除原webm文件
            # os.remove(webm_file)
            # print(f"已删除原文件：{webm_file}")

        except subprocess.CalledProcessError as e:
            print(f"✗ 转换失败：{webm_file}")
            print(f"错误信息：{e.stderr.decode('utf-8')}")
        except KeyboardInterrupt:
            print("\n用户中断了转换")
            return False

    print(f"\n转换任务完成！成功转换 {success_count} 个文件")
    return True

def main():
    """主函数"""
    # 检查是否提供了YouTube链接参数
    if len(sys.argv) < 2:
        print("使用方法：python3 main.py <YouTube_URL>")
        print("\n示例：")
        print("python3 main.py \"https://www.youtube.com/watch?v=CbZgAvfrYX8\"")
        return

    url = sys.argv[1]

    # 下载视频
    if not download_youtube_video(url):
        return

    # 转换为mp4格式
    if not convert_webm_to_mp4():
        return

    print("\n🎉 所有任务完成！")

if __name__ == "__main__":
    main()
