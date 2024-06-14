import pyautogui
import time


pyautogui.leftClick(x=605, y=1068,duration=1)
pyautogui.leftClick(x=27, y=114,duration=1)
pyautogui.leftClick(x=622, y=998,duration=1)


for i in range(100):
    time.sleep(1)
    pyautogui.typewrite("GOA THE BEST")
    pyautogui.hotkey("enter")
    