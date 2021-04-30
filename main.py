import speech_recognition as sr
import webbrowser   # for searching our speech in web
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTS


r = sr.Recognizer()  # Recognizer for speech recognition


def record_Audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            san_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            san_speak("Sorry, I did not get that")
        except sr.RequestError:
            san_speak("Sorry, my speech service is down")
        return voice_data

def respond_voice_data(voice_data):
    if 'what is your name' in voice_data:
        san_speak("May name is Sanath")
    if 'what is the time now' in voice_data:
        san_speak("The time is: " , ctime())
    if 'search' in voice_data:
        search = record_Audio('What do you want to search for ?')
        url ='https://google.com/search?q='+ search
        webbrowser.get().open(url)
        san_speak("Here is what I found for " + search)
    if 'find location' in voice_data:
        location = record_Audio('Which location do you want ')
        url ='https://google.com/maps/place/'+ location + '/&amp;'
        webbrowser.get().open(url)
        san_speak("Here is the location for " + location)
    if 'exit' in voice_data:
        exit()

def san_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en' )
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


time.sleep(1)
san_speak("How can I help you?")
while(1):
    voice_data= record_Audio()
    respond_voice_data(voice_data)

