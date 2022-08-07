import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime
import webbrowser
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        pass
    return command
def run_alexa():
    command = take_command()
    print(command)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+time)
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif "Login Page" in command:
        webbrowser.open("")
    elif "sign up" in command:
        webbrowser.open("")
    else:
        talk("Please say the command again")
run_alexa()