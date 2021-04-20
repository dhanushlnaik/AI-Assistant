"""
A Desktop Voice Assistant
Which recognise Human Voice and Work Acc. to it using speech recognition module
open command prompt and write following things (internet required)
pip install pyttsx3
pip install speech_recognition
pip install wikipedia

also to run this program insternart is needed
"""
# ______modules______
import pyttsx3  # Enables Computer to speak
import speech_recognition as sr # Recognize our Voice
import datetime # Current Time
import wikipedia # Search In WikiPedia In Present
import webbrowser # To search In Browser
import os # To Open File
import smtplib # Send Emails


# ______Main Engine For PYTTSX3
engine = pyttsx3.Engine('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
# ______Functions______


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Saturday Sir, Please tell me How can I help You")


def takecommmand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing ....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        print(e)
        print("Say That Again....")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

# ______Main Code________


if __name__ == '__main__':
    wishMe()
    while True:
        query = takecommmand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia ... ...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(f"According To Wikipedis , \n {results}")
            speak("According To Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'F:\\Music\\Favourite'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir[0]))
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M%S")
            speak(f"Sir ! The Time is {strtime}")
        elif 'open pycharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.3\\bin\\pycharm64.exe"
            os.startfile(codePath)
        elif 'email to dhanush' in query:
            try:
                speak("What Should I Say ?")
                content = takecommmand()
                to = "dhanushlnaik@gmail.com"
                sendEmail(to, content)
                speak('Email has been sent !')
            except Exception as e:
                speak("Sorry Sir ! But Due to some problems email was not sent !")
                print(e)
        elif 'in google' in query:
            query = query.replace('in google', '')
        elif 'close' in query:
            speak("Ok Boss")
            exit()
        elif 'hello' in query:
            speak("its Going Fine Boss all because of you")
        elif 'thank you' in query:
            speak("My Pleasure Boss! What Else can I do for you")
