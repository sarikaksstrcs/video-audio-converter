#  Audio Downloader

A Python tool to download audio from videos as MP3 files using `yt-dlp` and `ffmpeg`.

## Features

- Download audio from YouTube videos in MP3 format
- Automatic ffmpeg detection (supports Homebrew installations)
- Custom output directory support
- Video information display (title, duration)
- Command-line and interactive usage
- Cross-platform compatibility

## Installation

### Prerequisites

1. **Python 3.7+** is required
2. **ffmpeg** must be installed:
   - **macOS (Homebrew)**: `brew install ffmpeg`
   - **Ubuntu/Debian**: `sudo apt update && sudo apt install ffmpeg`
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html)

### Install the Package

#### Option 1: Quick Setup with Virtual Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/youtube-audio-downloader.git
cd youtube-audio-downloader

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

#### Option 2: Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/youtube-audio-downloader.git
cd youtube-audio-downloader

# Use the provided Makefile for easy setup
make setup

# Or manually:
make venv          # Create virtual environment
make install       # Install dependencies
make install-dev   # Install development dependencies
```

#### Option 3: Direct Installation

```bash
# Install in development mode (recommended for contributors)
pip install -e .

# Or install from PyPI (when published)
pip install youtube-audio-downloader
```

## Usage

### Command Line

```bash
# Basic usage
python main.py

# With URL as argument
python main.py "https://www.youtube.com/watch?v=VIDEO_ID"

# Using the installed package
youtube-downloader "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Programmatic Usage

```python
from src.youtube_downloader import download_audio

# Download with default settings
download_audio("https://www.youtube.com/watch?v=VIDEO_ID")

# Download to custom directory
download_audio("https://www.youtube.com/watch?v=VIDEO_ID", "./my_music")
```

## Configuration

The downloader automatically:
- Creates the output directory if it doesn't exist
- Detects ffmpeg installation (including Homebrew paths)
- Uses 192 kbps MP3 quality by default
- Sanitizes filenames for cross-platform compatibility

## Project Structure

```
youtube-audio-downloader/
├── src/youtube_downloader/    # Main package
├── tests/                     # Unit tests
├── examples/                  # Usage examples
├── downloads/                 # Default download directory
└── main.py                   # CLI entry point
```

## Virtual Environment Management

This project uses Python virtual environments to manage dependencies and ensure consistent development environments.

### Quick Start

```bash
# Create virtual environment
make venv

# Activate virtual environment
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows

# Install dependencies
make install

# When done working
deactivate
```

### Manual Virtual Environment Setup

```bash
# Create virtual environment
python3 -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# For development
pip install -r requirements-dev.txt

# Deactivate when done
deactivate
```

## Development

```bash
# Set up development environment
make setup

# Run tests
make test

# Run linting
make lint

# Format code
make format

# Install development dependencies manually
pip install -r requirements-dev.txt
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational and personal use only. Please respect YouTube's Terms of Service and copyright laws. Only download content you have permission to download.

## Troubleshooting

### Common Issues

- **"ffmpeg not found"**: Install ffmpeg using your system's package manager
- **Download errors**: Check if the YouTube URL is valid and accessible
- **Permission errors**: Ensure you have write permissions to the output directory

### Support

If you encounter issues, please [open an issue](https://github.com/yourusername/youtube-audio-downloader/issues) with:
- Your operating system
- Python version
- Error message (if any)
- YouTube URL (if public)
