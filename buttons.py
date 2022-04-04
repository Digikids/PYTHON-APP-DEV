from tkinter import *
import tkinter

master = tkinter.Tk()

def say_hello():
    greeting = tkinter.Label(text="Hello, User. How are you?", bg="Red")
    greeting.pack()

Button_1 = tkinter.Button(master, text = "Click me 1", relief=RAISED,
                            activebackground = "Purple", command=say_hello, bg="Red")

Button_2 = tkinter.Button(master, text = "Click me 2", relief=GROOVE)
Button_3 = tkinter.Button(master, text = "Click me 3", relief=RIDGE)
Button_1.pack()
Button_2.pack()
Button_3.pack()

Label_1 = tkinter.Label(master, text="User Name")
Label_1.pack(side = LEFT)
entry_1= tkinter.Entry(master, bd=5)
entry_1.pack(side = RIGHT)

Label_2 = tkinter.Label(master, text="Gender")
Label_2.pack(side = LEFT)
entry_2= tkinter.Entry(master, bd=5)
entry_2.pack(side = RIGHT)

master.mainloop()