#Modifizierter und ausgebauter Code auf Basis von tutorialspoint.com
#Original: https://www.tutorialspoint.com/return-the-input-of-the-entry-widget-in-tkinter

import tkinter as tk
from tkinter import PhotoImage
from glob import glob
from tkinter import *

#Nachfolgend wird ein Fenster erzeugt, in welchem eine Eingabe stattfinden kann
win = Tk()
win.title("Europaquiz")
win.geometry("700x250")

#Textrückgabe des Eingabefelds
def userInput():
    p = entry.get()
    print (p)

#Eingabefeld
entry = Entry(win, width = 42)
entry.place(anchor = CENTER)
entry.pack()

#Feldtitel
label= Label(win, text="Hauptstädtequiz Europa").pack()
tk.Label(win, text="Hauptstadt von <>").pack()

#Button
tk.Button(win, text= "Absenden", command = userInput).place(relx= .7, rely= .5, anchor= CENTER)

win.mainloop()

#Modifizierter und ausgebauter Code auf Basis von @GiovanniPython
#Original: https://pythonprogramming.altervista.org/how-to-show-and-image-with-tkinter/

#Dieser Teil zeigt die Umrisse der Länder (alphabetisch) in einem neuen Fenster, nachdem eine Eingabe stattfand
#Die beiden Codes müssen noch verknüpft werden und dienen bis jetzt nur als Basis

class Window:
    
    def __init__(self, images: list):
        self.images = images
        self.imagepos = 0
        self.root = tk.Tk()
        self.widgets()
        self.root.mainloop()

    def widgets(self):
        self.lab_image()
        self.start_button()

    def lab_image(self):
        self.img = PhotoImage(file=self.images[self.imagepos])
        self.label = tk.Label(self.root, image=self.img)
        self.label.pack()



    def start_button(self):
        self.butstart = tk.Button(self.root,
            text="Start",
            command=self.slideshow)
        self.butstart.pack()

    def slideshow(self):
        if self.imagepos < len(self.images) - 1:
            self.imagepos += 1
        else:
            self.imagepos = 0
        self.img = PhotoImage(file=self.images[self.imagepos])
        self.label["image"] = self.img


images = glob("*png")
win = Window(images)
