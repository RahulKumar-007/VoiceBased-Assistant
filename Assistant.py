import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning Boss")
    elif 12 <= hour < 18:
        speak("Good afternoon Boss")
    else:
        speak("Good evening")
    speak("I am Jarvis. Sir, how can I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again, please...")
        return "None"
    return query.lower()


if _name_ == '_main_':
    wishMe()
    while True:
        query = takeCommand()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia...')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('http://www.youtube.com')
        elif 'open google' in query:
            webbrowser.open('http://www.google.com')
        elif 'open geekforgeeks' in query:
            webbrowser.open('https://www.geeksforgeeks.org/')
        elif 'play music' in query:
            music_dir = '/home/rahul_singh/Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")
        elif 'chrome' in query:
            path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
            #your path to the application is added here 
            os.startfile(path)
