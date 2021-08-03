# CNConnect

Desktop Applikation, die das Einfügen und später auch das Löschen und Bearbeiten von Cocktails in die MySQL Datenbank ermöglichen soll.

## Framework

Verwendung des Qt Frameworks, wegen Portabilität und Einfachheit.

## Setup

Um die App selbst zum Laufen zu bringen wird lediglich Python, mySQL Connector und PyQt6 benötigt.

`pip install pyqt6`

`pip install mysql-connector-python`

Zusätzlich ist natürlich noch ein Zugang zur Datenbank erforderlich.

## Details

Die App besteht aus einem MainWindow, in dem eine Liste der bereits erstellten Cocktails zu sehen ist (später weitere Details wie Zutaten) und aus einem Dialogfenster, das über eine Toolleiste aufgerufen werden kann.
In diesem können neue Cocktails hinzugefügt werden (mithilfe von Zutaten in Dropdown Menüs).

## Zeitaufteilung

1. Einarbeiten in Qt Framework - 15h
2. Erstellen der ersten UI (rein in Python) - 10h
3. Verwendung des Qt Designers für neuere UI - 15h
4. Erstellen des Codes für die Oberfläche - 15h
5. Zusammenführen von UI Designs und Code + Probieren verschiedener Packages - 20h
6. Anbindung an Datenbank - 15h
7. Programmierung weiterer DesktopApp Features - 40h
8. Erstellen eines Docker Apache Servers - 10h
9. Serverwartung - 15h
10. Githubverwaltung und Toolchain - 10h

Gesamt: 165h
