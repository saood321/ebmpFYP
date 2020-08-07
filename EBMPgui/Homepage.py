from tkinter import *
import Signin
import Upgrade
import WindowInitializing
import mysql
import mysql.connector
import sys


def logout(win):
    win.destroy()
    Signin.call()




def history():

    import actual.MusicPlayer
    actual.MusicPlayer.call("Happy","History")


def write_file(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)


def readBLOB(name):
    from PIL import Image
    import io
    from PIL import Image, ImageTk
    import actual.DataBaseConnect
    try:
        connection,cursor = actual.DataBaseConnect.database()
        sql_fetch_blob_query = """SELECT Image from user where Username = %s"""
        cursor.execute(sql_fetch_blob_query, (name,))
        record = cursor.fetchall()
        if record[0][0] !=None:

            for row in record:
                image = row[0]

            file_like2 = io.BytesIO(image)
            img1 = Image.open(file_like2)
            img1 = img1.resize((200, 200), Image.ANTIALIAS)
            Image = ImageTk.PhotoImage(img1)
            return Image
        else:
            print("Failed")

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

def getEmail(name):
    import actual.DataBaseConnect
    mydb, mycursor = actual.DataBaseConnect.database()
    sql = ("""SELECT Email FROM user WHERE Username='%s'""" % name)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult[0][0]

def homepage1(name):
    root = WindowInitializing.window()
    Label(root, image=root.bg_icon_main).pack()
    Image=readBLOB(name)
    if Image!=None:
        ImageLabel = Label(root, image=Image, width=200, height=170)
        ImageLabel.image = Image
        ImageLabel.place(x=200, y=90)
    title = Label(root, text=name,width=22, font=("times new roman", 12), bg="#C1B1B6", fg="white")
    title.place(x=202, y=260)
    email=getEmail(name)
    title = Label(root, text=email, width=22, font=("times new roman", 12), bg="#C1B1B6", fg="white")
    title.place(x=202, y=280)

    btn_history = Button(root,command=history,image=root.history_icon).place(x=200,y=542)
    btn_logout = Button(root,image=root.logout_icon ,
                        command=lambda: logout(root)).place(x=885,y=542)
    btn_camera = Button(root, text="camera",image=root.playmain_icon, command=camera).place(x=510,y=360)
    btn_upgradeProfile = Button(root, image=root.setting_icon, command=lambda: upgradedata(root, name)).place(x=885,y=90)

    root.mainloop()

def upgradedata(win,name):
    win.destroy()
    Upgrade.callme(name)

def camera():
    with add_path(r'C:\Users\M.Saood Sarwar\PycharmProjects\ebmpFYP\actual'):
        mod = __import__('mainstart')
    del sys.modules['mainstart']

class add_path():
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        sys.path.insert(0, self.path)

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            sys.path.remove(self.path)
        except ValueError:
            pass
