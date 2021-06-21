import mysql.connector
from mysql.connector import errorcode
from getpass import getpass

try:
    password = getpass()
    cnx = mysql.connector.connect(user='cnc', database='CnC', host = 'filatonsserver.ddns.net', password = password)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
