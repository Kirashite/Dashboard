from math import floor
from tkinter import *
import shelve
from classes import *

kurs_db = shelve.open('db/kurse.db')
db_gebucht = shelve.open('db/kursstatus.db')
kurs = Kursauswahl(True)

root = Tk()
root.title("Noten")
root.state('zoomed')

def close():
    root.destroy()

#Funktion, um Durchschnitt zu kalkulieren
def calsum(l):
    try:
    # returning sum of list using List comprehension
        result = sum([int(i) for i in l if type(i)== int or float])/len(l)
        recalc = floor(result*(-5)/10+60)/10
        u = FinalGrade(recalc)
        durchschnitt_db = shelve.open('db/final.db')
        durchschnitt_db['final'] = u.final
        return durchschnitt_db['final']
    except KeyError:
        pass

#Prüft, ob der Name in boxvar gleich mit kursvar
def curcheck(boxvar, kurvar):
    try:
        if db_gebucht[kurvar].gebucht == 1:
            boxvar["text"] = kurs_db[kurvar].name
    except KeyError:
        pass
#Macht das gleiche, was curcheck macht
def gradecheck(boxvar, kurvar):
    try:
        if db_gebucht[kurvar].gebucht == 1:
            boxvar["text"] = kurs_db[kurvar].note.grade
    except KeyError:
        pass
    
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

ico = PhotoImage(file='inter/imgs/BLANK_ICON.png')
root.iconphoto(True, ico)

kursbox1 = Label(root, width=100, height=5, bg="grey")
curcheck(kursbox1, 'OOP')
kursbox1.place(x=width//20, y=height/13.170731707317072)

kursbox2 = Label(root, width=100, height=5, bg="grey")
curcheck(kursbox2, 'Mathematik')
kursbox2.place(x=width//20, y=height/4.462809917355372)

kursbox3 = Label(root, width=100, height=5, bg="grey")
curcheck(kursbox3, 'Cybersecurity')
kursbox3.place(x=width//20, y=height/2.6865671641791047)

kursbox4 = Label(root, width=100, height=5, bg="grey")
curcheck(kursbox4, 'Requirements Engineering')
kursbox4.place(x=width//20, y=height/1.9217081850533808)

kursbox5 = Label(root, width=100, height=5, bg="grey")
kursbox5.place(x=width//20, y=height/1.4958448753462603)

kursbox6 = Label(root, width=100, height=5, bg="grey")
kursbox6.place(x=width//1.9591836734693877, y=height/13.170731707317072)

kursbox7 = Label(root, width=100, height=5, bg="grey")
kursbox7.place(x=width//1.9591836734693877, y=height/4.462809917355372)

kursbox8 = Label(root, width=100, height=5, bg="grey")
kursbox8.place(x=width//1.9591836734693877, y=height/2.6865671641791047)

kursbox9 = Label(root, width=100, height=5, bg="grey")
kursbox9.place(x=width//1.9591836734693877, y=height/1.9217081850533808)

kursbox10 = Label(root, width=100, height=5, bg="grey")
kursbox10.place(x=width//1.9591836734693877, y=height/1.4958448753462603)

notenbox1 = Label(root, width=10, height=5, bg="grey")
gradecheck(notenbox1, 'OOP')
notenbox1.place(x=width//2.33, y=height/13.170731707317072)

notenbox2 = Label(root, width=10, height=5, bg="grey")
gradecheck(notenbox2, 'Mathematik')
notenbox2.place(x=width//2.33, y=height/4.462809917355372)

notenbox3 = Label(root, width=10, height=5, bg="grey")
gradecheck(notenbox3, 'Einführung in Cybersecurity')
notenbox3.place(x=width//2.33, y=height/2.6865671641791047)

notenbox4 = Label(root, width=10, height=5, bg="grey")
gradecheck(notenbox4, 'Requirements Engineering')
notenbox4.place(x=width//2.33, y=height/1.9217081850533808)

notenbox5 = Label(root, width=10, height=5, bg="grey")
notenbox5.place(x=width//2.33, y=height/1.4958448753462603)

notenbox6 = Label(root, width=10, height=5, bg="grey")
notenbox6.place(x=width//1.1225086367260166, y=height/13.170731707317072)

notenbox7 = Label(root, width=10, height=5, bg="grey")
notenbox7.place(x=width//1.1225086367260166, y=height/4.462809917355372)

notenbox8 = Label(root, width=10, height=5, bg="grey")
notenbox8.place(x=width//1.1225086367260166, y=height/2.6865671641791047)

notenbox9 = Label(root, width=10, height=5, bg="grey")
notenbox9.place(x=width//1.1225086367260166, y=height/1.9217081850533808)

notenbox10 = Label(root, width=10, height=5, bg="grey")
notenbox10.place(x=width//1.1225086367260166, y=height/1.4958448753462603)


durchschnittnote = Label(root, text=str(calsum(kurs_db['grades'])), width=10, height=5, bg="grey")
durchschnittnote.place(x=width/2.1215469613259668, y=height/1.2796208530805686)

button_zurueck = Button(root, text="Zurück", command=close)
button_zurueck.place(x=width/40, y=height/36.0)

root.mainloop()