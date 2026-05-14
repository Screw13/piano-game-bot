import pyautogui as pp 
import time
import keyboard
import pydirectinput

y = 470

while keyboard.is_pressed('x') == False:
    if pp.pixel(600,y)[0] == 0:
        pp.mouseDown(600,y)
        time.sleep(0.01)
        pp.mouseUp(600,y)

    if pp.pixel(680,y)[0] == 0:
        pp.mouseDown(680,y)
        time.sleep(0.01)
        pp.mouseUp(680,y)
        

    if pp.pixel(770,y)[0] == 0:
        pp.mouseDown(770,y)
        time.sleep(0.01)
        pp.mouseUp(770,y)

    if pp.pixel(855,y)[0] == 0:
        pp.mouseDown(855,y)
        time.sleep(0.01)
        pp.mouseUp(855,y)
