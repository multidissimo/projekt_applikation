#TODOs
#Daten Liste vervollständigen
#Bereits abgefragte, richtige Länder in neue Liste übertragen, um Wiederholungen zu Vermeiden
#Bereits abgefragte, falsche Länder in neue Liste übertragen und am Ende wiederholen lassen
#Wenn die "falsche Liste" leer und die "richtige Liste" voll sind, "Gratulation!" oder so anzeigen

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from random import randrange

#Liste mit allen Daten (Kürzel, Name, Hauptstadt)
daten = [["ch","Schweiz","Bern"],["deu","Deutschland","Berlin"],["be","Belgien","Brüssel"],["SK","Slowakei","Bratislava"],["AT","Österreich","Wien"],["PL","Polen","Warschau"],["CZ","Tschechien","Prag"],["LI","Fürstentum Liechtenstein","Vaduz"],["GB","England","London"],["IE","Irland","Dublin"],["FR","Frankreich","Paris"],["IT","Italien","Rom"],["LU","Luxemburg","Luxemburg"],["NL","Niederlande","Amsterdam"],["DK","Dänemark","Kopenhagen"],["SL","Slowenien","Ljubljana"],["HU","Ungarn","Budapest"],["HR","Kroatien","Zagreb"],["BA","Bosnien und Herzegowina","Sarajevo"],["AL","Albanien","Tirana"],["MK","Nordmazedonien","Skopje"],["ME","Montenegro","Podgorica"],["XK","Kosovo","Pristina"],["RS","Serbien","Belgrad",],["GR","Griechenland","Athen"],["TR","Türkei","Ankara"],["CY","Zypern","Nikosia"],["BG","Bulgarien","Sofia"],["RO","Rumänien","Bukarest"],["MT","Malta","Valletta"],["ES","Spanien","Madrid"],["PT","Portugal","Lissabon"],["AD","Andorra","Andorra la Vella"],["Ru","Russland","Moskau"],["SM","San Marino","San Marino"]["VA","Vatikanstadt","Vatikanstadt"],["EE","Estland","Tallinn"],["LV","Lettland","Riga"]["LT","Litauen","Vilnius"],["IS","Island","Reykjavik"],["NO","Norwegen","Oslo"],["BY","Belarus","Minsk"],["SE","Schweden","Stockholm"],["FI","Finnland","Helsinki"],["MD","Moldawien","Chisinau"]]

#Liste für Speicherung des aktuellen Spielstands
ebenen = []

#Zufällige Auswahl
def auswahl():
    global aktuell

    aktuell = randrange(len(daten))
    land = daten[aktuell][1]
    stadt = daten[aktuell][2]

    #Anzeige aktualisieren
    frage.config(text="Hauptstadt von " + land)

    #Aktualisiere das Bild im Label
    img_combined = ImageTk.PhotoImage(update())
    image_label.config(image=img_combined)
    image_label.image = img_combined

#Überprüfung der Eingabe
def check():
    global ebenen

    #Text aus Eingabefeld auslesen
    p = entry.get()
    #Lösung aus Liste auslesen
    stadt = daten[aktuell][2]

    #Überprüfung ob Eingabe korrekt ist (Ja = grüne Ebene / Nein = rote Ebene)
    if p == stadt:
        ebene = Image.open(daten[aktuell][0]+"_g.png").resize((400, 400), Image.LANCZOS)
    else:
        ebene = Image.open(daten[aktuell][0]+"_r.png").resize((400, 400), Image.LANCZOS)

    #Ebene in Liste speichern
    ebenen.append(ebene)

    #Neue Aufgabe generieren
    auswahl()

    #Kontrollen
    print(p)
    print(ebenen)

#Spielstand aktualisieren
def update():
    spielstand = Image.open("EuropaleereKarte.png").resize((400, 400), Image.LANCZOS)

    #Alle Ebenen aus Liste übereinanderlegen
    for ebene in ebenen:
        spielstand.paste(ebene, (0, 0), ebene)

    #Übereinandergelegtes Bild zurückgeben
    return spielstand

#Grundfunktionen / Setup

#Fenster
win = Tk()
win.title("Europaquiz")
win.geometry("800x600")

#Label für die Frage
frage = tk.Label(win)
frage.pack()

#Eingabefeld
entry = Entry(win, width=30)
entry.place(relx=.5, rely=.1, anchor=CENTER)

#Label für das Bild
img_combined = ImageTk.PhotoImage(update())
image_label = tk.Label(win, image=img_combined)
image_label.place(relx=.5, rely=.5, anchor=tk.CENTER)

#Button
Button = tk.Button(win, text="Check", command=check).pack()

#Generierung der ersten Aufgabe
auswahl()

win.mainloop()
