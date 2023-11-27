import pyautogui
import time
time.sleep(3)
count=0
while count<=50:
    pyautogui.typewrite("kya hal hai bhai ke")
    pyautogui.press("enter")
    count=count+1
