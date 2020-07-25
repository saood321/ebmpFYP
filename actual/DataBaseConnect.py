import mysql.connector
import pymysql

def database():
    mydb = pymysql.connect(
        host="localhost",
        user="",
        passwd="",
        database="ebmp"
    )
    mycursor = mydb.cursor()
    return mydb,mycursor