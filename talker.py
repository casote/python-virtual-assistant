import os
import random
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

#-------define the speaker voice and lang
def speak(text):
    tts = gTTS(text = text, lang = "en")#change to "en"
    audio_voice = "voice.mp3"
    tts.save(audio_voice)
    playsound.playsound(audio_voice)
    os.remove('voice.mp3')


#-------define the mike function
def get_voice():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recog.listen(source)
        said = ""

#-------Use google api to regonize audio
        try:
            said = recog.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exp: " + str (e))
    return said

print("listening...")

#-------variable answer

end = "goodbye"
finaltext = get_voice()

while end not in finaltext:

    finaltext = get_voice()

    if "hi" in finaltext:
        speak("konnich'wa")

    elif "hello" in finaltext:
        speak("hello, how are you?")

    elif "fine" in finaltext:
        speak("good for you m8")

quit()