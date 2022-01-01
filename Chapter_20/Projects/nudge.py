#!python3

import time, pyautogui

while True:
    print("nudging")
    pyautogui.moveRel(1, 0, 0.3)
    pyautogui.moveRel(-1, 0, 0.3)
    time.sleep(10)