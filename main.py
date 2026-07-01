from tkinter import *
import shelve
import os
from classes import *

kurs_db = shelve.open('db/kurse.db')
db_gebucht = shelve.open('db/kursstatus.db')
kurs = Kursauswahl(True)

root = Tk()
root.title("Home")
root.state('zoomed')

#Die einfache Funktion zum Schließen des Programms, später wird als "Zurück" auf vorherige Seite genutzt
def close():
    root.destroy()

def curcheck(boxvar, kursvar):
    try:
        if db_gebucht[kursvar].gebucht:
            boxvar["text"] = kurs_db[kursvar].name
    except KeyError:
        pass

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
#root.geometry("%dx%d" % (width, height))

ico = PhotoImage(file='inter/imgs/BLANK_ICON.png')
root.iconphoto(True, ico)

button_buchen = Button(root, text="Kurs buchen",
                       command= lambda: os.system('booking.py'),
                       width=24, height=1)
button_buchen.place(x=width/10, y=height/3.75)

button_aktuell = Button(root, text="Aktuelle Kurse",
                       command= lambda: os.system('current.py'),
                       width=24, height=1)
button_aktuell.place(x=width/1.3, y=height/3.75)

button_noten = Button(root, text="Noten ansehen",
                      command= lambda: os.system('marks.py'),
                      width=24, height=1)
button_noten.place(x=width/10, y=height/1.9)

kursbox = Label(root, width=24, height=13, bg="grey")
#Prüft, ob der Kurs gebucht ist und weist den Namen des Kurses der Kursbox zu
curcheck(kursbox, 'OOP')
kursbox.place(x=width/10, y=height/3.3)

kursbox2 = Label(root, width=24, height=13, bg="grey")
curcheck(kursbox2, 'Mathematik')
kursbox2.place(x=width/3.1, y=height/3.3)

kursbox3 = Label(root, width=24, height=13, bg="grey")
curcheck(kursbox3, 'Cybersecurity')
kursbox3.place(x=width/1.85, y=height/3.3)

kursbox4 = Label(root, width=24, height=13, bg="grey")
curcheck(kursbox4, 'Requirements Engineering')
kursbox4.place(x=width/1.3, y=height/3.3)

button_close = Button(root, text="Schließen", command=close)
button_close.place(x=width/40, y=height/36.0)

root.mainloop()