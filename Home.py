from tkinter import *
import os
from playsound import playsound
import speech_recognition as sr

##Functions
def funcOne():
    exec(open("color_palette.py").read())

def funcTwo():
    exec(open("Select_File.py").read())

def funcThree():
    exec(open("Voice_to_Text.py").read())

def funcFour():
    #exec(open("DinosaurBot.py").read())
    exec(open("DinosaurBot.py").read(), globals())

def funcFive():
    exec(open("face_detection.py").read())

def funcSix():
    exec(open("Voice_search.py").read())

###Window
root = Tk()
root.title('Project')   #Name of Project
root.geometry("1000x610")   #Window size of home screen

##Button 1
b1 = Button(root, command = funcOne, justify = LEFT)
photo_1 = PhotoImage(file = "Images/color_pallete.png")
b1.config(image = photo_1, width="250", height="200")
b1.pack(side=LEFT)
b1.grid(row=1, column= 1, padx=30, pady=(40,0))
#Button1 Text
w1 = Label(root, text="Color Pallete")
w1.config(font=("Courier", 18))
w1.grid(row=2, column= 1, padx=30)

##Button 2
b2 = Button(root, command = funcTwo)
photo_2 = PhotoImage(file="Images/edge_detection.png")
b2.config(image=photo_2, width="250", height="200")
b2.grid(row=1, column=2, padx=30, pady=(40,0))
#Button2 Text
w2 = Label(root, text="Edge Detection")
w2.config(font=("Courier", 18))
w2.grid(row=2, column=2, padx=30)

##Button 3
b3 = Button(root, command = funcThree)
photo_3 = PhotoImage(file ="Images/voice_to_text.png")
b3.config(image=photo_3, width="250", height="200")
b3.grid(row=1, column=3, padx=30, pady=(40,0))
#Button3 Text
w3 = Label(root, text="Voice To Text")
w3.config(font=("Courier", 18))
w3.grid(row=2, column=3, padx=30)

##Button 4
b4 = Button(root, command = funcFour)
photo_4 = PhotoImage(file="Images/t_rex_game.png")
b4.config(image=photo_4, width="250", height="200")
b4.grid(row=3, column=1, padx=30, pady=(60,0))
#Button4 Text
w4 = Label(root, text="Automated T-Rex Game")
w4.config(font=("Courier", 18))
w4.grid(row=4, column=1, padx=30, pady=(0, 40))

##Button 5
b5 = Button(root, command = funcFive)
photo_5 = PhotoImage(file="Images/face_detection1.png")
b5.config(image=photo_5, width="250", height="200")
b5.grid(row=3, column=2, padx=30, pady=(60,0))
#Button5 Text
w5 = Label(root, text="Face Detection")
w5.config(font=("Courier", 18))
w5.grid(row=4, column=2, padx=30, pady=(0, 40))

##Button 6
b6 = Button(root, command = funcSix)
photo_6 = PhotoImage(file="Images/voice_to_text.png")
b6.config(image=photo_6, width="250", height="200")
b6.grid(row=3, column=3, padx=30, pady=(60,0))
#Button5 Text
w6 = Label(root, text="Voice Search")
w6.config(font=("Courier", 18))
w6.grid(row=4, column=3, padx=30, pady=(0, 40))


root.iconbitmap("Images/icon1.ico")
root.resizable(0, 0)
root.mainloop()
