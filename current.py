from tkinter import *
import shelve
from classes import *

kurs_db = shelve.open('db/kurse.db')
db_gebucht = shelve.open('db/kursstatus.db')
kurs = Kursauswahl(True)

root = Tk()
root.title("Aktuelle Kurse")
root.state('zoomed')

def close():
    root.destroy()

def curcheck(boxvar, kursvar):
    try:
        if db_gebucht[kursvar].gebucht == 1:
            boxvar["text"] = kurs_db[kursvar].info
    except KeyError:
        pass

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
#root.geometry("%dx%d" % (width, height))

ico = PhotoImage(file='inter/imgs/BLANK_ICON.png')
root.iconphoto(True, ico)



kursbox1 = Label(root, width=45, height=25, bg="grey", wraplength=200)
curcheck(kursbox1, 'OOP')
kursbox1.place(x=width//20, y=height%100)

kursbox2 = Label(root, width=45, height=25, bg="grey", wraplength=200)
curcheck(kursbox2, 'Mathematik')
kursbox2.place(x=width//3.5, y=height%100)

kursbox3 = Label(root, width=45, height=25, bg="grey", wraplength=200)
curcheck(kursbox3, 'Cybersecurity')
kursbox3.place(x=width//1.9, y=height%100)

kursbox4 = Label(root, width=45, height=25, bg="grey", wraplength=200)
curcheck(kursbox4, 'Requirements Engineering')
kursbox4.place(x=width//1.3, y=height%100)

kursbox5 = Label(root, width=45, height=25, bg="grey")
kursbox5.place(x=width//20, y=height//2)

kursbox6 = Label(root, width=45, height=25, bg="grey")
kursbox6.place(x=width//3.5, y=height//2)

kursbox7 = Label(root, width=45, height=25, bg="grey")
kursbox7.place(x=width//1.9, y=height//2)

kursbox8 = Label(root, width=45, height=25, bg="grey")
kursbox8.place(x=width//1.3, y=height//2)

button_zurueck = Button(root, text="Zurück", command=close)
button_zurueck.place(x=width/40, y=height/36.0)

root.mainloop()