import pyttsx3
import getpass
import time
import datetime
import wolframalpha
import os
import wikipedia
import webbrowser
import random
from translate import Translator
from time import ctime

client = wolframalpha.Client('7735QA-WQ8555VHA8')

def speak(str):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 150)
    engine.runAndWait()
    engine.say(str)
    engine.runAndWait()

speak("Please enter the password")
keyword = getpass.getpass(prompt = "Please enter the Password: ")
if keyword == "Loser@2004":
    print("Your Welcome")
    speak("Your Welcome")
    print("------"*12)
else:
    speak("Sorry, you can't access!")
    print("------"*12)
    exit( )

def greet( ):
    t_hour = datetime.datetime.now( ).hour
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
greet( )

time.sleep(1)
print("How can i help you...")
speak("How can i help you...")
print("------"*12)


# Main Task For Jarvis To Do
def main( ):
    ans = input('Give Command... \n')
    if ans.lower( ) == 'google':
        speak("what do you want to search")
        search = str(input('what do you want to search:: '))
        url = 'https://google.com/search?q=' + search
        webbrowser.get( ).open(url)
        speak('Here is what i found for' + search)
        print("------"*12)
        main( )
    elif ans.lower( ) == "help(command)":
        print("location/google/time/youtube/news/game/query/flip a coin/roll a dice/play songs/play movies/translator/research/open folder/trivia/shutdown")
        print("------"*12)
        main( )
    elif ans.lower( ) == 'time':
        print(ctime( ))
        speak(ctime( ))
        main( )
    elif ans.lower( ) == "roll a dice":
        roll = ["One","Two","Three","Four","Five","Six"]
        dices = random.choice(roll)
        print(dices)
        speak(dices)
        print("------"*12)
        main( )
    elif ans.lower() == "how are you":
        print("I am absolutly fine sir what about you?")
        speak("I am absolutly fine sir what about you?")
        mood = input(">>>")
        if mood.lower() == "i am good":
            print("Okay!")
            speak("Okay!")
        elif mood.lower() == "good":
            print("Okay!")
            speak("Okay!")
        elif mood.lower() == "perfect":
            print("Okay!")
            speak("Okay!")
        else:
            print("Hope you are doing good!")
            speak("Hope you are doing good!")
        print("------"*12)
        main()
    elif ans.lower( ) == 'location':
        location = str(input('what is the location? '))
        url = 'https://google.nl/maps/place/' + location + '&mp;'
        webbrowser.get( ).open(url)
        speak('Here is your location' + location)
        print("------"*12)
        main( )
    elif ans.lower( ) == "flip a coin":
        speak("Which one you choose, head or tail?")
        ask = input("Which one you choose:: ")
        coin = ["tail","head"]
        toss = random.choice(coin)
        if ask == "tail":
            print(toss)
            speak(toss)
            if toss == "tail":
                print("You Win the Toss. :)")
                speak("you win the toss")
                print("------"*12)
            elif toss == "head":
                print("You Lose the Toss. :(")
                speak("you lose the toss")
                print("----" * 12)
            else:
                pass
        elif ask == "head":
            print(toss)
            speak(toss)
            if toss == "head":
                print("You Win the Toss. :)")
                speak("you win the toss")
                print("------"*12)
            elif toss == "tail":
                print("You Lose the Toss. :(")
                speak("You lose the toss")
                print("----" * 12)
            else:
                pass
        else:
            print(toss)
            speak(toss)
            print("You Got Nothing. XD")
            speak("You Got Nothing. XD")
            print("You should choose head or tail")
            speak("You should choose head or tail")
            print("------"*12)
        main( )
    elif ans.lower( ) == "query":
        speak("What is your query:: ")
        query = str(input("What is your query:: "))
        res = client.query(query)
        output = next(res.results).text
        print(output)
        speak(output)
        print("------"*12)
        main( )
    elif ans.lower( ) == "thank you jarvis":
        speak("That's my job sir :) ")
        print("------"*12)
        main( )
    elif ans.lower( ) == "thanks jarvis":
        speak("That's my job sir :) ")
        print("------"*12)
        main( )
    elif ans.lower( ) == "thank you":
        speak("That's my job sir :) ")
        print("------"*12)
        main( )
    elif ans.lower( ) == 'news':
        url = 'https://news.google.com/'
        webbrowser.get( ).open(url)
        speak('Here is your news')
        print("------"*12)
        main( )
    elif ans.lower( ) == 'youtube':
        url = 'https://www.youtube.com'
        webbrowser.get( ).open(url)
        speak("opening youtube...")
        print("------"*12)
        main( )

    # Play Songs
    elif ans.lower( ) == 'play songs':
        speak("What is your favourite song")
        ans = input('What is your favourite song: ')
        if ans.lower() == 'el perdon':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... el perdon. enjoy the music")
            speak("Now you are listening... el perdon. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[0]))
            print("------"*12)
            main()
        elif ans.lower() == "ezio family":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... ezio family. enjoy the music")
            speak("Now you are listening... ezio family. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[1]))
            print("------"*12)
            main()
        elif ans.lower() == 'valhalla':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... valhalla. enjoy the music")
            speak("Now you are listening... valhalla. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[2]))
            print("------"*12)
            main()
        elif ans.lower() == "ezio family 2":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are watching... ezio faimly 2. enjoy the video")
            speak("Now you are watching... ezio faimly 2. enjoy the video")
            os.startfile(os.path.join(music_dir, songs[3]))
            print("------"*12)
            main()
        elif ans.lower() == 'ready to fight':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are watching... ready to fight. enjoy the video")
            speak("Now you are watching... ready to fight. enjoy the video")
            os.startfile(os.path.join(music_dir, songs[4]))
            print("------"*12)
            main()
        elif ans.lower() == "avenger main theme":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... avenger main theme. enjoy the music")
            speak("Now you are listening... avenger main theme. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[5]))
            print("------"*12)
            main()
        elif ans.lower() == 'the nights':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... the night. enjoy the music")
            speak("Now you are listening... the night. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[6]))
            print("------"*12)
            main()
        elif ans.lower() == "24k magic":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... 24k magic. enjoy the music")
            speak("Now you are listening... 24k magic. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[7]))
            print("------"*12)
            main()
        elif ans.lower() == "that's what i like":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now Playing... that's what i like. enjoy the music")
            speak("Now Playing... that's what i like. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[8]))
            print("------"*12)
            main()
        elif ans.lower() == "havana":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... havana. enjoy the music")
            speak("Now you are listening... havana. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[9]))
            print("------"*12)
            main()
        elif ans.lower() == 'hey dj':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... hey dj. enjoy the music")
            speak("Now you are listening... hey dj. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[10]))
            print("------"*12)
            main()
        elif ans.lower() == "para enamorarte":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... para enamorarte. enjoy the music")
            speak("Now you are listening... para enamorarte. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[11]))
            print("------"*12)
            main()
        elif ans.lower() == 'hymn for the weeknd':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... hymn for the weeknd. enjoy the music")
            speak("Now you are lisening... hymn for the weeknd. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[12]))
            print("------"*12)
            main()
        elif ans.lower() == "run free":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... run free. enjoy the music")
            speak("Now you are listening... run free. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[13]))
            print("------"*12)
            main()
        elif ans.lower() == "sunio bragging":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... sunio bragging. enjoy the music")
            speak("Now you are listening... sunio bragging. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[14]))
            print("------"*12)
            main()
        elif ans.lower() == 'doraemon':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... doraemon. enjoy the music")
            speak("Now you are listening... doraemon. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[15]))
            print("------"*12)
            main()
        elif ans.lower() == 'drift':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... drift, enjoy the music")
            speak("Now you are listening... drift. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[16]))
            print("------"*12)
            main()
        elif ans.lower() == "not afraid":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... not afraid. enjoy the music")
            speak("Now you are listening... not afraid. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[17]))
            print("------"*12)
            main()
        elif ans.lower() == 'venom':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... venom. enjoy the music")
            speak("Now you are listening... venom. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[18]))
            print("------"*12)
            main()
        elif ans.lower() == "call of duty eminem":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are watching... call of duty eminem. enjoy the video")
            speak("Now you are watching... call of duty eminem. enjoy the video")
            os.startfile(os.path.join(music_dir, songs[19]))
            print("------"*12)
            main()
        elif ans.lower() == 'fed up':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... fed up. enjoy the music")
            speak("Now you are listening... fed up. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[20]))
            print("------"*12)
            main()
        elif ans.lower() == 'thunder':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... thunder. enjoy the music")
            speak("Now you are listening... thunder. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[21]))
            print("------"*12)
            main()
        elif ans.lower() == 'whatever it takes':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... what ever it takes. enjoy the music")
            speak("Now you are listening... what ever it takes. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[22]))
            print("------"*12)
            main()
        elif ans.lower() == 'helden':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... helden. enjoy the music")
            speak("Now you are listening... helden. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[23]))
            print("------"*12)
            main()
        elif ans.lower() == 'intentions':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... intentions. enjoy the music")
            speak("Now you are listening... intentions. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[24]))
            print("------"*12)
            main()
        elif ans.lower() == "l theme":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... l theme. enjoy the music")
            speak("Now you are listening... l theme. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[25]))
            print("------"*12)
            main()
        elif ans.lower() == "legends never die":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... legends never die. enjoy the music")
            speak("Now you are listening... legends never die. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[26]))
            print("------"*12)
            main()
        elif ans.lower() == 'despacito':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... despacito. enjoy the music")
            speak("Now you are listening... despacito. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[27]))
            print("------"*12)
            main()
        elif ans.lower() == 'mi':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... mi. enjoy the music")
            speak("Now you are listening... mi. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[28]))
            print("------"*12)
            main()
        elif ans.lower() == "avengers age of ultron":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... avengers age of ultron. enjoy the music")
            speak("Now you are listening... avengers age of ultron. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[29]))
            print("------"*12)
            main()
        elif ans.lower() == "good life":
            music_dir = "D:\Songs"
            songs = os.listdir(music_dir)
            print("Now you are listening... good life. enjoy the music")
            speak("Now you are listening... good life. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[30]))
            print("------"*12)
            main()
        elif ans.lower() == "bilionera":
            music_dir = "D:\Songs"
            songs = os.listdir(music_dir)
            print("Now you are listening... bilionera. enjoy the music")
            speak("Now you are listening... bilionera. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[31]))
            print("------"*12)
            main()
        elif ans.lower() == 'calma':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... calma. enjoy the music")
            speak("Now you are listening... calma. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[32]))
            print("------"*12)
            main()
        elif ans.lower() == "me necesita":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... me necesita. enjoy the music")
            speak("Now you are listening... me necesita. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[33]))
            print("------"*12)
            main()
        elif ans.lower() == 'come and get your love':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... come and get your love. enjoy the music")
            speak("Now you are listening... come and get your love. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[34]))
            print("------"*12)
            main()
        elif ans.lower() == "scam 1992 theme":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... scam 1992 theme. enjoy the music")
            speak("Now you are listening... scam 1992 theme. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[35]))
            print("------"*12)
            main()
        elif ans.lower() == "scatman and hatman":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... scatman and hatman. enjoy the music")
            speak("Now you are listening... scatman and hatman. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[36]))
            print("------"*12)
            main()
        elif ans.lower() == "komm gib mir deine hand":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... komm gib mir deine hand. enjoy the music")
            speak("Now you are listening... komm gib mir deine hand. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[37]))
            print("------"*12)
            main()
        elif ans.lower() == 'i want something just like this':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... i want something just like this. enjoy the music")
            speak("Now you are listening... i want something just like this. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[38]))
            print("------"*12)
            main()
        elif ans.lower() == "closer":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listennig... closer. enjoy the music")
            speak("Now you are listening... closer. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[39]))
            print("------"*12)
            main()
        elif ans.lower() == "kills you slowly":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... kills you slowly. enjoy the music")
            speak("Now you are listening... kills you slowly. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[40]))
            print("------"*12)
            main()
        elif ans.lower() == "take away":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are watching... take away. enjoy the video")
            speak("Now you are watching... take away. enjoy the video")
            os.startfile(os.path.join(music_dir, songs[41]))
            print("------"*12)
            main()
        elif ans.lower() == 'hall of fame':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... hall of fame. enjoy the music")
            speak("Now you are listening... hall of fame. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[42]))
            print("------"*12)
            main()
        elif ans.lower() == 'blindings light':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... blindings light. enjoy the music")
            speak("Now you are listening... blindings light. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[43]))
            print("------"*12)
            main()
        elif ans.lower() == "heartless":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... heartless. enjoy the music")
            speak("Now you are listening... heartless. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[44]))
            print("------"*12)
            main()
        elif ans.lower() == "starboy":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... starboy. enjoy the music")
            speak("Now you are listening... starboy. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[45]))
            print("------"*12)
            main()
        elif ans.lower() == "pray for me":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... pray for me. enjoy the music")
            speak("Now you are listening... pray for me. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[46]))
            print("------"*12)
            main()
        elif ans.lower() == 'no no no':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are playing... no no no. enjoy the music")
            speak("Now you are playing... no no no. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[47]))
            print("------"*12)
            main()
        elif ans.lower() == "rise up":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... rise up. enjoy the music")
            speak("Now you are listening... rise up. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[48]))
            print("------"*12)
            main()
        elif ans.lower() == 'bad boy':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... bad boy. enjoy the music")
            speak("Now you are listening... bad boy. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[49]))
            print("------"*12)
            main()
        elif ans.lower() == "chlorine":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... chlorine. enjoy the music")
            speak("Now you are listening... chlorine. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[50]))
            print("------"*12)
            main()
        elif ans.lower() == 'ride':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... ride. enjoy the music")
            speak("Now you are listening... ride. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[51]))
            print("------"*12)
            main()
        elif ans.lower() == "stressed out":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... stressed out. enjoy the music")
            speak("Now you are listening... stressed out. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[52]))
            print("------"*12)
            main()
        elif ans.lower() == "heavy dirty soul":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... heavy dirty soul. enjoy the music")
            speak("Now you are listening... heavy dirty soul. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[53]))
            print("------"*12)
            main()
        elif ans.lower() == 'the hype':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... the hype. enjoy the music")
            speak("Now you are listening... the hype. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[54]))
            print("------"*12)
            main()
        elif ans.lower() == 'paris':
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... paris. enjoy the music")
            speak("Now you are listening... paris. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[55]))
            print("------"*12)
            main()
        elif ans.lower() == "heroes":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... the heroes. enjoy the music")
            speak("Now you are listening... the heroes. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[56]))
            print("------"*12)
            main()
        elif ans.lower() == "dusk till dawn":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print("Now you are listening... dusk till dawn. enjoy the music")
            speak("Now you are listening... dusk till dawn. enjoy the music")
            os.startfile(os.path.join(music_dir, songs[57]))
            print("------"*12)
            main()
        elif ans.lower( ) == "help(songs)":
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            print("\nHere is your list of songs, which is currently present on my system")
            speak("Here is your list of songs, which is currently present on my system")
            print("------"*12)
            main( )
        else:
            print("Sorry, This song is not available on my system!")
            speak("Sorry, This song is not available on my system!")
            print("------"*12)
            main( )
    elif ans.lower( ) == "game":
        print("Now you are going to play Rock Paper Scissor...")
        speak("Now you are going to play Rock Paper Scissor...")
        # Ask Permission To Proceed the Game
        speak("Are you ready to play?")
        ask = input("Are you ready to play? Do answer in y(yes) or n(no):: ")
        if ask.lower() == "y":
            pass
        else:
            exit()

        your_score = 0
        comp_score = 0

        # Rules
        speak("Did you want to know the rules?")
        per = input("Did you want to know the rules? Do answer in y(yes) or n(no):: ")
        if per.lower() == "y":
            print("Some Basics Rules :)")
            speak("Some basics rules")
            time.sleep(2)
            print("------"*12)
            print("What are the conditions when match will tie? ")
            speak("What are the conditions when match will tie? ")
            print("rock = rock => Match will tie")
            print("paper = paper => Match will tie")
            print("scissor = scissor => Match will tie")
            time.sleep(2)
            print("------"*12)
            print("What are the conditions when you win the match? ")
            speak("What are the conditions when you win the match? ")
            print("rock > scissor => you will win the match")
            print("paper > rock => you will win the match")
            print("scissor > paper => you will win the match")
            time.sleep(2)
            print("------"*12)
            print("What are the conditions when you lose the match? ")
            speak("What are the conditions when you lose the match? ")
            print("rock < paper => you will lose the match")
            print("paper < scissor => you will lose the match")
            print("scissor < rock => you will lose the match")

        else:
            pass

        # Enter Your Name
        print("------"*12)
        print("Loading...")
        time.sleep(2)
        speak("Enter your name")
        
        name = input("Enter your name:: ")
        time.sleep(2)
        speak("How many times you play?")
        loop = int(input("How many times you play? "))
        print("------"*12)

        # Main Game Loop
        for i in range(1,loop+1):
            list = ["rock", "paper", "scissor"]
            obj = (random.choice(list))

            ans = input("Select your object(rock/paper/scissor):: ")
            if ans.lower( ) == "rock":
                print(obj)
                speak(obj)
                if obj == "rock":
                    print("Well try",name, "... Match tie!")
                    speak("Well try"+name+"... Match tie!")
                    print("rock = rock")
                elif obj == "scissor":
                    print("Congratulations",name, "... You Win!")
                    speak("Congratulations"+name+"... You Win!")
                    print("rock > scissor")
                    your_score += 1
                elif obj == "paper":
                    print("Well try",name,"... You Lose!")
                    speak("Well try"+name+"... You Lose!")
                    print("rock < paper")
                    comp_score += 1
                else:
                    pass
                print("----" * 12)

            elif ans.lower( ) == "paper":
                print(obj)
                speak(obj)
                if obj == "paper":
                    print("Well try", name,"... Match tie!")
                    speak("Well try"+name+"... Match tie!")
                    print("paper = paper")
                elif obj == "rock":
                    print("Congratulations",name,"... You Win!")
                    speak("Congratulations"+name+"... You Win!")
                    print("paper > rock")
                    your_score += 1
                elif obj == "scissor":
                    print("Well try", name,"... You Lose!")
                    speak("Well try"+name+"... You Lose!")
                    print("paper < scissor")
                    comp_score += 1
                else:
                    pass
                print("------"*12)

            elif ans.lower( ) == "scissor":
                print(obj)
                speak(obj)
                if obj == "scissor":
                    print("Well try", name,"... Match tie!")
                    speak("Well try"+name+"... Match tie!")
                    print("scissor = scissor")
                elif obj == "paper":
                    print("Congratulations", name,"... You Win!")
                    speak("Congratulations"+name+"... You Win!")
                    print("scissor > paper")
                    your_score += 1
                elif obj == "rock":
                    print("Well try", name,"... You Lose!")
                    speak("Well try"+name+"... You Lose!")
                    print("scissor < rock")
                    comp_score += 1
                else:
                    pass
                print("------"*12)
            else:
                print("Please choose the correct object!")
                speak("Please choose the correct object!")
                print("------"*12)

        time.sleep(2)
        # Results
        print("Collecting your results please wait....")
        speak("Collecting your results please wait....")
        
        time.sleep(2)
        if comp_score < your_score:
            print("Your Score =",your_score,"/",loop)
            print("Comp Score =",comp_score,"/",loop)
            print("You Win!")
            speak("You Win!")
            print("------"*12)
        elif comp_score > your_score:
            print("Your Score =",your_score,"/",loop)
            print("Comp Score =",comp_score,"/",loop)
            print("You Lose!")
            speak("You Lose!")
            print("------"*12)
        else:
            print("Your Score =",your_score,"/", loop)
            print("Comp Score =",comp_score,"/", loop)
            print("Match Tie")
            speak("Match Tie")
            print("------"*12)

    # Play Movies       
    elif ans.lower( ) == 'play movies':
        speak("Enter the name of movie")
        ans = input('Enter the name of movie: ')
        if ans.lower( ) == 'iron man':
            movies_dir = 'D:\Movies'
            pictures = os.listdir(movies_dir)
            print("Now you are watching iron man... enjoy the movie :)")
            speak("Now you are watching iron man... enjoy the movie")
            os.startfile(os.path.join(movies_dir, pictures[0]))
            print("------"*12)
            main( )
        elif ans.lower( ) == 'jojo rabbit':
            movies_dir = 'D:\Movies'
            pictures = os.listdir(movies_dir)
            print("Now you are watching jojo rabbit... enjoy the movie :)")
            speak("Now you are watching jojo rabbit... enjoy the movie")
            os.startfile(os.path.join(movies_dir, pictures[1]))
            print("---"*12)
            main( )
        elif ans.lower( ) == 'spiderman':
             movies_dir = 'D:\Movies'
             pictures = os.listdir(movies_dir)
             print("Now you are watching spiderman... enjoy the movie :)")
             speak("Now you are watching spiderman... enjoy the movie")
             os.startfile(os.path.join(movies_dir, pictures[2]))
             print("------"*12)
             main( )
        elif ans.lower( ) == 'avengers':
             movies_dir = 'D:\Movies'
             pictures = os.listdir(movies_dir)
             print("Now you are watcing avengers... enjoy the movie :)")
             speak("Now you are watching avengers... enjoy the movie")
             os.startfile(os.path.join(movies_dir, pictures[3]))
             print("------"*12)
             main( )
        elif ans.lower( ) == 'thor':
             movies_dir = 'D:\Movies'
             pictures = os.listdir(movies_dir)
             print("Now you are watching thor... enjoy the movie :)")
             speak("Now you are watching thor... enjoy the movie")
             os.startfile(os.path.join(movies_dir, pictures[4]))
             print("------"*12)
             main( )
        elif ans.lower( ) == 'thor the dark world':
             movies_dir = 'D:\Movies'
             pictures = os.listdir(movies_dir)
             print("Now you are watching thor the dark world... enjoy the movie :)")
             speak("Now you are watching thor the dark world... enjoy the movie")
             os.startfile(os.path.join(movies_dir, pictures[5]))
             print("------"*12)
             main( )
        elif ans.lower( ) == "help(movies)":
            movies_dir = 'D:\Movies'
            pictures = os.listdir(movies_dir)
            print(pictures)
            print("\nHere is your list of movies, which is currently present in your device")
            speak("Here is your list of movies, which is currently present in your device")
            print("------"*12)
            main( )
        else:
            print("Sorry, This movie is not available on my system!")
            speak("Sorry, This movie is not available on my system!")
            print("------"*12)
            main( )

    # Search Info
    elif ans.lower( ) == 'research':
        value = input("Input the subject to get information from the wikipedia: ")
        print(wikipedia.suggest(value))
        print(wikipedia.summary(value, sentences = 4))
        speak(wikipedia.summary(value, sentences = 4))
        print("------"*12)
        main( )
        
    # Translator
    elif ans.lower( ) == "translator":
        ask = input("Which language you want to translate:: ")
        if ask.lower( ) == "english to hindi":
            translator= Translator(from_lang="english",to_lang="hindi")
            translation = translator.translate(str(input("Type a phrase to be translate: ")))
            speak("translated in english to hindi is "+translation)
            print(translation)
            print("------"*12)
        elif ask.lower( ) == "english to spanish":
            translator= Translator(from_lang="english",to_lang="spanish")
            translation = translator.translate(str(input("Type a phrase to be translate: ")))
            speak("translated in english to spanish is "+translation)
            print(translation)
            print("------"*12)
        elif ask.lower( ) == "spanish to english":
            translator= Translator(from_lang="spanish",to_lang="english")
            translation = translator.translate(str(input("Type a phrase to be translate: ")))
            speak("translated in spanish to english is "+translation)
            print(translation)
            print("------"*12)
        elif ask.lower( ) == "spanish to hindi":
            translator= Translator(from_lang="spanish",to_lang="hindi")
            translation = translator.translate(str(input("Type a phrase to be translate: ")))
            speak("translated in spanish to hindi is "+translation)
            print(translation)
            print("------"*12)
        elif ask.lower( ) == "german to hindi":
            translator= Translator(from_lang="german",to_lang="hindi")
            translation = translator.translate(str(input("Type a phrase to be translate: ")))
            speak("translated in german to hindi is ")
            print(translation)
            print("------"*12)
        elif ask.lower( ) == "german to english":
            translator= Translator(from_lang="german",to_lang="english")
            translation = translator.translate(str(input("Type a phrase to be translate: ")))
            speak("translated in german to english is "+translation)
            print(translation)
            print("------"*12)
        elif ask.lower( ) == "german to spanish":
            translator= Translator(from_lang="german",to_lang="spanish")
            translation = translator.translate(str(input("Type a phrase to be translate: ")))
            speak("translated in german to hindi is "+translation)
            print(translation)
            print("------"*12)
        elif ask.lower( ) == "spanish to german":
            translator= Translator(from_lang="spanish",to_lang="german")
            translation = translator.translate(str(input("Type a phrase to be translate: ")))
            speak("translated in spanish to german is "+translation)
            print(translation)
            print("------"*12)
        elif ask.lower( ) == "english to german":
            translator= Translator(from_lang="english",to_lang="german")
            translation = translator.translate(str(input("Type a phrase to be translate: ")))
            speak("translated in english to german is "+translation)
            print(translation)
            print("------"*12)
        elif ask.lower( ) == "help(translator)":
            print("english to hindi")
            print("english to spanish")
            print("english to german")
            print("spanish to english")
            print("spanish to hindi")
            print("spanish to german")
            print("german to hindi")
            print("german to english")
            print("german to spanish")
            print("------"*12)
            main( )
        else:
            print("Didn't get :(")
            speak("Didn't get :(")
            print("------"*12)
        main( )

    # To open the folder
    elif ans.lower( ) == "open folder":
        ask = input("Type your software name:: ")
        if ask.lower( ) == "open atom":
            my_file = "D:\My Folders"
            folder = os.listdir(my_file)
            print("Opening Atom...")
            speak("Opening Atom...")
            os.startfile(os.path.join(my_file, folder[0]))
            print("------"*12)
            main( )
        elif ask.lower( ) == "open avogadro":
            my_file = "D:\My Folders"
            folder = os.listdir(my_file)
            print("Opening avogadro...")
            speak("Opening avogadro...")
            os.startfile(os.path.join(my_file, folder[1]))
            print("------"*12)
            main( )
        elif ask.lower( ) == "open c++":
            my_file = "D:\My Folders"
            folder = os.listdir(my_file)
            print("Opening C++...")
            speak("Opening C++...")
            os.startfile(os.path.join(my_file, folder[2]))
            print("------"*12)
            main( )
        elif ask.lower( ) == "open geogebra":
            my_file = "D:\My Folders"
            folder = os.listdir(my_file)
            print("Opening geogbra...")
            speak("Opening geogbra...")
            os.startfile(os.path.join(my_file, folder[3]))
            print("------"*12)
            main( )
        elif ask.lower( ) == "open graphic calc":
            my_file = "D:\My Folders"
            folder = os.listdir(my_file)
            print("Opening graphic calculator...")
            speak("Opening graphic calculator...")
            os.startfile(os.path.join(my_file, folder[4]))
            print("------"*12)
            main( )
        elif ask.lower( ) == "open python":
            my_file = "D:\My Folders"
            folder = os.listdir(my_file)
            print("Opening python...")
            speak("Opening python...")
            os.startfile(os.path.join(my_file, folder[5]))
            print("------"*12)
            main( )
        elif ask.lower( ) == "open ms edge":
            my_file = "D:\My Folders"
            folder = os.listdir(my_file)
            print("Opening microsoft edge...")
            speak("Opening microsoft edge...")
            os.startfile(os.path.join(my_file, folder[6]))
            print("------"*12)
            main( )
        elif ask.lower( ) == "open pycharm":
            my_file = "D:\My Folders"
            folder = os.listdir(my_file)
            print("Opening pycharm...")
            speak("Opening py charm...")
            os.startfile(os.path.join(my_file, folder[7]))
            print("------"*12)
            main( )
        elif ask.lower( ) == "open sahil.r":
            my_file = "D:\My Folders"
            folder = os.listdir(my_file)
            print("Opening sahil.r...")
            speak("Opening sahil.r...")
            os.startfile(os.path.join(my_file, folder[8]))
            print("------"*12)
            main( )
        elif ask.lower( ) == "open vs code":
            my_file = "D:\My Folders"
            folder = os.listdir(my_file)
            print("Opening vs code...")
            speak("Opening visual studio code...")
            os.startfile(os.path.join(my_file, folder[9]))
            print("------"*12)
            main( )
        elif ask.lower( ) == "open video editor":
            my_file = "D:\My Folders"
            folder = os.listdir(my_file)
            print("Opening video editor...")
            speak("Opening video editor...")
            os.startfile(os.path.join(my_file, folder[10]))
            print("------"*12)
            main( )
        elif ask.lower( ) == "open zoom":
            my_file = "D:\My Folders"
            folder = os.listdir(my_file)
            print("Opening zoom...")
            speak("Opening zoom...")
            os.startfile(os.path.join(my_file, folder[11]))
            print("------"*12)
            main( )
        elif ask.lower( ) == "help(folder)":
            my_file = "D:\My Folders"
            folder = os.listdir(my_file)
            print(folder)
            print("\nHere is your list of applications, which is currently present on my system")
            speak("Here is your list of applications, which is currently present on my system")
            print("------"*12)
            main( )
        else:
            print("This file is not available on my system :(")
            speak("This file is not available on my system")
            print("------"*12)
            main( )
    elif ans.lower( ) == 'trivia':
        # It will ask your name
        speak("Enter your name")
        name = str(input("Enter your name:: "))
        time.sleep(2)
        print("Hello?",name,"welcome to trivia")
        speak("Hello?"+name+"welcome to trivia")
        time.sleep(2)

        # Ask permission to starts trivia or not
        speak("Are you Ready to Play???")
        ans = input("Are you ready to play(yes/no)")
        score = 0

        if ans.lower( ) == "yes":
            # Some Basics Rules of trivia
            speak("Some Basics Rules::")
            print("Some Basics Rules::")
            time.sleep(2)
            speak("!!There are total 20 question!!")
            print("!!There are total 20 question!!")
            time.sleep(2)
            speak("!!Each questions contains 1 marks only!!")
            print("!!Each questions contains 1 marks only!!")
            time.sleep(2)
            speak("!!Be Honest and Don't use google!!")
            print("!!Be Honest and Don't use google!!")
            time.sleep(2)
            speak("!!Negative marking is not allowed so don't worry!!")
            print("!!Negative marking is not allowed so don't worry!!")
            time.sleep(2)
            speak("!!Best Of Luck"+name+"!!")
            print("!!Best Of Luck",name,"!!")
            time.sleep(2)
            speak("Ready for the questions...")
            print("Ready for the questions...")
            time.sleep(3)

            speak("1. Which is the best programing language?")
            ans = input("1. Which is the best programing language? ")
            if ans.lower( ) == "python":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is python")
                print("Correct answer is python")
                time.sleep(1)

            speak("2. Name the computer scientist who made python interpreter?")
            ans = input("2. Name the computer scientist who made python interpreter? ")
            if ans.lower( ) == "guido van russom":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is guido van russom")
                print("Correct answer is guido van russom")
                time.sleep(1)

            speak("3. Name the Scientist who said that 'The Time Is Not Absolute In The Universe?")
            ans = input("3. Name the Scientist who said that 'The Time Is Not Absolute In The Universe!' ? ")
            if ans.lower( ) == "albert einstein":
                speak("Correct")
                print("Correct :)")
                score +=1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is albert einstein")
                print("Correct answer is albert einstein")

            speak("4. What is the speed of light in kilometers per second?")
            ans = input("4. What is the speed of light in km/sec? ")
            if ans.lower( ) == "300000km/sec":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is 3 hundred thousand kilometers per second")
                print("Correct answer is 300000km/sec")

            speak("5. When Voyager 1 was launch?")
            ans = input("5. When Voyager 1 was launch? ")
            if ans.lower( ) == "5th september 1977":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is 5th september 1977")
                print("Correct answer is 5th september 1977")

            speak("6. When Voyager 2 was launch?")
            ans = input("6. When Voyager 2 was launch? ")
            if ans.lower( ) == "20th august 1977":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is 20th august 1977")
                print("Correct answer is 20th august 1977")

            speak("7. When Galileo Probe was launched?")
            ans = input("7. When Galileo Probe was launched? ")
            if ans.lower( ) == "18th october 1989":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is 18th october 1989")
                print("Correct answer is 18th october 1989")

            speak("8. Who is the father of periodic table?")
            ans = input("8. Who is the father of periodic table? ")
            if ans.lower( ) == "dimitri mendeleev":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is dimitri mendeleev")
                print("Correct answer is dimitri mendeleev")

            speak("9. Who is the father of telescope? ")
            ans = input("9. Who is the father of telescope? ")
            if ans.lower( ) == "galileo galilie":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is galileo galilie")
                print("Correct answer is galileo galilie")

            speak("10. Who is the father of chemistry?")
            ans = input("10. Who is the father of chemistry? ")
            if ans.lower( ) == "antoine lavoisier":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is antoine lavoisier")
                print("Correct answer is antoine lavoisier")

            speak("11. Who is the father of computer? ")
            ans = input("11. Who is the father of computer? ")
            if ans.lower( ) == "charls babbage":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is charls babbage")
                print("Correct answer is charls babbage")

            speak("12. Who is the founder of google?")
            ans = input("12. Who is the founder of google? ")
            if ans.lower( ) == "larry page and sergey brin":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is larry page and sergey brin")
                print("Correct answer is larry page and sergey brin")

            speak("13. Who is the founder of youtube?")
            ans = input("13. Who is the founder of youtube? ")
            if ans.lower( ) == "jawed karim, steve chen and chad hurley":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is jawed karim, steve chen and chad hurley")
                print("Correct answer is jawed karim, steve chen and chad hurley")

            speak("14. Who is the founder of space x?")
            ans = input("14. Who is the founder of space x? ")
            if ans.lower( ) == "elon musk":
                speak("Correct :)")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is elon musk")
                print("Correct answer is elon musk")

            speak("15. Name the fist man who landed on moon?")
            ans = input("15. Name the fist man who landed on moon? ")
            if ans.lower( ) == "neil armstrong":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is neil armstrong")
                print("Correct answer is neil armstrong")

            speak("16. Name the first woman who landed on moon?")
            ans = input("16. Name the first woman who landed on moon? ")
            if ans.lower( ) == "valentina tereshkova":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incoorect")
                print("Incoorect :(")
                time.sleep(1)
                speak("Correct answer is valentina tereshkova")
                print("Correct answer is valentina tereshkova")

            speak("17. Fastest probe in the space? ")
            ans = input("17. Fastest probe in the space? ")
            if ans.lower( ) == "parker solar probe":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is parker solar probe")
                print("Correct answer is parker solar probe")

            speak("18. Name the astronomer who goes to the space? ")
            ans = input("18. Name the astronomer who goes to the space? ")
            if ans.lower() == "yuri gagarin":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is yuri gagarin")
                print("Correct answer is yuri gagarin")

            speak("19. ‘New Horizons’ spacecraft was launched by NASA to study of which planet? ")
            ans = input("19. ‘New Horizons’ spacecraft was launched by NASA to study of which planet? ")
            if ans.lower() == "pluto":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is pluto")
                print("Correct answer is pluto")

            speak("20. How old is solar system?")
            ans = input("20. How old is solar system? ")
            if ans.lower() == "5 billion years":
                speak("Correct")
                print("Correct :)")
                score += 1
            else:
                speak("Incorrect")
                print("Incorrect :(")
                time.sleep(1)
                speak("Correct answer is 5 billion years")
                print("Correct answer is 5 billion years")

            time.sleep(3)
            speak("Collecting your results...")
            print("Collecting your results...")
            time.sleep(2)

            # Gerenerate your score
            if score >= 12:
                speak("Excllence")
                print("Excllence,",name,"!!")
            elif score >= 12:
                speak("Not bad")
                print("Not bad!!")
            else:
                speak("Try Next Time...")
                print("Try Next Time...")
            time.sleep(2)

            # Give percentage
            per = (score/20)*100
            speak("Your score")
            print("You got", score,"out of 20")
            time.sleep(1)
            speak("Your Percentage")
            print("Your percentages", per, "%")
            time.sleep(3)
            speak("Hope You Enjoy This Game... ;)")
            print("Hope You Enjoy This Game... ;)")

            speak("This is trivia by Sahil Rajwar...")
            about = "This is trivia by Sahil Rajwar..."
            main( )
    elif ans.lower( ) == 'who are you':
        print('I am Jarvis, means Just A Rather Very Intelligent System and my nick name is Edwin Jarvis, You can assign me any task such as play songs,movies,etc. For more information just type "help(command)" to know that what i can do!')
        speak('I am Jarvis, means Just A Rather Very Intelligent System and my nick name is Edwin Jarvis, You can assign me any task such as play songs,movies,etc. For more information just type "help(command)" to know that what i can do!')
        print("------"*12)
        main( )
    elif ans.lower( ) == "shutdown":
        speak("Are you sure!")
        que = input("Are you sure?")
        if que.lower( ) == "no":
            print("Ok, How can i help you?")
            speak("Ok, How can i help you?")
            main( )
        elif que.lower( ) == "yes":
            speak("Have A Nice Day Sir!")
            exit( )
        else:
            print("You have to answer in yes/no")
            speak("You have to answer in yes or no?")
            que = input("Are you sure sir?")
            if que.lower( ) == "yes":
                print("Have A Nice Day Sir!")
                speak("have nice day sir!")
                exit( )
            elif que.lower( ) == "no":
                print("Ok, How can i help you?")
                speak("Ok, how can i help you?")
                main( )
            else:
                print("How can i help you?")
                speak("How can i help you?")
                main( )
            main( )
    else:
        print("Sorry I didn't get that :(")
        speak("Sorry I didn't get that")
        print("------"*12)
        main( )
        
    main( )
main( )
