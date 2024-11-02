# src/main/__init__.py

"""
Nexus Hyperion - Main Application Package

Nexus Hyperion is an advanced intergalactic financial and resource management system.
This package serves as the core of the application, providing essential functionalities
for risk assessment, currency exchange, and resource optimization across civilizations.

Version: 1.0.0
Author: Your Name
License: MIT License
"""

__version__ = "1.0.0"
__author__ = "KOSASIH"
__email__ = "kosasihg88@gmail.com"
__description__ = "A high-tech financial and resource management system for intergalactic economies."
__license__ = "MIT"

# Importing necessary modules for easy access
from .app import main
from .config import Config
from .logger import setup_logger

# Expose key functionalities
__all__ = [
    "main",
    "Config",
    "setup_logger",
]
