import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("This is Lily  Please tell me how may I help you ")


def takeCommand():
    """It takes microphone input from the user and returns string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source, timeout=1, phrase_time_limit=10)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    """This will send the Email to the input user """
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("princeyadav7231236@gmail.com", "prince7231236")
    server.sendmail("princeyadav7231236@gmail.com", to, content)

if __name__ == '__main__':
    speak("Hello boss how are you ")
    wishMe()
    takeCommand()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if "wikipedia" in query:
            speak("Searching Wikipedia ")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=100)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("youtube.com")

        elif "open google" in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("google.com")

        elif "open stack overflow" in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("stackoverflow.com")

        elif "open github" in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("github.com")
            # path = "C:\\Users\\Bansh\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            # os.startfile(path)

        elif "play music" in query:
            music_dir = "G:\\music"
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs) - 1)]))

        elif "the time" in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Boss the time is {str_time}")
        elif "send email" in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = "princeyadav7231236@gmail.com"
                sendEmail(to, content)
                speak("Email has been send !")
            except Exception as e:
                print(e)
                speak("Sorry Boss, I am not able to send this email. ")

        elif "exit" in query:
            exit()
        elif "open photos" in query:
            os.open("camera")






