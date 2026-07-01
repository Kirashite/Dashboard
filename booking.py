from tkinter import *
import shelve
from classes import *

kurs_db = shelve.open('db/kurse.db')
db_gebucht = shelve.open('db/kursstatus.db')
kurs = Kursauswahl(True)

root = Tk()
root.title("Kurse buchen")
root.state('zoomed')

def close():
    root.destroy()

#Prüft, ob der Kurs gebucht ist und schaltet die Button permanent aus
def boolcheck(placeholder):
    try:
        if db_gebucht[placeholder["text"]].gebucht == 1:
            placeholder["state"] = "disabled"
    except KeyError:
        pass

#Dieser Codeabschnitt ermittelt ob eine Button aktiviert wird und dann sich nach der Aktivierung ausschaltet
def savebutton(button):
  if button["state"] == "normal":
      button["state"] = "disabled"
      db_gebucht[button["text"]] = kurs


width = root.winfo_screenwidth()
height = root.winfo_screenheight()
#root.geometry("%dx%d" % (width, height))

ico = PhotoImage(file='inter/imgs/BLANK_ICON.png')
root.iconphoto(True, ico)

kurs_button1 = Button(root, text=kurs_db['Cybersecurity'].name, width=80, height=5, command=lambda: savebutton(kurs_button1))
boolcheck(kurs_button1)
kurs_button1.place(x=width/10, y=height/7)


kurs_button2 = Button(root, text=kurs_db['OOP'].name, width=80, height=5, command=lambda: savebutton(kurs_button2))
boolcheck(kurs_button2)
kurs_button2.place(x=width/1.7, y=height/7)

kurs_button3 = Button(root, text=kurs_db['Mathematik'].name, width=80, height=5, command=lambda: savebutton(kurs_button3))
boolcheck(kurs_button3)
kurs_button3.place(x=width/10, y=height/3.5)

kurs_button4 = Button(root, text=kurs_db['Requirements Engineering'].name, width=80, height=5, command=lambda: savebutton(kurs_button4))
boolcheck(kurs_button4)
kurs_button4.place(x=width/1.7, y=height/3.5)

kurs_button5 = Button(root, text="Kurs buchen", width=80, height=5)
kurs_button5.place(x=width/10, y=height/2.3)
#boolcheck(kurs_button5)

kurs_button6 = Button(root, text="Kurs buchen", width=80, height=5)
kurs_button6.place(x=width/1.7, y=height/2.3)
#boolcheck(kurs_button6)

kurs_button7 = Button(root, text="Kurs buchen", width=80, height=5)
kurs_button7.place(x=width/10, y=height/1.7)
#boolcheck(kurs_button7)

kurs_button8 = Button(root, text="Kurs buchen", width=80, height=5)
kurs_button8.place(x=width/1.7, y=height/1.7)
#boolcheck(kurs_button8)

button_zurueck = Button(root, text="Zurück", command=close)
button_zurueck.place(x=width/40, y=height/36.0)

root.mainloop()