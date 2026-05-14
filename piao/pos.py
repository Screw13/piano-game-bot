import pyautogui as pp
import keyboard

a = 1

while not keyboard.is_pressed('x'):
    if keyboard.is_pressed("p"):
        if a == 1:
            a += 1
            print(pp.position())
    if keyboard.is_pressed('o'):
        a =1