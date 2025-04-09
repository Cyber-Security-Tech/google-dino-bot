from PIL import ImageGrab
from bot.config import GAME_AREA

def capture_game_area():
   
    screenshot = ImageGrab.grab(bbox=GAME_AREA)
    return screenshot.convert("L")  # Convert to grayscale
