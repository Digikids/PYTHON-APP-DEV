from tkinter import *
import tkinter

top = tkinter.Tk()

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=10, \
                 width = 30)
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=20, \
                 width = 30)
C1.pack()
C2.pack()
top.mainloop()