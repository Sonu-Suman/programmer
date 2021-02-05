# import module 
import webbrowser as wb
import pyautogui
import time

# Open your whats app in web browser
wb.open("web.whatsapp.com")
time.sleep(20)
# define your numbmer of message
for i in range(50):
    # let's generate your message
    pyautogui.press("I")
    pyautogui.press(" ")
    pyautogui.press("L")
    pyautogui.press("O")
    pyautogui.press("V")
    pyautogui.press("E")
    pyautogui.press(" ")
    pyautogui.press("I")
    pyautogui.press("N")
    pyautogui.press("D")
    pyautogui.press("I")
    pyautogui.press("A")
    pyautogui.press("!")
    pyautogui.press("enter")
