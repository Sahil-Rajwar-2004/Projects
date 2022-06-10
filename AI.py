import wikipedia
import pyautogui as pg
import webbrowser
import os
import time
import getpass
import requests
import datetime
import randfacts
#from datetime import datetime
#from time import ctime
#import random
#import pyttsx3

running = None

def greet():
    t_hour = datetime.datetime.now().hour
    if 24 > t_hour < 4:
        print("Pleasant Night")
    elif 12 > t_hour >= 4:
        print("Good Morning")
    elif 18 > t_hour >= 12:
        print("Good Afternoon")
    else:
        print("Good Evening")

def verify():
    global running
    user = getpass.getpass(prompt = "User Name: ")
    password = getpass.getpass(prompt = "Password: ")
    if user == "Heisenberg":
        if password == "Heisenberg@1901":
            running = True
            greet()
        else:
            print("Invalid Username or Password")
            running = False
    else:
        print("Invalid Username or Password")
        running = False
verify()


"""
def speak(str):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 150)
    engine.runAndWait()
    engine.say(str)
    engine.runAndWait()
"""


while running:
    ask = input("Command: ")
    if ask.lower() == "youtube":
        url = 'https://www.youtube.com'
        print(f"Result: {webbrowser.get().open(url)}")
        
    elif ask.lower() == "google":
        url = 'https://www.google.com'
        print(f"Result: {webbrowser.get().open(url)}")

    elif ask.lower() == "google earth":
        url = 'https://earth.google.com'
        print(f"Result: {webbrowser.get().open(url)}")
        
    elif ask.lower() == "facts":
        fact = randfacts.get_fact()
        print(f"Result: {fact}")
        
    elif ask.lower() == "python":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","q")
        pg.write("python")
        pg.press("Enter")
        
    elif ask.lower() == "txt":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","r")
        pg.write("notepad")
        pg.press("Enter")
        
    elif ask.lower() == "vscode":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","q")
        pg.write("vscode")
        pg.press("Enter")
        
    elif ask.lower() == "calc":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","r")
        pg.write("calc")
        pg.press("Enter")

    elif ask.lower() == "msg":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","q")
        pg.write("whatsapp")
        pg.press("Enter")

    elif ask.lower() == "tele":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","q")
        pg.write("telegram")
        pg.press("Enter")

    elif ask.lower() == "insta":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","q")
        pg.write("instagram")
        pg.press("Enter")

    elif ask.lower() == "twitter":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","q")
        pg.write("twitter")
        pg.press("Enter")

    elif ask.lower() == "control":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","r")
        pg.write("control")
        pg.press("Enter")

    elif ask.lower() == "paint":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","r")
        pg.write("mspaint")
        pg.press("Enter")

    elif ask.lower() == "excel":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","r")
        pg.write("excel")
        pg.press("Enter")

    elif ask.lower() == "ppt":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","r")
        pg.write("powerpnt")
        pg.press("Enter")

    elif ask.lower() == "cmd":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","r")
        pg.write("cmd")
        pg.press("Enter")

    elif ask.lower() == "file":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","e")

    elif ask.lower() == "screenshot":
        time.sleep(7)
        shot = pg.screenshot()
        name = input("Name: ")
        shot.save("E:\\Astro\\Shot\\"+str(name)+".png")
        print("Result: Screenshot has been saved")
        print(pg.confirm(text = "Screenshot has been saved", title = "Confirmation", buttons = ['Yes']))

    elif ask.lower() == "weather":
        from datetime import datetime
        location = input("Location: ")
        
        api_key = "b1d029ef12c6f31e243a74fb7ffff752"
        link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
        response = requests.get(link)
        data = response.json()

        if data["cod"] == "404":
            print(f"Invalid City: {location}, Please chec your City!")
        else:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            time = datetime.now().strftime("%d %b %Y | %H:%M:%S %p")

            from time import ctime
            print(f"Weather Forecaste: {location} Time: {ctime()}")
            print(f"Temperature: {temp} kelvin | {round(temp-273.15,3)} celcius")
            print(f"Description: {desc}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed}kmph")
        
    elif ask.lower() == "songs":
        song = str(input("Song: "))
        music_dir = 'E:\Music'
        songs = os.listdir(music_dir)
        exe_mp3 = song + ".mp3"
        exe_mp4 = song + ".mp4"
        if exe_mp3 in songs:
            print(f"Now Playing {song}...")
            os.startfile(os.path.join(music_dir, f"E:\\Music\\{exe_mp3}"))
        elif exe_mp4 in songs:
            print(f"Now Playing {song}...")
            os.startfile(os.path.join(music_dir, f"E:\\Music\\{exe_mp4}"))
        else:
            print("Song Is Unavailable :(")

    elif ask.lower() == "time":
        print(time.ctime())

    elif ask.lower() == "mysql":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","q")
        pg.write("mysql")
        pg.press("Enter")

    elif ask.lower() == "spotify":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","q")
        pg.write("spotify")
        pg.press("Enter")

    elif ask.lower() == "discord":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","q")
        pg.write("discord")
        pg.press("Enter")

    elif ask.lower() == "bluetooth":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","q")
        pg.write("bluetooth")
        pg.press("Enter")

    elif ask.lower() == "settings":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","r")
        pg.write("ms-settings:")
        pg.press("Enter")

    elif ask.lower() == "bash":
        print(f"Result: Opening {ask.lower()}...")
        pg.hotkey("win","q")
        pg.write("git bash")
        pg.press("Enter")

    elif ask.lower() == "integral":
        url = 'https://www.integral-calculator.com/'
        print(f"Result: {webbrowser.get().open(url)}")

    elif ask.lower() == "derivative":
        url = 'https://www.derivative-calculator.net/'
        print(f"Result: {webbrowser.get().open(url)}")
        
    elif ask.lower() == "q":
        print("Bye! Have a nice day")
        running = False

    elif ask.lower() == "e":
        print("Bye! Have a nice Day")
        running = False
        
    else:
        print("Invalid Command!")



