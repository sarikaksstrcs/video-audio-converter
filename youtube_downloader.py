#!/usr/bin/env python3
"""
YouTube Audio Downloader
Downloads audio from YouTube videos as MP3 files.
"""

import os
import sys
import yt_dlp
import subprocess
from pathlib import Path

# Detect ffmpeg location (Homebrew or system)
def get_ffmpeg_path():
    try:
        # Check if ffmpeg is available in PATH
        subprocess.run(['ffmpeg', '-version'],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL,
                       check=True)
        return None  # PATH is fine, let yt-dlp auto-detect
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Check common Homebrew path
        homebrew_path = "/opt/homebrew/bin/ffmpeg"
        if os.path.exists(homebrew_path):
            return "/opt/homebrew/bin"
        return None

def download_audio(youtube_url, output_path="./downloads"):
    """
    Download audio from YouTube video as MP3
    """
    Path(output_path).mkdir(parents=True, exist_ok=True)

    ffmpeg_location = get_ffmpeg_path()

    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    # Pass ffmpeg location if detected
    if ffmpeg_location:
        ydl_opts['ffmpeg_location'] = ffmpeg_location

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Fetching video information...")
            info = ydl.extract_info(youtube_url, download=False)
            title = info.get('title', 'Unknown')
            duration = info.get('duration', 0)
            print(f"Title: {title}")
            print(f"Duration: {duration // 60}:{duration % 60:02d}")
            print("Starting download...")
            ydl.download([youtube_url])
            print(f"✅ Successfully downloaded: {title}")
    except yt_dlp.utils.DownloadError as e:
        print(f"❌ Download error: {e}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

def main():
    print("🎵 YouTube Audio Downloader")
    print("=" * 40)

    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter YouTube URL: ").strip()

    if not url:
        print("❌ No URL provided!")
        return

    if "youtube.com" not in url and "youtu.be" not in url:
        print("❌ Please provide a valid YouTube URL!")
        return

    output_dir = input("Enter output directory (press Enter for './downloads'): ").strip()
    if not output_dir:
        output_dir = "./downloads"

    download_audio(url, output_dir)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Download cancelled by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
