import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from random import randrange

#Liste mit allen Daten (Kürzel, Name, Hauptstadt)
daten = [["ch","Schweiz","Bern"],["DEU","Deutschland","Berlin"],["BE","Belgien","Brüssel"]]

def start(aktuell, stadt, land):
    tk.Label(win, text="Hauptstadt von " + land).pack()
    userInput(aktuell, stadt)

#Zufällige Auswahl
def auswahl():
    aktuell = randrange(len(daten))
    land = daten[aktuell][1]
    stadt = daten[aktuell][2]

#Textrückgabe des Eingabefelds
def userInput(aktuell, stadt):
    p = entry.get()

    if p == stadt:
        pasten = Image.open(daten[aktuell][0]+"_g.png").resize((400, 400), Image.LANCZOS)
    else:
        pasten = Image.open(daten[aktuell][0]+"_r.png").resize((400, 400), Image.LANCZOS)

    # Erstelle ein neues Bild als Kopie von img_bottom
    combined_img = pasten.copy()

    # Füge das obere Bild auf das untere Bild ein
    #combined_img.paste(img_top, (0, 0), img_top)

    # Aktualisiere das Bild im Label
    img_combined = ImageTk.PhotoImage(combined_img)
    image_label.config(image=img_combined)
    image_label.image = img_combined

    print(p)

# Nachfolgend wird ein Fenster erzeugt, in welchem eine Eingabe stattfinden kann
win = Tk()
win.title("Europaquiz")
win.geometry("800x600")

#Initialisiere das Label für das Bild
img = ImageTk.PhotoImage(Image.open("EuropaleereKarte.png").resize((400, 400), Image.LANCZOS))
image_label = tk.Label(win, image=img)
image_label.place(relx=.5, rely=.5, anchor=tk.CENTER)

aktuell = randrange(len(daten))
land = daten[aktuell][1]
stadt = daten[aktuell][2]

tk.Label(win, text="Hauptstädtequiz Europa").pack()
tk.Label(win, text="Hauptstadt von " + land).pack()

#Eingabefeld
entry = Entry(win, width=30)
entry.place(relx=.5, rely=.13, anchor=CENTER)

#Button
startButton = tk.Button(win, text="Check", command=userInput(aktuell, stadt)).pack()

win.mainloop()
