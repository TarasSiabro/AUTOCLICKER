from pyautogui import *
import pyautogui
import time
import win32api, win32con
import pygetwindow as gw
from threading import Thread
import keyboard
from tkinter import *


def click(x,y):

    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0 ,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)



    
def main():

    global A
    blumWindow = gw.getWindowsWithTitle('TelegramDesktop')[0]
    left_window = blumWindow.left
    top_window = blumWindow.top
    bottom_of_window = blumWindow.bottom
    width_of_window = blumWindow.width
    height_of_window = blumWindow.height
    pause_button = False
    games_counter = 0

    print('Пробел - запустить, Q - пауза.')
    
    blumWindow.activate()


    while True:
        if keyboard.is_pressed('Space'):
            pause_button = True
        while pause_button:

        
                # pyinstaller -F main.py
            pic = pyautogui.screenshot(region=(left_window,top_window + int(height_of_window - height_of_window//1.3),width_of_window,int(height_of_window//1.3)))
            width, height = pic.size

            for x in range (0, width, 3):
                for y in range(0, height, 3):
                    r,g,b = pic.getpixel((x, y))
                    if(g in range(200, 255)) and (r in range(180,229)) and b <= 60:
                        click(x + left_window, y + top_window + int(height_of_window - height_of_window//1.3))
                        time.sleep(0.001)
                        break
                
            pyautogui.useImageNotFoundException()

            try:
                location = pyautogui.locateOnScreen('play_buttom.png', confidence = 0.8)
                pyautogui.click(location)
                games_counter += 1
                print(games_counter, 'Игр сыграно, 0 проигано')
            except pyautogui.ImageNotFoundException:
                None
            
            if keyboard.is_pressed("q"):
                pause_button = False
                print('Что бы продолжить ебани пробел')
                break
    

Thread(target=main).start()
