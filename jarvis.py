import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
# emails= {'vishal' : 'vishalvk386879@gmail.com',}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id) 
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir")
    elif hour>=12 and hour<18:
        speak("Good evening sir")
    else :
        speak("Good Evening")
    speak("I am jarvis. How may i help you?")

def takeCommond():
    #take mic input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")  
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recongnizing...")
        query = r.recognize.google(audio, language ='en-in')
        print("user said: ", query)
    except Exception as e:
        print(e)
        print("say that again please..")
        return "None"
    return query

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your=password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__=="__main__":
    speak("good morning master vishal")
    # TakeCommond()
    while True:
        query =takeCommond().lower()
        # Task based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Hp\\Music'
            songs = os.listdir(music_dir)      
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        
        elif 'open codes' in query:
            try:
                codepath="C:\\Users\\Hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
            except:
                speak("Please Install VSCode First!")
                webbrowser.open("https://code.visualstudio.com/")

        elif 'who made you' in query:
            speak("Vishal Kumar Is The Creator Of Me! I Love him 3000!")
        
        elif 'you there' in query:
            j_there = ["Always at your service sir", "Yes Sir", "Always!", "Yes Sir, I Love Seeing you work"]
            j_speak = random.choice(j_there)
            speak(j_speak)
        
        elif 'love you' in query:
            j_love = ["I Love You 3000 Sir", "I Love you too!", "yeah Sir Love You Too!"]
            j_speak = random.choice(j_love)
            speak(j_speak)
         
        elif 'send an email' in query:
            try:
                speak("what should i say")
                content = takeCommond()
                to = "vishalvk386879@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry! unable to send email right now")
  
        elif 'stop' in query:
            speak("good by sir")
            quit()
