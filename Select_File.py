from tkinter import *
import os

def FileName():
    global e, new_win
    st = e.get()
    file = open('temp.txt','w')
    file.write(st)
    file.close()
    new_win.destroy()
    exec(open("Edge_detection.py").read())
    

new_win = Tk()
new_win.title('Enter Name')
new_win.geometry('250x120')
e = Entry(new_win)
e.grid(row=1, column=1, padx=(60,0), pady=(40,0))
e.focus_set()
b = Button(new_win, text = 'Open', command=FileName)
b.grid(row=2, column=1, padx=(65,0), pady=5)
new_win.mainloop()
