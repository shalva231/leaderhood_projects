import pyautogui
import time



time.sleep(1)

for _ in range(200):
    pyautogui.typewrite("hello")
    pyautogui.press("enter")