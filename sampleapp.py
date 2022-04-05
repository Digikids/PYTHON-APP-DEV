from tkinter import *
import tkinter

#SETUP
bg1 = "aquamarine3"
surface = tkinter.Tk()
surface.title("SampleApp")
surface.geometry("440x450")
surface.configure(bg=bg1)


btn = tkinter.Button(surface, text="Button 1", activebackground="Purple",
fg="RED", bg=bg1, padx=40, pady=20)
btn.grid(column=0, row=1)

lbl = tkinter.Label(surface, text="Creating an app on my own", bg=bg1)
lbl.grid(column=1, row=0)

lbl_2 = tkinter.Label(surface, text="My Name", bg=bg1)
lbl_2.grid(column=0, row=2)
etr = tkinter.Entry(surface, bd=5)
etr.grid(column=1, row=2)

surface.mainloop()