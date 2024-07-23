import speech_recognition as sr
import openai
import webbrowser as wb
# from pygsr import Pygsr
import pyttsx3
from sympy import true

engine = pyttsx3.init()

# def search_in_google(self, params):
#     query = "+".join(params)
#     url = f"www.google.com/search?q={query}"
#     wb.open(url)

def process(text):
    if text == 'good morning':
        speak('good morning sir, how are you')
    if text == 'i am fine':
        speak('so how can i help you')
    if text == 'no':
        speak('okay')
    if text == 'jarvis stop':
        speak('okay sir, i am leaving')
        exit()

def speak(text):
    print("jarvis :",text)
    engine.say(text)
    engine.runAndWait()
    

if __name__ == "__main__":
    while true:
        feed = input('user : ')
        process(feed)