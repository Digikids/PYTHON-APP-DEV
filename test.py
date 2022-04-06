from tkinter import *
import tkinter
from tkinter import messagebox

#functions
def entry_delete():
    ent.delete(0, END)

def addition():
        global f_num
        f_num = ent.get()

        global math
        math = "Addition"
        ent.delete(0, END)

def subtraction():
        global f_num
        f_num = ent.get()
        global math
        math = "Subtraction"
        ent.delete(0, END)

def division():
        global f_num
        f_num = ent.get()
        global math
        math = "Division"
        ent.delete(0, END)

def multiplication():
        global f_num
        f_num = ent.get()
        global math
        math = "Multiplication"
        ent.delete(0, END)

def equals():
        second_number = ent.get()
        ent.delete(0, END)
        try:
            if math == "Addition":
                    ent.insert(0, int(f_num) + int(second_number))
            elif math == "Subtraction":
                    ent.insert(0, int(f_num) - int(second_number))
            elif math == "Division":
                    ent.insert(0, int(f_num) / int(second_number))
            elif math == "Multiplication":
                    ent.insert(0, int(f_num) * int(second_number))
            else:
                    pass
        except ValueError:
            messagebox.showwarning("Error", "Please input interger values")
            
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
        activebackground=colours[1], command=addition)
btn2 = tkinter.Button(surface, text="-", padx=60, pady=30, bg=colours[4],
        activebackground=colours[1], command=subtraction)
btn3 = tkinter.Button(surface, text="X", padx=60, pady=30, bg=colours[4],
        activebackground=colours[1], command=multiplication)
btn4 = tkinter.Button(surface, text="/", padx=60, pady=30, bg=colours[4],
        activebackground=colours[1], command=division)

btn5 = tkinter.Button(surface, text="=", padx=60, pady=30, bg=colours[4],
        activebackground=colours[1], command=equals)
btn6 = tkinter.Button(surface, text="Clear", padx=60, pady=30, bg=colours[4],
        activebackground=colours[1], command=entry_delete)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)
btn4.grid(row=1, column=3)

btn5.grid(row=2, column=0, columnspan=2)
btn6.grid(row=2, column=2, columnspan=2)


surface.mainloop()
