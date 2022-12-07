# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 20:57:52 2021

@author: József
"""
import _thread 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import winsound 
import pyttsx3
import speech_recognition as sr
import os
import pyttsx3
import subprocess
import pyautogui
import datetime
import webbrowser as wb
import smtplib
import pywhatkit
import time as tt
import sys

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak("The current time is")
    speak(Time)


def date():
    Year = datetime.datetime.now().year
    Month = datetime.datetime.now().month
    Day = datetime.datetime.now().day
    speak("Today the date is:")
    speak(Year)
    speak(Month)
    speak(Day)

def greet_user():
    speak("Personal voice recognition assissstant is on.")
    hour = datetime.datetime.now().hour
    if hour < 12 and hour > 6:
        speak("Good morning! How did you sleep? How Can I help you?")
        
    elif hour < 18 and hour > 12:
        speak("Good afternoon! How is your day? How can I assisst you?")
        
    elif hour < 24 and hour > 18:
        speak("Good Evening! How was your day? Do you mind helping you with something before sleep?")
              
             
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query   
    
    
def longBeep():
    
    
    
    frequency = 3000

    duration = 6000


    
    winsound.Beep(frequency, duration)
    
def building_Barchart():
    pass




def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\József\\Desktop\\károli válogatás 1\\Screenshot\\image.jpg")
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.freemail.hu', 587)
    server.ehlo()
    server.starttls()
    server.login('eckert91@freemail.hu', '***************************')
    server.sendmail('eckertjozsef5@gmail.com', to, content)
    server.close()

def handwrite():
    speak("What should I write?")
    note = takeCommand()
    speak("you told me to write it down with handwriting" + note)
    take_note = open('taken_note.txt', 'w')
    take_note.write(note)
    take_note.close()
    pywhatkit.text_to_handwriting(note, rgb=(0,0,300))
    

def timeSleep():
    time.sleep(10)
    print("Goodbye!")
    

   
 
                

    



if __name__ == '__main__':
    greet_user()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()
            
        elif "long beep" in query:
            longBeep()
            
        elif 'create chart' in query:
            try:
                while True:
                    list1 = []
                    speak("How many elements would you like to have for the x axis?")
                    numofel = takeCommand()
                    speak(f"So the first list will have: {numofel} elements.")
                    for i in range(int(numofel)):
                        speak("What elements should it contain?")
                        ele = takeCommand()
                        ele = str(ele)
                    
                        list1.append(ele)
                    list2 = []
                    speak("And how many elements would you like to have for the y axis?")
                    numofel2 = takeCommand()
                    speak(f"So the second list will have: {numofel2} elements.")
                    for i in range(int(numofel2)):
                        speak("What elements should it contain?")
                        ele2 = takeCommand()
                        ele2 = int(ele2)
                     
                        list2.append(ele2)
                        
                    
                        
                    Country = [list1]
                    GDP_Per_Capita = [list2]
                    fig = plt.figure(figsize = (10, 5))
            
                    plt.bar(Country, GDP_Per_Capita)
                    plt.title('Country Vs GDP Per Capita')
                    plt.xlabel('Country')
                    plt.ylabel('GDP Per Capita')
                    plt.show()
                    
                break  
                   
                 
                print("Well done, your list of numbers is complete!", list1)
            
            except ValueError:
               print("Invalid input")
               
            
            
           

            building_Barchart()
            
        elif "simple bar chart" in query or "build a bar chart" in query:
             speak("Hello! I am a simple bar chart building application, named Charty. \t When you giving me the elements of X axis, please note that you can only use strings. And elements of Y axis can only be integers.")
             print("Hello! I am a simple bar chart building application, named Charty. \t When you giving me the elements of X axis, please note that you can only use strings. And elements of Y axis can only be integers.")
             plt.bar([str(input("Give me the elements of the X axis! ")) for i in range(int(input(speak("How many elements will the X axis have? "))))], [float(input(speak("Give me the elements of the Y axis! "))) for i in range(int(input(speak("How many elements will the Y axis have? "))))], color = input(speak("Give me the color of the columns: ")))
             plt.title(input(speak("What will be the title of the bar chart? ")))
             plt.xlabel(input(speak("What will be the name of the X axis?: ")))
             plt.ylabel(input(speak("What will be the name of the Y axis?: ")))
             data = input(speak("Your diagram is complete. Would you like to save it? [yes/no] "))
             if "yes" in data:
                 plt.savefig(input(speak("With what name would you like to save your chart? "))+'.png', dpi=400, bbox_inches='tight')
                 plt.show()      

            
          
            
        

        elif "log off" in query or "logoff" in query:
            speak("Ok , your pc is logging off")
            subprocess.call(["shutdown", "/l"])

        elif 'open youtube' in query:
            wb.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            
        elif "execute order 66" in query:
            wb.open_new_tab("https://www.youtube.com/watch?v=xSN6BOgrSSU&ab_channel=hardrivefreak")
            speak("As you wish My Lord!")

        elif 'open google' in query:
            wb.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")

        elif 'open gmail' in query:
            wb.open_new_tab("gmail.com")
            speak("Gmail is open now")

        elif 'play songs' in query:
            songs_dir = 'C:\\Music'
            songs = os.listdir(songs_dir)
            song_name = takeCommand()
            if "toss a coin" in song_name:
                os.startfile(os.path.join(songs_dir, songs[1]))
                tt.sleep(4)
            elif "toss a coin" not in song_name:
                os.startfile(os.path.join(songs_dir, songs[0]))
           
            else:
                print("Error")
                
            
            # songs[1]
            
        elif 'send an email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = 'eckertjozsef5@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
                
        elif "execute system command" in query:
            speak("Choose an operation command: ")
            try:
                
                logout_confirmation = takeCommand()

                if logout_confirmation == "restart":
                    speak("Understood. Restarting computer immediately.")
                    print("Understood. Restarting computer imemdiately.")
                    
                    os.system("shutdown /r /t 1") #command to logout
                
                elif logout_confirmation == "shutdown computer":
                    speak("Understood. Shutting down computer.")
                    print("Understood. Shuting down computer.")
                    os.system('shutdown /s /t 1')
    
                elif logout_confirmation == "just quit":
                        exit()
    
                else:
                        print("Invalid Command")
                        speak("Invalid Command.")
            except Exception as e:
                print(e)
                speak("Unable to execute command.")
            
    
                

        elif 'remember that' in query:
            speak("What should i remember?")
            data = takeCommand()
            speak("you said me to remember that" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
            
        elif 'write down the following' in query:
           handwrite()
           speak("Your handwritten note is done! You may open it from the current writing directory!")
            

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you told me to remember that" + remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
            
        elif "open game" in query:
            games_dir = "C:\\GOG Games\\Star Wars Jedi Knight - Jedi Academy"
            games = os.listdir(games_dir)
            os.startfile(os.path.join(games_dir, games[8]))
            speak("Star Wars Jedi Knight Jedi Academy is open now.")
            
        elif "open video" in query:
            videos_dir = "C:\\Users\\József\\Desktop\\károli válogatás 1\\videók"
            videos = os.listdir(videos_dir)
            os.startfile(os.path.join(videos_dir, videos[0]))
            speak("The requested video is open now.")
            
            

