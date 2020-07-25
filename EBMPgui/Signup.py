import Database
import Homepage
import Signin
from tkinter import*
from tkinter import messagebox
import WindowInitializing

def start(root):
    Label(root, image=root.bg_icon_signup).pack()
    username = StringVar()
    password = StringVar()
    email = StringVar()
    txtuser = Entry(root, textvariable=username, bd=5,width=35, relief=GROOVE, font=("", 15)).place(x=225,y=265)
    txtemail = Entry(root, bd=5, textvariable=email,width=35, relief=GROOVE, font=("", 15)).place(x=225,y=365)
    txtpassword = Entry(root, show="*", bd=5, textvariable=password,width=35, relief=GROOVE, font=("", 15)).place(x=225,y=465)
    btn_login = Button(root, text="Signup", width=15, command=lambda: login(root, username, password, email),
                       font=("times new roman", 12, "bold"), bg="#BBBAAA", fg="#FAF9F3").place(x=320,y=520)
    create_account = Button(root, text="Already have an account?", width=20, command=lambda: change(root),
                            font=("times new roman", 12, "bold"), bg="#E55B8D", fg='white').place(x=720,y=520)

def change(root):
    root.destroy()
    Signin.call()

def login(root, username, password,email):
    name=username.get()

    if password == "" or username == "" or email == "":
        messagebox.showerror("Error","Enter Valid Data")
    else:
        var=Database.insertuser(username,email,password)
        if var == 1:
            root.destroy()
            Signin.call()
        else:
            messagebox.showerror("Error", var)

def Call(root):
    root = WindowInitializing.window()
    start(root)
    root.mainloop()