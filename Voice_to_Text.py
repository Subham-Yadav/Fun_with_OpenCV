    from tkinter import *
from playsound import playsound
import speech_recognition as sr

def recordVo():
    global e
    recording = sr.Recognizer()
    with sr.Microphone() as source:
        recording.adjust_for_ambient_noise(source)
        playsound('Sound\speech.wav')
        audio = recording.listen(source)
        try:
            #print(recording.recognize_google(audio))
            Text.insert(e, END,  recording.recognize_google(audio) + " ")
        except Exception as ep:
            Text.insert(e, END, ep)
            #print(ep)


new_win = Tk()
new_win.title("Voice to Text")
new_win.geometry("375x200")

record = Button(new_win, text="Record", command=recordVo)
record.grid(row=1, column=1, padx=(25,0), pady=(30,0))

e = Text(new_win, height=5, width=40)
e.grid(row=2, column = 1, padx=(25,25), pady=(20,10))
e.focus_set()

new_win.resizable(0,0)
new_win.mainloop()
