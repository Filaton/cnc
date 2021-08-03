from typing import List
from PyQt6 import QtCore, QtGui
from PyQt6 import uic, QtSql
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QListWidget, QMenu, QSizePolicy, QTableWidgetItem, QTableWidget, QApplication, QMainWindow, QWidget
from PyQt6.QtCore import QEvent, Qt
import sys
from PyQt6.uic.load_ui import loadUi
from PyQt6.uic.uiparser import QtWidgets

import mysql.connector
from mysql.connector import errorcode
from getpass import getpass

class SQLDatabase:
    """Hersetllen der Verbindung zur Datenbank
    """
    def __init__(self) -> None:
        try:
            self.cnx = mysql.connector.connect(user='cnc', database='CnC', host = 'filatonsserver.ddns.net', password = getpass(), port = 51001)
            if self.cnx.is_connected():
                print('Connection established')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def disconnect(self):
        """Verbindung trennen
        """
        self.cnx.close()

myDB = SQLDatabase()

class Cocktail:
    """Cocktail Objekt
    """
    def __init__(self, name: str, zutaten: List[int], mengen: List[str]) -> None:
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
        self.mengen = mengen
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

        for i in range(len(self.zutaten)):
            zutatendata = (newid, self.zutaten[i], self.mengen[i])
            cursor.execute(add_cocktailzutaten, zutatendata)

        cursor.execute(add_cocktailname, cocktaildata)
        myDB.cnx.commit()
        cursor.close()


class AddCocktail(QWidget):
    """Qt Klasse zum Hinzufuegen eines Cocktails
    """
    def __init__(self, parent):
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

        mengen = [self.menge1.cleanText(),
                  self.menge2.cleanText(),
                  self.menge3.cleanText(),
                  self.menge4.cleanText(),
                  self.menge5.cleanText(),
                  self.menge6.cleanText()]

        temp = Cocktail(self.cocktailnameedit.text(), zutaten, mengen)
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

class CocktailInfo(QWidget):
    def __init__(self, parent, ID):
        super().__init__()
        uic.loadUi('cocktailInfo.ui', self)
        
        self.zutatenlist = []
        pixmap = QtGui.QPixmap('Pics/noAlk.png')
        self.cocktailPic.setPixmap(pixmap)

        self.pullCocktailInfo(ID)

    def pullCocktailInfo(self, ID):
        cursor = myDB.cnx.cursor()

        data = (ID,)
        get_zutaten = ("SELECT Zutat, Menge FROM Cocktail_mit_zutaten WHERE Cocktails = (SELECT Name FROM cocktails WHERE ID = (%s));")
        cursor.execute(get_zutaten, data)
        zutatenpull = cursor.fetchall()
        
        self.zutatenTable.setRowCount(len(zutatenpull))

        count = 0
        for i in zutatenpull:
            zutatenitem = QTableWidgetItem(i[0])
            # zutatenitem.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            mengenitem = QTableWidgetItem(str(i[1]) + "cl")
            # mengenitem.setTextAlignment(Qt.AlignmentFlag.AlignRight)
            self.zutatenTable.setItem(count, 0, zutatenitem)
            self.zutatenTable.setItem(count, 1, mengenitem)
            count = count + 1
        
        self.zutatenTable.resizeColumnsToContents()

class Ui(QMainWindow):
    """Hauptteil der Anwendung
    """
    def __init__(self):
        """Laden des UI Files und Trigger Zuweisung
        """
        super().__init__() # Call the inherited classes __init__ method
        uic.loadUi('mainwindow.ui', self) # Load the .ui file

        self.setWindowTitle("CnConnect")

        self.actionCocktail_hinzufuegen.triggered.connect(self.cocktailAdd)
        self.RefreshButton.clicked.connect(self.refreshList)
        
        self.loadCocktails()

        # self.infococktailwindow

        self.cocktailList.installEventFilter(self)
        self.cocktailList.itemDoubleClicked.connect(self.cocktailInfo)

        self.show() # Show the GUI

    def eventFilter(self, source, event) -> bool:
        if (event.type() == QtGui.QContextMenuEvent.Type.ContextMenu and
            source is self.cocktailList):
            menu = QMenu(self.cocktailList)
            menu.addAction('Cocktail löschen')
            if menu.exec(event.globalPos()):
                self.cocktailDelete(self.cocktailList.currentRow())
                # item = source.itemAt(event.pos())
                # dialog = DelDialog(self)
                # if dialog.exec() == QDialog.accepted:
                #     print('Accepted')
                # else:
                #     print('Cancelled')
                # dialog.deleteLater()
            return True
        return super().eventFilter(source, event)

    def cocktailAdd(self):
        """Aufrufen des zweiten Fensters
        """
        self.cocktailwindow = AddCocktail(self)
        self.cocktailwindow.show()

    def cocktailDelete(self, ID):
        cursor = myDB.cnx.cursor()
        data = (ID,)
        del_cocktail = ("DELETE FROM cocktails WHERE (ID = (%s));")
        del_zutatvon = ("DELETE FROM zutat_von WHERE (CocktailID = (%s));")
        cursor.execute(del_cocktail, data)
        cursor.execute(del_zutatvon, data)
        myDB.cnx.commit()
        cursor.close()
        self.cocktailList.takeItem(ID)

    def loadCocktails(self):
        """Laden der bereits vorhandenen Cocktails
        """
        cursor = myDB.cnx.cursor()
        get_cocktailnames = ("SELECT Name FROM cocktails;")
        cursor.execute(get_cocktailnames)
        for (Name, ) in cursor:
            self.cocktailList.addItem(Name)
        cursor.close()

    def refreshList(self):
        self.cocktailList.clear()
        self.loadCocktails()

    def cocktailInfo(self):
        cocid = self.cocktailList.currentRow()
        self.infococktailwindow = CocktailInfo(self, cocid)
        self.infococktailwindow.show()

# class DelDialog(QDialog):
#     def __init__(self, callwindow: Ui):
#         super().__init__()
#         uic.loadUi('deleteDialog.ui', self)

#         self.buttonBox.accepted.connect(self.cdelete)
#         self.buttonBox.rejected.connect(self.cabort)

#     def cdelete(self):
#         self.close()

#     def cabort(self):
#         self.close()


app = QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec() # Start the application
myDB.disconnect()
