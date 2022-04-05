from tkinter import *
import tkinter

#setup
colours = ["aquamarine3", "Red", "Black", "Yellow", "aqua"]
surface = tkinter.Tk()
surface.title("Calculator")
surface.geometry("550x300")
surface.configure(bg=colours[0])

#widgets
ent = tkinter.Entry(surface, bd=2, width=35, bg=colours[3], fg=colours[2])
ent.grid(row=0,column=1, columnspan=2)

#buttons
btn1 = tkinter.Button(surface, text="+", padx=60, pady=30, bg=colours[4],
        activebackground=colours[1])
btn2 = tkinter.Button(surface, text="-", padx=60, pady=30, bg=colours[4],
        activebackground=colours[1])
btn3 = tkinter.Button(surface, text="X", padx=60, pady=30, bg=colours[4],
        activebackground=colours[1])
btn4 = tkinter.Button(surface, text="/", padx=60, pady=30, bg=colours[4],
        activebackground=colours[1])

btn5 = tkinter.Button(surface, text="=", padx=60, pady=30, bg=colours[4],
        activebackground=colours[1])
btn6 = tkinter.Button(surface, text="Clear", padx=60, pady=30, bg=colours[4],
        activebackground=colours[1])

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)
btn4.grid(row=1, column=3)

btn5.grid(row=2, column=0, columnspan=2)
btn6.grid(row=2, column=2, columnspan=2)

surface.mainloop()