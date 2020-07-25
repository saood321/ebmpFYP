import mysql.connector
import mysql
import Rules

def database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="",
        passwd="",
        database="ebmp"
    )
    return mydb

def databaseConnectivity():
    return database()

def verifyUser(username,password):
    name = username.get()
    password = password.get()

    mydb = database()
    mycursor = mydb.cursor()
    sql = ("""SELECT * FROM user WHERE Username='%s' and Password ='%s'""" % (name, password))
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

def insertuser(username,email,password):
    name = username.get()
    password = password.get()
    email = email.get()

    mydb = database()
    mycursor = mydb.cursor()
    sql = ("""SELECT * FROM user WHERE Username='%s'""" % name)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    verifierResult = Rules.verifier(email, password)

    if verifierResult != 0 or len(myresult) >= 1:
        if verifierResult != 0 and len(myresult) >= 1:
            return verifierResult + " and Username is already taken"
        elif verifierResult == 0 and len(myresult) >= 1:
            return "Username is already taken"
        elif verifierResult != 0 and not len(myresult) >= 1:
            return verifierResult
    else:
        sql = "INSERT INTO user (Username, Password,Email) VALUES (%s, %s,%s)"
        val = (name, password, email)
        mycursor.execute(sql, val)
        mydb.commit()
        var = mycursor.rowcount
        return 1


def upgradePassword(name,newPassword,oldPassword):
    np=newPassword.get()
    op=oldPassword.get()

    mydb = database()
    mycursor = mydb.cursor()
    sql = "UPDATE user SET Password = %s WHERE Password= %s AND Username=%s"
    val = (np, op, name)
    mycursor.execute(sql, val)
    mydb.commit()
    var = mycursor.rowcount
    if var >= 1:
        return 1
    else:
        return 0
