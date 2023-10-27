import os
import keyboard
import webbrowser
import pyautogui
import time
import mss
import mss.tools
def messages(text):
      os.system("open /Applications/messages.app")
      while True:
            keyboard.write(text)
            keyboard.send('enter')
      

def email(email, text):
      #webbrowser.open('https://mail.google.com/')
      #time.sleep(10)
      pyautogui.click(36,222)
      while True:
            pyautogui.click(36,222)
            time.sleep(1)
            pyautogui.click(301,402)
            time.sleep(1)
            pyautogui.click(301,402)
            time.sleep(1)
            pyautogui.write(email)
            pyautogui.hotkey('enter')
            time.sleep(.5)
            pyautogui.click(277, 434)
            pyautogui.write(text)
            pyautogui.hotkey('command', 'enter')
            time.sleep(.2)


