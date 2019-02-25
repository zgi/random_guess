# -*- coding: utf-8 -*-
import Tkinter
import random
import tkMessageBox

window = Tkinter.Tk()
width = 350
height = 100
window.geometry("%sx%s" % (width, height))
window.resizable(0, 0)
greeting_text = "Ugani število"
greeting = Tkinter.Label(window, text=greeting_text)
greeting.pack()
input_label = Tkinter.Label(window, text="Vpiši št.:")
input_label.pack()
input_label.place(x=60, y=30)
guess = Tkinter.Entry(window)
guess.pack()
guess.place(x=110, y=30)

secret = random.randint(0, 100)

def preveri():
    try:
        if int(guess.get()) == secret:
            message = "PRAVILNO"
        elif int(guess.get()) > secret:
            message = "NAPACNO! Ugibal si previsoko"
        elif int(guess.get()) < secret:
            message = "NAPACNO! Ugibal si prenizko"
    except ValueError:
        message = "Napačen vnos. Poskusi vnesti število."

    tkMessageBox.showinfo("Sporočilo", message)

potrdi = Tkinter.Button(window, text="Potrdi", command=preveri)
potrdi.pack()
potrdi.place(x=240, y=25)
izhod = Tkinter.Button(window, text="Izhod", command=exit)
izhod.pack()
izhod.place(x=150, y=60)

window.mainloop()