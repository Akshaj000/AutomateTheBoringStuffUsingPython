#!python3
# message someone on whatapp 
import pyautogui, time, webbrowser

def message(name,message):
    time.sleep(3)
    newconvo = pyautogui.locateOnScreen('Projects/instantmessagebox/newconvo.png')
    pyautogui.click(newconvo); pyautogui.write(name)
    pyautogui.press('enter')

    online = pyautogui.locateOnScreen('Projects/instantmessagebox/online.png')

    if not online:
        print("offline")
        return
    
    time.sleep(2)
    newmsg = pyautogui.locateOnScreen('Projects/instantmessagebox/newmessage.png')
    pyautogui.click(newmsg); pyautogui.write(message); pyautogui.press('enter')
    
webbrowser.open("https://web.whatsapp.com/")
time.sleep(7)
name =['Aashray','anushka']
for i in name:
    message(i,'ignore this message')

    
