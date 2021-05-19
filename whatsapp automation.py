
from pyautogui import click
from keyboard import press
from keyboard import write
import webbrowser
from time import sleep
from AI_Voice_Assistant import speak,take_command

def whatsappmsg(name,message):
    webbrowser.open("https://web.whatsapp.com")
    sleep(15)
    click(x=204 , y=187)
    sleep(1)
    write(name)
    sleep(2)
    click(x=234, y=323)
    sleep(2)
    click(x=623, y=737)
    sleep(1)
    write(message)
    press('enter')
    sleep(2)



speak("To whom you want to send message")
name = take_command().lower()
speak("What do you want send ?")
message = take_command().lower()
whatsappmsg(name,message)
