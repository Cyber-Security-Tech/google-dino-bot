"""
controller.py - Simulates keyboard inputs for controlling the Dino game

This module uses pyautogui to:
- Start the game by pressing the spacebar
- Make the Dino jump when an obstacle is detected
"""

import pyautogui

def jump():
    """
    Simulates a spacebar press to make the Dino jump.
    Called when an obstacle is detected in the bot loop.
    """
    pyautogui.press("space")

def start_game():
    """
    Starts or restarts the game by pressing space.
    Should be called once after countdown.
    """
    pyautogui.press("space")
