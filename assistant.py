import speech_recognition as sr
import os
import pyautogui

recognizer_instance = sr.Recognizer() 

with sr.Microphone() as source:
    recognizer_instance.adjust_for_ambient_noise(source)
    print("Sto ascoltando")
    audio = recognizer_instance.listen(source)
    print("Elaboro...")
try:
    text = recognizer_instance.recognize_google(audio, language="it-IT")
    print("Ho capito \n", text)
except Exception as e:
    print(e)
