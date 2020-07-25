import Homepage
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import filedialog
from PIL import Image, ImageTk
import mysql.connector
import actual.DataBaseConnect
def button(self,name):
    self.button = ttk.Button(self, text="Browse A File", command=lambda:fileDialog(self,name))
    self.button.place(x=300,y=200)

def fileDialog(self,name):

    self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
    (("jpeg files", "*.jpg",".png"), ("all files", "*.*")))
    self.label = ttk.Label(self, text="")
    self.label.place(x=320,y=220)
    self.label.configure(text=self.filename)

    img = Image.open(self.filename)
    photo = ImageTk.PhotoImage(img)

    self.label2 = Label(image=photo)
    self.label2.image = photo
    self.label2.place(x=350,y=250)

    insertBLOB(name,self.filename)

def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(name,photo):


    mydb, mycursor = actual.DataBaseConnect.database()
    try:
        cursor = mydb.cursor()
        sql_insert_blob_query = "UPDATE user SET Image = %s WHERE Username=%s"
        empPicture = convertToBinaryData(photo)
        insert_blob_tuple = (empPicture,name)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        mydb.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

def start(window,name):
    Label(window, image=window.bg_update).pack()
    button(window,name)
    back = Button(window, image=window.back_icon, command=lambda: change(window,name)).place(x=200,y=90)
    window.mainloop()

def change(window,name):
    window.destroy()
    Homepage.homepage1(name)

def callme(name):
    import WindowInitializing
    root = WindowInitializing.window()
    start(root,name)
