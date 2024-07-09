import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
import random
import pyautogui
import string 
import pywhatkit 
import wikipedia

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

def wishme():
    print("Welcome back!!")
    speak("Welcome back!!")

    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning!!")
        print("Good Morning!!")
    elif 12 <= hour < 16:
        speak("Good Afternoon!!")
        print("Good Afternoon!!")
    elif 16 <= hour < 24:
        speak("Good Evening!!")
        print("Good Evening!!")
    else:
        speak("Good Night, See You Tommorrow")

    speak("I am at your service, please tell me how may I help you.")
    print("I am at your service, please tell me how may I help you.")

def generate_random_string(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def screenshot():
    img = pyautogui.screenshot()  
    folder_path = "C:\\Users\\ASHWINI SONI\\Pictures"     
    random_filename = generate_random_string() + ".png"
    img_path = os.path.join(folder_path, random_filename)
    img.save(img_path)
    print(f"Screenshot saved as: {random_filename}")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I am a virtual assistant created by Ms. Ashwini.")
            print("I am a virtual assistant created by Ms. Ashwini.")

        elif "how are you" in query:
            speak("I'm fine, What about you?")
            print("I'm fine, What about you?")

        elif "fine" in query:
            speak("Glad to hear that!!")
            print("Glad to hear that!!")

        elif "good" in query:
            speak("Glad to hear that!!")
            print("Glad to hear that!!")

        elif 'who is' in query:
          human = query.replace('who is', " ") 
          info = wikipedia.summary(human, 1)
          print(info) 
          speak(info) 

        elif "play" in query: 
         song = query.replace('play', "") 
         speak("playing" + song) 
         pywhatkit.playonyt(song) 

        elif "open google" in query:
            wb.open("google.com")

        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif "open chrome" in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")

        elif "offline" in query:
            quit()