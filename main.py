import time
from bot.detector import is_obstacle_in_path
from bot.controller import jump, start_game
from utils.screen_tools import capture_game_area

def countdown(seconds: int = 3):
    print("Dino Bot starting in:")
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)
    print("Go!\n")

def main():
    countdown()
    start_game()  # Automatically starts the game by pressing space

    time.sleep(1.5)  # Let the game begin and first obstacle appear

    while True:
        image = capture_game_area()
        if is_obstacle_in_path(image):
            jump()

if __name__ == "__main__":
    main()
