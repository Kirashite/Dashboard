import shelve
from classes import *

#value: float

def addedit():
    db = shelve.open('db/kurse.db', writeback=True)
    grades_key = shelve.open('db/kurse.db', writeback=True)
    while True:
            kursname = input("Schreibe den Namen des Kurses: ")
            if kursname not in db:
                print("Schreibe die Daten des Kurses: ")
                kurs = Kurs(
                    kursname,
                    input("Info: "),
                    int(input("ECTS: ")),
                    float(input("Note: ")),
                )

            else:
                print("Kurs existiert schon!")
                break

            if 'grades' not in grades_key:
                grades_key['grades'] = []
            grades_key['grades'].append(kurs.grade)

            db[kursname] = kurs
            db.close()
            break
addedit()