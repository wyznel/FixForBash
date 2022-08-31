import os
import sys
import time 
import pyautogui




os.startfile("C:\\Program Files\\Git\\git-bash.exe")




txt = "alias ls='ls -F --color=auto --show-control-chars'"

time.sleep(0.5)


pyautogui.write(txt)

pyautogui.press("enter")

pyautogui.write("alias cls=clear")
pyautogui.press("enter")
pyautogui.write("alias subl='/c/Program\ Files/Sublime\ Text/subl.exe'")
pyautogui.press("enter")
pyautogui.write("cls")
pyautogui.press("enter")