"""
config.py - Configuration constants for Dino Bot

This file defines screen coordinates and detection thresholds used by the bot.
Adjust these values if your screen resolution, browser zoom, or DPI scaling is different.
"""

# (left, top, right, bottom) coordinates of the game region on the screen
# Used by capture_game_area() to take a focused screenshot of the Dino game
GAME_AREA = (670, 265, 830, 310)

# Pixel brightness threshold for detecting dark objects (e.g., cacti/birds)
# Lower values = darker pixels; tweak if detection fails or misfires
PIXEL_DARKNESS_THRESHOLD = 100

# Minimum number of dark pixels needed to consider it an obstacle
# Prevents false positives from minor noise in the image
OBSTACLE_PIXEL_COUNT = 45
