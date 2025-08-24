.PHONY: help setup venv install install-dev test lint format clean build upload

# Default Python version
PYTHON := python3
VENV_DIR := venv
PIP := $(VENV_DIR)/bin/pip
PYTHON_VENV := $(VENV_DIR)/bin/python

# Help target
help:
	@echo "Available commands:"
	@echo "  setup       - Complete setup (venv + dependencies)"
	@echo "  venv        - Create virtual environment"
	@echo "  install     - Install production dependencies"
	@echo "  install-dev - Install development dependencies"
	@echo "  test        - Run tests with coverage"
	@echo "  lint        - Run linting (flake8, mypy)"
	@echo "  format      - Format code (black, isort)"
	@echo "  clean       - Remove build artifacts and cache"
	@echo "  build       - Build distribution packages"
	@echo "  upload      - Upload to PyPI (requires credentials)"

# Complete setup
setup: venv install-dev
	@echo "✅ Development environment ready!"
	@echo "💡 Activate with: source $(VENV_DIR)/bin/activate"

# Create virtual environment
venv:
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "🐍 Creating virtual environment..."; \
		$(PYTHON) -m venv $(VENV_DIR); \
		echo "✅ Virtual environment created at $(VENV_DIR)"; \
	else \
		echo "✅ Virtual environment already exists"; \
	fi

# Install production dependencies
install: venv
	@echo "📦 Installing production dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "✅ Production dependencies installed"

# Install development dependencies
install-dev: install
	@echo "🔧 Installing development dependencies..."
	$(PIP) install -r requirements-dev.txt
	$(PIP) install -e .
	@echo "✅ Development dependencies installed"

# Run tests
test:
	@echo "🧪 Running tests with coverage..."
	$(PYTHON_VENV) -m pytest tests/ -v --cov=src/youtube_downloader --cov-report=html --cov-report=term
	@echo "📊 Coverage report generated in htmlcov/"

# Run linting
lint:
	@echo "🔍 Running linting..."
	$(PYTHON_VENV) -m flake8 src/ tests/ main.py
	$(PYTHON_VENV) -m mypy src/ --ignore-missing-imports
	@echo "✅ Linting completed"

# Format code
format:
	@echo "🎨 Formatting code..."
	$(PYTHON_VENV) -m black src/ tests/ main.py examples/
	$(PYTHON_VENV) -m isort src/ tests/ main.py examples/
	@echo "✅ Code formatted"

# Clean build artifacts
clean:
	@echo "🧹 Cleaning up..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete
	@echo "✅ Cleanup completed"

# Build distribution packages
build: clean
	@echo "📦 Building distribution packages..."
	$(PYTHON_VENV) -m build
	@echo "✅ Build completed - check dist/ directory"

# Upload to PyPI
upload: build
	@echo "🚀 Uploading to PyPI..."
	$(PYTHON_VENV) -m twine upload dist/*
	@echo "✅ Upload completed"

# Development server (if you add a web interface later)
dev:
	@echo "🔧 Starting development server..."
	$(PYTHON_VENV) main.py