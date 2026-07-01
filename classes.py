from dataclasses import dataclass


@dataclass
class Kurs:
        name: str
        info: str
        ects: int
        grade: float | None = None

class Student:
    def __init__(self, vorname, nachname, matrikelnummer, studiengang, final):
        self.vorname = vorname
        self.nachname = nachname
        self.matrikelnummer = matrikelnummer
        self.studiengang = studiengang
        self.note = FinalGrade(final)

class Studiengang:
    semester = []
    def __init__(self, name, anzahl_studenten, anzahl_semester):
        self.name = name
        self.anzahl_studenten = anzahl_studenten
        self.anzahl_semester = anzahl_semester

class FinalGrade:
    def __init__(self, final_grade):
        self.final = float(final_grade)

@dataclass
class Kursauswahl:
    gebucht: bool