from typing import List
from PyQt6 import QtCore
from PyQt6 import uic, QtSql
from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget, QApplication, QMainWindow, QWidget
from PyQt6.QtCore import Qt
import sys

import mysql.connector
from mysql.connector import errorcode
from getpass import getpass

class SQLDatabase:
    """Hersetllen der Verbindung zur Datenbank
    """
    def __init__(self) -> None:
        self.cnx = mysql.connector.connect(user='cnc', database='CnC', host = 'filatonsserver.ddns.net', password = getpass())
        if self.cnx.is_connected():
            print('Connection established')

    def disconnect(self):
        """Verbindung trennen
        """
        self.cnx.close()

myDB = SQLDatabase()

class Cocktail:
    """Cocktail Objekt
    """
    def __init__(self, name: str, zutaten: List[int]) -> None:
        """Weist Daten zu

        Parameters
        ----------
        name : str
            Name des Cocktails
        zutaten : [int]
            Array mit Zutaten-IDs der Cocktails
        """
        self.name = name
        self.zutaten = []
        for i in zutaten:
            if (i != 0):
                self.zutaten.append(i)
        
    def addToDB(self):
        """Hinzufuegen eines Cocktails zur Datenbank
        """
        cursor = myDB.cnx.cursor()

        get_cocktail_count = ("SELECT count(ID) from cocktails;")
        cursor.execute(get_cocktail_count)
        newid = (cursor.fetchone())[0]
        add_cocktailname = ("INSERT INTO cocktails (`ID`, `Name`) VALUES (%s, %s);")

        add_cocktailzutaten = ("INSERT INTO zutat_von (CocktailID, ZutatID, Menge) VALUES (%s, %s, %s);")
        
        cocktaildata = (newid, self.name)

        for i in self.zutaten:
            zutatendata = (newid, i, 0)
            cursor.execute(add_cocktailzutaten, zutatendata)

        cursor.execute(add_cocktailname, cocktaildata)
        myDB.cnx.commit()
        cursor.close()


class AddCocktail(QWidget):
    """Qt Klasse zum Hinzufuegen eines Cocktails
    """
    def __init__(self):
        """Init der Buttons und erste Datenbankabfragen
        """
        super().__init__()
        uic.loadUi('addcocktail.ui', self)
        self.SaveButton.clicked.connect(self.saveCocktail)
        self.AbortButton.clicked.connect(self.abort)
        self.getZutaten()

    def saveCocktail(self):
        """Speichern des Cocktails in der Datenbank
        """
        zutaten = [self.getChosenZutaten(self.zutatenbox1),
                   self.getChosenZutaten(self.zutatenbox2),
                   self.getChosenZutaten(self.zutatenbox3),
                   self.getChosenZutaten(self.zutatenbox4),
                   self.getChosenZutaten(self.zutatenbox5),
                   self.getChosenZutaten(self.zutatenbox6)]

        temp = Cocktail(self.cocktailnameedit.text(), zutaten)
        temp.addToDB()
        self.close()
    
    def getZutaten(self):
        """Befuellen der Zutatenmenus
        """
        cursor = myDB.cnx.cursor()
        getZutatenList = ("SELECT ID, Name FROM zutaten;")
        cursor.execute(getZutatenList)
        self.zutatenbox1.addItem('Leer')
        self.zutatenbox2.addItem('Leer')
        self.zutatenbox3.addItem('Leer')
        self.zutatenbox4.addItem('Leer')
        self.zutatenbox5.addItem('Leer')
        self.zutatenbox6.addItem('Leer')
        for (ID, Name) in cursor:
            self.zutatenbox1.addItem(Name)
            self.zutatenbox2.addItem(Name)
            self.zutatenbox3.addItem(Name)
            self.zutatenbox4.addItem(Name)
            self.zutatenbox5.addItem(Name)
            self.zutatenbox6.addItem(Name)
        cursor.close()

    def getChosenZutaten(self, box):
        """Aktuelle Zutat zurueckgeben

        Parameters
        ----------
        box : [type]
            Gesuchte Box

        Returns
        -------
        [type]
            Index der Auswahl im Dropdown Menu
        """
        return box.currentIndex()
    
    def abort(self):
        """Abbrechen der Erstellung
        """
        self.close()

class Ui(QMainWindow):
    """Hauptteil der Anwendung
    """
    def __init__(self):
        """Laden des UI Files und Trigger Zuweisung
        """
        super().__init__() # Call the inherited classes __init__ method
        uic.loadUi('mainwindow.ui', self) # Load the .ui file

        self.actionCocktail_hinzufuegen.triggered.connect(self.cocktailAdd)
        
        self.loadCocktails()

        self.cocktailwindow = AddCocktail()

        self.show() # Show the GUI

    def cocktailAdd(self):
        """Aufrufen des zweiten Fensters
        """
        self.cocktailwindow.show()

    def loadCocktails(self):
        """Laden der bereits vorhandenen Cocktails
        """
        cursor = myDB.cnx.cursor()
        get_cocktailnames = ("SELECT Name FROM cocktails")
        cursor.execute(get_cocktailnames)
        for (Name, ) in cursor:
            self.cocktailList.addItem(Name)


app = QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec() # Start the application
myDB.disconnect()
