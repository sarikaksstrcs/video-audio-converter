import os
import sys
import yt_dlp
from pathlib import Path

from .utils import get_ffmpeg_path, validate_youtube_url, format_duration


def download_audio(youtube_url, output_path="./downloads"):
    """
    Download audio from YouTube video as MP3
    
    Args:
        youtube_url (str): YouTube video URL
        output_path (str): Output directory path
        
    Returns:
        bool: True if download successful, False otherwise
    """
    # Create output directory if it doesn't exist
    Path(output_path).mkdir(parents=True, exist_ok=True)

    # Get ffmpeg path
    ffmpeg_location = get_ffmpeg_path()

    # Configure yt-dlp options
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
            print(f"Duration: {format_duration(duration)}")
            print("Starting download...")
            
            ydl.download([youtube_url])
            print(f"✅ Successfully downloaded: {title}")
            return True
            
    except yt_dlp.utils.DownloadError as e:
        print(f"❌ Download error: {e}")
        return False
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return False


def main():
    """Main CLI function"""
    print("🎵 YouTube Audio Downloader")
    print("=" * 40)

    # Get URL from command line argument or user input
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter YouTube URL: ").strip()

    if not url:
        print("❌ No URL provided!")
        return

    if not validate_youtube_url(url):
        print("❌ Please provide a valid YouTube URL!")
        return

    # Get output directory
    output_dir = input("Enter output directory (press Enter for './downloads'): ").strip()
    if not output_dir:
        output_dir = "./downloads"

    # Download audio
    success = download_audio(url, output_dir)
    
    if success:
        print(f"\n🎉 Download completed! Files saved to: {os.path.abspath(output_dir)}")
    else:
        print("\n❌ Download failed. Please check the URL and try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Download cancelled by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")