
import pyscreenshot as ImageGrab
import PIL 
import win32api
import time 
import numpy as np
import pyautogui
import warnings
import cv2
import keyboard
import random

# filter warnings
warnings.filterwarnings('ignore')


def Random():
    r1 = random.uniform(0.4, 0.7)
    return round(r1, 2)


def DeadDecay():
    pyautogui.press('4')
    time.sleep(Random())
def Frost_Strike():
    pyautogui.press('3')
    time.sleep(Random())
def Howling_blast():
    pyautogui.press('8')
    time.sleep(Random())
def Interrupt():
    pyautogui.press('g')
    time.sleep(0.1)
def Oblitarate():
    pyautogui.press('2')
    time.sleep(Random())
def Pillar_of_frost():
    pyautogui.press('f')
    time.sleep(0.1)
def Remowless_winter():
    pyautogui.press('0')
    time.sleep(Random())
    


a=win32api.GetKeyState(49)
b=a


hb = cv2.imread('D:/Data/Wow/imgg2.jpg', cv2.TM_CCOEFF_NORMED)
fs = cv2.imread('D:/Data/Wow/imgg3.jpg', cv2.TM_CCOEFF_NORMED)
ob = cv2.imread('D:/Data/Wow/imgg1.jpg', cv2.TM_CCOEFF_NORMED)
        
while True:

    a=win32api.GetKeyState(49)
    
    if a == b:
        continue
        time.sleep(0.1)
        
    elif a!= b:
        
        """
        print("here")
        if keyboard.is_pressed('shift+f'):
            
            Remowless_winter()
            while True:
                print("while")
                Oblitarate()
                if keyboard.is_pressed('shift+f'):
                    pyautogui.press('f')
                    time.sleep(0.1)
                    pyautogui.press('9')
                    time.sleep(1.5)
                    pyautogui.press('5')
                    time.sleep(11.5)
                    break
        """    


        
        
        img=ImageGrab.grab(bbox=(0,820,385,1015))
        full = np.array(img)
        

        
         

        
        result=np.array([])
        
        resulthb = cv2.matchTemplate(full, hb, cv2.TM_CCOEFF_NORMED)
        min_val, max_val1, min_loc, max_loc = cv2.minMaxLoc(resulthb)
        
        
        resulthfs = cv2.matchTemplate(full, fs, cv2.TM_CCOEFF_NORMED)
        min_val, max_val2, min_loc, max_loc = cv2.minMaxLoc(resulthfs)    
        
        resulthob = cv2.matchTemplate(full, ob, cv2.TM_CCOEFF_NORMED)
        min_val, max_val2_2, min_loc, max_loc = cv2.minMaxLoc(resulthob)
        
        

        if max_val2_2 > 0.7:
            Oblitarate()
            
        
        else:
            if max_val1 > 0.7:
                Howling_blast()

            else: 
                if max_val2 > 0.7:
                    Frost_Strike()
                
                else:
            
                    Oblitarate()
                
            

                      
            """
            if b ==1:
                b=0
            elif b==0:
                b=1
            """
