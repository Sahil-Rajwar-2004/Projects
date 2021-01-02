from tkinter import *
from time import *
from tkinter import messagebox
from translate import Translator
import datetime
import pyttsx3
import webbrowser
import wikipedia
import os
import getpass

win = Tk()
win.geometry("600x460")
win.configure(background = "#000000")
win.resizable(0, 0)
win.title("JARVIS")

def speak(str):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 150)
    engine.runAndWait()
    engine.say(str)
    engine.runAndWait()


speak("Please enter the password")
keyword = getpass.getpass(prompt="Please enter the Password: ")
if keyword == "Loser@2004":
    print("Your Welcome")
    speak("Your Welcome")
    print("------" * 12)
else:
    speak("Sorry, you can't access!")
    print("------" * 12)
    exit()

def greet():
    t_hour = datetime.datetime.now().hour
    if 24 > t_hour < 4:
        print("Pleasant Night sir.")
        speak("Pleasant Night sir.")
    elif 12 > t_hour >= 4:
        print("Good Morning sir.")
        speak("Good Morning sir.")
    elif 18 > t_hour >= 12:
        print("Good Afternoon sir.")
        speak("Good Afternoon sir.")
    else:
        print("Good Evening sir. hope you enjoy your whole day.")
        speak("Good Evening sir. hope you enjoy your whole day.")

greet()


def Reset():
    entry1.delete(0,END)
    entry2.delete(0,END)

def Shutdown():
    print("Have a nice day sir!")
    speak("Have a nice day sir!")
    exit()

def About():
    print("I am Jarvis, means Just A Rather Very Intelligent System and my nick name is Edwin Jarvis, You can assign me any task such as play songs,movies,etc. For more information just type help(command) to know that what i can do!")
    speak('I am Jarvis, means Just A Rather Very Intelligent System and my nick name is Edwin Jarvis, You can assign me any task such as play songs,movies,etc. For more information just type "help(command)" to know that what i can do!')

def Give():
    var = entry1.get( )
    if var.lower() == 'google':
        speak("what do you want to search")
        search = entry2.get( )
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what i found for' + search)
        Reset()
        print("------"*12)
    elif var.lower() == "time":
        print(ctime())
        speak(ctime())
        Reset()
        print("------"*12)
    elif var.lower() == 'research':
        value = entry2.get()
        #print(wikipedia.suggest(value))
        print(wikipedia.summary(value, sentences=4))
        speak(wikipedia.summary(value, sentences=4))
        Reset()
        print("------" * 12)
    elif var.lower() == 'location':
        location = str(input('what is the location? '))
        url = 'https://google.nl/maps/place/' + location + '&mp;'
        webbrowser.get().open(url)
        speak('Here is your location' + location)
        Reset()
        print("------" * 12)
        main()
    elif var.lower() == "translator":
        ask = entry2.get()
        if ask.lower() == "english to hindi":
            a = entry3.get()
            translator = Translator(from_lang="english", to_lang="hindi")
            translation = translator.translate(a)
            speak("translated in english to hindi is " + translation)
            print(translation)
            Reset()
            print("------" * 12)
        elif ask.lower() == "english to spanish":
            a = entry3.get()
            translator = Translator(from_lang="english", to_lang="spanish")
            translation = translator.translate(a)
            speak("translated in english to spanish is " + translation)
            print(translation)
            Reset()
            print("------" * 12)
        elif ask.lower() == "spanish to english":
            a = entry3.get()
            translator = Translator(from_lang="spanish", to_lang="english")
            translation = translator.translate(a)
            speak("translated in spanish to english is " + translation)
            print(translation)
            Reset()
            print("------" * 12)
        elif ask.lower() == "spanish to hindi":
            a = entry3.get()
            translator = Translator(from_lang="spanish", to_lang="hindi")
            translation = translator.translate(a)
            speak("translated in spanish to hindi is " + translation)
            print(translation)
            Reset()
            print("------" * 12)
        elif ask.lower() == "german to hindi":
            a = entry3.get()
            translator = Translator(from_lang="german", to_lang="hindi")
            translation = translator.translate(a)
            speak("translated in german to hindi is ")
            print(translation)
            Reset()
            print("------" * 12)
        elif ask.lower() == "german to english":
            a = entry3.get()
            translator = Translator(from_lang="german", to_lang="english")
            translation = translator.translate(a)
            speak("translated in german to english is " + translation)
            print(translation)
            Reset()
            print("------" * 12)
        elif ask.lower() == "german to spanish":
            a = entry3.get()
            translator = Translator(from_lang="german", to_lang="spanish")
            translation = translator.translate(a)
            speak("translated in german to hindi is " + translation)
            print(translation)
            Reset()
            print("------" * 12)
        elif ask.lower() == "spanish to german":
            a = entry3.get()
            translator = Translator(from_lang="spanish", to_lang="german")
            translation = translator.translate(a)
            speak("translated in spanish to german is " + translation)
            print(translation)
            Reset()
            print("------" * 12)
        elif ask.lower() == "english to german":
            a = entry3.get()
            translator = Translator(from_lang="english", to_lang="german")
            translation = translator.translate(a)
            speak("translated in english to german is " + translation)
            print(translation)
            Reset()
            print("------" * 12)
        elif ask.lower() == "help(translator)":
            print("english to hindi")
            print("english to spanish")
            print("english to german")
            print("spanish to english")
            print("spanish to hindi")
            print("spanish to german")
            print("german to hindi")
            print("german to english")
            print("german to spanish")
            Reset()
            print("------" * 12)
            main()
        else:
            print("Didn't get :(")
            speak("Didn't get :(")
            print("------" * 12)
    elif var.lower() == 'play songs':
        speak("What is your favourite song")
        ans = entry2.get()
        if ans.lower() == 'el perdon':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... el perdon. enjoy the music")
            speak("Now you are listening... el perdon. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[0]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "ezio family":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... ezio family. enjoy the music")
            speak("Now you are listening... ezio family. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[1]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'valhalla':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... valhalla. enjoy the music")
            speak("Now you are listening... valhalla. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[2]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "ezio family 2":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are watching... ezio faimly 2. enjoy the video")
            speak("Now you are watching... ezio faimly 2. enjoy the video")
            os.startfile(os.path.join(music_dir, songs[3]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'ready to fight':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are watching... ready to fight. enjoy the video")
            speak("Now you are watching... ready to fight. enjoy the video")
            os.startfile(os.path.join(music_dir, songs[4]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "avenger main theme":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... avenger main theme. enjoy the music")
            speak("Now you are listening... avenger main theme. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[5]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'the nights':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... the night. enjoy the music")
            speak("Now you are listening... the night. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[6]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "24k magic":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... 24k magic. enjoy the music")
            speak("Now you are listening... 24k magic. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[7]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "that's what i like":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now Playing... that's what i like. enjoy the music")
            speak("Now Playing... that's what i like. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[8]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "havana":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... havana. enjoy the music")
            speak("Now you are listening... havana. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[9]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'hey dj':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... hey dj. enjoy the music")
            speak("Now you are listening... hey dj. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[10]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "para enamorarte":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... para enamorarte. enjoy the music")
            speak("Now you are listening... para enamorarte. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[11]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'hymn for the weeknd':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... hymn for the weeknd. enjoy the music")
            speak("Now you are lisening... hymn for the weeknd. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[12]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "run free":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... run free. enjoy the music")
            speak("Now you are listening... run free. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[13]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "sunio bragging":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... sunio bragging. enjoy the music")
            speak("Now you are listening... sunio bragging. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[14]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'doraemon':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... doraemon. enjoy the music")
            speak("Now you are listening... doraemon. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[15]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'drift':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... drift, enjoy the music")
            speak("Now you are listening... drift. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[16]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "not afraid":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... not afraid. enjoy the music")
            speak("Now you are listening... not afraid. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[17]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'venom':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... venom. enjoy the music")
            speak("Now you are listening... venom. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[18]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "call of duty eminem":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are watching... call of duty eminem. enjoy the video")
            speak("Now you are watching... call of duty eminem. enjoy the video")
            os.startfile(os.path.join(music_dir, songs[19]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'fed up':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... fed up. enjoy the music")
            speak("Now you are listening... fed up. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[20]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'thunder':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... thunder. enjoy the music")
            speak("Now you are listening... thunder. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[21]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'whatever it takes':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... what ever it takes. enjoy the music")
            speak("Now you are listening... what ever it takes. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[22]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'helden':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... helden. enjoy the music")
            speak("Now you are listening... helden. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[23]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'intentions':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... intentions. enjoy the music")
            speak("Now you are listening... intentions. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[24]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "l theme":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... l theme. enjoy the music")
            speak("Now you are listening... l theme. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[25]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "legends never die":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... legends never die. enjoy the music")
            speak("Now you are listening... legends never die. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[26]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'despacito':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... despacito. enjoy the music")
            speak("Now you are listening... despacito. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[27]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'mi':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... mi. enjoy the music")
            speak("Now you are listening... mi. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[28]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "avengers age of ultron":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... avengers age of ultron. enjoy the music")
            speak("Now you are listening... avengers age of ultron. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[29]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "good life":
            music_dir = "D:\Songs"
            songs = os.listdir(music_dir)
            print("Now you are listening... good life. enjoy the music")
            speak("Now you are listening... good life. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[30]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "bilionera":
            music_dir = "D:\Songs"
            songs = os.listdir(music_dir)
            print("Now you are listening... bilionera. enjoy the music")
            speak("Now you are listening... bilionera. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[31]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'calma':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... calma. enjoy the music")
            speak("Now you are listening... calma. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[32]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "me necesita":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... me necesita. enjoy the music")
            speak("Now you are listening... me necesita. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[33]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'come and get your love':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... come and get your love. enjoy the music")
            speak("Now you are listening... come and get your love. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[34]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "scam 1992 theme":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... scam 1992 theme. enjoy the music")
            speak("Now you are listening... scam 1992 theme. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[35]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "scatman and hatman":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... scatman and hatman. enjoy the music")
            speak("Now you are listening... scatman and hatman. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[36]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "komm gib mir deine hand":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... komm gib mir deine hand. enjoy the music")
            speak("Now you are listening... komm gib mir deine hand. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[37]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'i want something just like this':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... i want something just like this. enjoy the music")
            speak("Now you are listening... i want something just like this. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[38]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "closer":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listennig... closer. enjoy the music")
            speak("Now you are listening... closer. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[39]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "kills you slowly":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... kills you slowly. enjoy the music")
            speak("Now you are listening... kills you slowly. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[40]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "take away":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are watching... take away. enjoy the video")
            speak("Now you are watching... take away. enjoy the video")
            os.startfile(os.path.join(music_dir, songs[41]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'hall of fame':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... hall of fame. enjoy the music")
            speak("Now you are listening... hall of fame. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[42]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'blindings light':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... blindings light. enjoy the music")
            speak("Now you are listening... blindings light. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[43]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "heartless":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... heartless. enjoy the music")
            speak("Now you are listening... heartless. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[44]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "starboy":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... starboy. enjoy the music")
            speak("Now you are listening... starboy. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[45]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "pray for me":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... pray for me. enjoy the music")
            speak("Now you are listening... pray for me. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[46]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'no no no':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are playing... no no no. enjoy the music")
            speak("Now you are playing... no no no. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[47]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "rise up":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... rise up. enjoy the music")
            speak("Now you are listening... rise up. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[48]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'bad boy':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... bad boy. enjoy the music")
            speak("Now you are listening... bad boy. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[49]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "chlorine":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... chlorine. enjoy the music")
            speak("Now you are listening... chlorine. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[50]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'ride':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... ride. enjoy the music")
            speak("Now you are listening... ride. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[51]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "stressed out":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... stressed out. enjoy the music")
            speak("Now you are listening... stressed out. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[52]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "heavy dirty soul":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... heavy dirty soul. enjoy the music")
            speak("Now you are listening... heavy dirty soul. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[53]))
            Reset()
            print("------" * 12)
        elif ans.lower() == 'the hype':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... the hype. enjoy the music")
            speak("Now you are listening... the hype. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[54]))
            Reset()
            print("------" * 12)      
        elif ans.lower() == 'paris':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... paris. enjoy the music")
            speak("Now you are listening... paris. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[55]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "heroes":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... the heroes. enjoy the music")
            speak("Now you are listening... the heroes. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[56]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "dusk till dawn":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... dusk till dawn. enjoy the music")
            speak("Now you are listening... dusk till dawn. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[57]))
            Reset()
            print("------" * 12)
        elif ans.lower() == "help(songs)":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            print("\nHere is your list of songs, which is currently present on my system")
            speak("Here is your list of songs, which is currently present on my system")
            Reset()
            print("------" * 12)
        else:
            print("Sorry, This song is not available on my system!")
            speak("Sorry, This song is not available on my system!")
            print("------" * 12)
    else:
        print("Sorry i didn't get that!")
        speak("Sorry i didn't get that!")
        print("------"*12)
        


#Structure of first command
label1 = Label(win, font = ("Comic sans ms", 16), text = "Give command: ",bg = "#000000", fg = "#ffffff")
label1.pack(fill = BOTH, pady = 20)
entry1 = Entry(win, font = ("Comic sans ms", 16))
entry1.pack(fill = BOTH)

#Structure of second command
label2 = Label(win, font = ("Comic sans ms",16), text =  "Purpose: ", bg = "#000000", fg = "#ffffff")
label2.pack(fill = BOTH, pady = 20)
entry2 = Entry(win, font = ("Comic sans ms", 16))
entry2.pack(fill = BOTH)

#Structure of Output
label3 = Label(win, font = ("Comic sans ms", 16), text = "Input: ", bg = "#000000", fg = "#ffffff")
label3.pack(fill = BOTH, pady = 20)
entry3 = Entry(win, font = ("Comic sans ms", 16))
entry3.pack(fill = BOTH)

#Structure of the button
btn1 = Button(win, text = "Give", command = Give, border = 6, bg = "grey", fg = "#37ff00", relief = "sunken")
btn1.pack(fill = BOTH)
btn2 = Button(win, text = "Reset", command = Reset, border = 6, bg = "grey", fg = "#37ff00", relief = "sunken")
btn2.pack(fill = BOTH)
btn3 = Button(win, text = "About", command = About, border = 6, bg = "grey", fg = "#37ff00", relief = "sunken")
btn3.pack(fill = BOTH)
btn4 = Button(win, text = "Shutdown", command = Shutdown, border = 6, bg = "grey", fg = "#37ff00", relief = "sunken")
btn4.pack(fill = BOTH)

mainloop()
