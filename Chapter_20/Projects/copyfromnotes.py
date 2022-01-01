#!python3

import pyautogui
import time, subprocess, pyperclip

subprocess.Popen(['/usr/bin/gnome-text-editor','chaptertwenty/notes'])

time.sleep(4)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

text = pyperclip.paste()
print(text)