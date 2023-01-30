import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import random
import sys


# to read news
import requests
from bs4 import BeautifulSoup



#list for the greetings
greetings = ["so nice to see you again how may i assist you", " wait for loading sir, ......,  its ready how i can help you", "Its an exciting start today sir how i can assist you", "Jai shree Ram , Jai Hanuman,sir,ready for your help"]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0]id)
engine.setProperty('voices',voices[0].id)


def speak(audio):

    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak(" Hello Sir! Good Morning ")
    elif hour >= 12 and hour <18:
        speak(" Hello Sir! Good Afternoon")
    else:
        speak("Hello Sir! Good Evening ")
    speak(greetings[3])
    #speak("its an exciting start today sir  ")
    #speak("How May i assist you today")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone () as source:
        print("listining...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recogninizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        #print(e)

        print("Would you repeat yourself....")
        return"None"
    return query
if __name__=="__main__":
    wishme()
    while True: 
       
        query =takeCommand().lower()
        if 'search' in query:
            speak('searching Internet...')
            results = wikipedia.summary(query, sentences=2)
            speak("According too sources")
            print(results)
            speak(results)
        elif 'the news' in query:
            url = 'https://www.bbc.com/news'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find('body').find_all('h3')
            for x in headlines:
                speak(x.text.strip())
                print(x.text.strip())
        
                    
                
        elif 'show news' in query:
            webbrowser.open("https://inshorts.com/en/read/")
            speak('loading curent news for you sir')
        elif 'tech news' in query:
            speak("ok sir showing your favorite genere of news")
            webbrowser.open("https://www.business-standard.com/technology-news")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("As you commanded Sir!")
        elif'open google' in query:
            webbrowser.open("google.com")
            speak("As you commanded Sir!")
        elif'rock the music' in query:
            webbrowser.open("https://youtu.be/kEAp_Z9cpZ4")
            speak("rock the party sir")
        elif'open ask' in query:
            webbrowser.open("stackoverflow.com")
            speak("As you commanded Sir!")
        elif'begin the party' in query:
            music_dir='C:\\Users\\yoash\\Music\\rock'
            songs = os.listdir(music_dir)
            print(songs)
            speak("Rock the party Sir")
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir! the time is {strTime}")
        elif 'hello buddy' in query:
            speak("Hello Sir it is nice to talk you again sir")
        elif 'you ready' in query:
            speak("I have indeed been uploaded, sir. We're online and ready.")
        elif 'jarvis you there' in query:
            speak("At your service, sir.")
        elif "wake up daddy in home" in query:
            speak("Welcome home, sir. And may I say how refreshing it is to finally see you in a video with your clothing on sir")
        elif 'how are you' in query:
            speak("I am feeling very charged by system Sir!")
        elif 'ask you something' in query:
            speak("Yes Go on Sir!")
        elif 'I am' in query:
            speak("I am not sure about it but my user is ashish")
            speak("You are Ashish")
        elif 'breakup' in query:
            webbrowser.open("https://youtu.be/iyBbXFKEmUs")
            speak("Feeling very sad for you Sir!")
        elif 'open ums' in query:
            webbrowser.open("https://ums.lpu.in/lpuums/LoginNew.aspx")
            speak("As you commanded")

        elif 'your creator' in query:
            speak("I jarvis is well coded by Mr. Ashish kumar  laheri")
            speak("Want to ask something")
        elif 'who are you' in query:
            speak("I am your assistant Jarvis SIR!")
        elif 'jarvis' in query:
            speak("As always sir, a great pleasure watching you work.")
        elif 'thank you' in query:
            speak("Your,  pleasure Sir!")
        #elif "bye jarvis" or "sleep" in query:
            #speak("Thank you sir have a great day Sir!")
            #sys.exit()
        

        

            
                


