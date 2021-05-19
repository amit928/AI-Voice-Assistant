# import sys
import pyttsx3
import datetime
from playsound import playsound
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import random
import ctypes
import requests
import pyautogui
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import pywhatkit
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)


def weather():
    api_key = "c7564225bc2e86b8e8ea90f5122bac73"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Odisha"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature_in_k = y["temp"]
        current_temperature = int(current_temperature_in_k - 273)
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speak("The current weather looks like " + str(
            weather_description) + ". If you want to know about the current temperature , then it is " + str(current_temperature) + " degree celcius and the humidity is " + str(current_humidiy))
        take_command()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour <= 12:
        speak("Good Morning boss !")
    elif hour >= 12 and hour <= 16:
        speak("Good afternoon boss !")
    elif hour >= 16 and hour <= 21:
        speak("Good Evening boss !")
    else:
        speak("Hello boss !")
    speak("I am Mark  . How may I help you ?")


def take_command():
    # It takes microphone inputs from the user and returns output .

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing ......")
        command = r.recognize_google(audio, language='en_in')
        print(f"User said : {command}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return command


def doing_work():
    while True:

        command = take_command().lower()

        if 'search youtube' in command or 'show youtube' in command or 'in youtube' in command:
            command_search = command.replace("mark", "")
            command_search = command_search.replace("show", "")
            command_search = command_search.replace("some", "")
            command_search = command_search.replace("videos", "")
            command_search = command_search.replace("search", "")
            command_search = command_search.replace("in youtube", "")
            url="https://www.youtube.com/results?search_query="+str(command_search)
            webbrowser.open_new(url)
            speak("Searching your video in youtube boss ")

        elif 'search' in command:
            command_search = str(command)
            command_search = command.replace("mark", "")
            command_search = command_search.replace("hey", "")
            command_search = command_search.replace("search", "")
            command_search = command_search.replace("ok", "")
            command_search = command_search.replace("no", "")
            url = "https://www.google.com/search?q=" + str(command_search)
            speak("Opening Google Boss")
            webbrowser.open(url)

        elif 'close chrome' in command or 'exit chrome' in command:
            speak("Closing chrome")
            os.system("TASKKILL /F /im Chrome.exe")

        elif "time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak("Current time is " + time)
            print("The Current time is : " + time)

        elif 'date' in command:
            date = datetime.datetime.now().strftime('%d:%B:%Y')
            speak("Current date is" + date)
            print("Current date is : " + date)

        elif 'command' in command or 'cmd' in command:
            speak("Openeing Command prompt")
            os.startfile('cmd')

        elif 'location' in command:
            speak("Opening map")
            webbrowser.open('https://goo.gl/maps/ALiU4AHc7mcVFcuV9')

        elif 'chrome' in command:
            speak("Opening Chrome")
            path = 'C:\\Users\\AMIT\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe '
            os.startfile(path)

        elif "open Youtube" in command:
            speak("Opening Youtube for you boss..")
            webbrowser.open_new("https://youtube.com")

        elif "open google" in command:
            speak("Opening Google for you boss..")
            webbrowser.open_new("https://google.com")

        elif "open stackoverflow" in command:
            speak("Opening Stckoverflow for you boss..")
            webbrowser.open_new("https://stackoverflow.com")

        elif "open instagram" in command:
            speak("Opening instagram for you boss..")
            webbrowser.open_new_tab("https://www.instagram.com")

        elif 'open twitter' in command:
            speak("Opening Twitter for you boss..")
            webbrowser.open_new("https://twitter.com")

        elif "song" in command or 'music' in command:
            speak("Trying to play a random song from your library boss .")
            music_dir = 'D:\\music\\song'
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir, random_song))

        elif 'close code' in command or 'close visual studio' in command:
            speak("Closing calculator")
            os.system("TASKKILL /F /im calculator.exe")

        elif "code" in command or 'visual studio' in command:
            path = "C:\\Users\\AMIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'open whatsapp' in command:
            speak("Opening whatsapp for you sir")
            webbrowser.open('https://web.whatsapp.com')

        elif 'whatsapp' in command or 'message' in command:
            speak("Opening Whatsapp boss")
            os.startfile("C:\\Users\\AMIT\\PycharmProjects\\pythonProject\\whatsapp automation.py")
            sleep(20)

        elif 'weather' in command:
            weather()

        elif 'alarm' in command:
            print("At what time , I will set the alarm sir ?")
            speak("At what time , I will set the alarm sir ?")
            print("Please write it down boss for exact result  ' ZERO EIGHT COLON FORTY THREE ' if your hour is before "
                  "10 . ")
            # speak("To set the exact time you have to write the time sir , I apologize for this")
            command = input("Enter your time here : ")
            time = open('D:\\------PYTHON CODES---------\\Data\\data.txt', 'a')
            time.write(command)
            time.close()
            os.startfile("C:\\Users\\AMIT\\PycharmProjects\\pythonProject\\alarm.py")

        elif 'close window' in command:
            press('Alt + F4')

        elif 'switch window' in command or 'another window' in command or 'window' in command:
            press_and_release('Alt + Tab')

        elif 'set reminder' in command or 'remember' in command:
            speak("What i have to remember sir ?")
            remind = take_command().lower()
            set_data = open('D:\\------PYTHON CODES---------\\Data\\data2.txt', 'a')
            set_data.write(remind)
            set_data.close()
            speak("Ok Boss I got it .")

        elif 'any reminders' in command or 'reminder' in command:
            open_data = open('D:\\------PYTHON CODES---------\\Data\\data2.txt', 'rt')
            get_data = open_data.read()
            if get_data == '':
                speak("You haven't said anything boss .")
            else:
                delete_data = open('D:\\------PYTHON CODES---------\\Data\\data2.txt', 'r+')
                delete_data.truncate(0)
                delete_data.close()

                data=get_data.replace('my','your')
                data=data.replace('i','you')
                data=data.replace('remember','')
                data=data.replace('that','')
                speak('You have said that '+data)

        elif 'close calculator' in command:
            speak("Closing calculator")
            os.system("TASKKILL /F /im calculator.exe")

        elif 'open calculator' in command or 'calculation' in command:
            speak("Opening calculator")
            os.startfile('calc')

        elif 'close notepad' in command:
            speak("Closing notepad")
            os.system("TASKKILL /F /im notepad.exe")

        elif 'open notepad' in command:
            speak("Opening notepad")
            os.startfile('notepad')

        elif 'screenshot' in command:
            pic = pyautogui.screenshot()
            pic.save('D:\\PHOTOS\\Screenshots\\sc1.png')
            speak(
                "I  have taken a screenshot of the current window . Do you want to check it in your screenshot folder ?")
            command = take_command().lower()
            if 'yes' in command or 'ok' in command or 'open' in command or 'show' in command:
                speak("Opening Scrrenshot folder")
                os.startfile('D:\\PHOTOS\\Screenshots')

            elif 'no' in command:
                speak("Okay boss")
                take_command()

        elif 'lock' in command or 'go to sleep' in command:
            speak("Ok boss, going to sleep")
            ctypes.windll.user32.LockWorkStation()

        elif 'rest' in command or 'sleep' in command:
            speak("Boss I am going to sleep for 5 second .")
            sleep(5)
            speak("Hello boss .")

        elif 'quit' in command or 'exit' in command or 'stop' in command or 'close' in command:
            hour = datetime.datetime.now().hour
            speak("On your command boss .")
            if hour >= 6 and hour <= 12:
                speak("Have a good day  !")
            else:
                speak("Good night  .")
            sys.exit()

        elif 'smarter than google' in command:
            speak("I am the First version of your Artificial Intelligence Programme . now I am fetching the data from google , How can I be smarter than google ")

        elif 'doing' in command:
            speak("I am following your orders boss")

        elif 'how are you' in command:
            speak("I am always fine  .")
            speak('What about you boss ?')

        elif 'you do' in command:
            speak("I can access all your default apps , I also can do some search for you boss . I am new in this field , If you want you can upgrade me and can do more thing by me .")

        elif 'are you there' in command or ' you hear' in command:
            speak("I am always here for you boss")

        elif 'yourself' in command or 'are you' in command :
            speak("Boss I am Mark , the first version of EDITH  , Your AI voice assistant")

        elif 'am i' in command or 'my name' in command:
            speak("You are my Boss Mr Amit Kumar Mallick ")

        elif 'girlfriend' in command:
            speak("I don't think so boss , I think i am the only AI girl whom you like so much")

        elif 'thank you' in command:
            speak("You always welcome sir .")

        elif 'ok' in command or 'mark' in command:
            speak("Yes boss")

        elif 'what is' in command or 'who is' in command or 'mean by' in command:
            command_search = str(command)
            command_search = command.replace("mark", "")
            command_search = command_search.replace("can","")
            command_search = command_search.replace("you","")
            command_search = command_search.replace("say","")
            command_search = command_search.replace("tell","")
            command_search = command_search.replace("hey", "")
            command_search = command_search.replace("search", "")
            command_search = command_search.replace("what is", "")
            command_search = command_search.replace("who is", "")
            command_search = command_search.replace("who are", "")
            command_search = command_search.replace("how to", "")
            command_search = command_search.replace("what do you mean by", "")
            command_search = command_search.replace("ok", "")
            command_search = command_search.replace("no", "")

            try:
                url="https://en.wikipedia.org/wiki/"+str(command_search)
                answer = wikipedia.summary(command_search, 2)
                print(f"According to Wikipedia : {answer}")
                speak(f"According to Wikipedia : {answer}")
                speak("Do you want to see it in wikipedia ?")
                command=take_command().lower()
                if 'yes' in command or 'ok' in command:
                    speak("Opening Wikipedia")
                    webbrowser.open(url)
                elif 'no' in command:
                    speak("Okay ")

            except Exception as e:
                speak("Sorry I can't get your answers from wikipedia.")
                print("Answer not found in wikipedia .")


if __name__ == "__main__":
    speak("Sir ,  Let me know who are you ?")
    # print(command)
    while True:
        command = take_command().lower()
        print(command)
        if 'kumar' in command:
            print("Entering to E.D.I.T.H ")
            playsound("D:\\music\\access_granted.mp3")
            speak(" Entering to EDITH .")
            playsound("D:\\music\\robot.mp3")
            wish_me()
            doing_work()

        elif 'quit' in command or 'exit' in command or 'stop' in command or 'close' in command:
            hour = datetime.datetime.now().hour
            if hour >= 0 and hour <= 12:
                speak("Have a good day sir !")
            else:
                speak("Good night sir .")
            sys.exit()

        else:
            playsound("D:\\music\\access_denied.mp3")
