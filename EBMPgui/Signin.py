import Database
import Homepage
import Signup
from tkinter import*
from tkinter import messagebox
import WindowInitializing


class Geek:
    def getVal(self):
        return name

def change(root):
    root.destroy()
    Signup.Call(root)

def change_case(event=None):
    messagebox.showerror("Error", "Enter Valid Data")

global name
def login(root, username, password):
    global name
    name=username.get()
    myresult=Database.verifyUser(username,password)

    if len(myresult) >= 1:
        root.destroy()
        Homepage.homepage1(name)
    else:
        messagebox.showerror("Error","Enter Valid Data")
def name():
    return name
def Start(root):
    Label(root, image=root.bg_icon_signin).pack()
    username = StringVar()
    password = StringVar()
    txtuser = Entry(root, textvariable=username, bd=2, relief=GROOVE,width=30, font=("", 18)).place(x=225,
                                                                                           y=270)
    txtpassword = Entry(root, textvariable=password, show="*", bd=2,width=30, relief=GROOVE, font=("", 18)).place(
                                                                                                         x=225,
                                                                                                         y=370)
    btn_login = Button(root, text="Login", width=15,height=1, command=lambda: login(root,username,password),
                       font=("times new roman", 12,"bold"), bg="#BBBAAA", fg="#FAF9F3").place( x=340,
                                                                                           y=440)

    create_account = Button(root, text="Create new account",width=15, command=lambda: change(root),
    font=("times new roman", 12, "bold"), bg="#E55B8D", fg='white').place(x=740,y=520)

def call():
    root=WindowInitializing.window()
    Start(root)
    root.mainloop()