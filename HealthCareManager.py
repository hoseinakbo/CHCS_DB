
# import tkinter
# top = tkinter.Tk()
# # Code to add widgets will go here...
# w = tkinter.Entry(top)
# top.mainloop()

from tkinter import *
from tkinter import ttk

window = Tk()

window.style = ttk.Style()
window.style.theme_use("alt")
window.title("Health Care System")

L1 = Label(window, text="Enter Query: ")
L1.pack()
# L1.pack( side = LEFT)

E1 = Entry(window, width=50)
E1.pack()
# E1.pack(side = RIGHT)

ok = Button(window, text="OK")
ok.pack()
# ok.pack(side = BOTTOM)

window.mainloop()