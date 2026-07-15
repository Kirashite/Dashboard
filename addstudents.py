import shelve
from classes import *

print("Schreibe die ID des Studenten (z.B. student1):")


student = input()

print("Schreibe die Daten des Studenten (in Reihenfolge Vorname, Nachname, Matrikelnummer, Studiengang, Note, Durchschnitt):")

u = Student(
    input(),
    input(),
    input(),
    input(),
    input(),
)
with shelve.open('db/data.db') as db:
    db[student] = u


