"""
screen_tools.py - Screen capture utility for the Google Dino Bot

This module captures a specific region of the screen where the Dino game is visible.
The coordinates are defined in config.py. The captured image is converted to
grayscale to simplify image processing and obstacle detection.
"""

from PIL import ImageGrab
from bot.config import GAME_AREA

def capture_game_area():
    """
    Captures a screenshot of the game area defined in config.py,
    and converts it to grayscale for analysis.

    Returns:
        PIL.Image: Grayscale image of the defined screen region.
    """
    # Capture a region of the screen using the bounding box (bbox)
    screenshot = ImageGrab.grab(bbox=GAME_AREA)

    # Convert the image to grayscale (mode 'L') for simpler pixel analysis
    return screenshot.convert("L")
