from tkinter import *
import sys
import tkinter.messagebox
from tkinter import messagebox
tkinter.messagebox

top = tkinter.Tk()
def hello():
   tkMessageBox.showinfo("Say Hello", "Hello World")

B1 = tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()