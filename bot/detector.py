from PIL import Image
from bot.config import PIXEL_DARKNESS_THRESHOLD, OBSTACLE_PIXEL_COUNT

def is_obstacle_in_path(image: Image.Image) -> bool:
    """
    Checks if the captured grayscale image has enough dark pixels
    to be considered an obstacle.
    """
    dark_pixel_count = 0
    width, height = image.size

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            if pixel < PIXEL_DARKNESS_THRESHOLD:
                dark_pixel_count += 1
                if dark_pixel_count >= OBSTACLE_PIXEL_COUNT:
                    return True
    return False
