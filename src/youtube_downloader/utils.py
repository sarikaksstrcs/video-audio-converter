import os
import subprocess


def get_ffmpeg_path():
    """
    Detect ffmpeg location (Homebrew or system)
    
    Returns:
        str or None: Path to ffmpeg directory if found in non-standard location,
                    None if ffmpeg is available in PATH
    """
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


def validate_youtube_url(url):
    """
    Validate if URL is a YouTube URL
    
    Args:
        url (str): URL to validate
        
    Returns:
        bool: True if valid YouTube URL, False otherwise
    """
    return "youtube.com" in url or "youtu.be" in url


def format_duration(seconds):
    """
    Format duration in seconds to MM:SS format
    
    Args:
        seconds (int): Duration in seconds
        
    Returns:
        str: Formatted duration string
    """
    if not seconds:
        return "Unknown"
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}:{seconds:02d}"