"""
main.py - Entry point for the Google Dino Bot

This script starts and runs the Dino bot, which:
- Automatically starts the Chrome Dino game
- Continuously captures the game screen
- Uses image analysis to detect obstacles
- Jumps when an obstacle is detected

To use:
1. Open Chrome and navigate to chrome://dino
2. Make sure the Dino game is visible on screen
3. Run this script while the Chrome window is focused
"""

import time
from bot.detector import is_obstacle_in_path        # Obstacle detection logic
from bot.controller import jump, start_game         # Game control functions
from utils.screen_tools import capture_game_area    # Screen capture function

def countdown(seconds: int = 3):
    """
    Displays a countdown in the terminal before the bot starts.
    Useful for giving the user time to switch to the game window.
    """
    print("Dino Bot starting in:")
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)
    print("Go!\n")

def main():
    """
    Main function that runs the Dino Bot:
    - Starts the game
    - Continuously captures the screen
    - Jumps if an obstacle is detected
    """
    countdown()
    start_game()  # Presses space to start the Dino game

    time.sleep(1.5)  # Give the game time to load and the first obstacle to appear

    while True:
        # Capture a grayscale screenshot of the game area
        image = capture_game_area()

        # Check if an obstacle is detected in the screenshot
        if is_obstacle_in_path(image):
            jump()  # Simulate a spacebar press to make the Dino jump

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
