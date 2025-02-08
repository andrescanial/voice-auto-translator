import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import playsound

def translate_speech():
    recognizer = sr.Recognizer()
    translator = Translator()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            # Recognize speech
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")

            # Translate to English
            translation = translator.translate(text, dest='en')
            print(f"Translated: {translation.text}")

            # Convert translated text to speech
            tts = gTTS(text=translation.text, lang='en')
            tts.save("translated.mp3")
            playsound.playsound("translated.mp3")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    translate_speech()
