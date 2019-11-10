import speech_recognition as sr
import os
import pyautogui


try:
    while True:
        recognizer_instance = sr.Recognizer() 

        with sr.Microphone() as source:
            recognizer_instance.adjust_for_ambient_noise(source)
            print("Sto ascoltando")
            audio = recognizer_instance.listen(source)
            print("Elaboro...")
        try:
            text = recognizer_instance.recognize_google(audio, language="it-IT")
            
            textstr = str(text) 
            

            go_up = ["Su","Vai su", "Scorri sopra","Vai in alto"]
            if textstr in go_up:
                pyautogui.press(["up"])
            


            go_down = ["Giù","Vai giù"]
            if textstr in go_down:
                pyautogui.press["down"]



            press_enter = ["Invio","Enter"]
            if textstr in press_enter:
                pyautogui.press(["enter"])


            stop = ["Stop","stop"]
            if textstr in stop:
                exit(0)

        except Exception as e:
            print(e)




except KeyboardInterrupt:
    print("Exiting...")
    exit(0)