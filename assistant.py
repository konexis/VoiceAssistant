#!/usr/bin/env/python3
#coding=utf-8

import speech_recognition as sr
import os
import pyautogui


try:
    while True:
        recognizer_instance = sr.Recognizer() 
       
        with sr.Microphone() as source:
            recognizer_instance.adjust_for_ambient_noise(source)
            os.system("clear")
            print("Sto ascoltando")
            audio = recognizer_instance.listen(source)
            print("Elaboro...")
        try:
            text = recognizer_instance.recognize_google(audio, language="it-IT")
            
            textstr = str(text) 
            
            
            tab = ["Tab","tab","tabulazione","Tabulazione"] 
            if textstr in tab:
                pyautogui.press("tab")


            tab_rev = ["Tabulazione inversa","tabulazione inversa"]
            if textstr in tab_rev:
                pyautogui.hotkey('shift','tab')

            go_up = ["Su","Vai su","Vai in alto","vai in alto"]
            if textstr in go_up:
                pyautogui.press("up")
            

            pageup = ["Pagina su","pagina su"] 
            if textstr in pageup:
                pyautogui.press("pageup")	    

            go_down = ["Giù","Vai giù","Vai in basso","vai in basso","vai giù"]

            if textstr in go_down:
                pyautogui.press("down")

            pagedown = ["Pagina giù","pagina giù","pagina giu","Pagina giu"] 

            if textstr in pagedown:
                pyautogui.press("pagedown")	    

            press_enter = ["invio","Invio","Enter"]
            if textstr in press_enter:
                pyautogui.press(["enter"])


            stop = ["Stop","stop"]
            if textstr in stop:
                exit(0)

            change_tab = ["Cambia finestra","cambia finestra","cambia la finestra"]
            if textstr in change_tab:
                pyautogui.hotkey('altleft','tab')
                pyautogui.press("enter")

            gotoend = ["Vai alla fine","vai alla fine", "scorri alla fine"]
            if textstr in gotoend:
                pyautogui.hotkey('ctrl','down')


            gotobeginning = ["Vai all'inizio","vai all'inizio", "scorri all'inizio"]
            if textstr in gotoend:
                pyautogui.hotkey('ctrl','up')

            exitwindow = ["Chiudi", "chiudi", "chiudi la finestra"]
            if textstr in exitwindow:
                pyautogui.hotkey('alt','f4')

            click = ["Clicca","clicca","premi","Premi"]
            if textstr in click:
                pyautogui.click()

        except Exception as e:
            print(e)




except KeyboardInterrupt:
    print("\n\nExiting...")
    exit(0)
