"""
detector.py - Obstacle detection logic for the Google Dino Bot

This module analyzes a grayscale image of the game area and counts how many
pixels fall below a brightness threshold. If the number of dark pixels exceeds
a defined limit, it determines that an obstacle (like a cactus or bird) is present.
"""

from PIL import Image
from bot.config import PIXEL_DARKNESS_THRESHOLD, OBSTACLE_PIXEL_COUNT

def is_obstacle_in_path(image: Image.Image) -> bool:
    """
    Checks if the captured grayscale image contains enough dark pixels
    to be considered an obstacle.

    Args:
        image (PIL.Image): Grayscale screenshot of the game area.

    Returns:
        bool: True if obstacle is detected, False otherwise.
    """
    dark_pixel_count = 0
    width, height = image.size

    # Loop through each pixel in the image
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))  # Pixel value ranges from 0 (black) to 255 (white)

            # If the pixel is dark enough, count it
            if pixel < PIXEL_DARKNESS_THRESHOLD:
                dark_pixel_count += 1

                # If enough dark pixels are found, return True (obstacle detected)
                if dark_pixel_count >= OBSTACLE_PIXEL_COUNT:
                    return True

    # If not enough dark pixels are found, return False (no obstacle)
    return False
