# 🦖 Google Dino Bot (Day Mode)

An automated bot that plays the Google Chrome Dino game by detecting obstacles in real time and jumping to avoid them — entirely hands-free.

---

## 🚀 Overview

This project uses `pyautogui` and `Pillow` to:
- Take rapid screenshots of the game
- Analyze a fixed region for upcoming obstacles
- Trigger a spacebar press (jump) when an obstacle is detected

---

## 🧠 What I Learned

- **Screen automation** with `pyautogui`
- **Image processing** using `Pillow`
- **Real-time obstacle detection** with pixel thresholding
- **Jump buffering** to avoid false positives or premature reactions
- **Structuring a Python project** with clear separation of concerns
- **Using Git & GitHub** for version control

---

## 🛠 Technologies Used

- Python 3
- `pyautogui`
- `Pillow`
- `time`
- `os` / basic standard libraries

---

## 🧪 How It Works

- Captures a specific portion of the screen where obstacles appear
- Converts the screenshot to grayscale
- Counts dark pixels using a pixel brightness threshold
- If enough dark pixels are found (indicating an obstacle), it jumps

---

## 🌌 Future Enhancements: Night Mode Support

In night mode, the game background turns dark and the obstacles become lighter (gray), which reverses the pixel brightness logic used in day mode.

To support this:
1. Calculate the **average brightness** of the captured image.
2. If the brightness is **below a certain threshold** (e.g. < 128), assume night mode is active.
3. **Reverse the detection logic**:
   - In **day mode**, look for pixels **darker** than the threshold.
   - In **night mode**, look for pixels **lighter** than a separate light threshold.

This dynamic switching will allow the bot to adapt to the game’s visual changes without relying on templates or hardcoding specific obstacle types.

---

## 🧾 License

MIT License