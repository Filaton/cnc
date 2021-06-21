from PyQt6 import QtCore
from PyQt6 import uic, QtSql
from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget, QApplication, QMainWindow, QWidget
from PyQt6.QtCore import Qt
import sys

import mysql.connector
from mysql.connector import errorcode
from getpass import getpass

class SQLDatabase:
    def __init__(self) -> None:
        self.cnx = mysql.connector.connect(user='cnc', database='CnC', host = 'filatonsserver.ddns.net', password = getpass())
        if self.cnx.is_connected():
            print('Connection established')

    def disconnect(self):
        self.cnx.close()

myDB = SQLDatabase()

class Cocktail:
    def __init__(self, name: str, zutaten) -> None:
        self.name = name
        self.zutaten = []
        for i in zutaten:
            if (i != 0):
                self.zutaten.append(i)
        
    def addToDB(self):
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
    def __init__(self):
        super().__init__()
        uic.loadUi('addcocktail.ui', self)
        self.SaveButton.clicked.connect(self.saveCocktail)
        self.AbortButton.clicked.connect(self.abort)
        self.getZutaten()

    def saveCocktail(self):
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
        return box.currentIndex()
    
    def abort(self):
        self.close()

class Ui(QMainWindow):
    def __init__(self):
        super().__init__() # Call the inherited classes __init__ method
        uic.loadUi('mainwindow.ui', self) # Load the .ui file

        newItem = QTableWidgetItem("Hallo")
        self.tableWidget.setItem(1, 1, newItem)
        self.actionCocktail_hinzufuegen.triggered.connect(self.cocktailAdd)

        self.cocktailwindow = AddCocktail()

        self.show() # Show the GUI

    def cocktailAdd(self):
        self.cocktailwindow.show()


app = QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec() # Start the application
myDB.disconnect()
