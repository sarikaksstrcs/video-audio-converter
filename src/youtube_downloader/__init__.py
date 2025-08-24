
"""
YouTube Audio Downloader Package
"""

from .downloader import download_audio
from .utils import get_ffmpeg_path

__version__ = "1.0.0"
__all__ = ["download_audio", "get_ffmpeg_path"]

