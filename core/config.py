"""
Configuration management for CryptoMatrix
Handles app settings and constants
"""

import os
from pathlib import Path


# App metadata
APP_NAME = "CryptoMatrix"
APP_VERSION = "0.1"

# Directories
APP_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent
DATA_DIR = APP_DIR / "data"
LOGS_DIR = APP_DIR / "logs"

# Create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

# Database
DATABASE_PATH = DATA_DIR / "cryptomatrix.db"

# Logging
LOG_FILE = LOGS_DIR / "app.log"
LOG_LEVEL = "INFO"

# UI
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 1920
