from tkinter import*
from PIL import ImageTk

def window():
    root = Tk()
    root.title("EBMP")
    root.geometry("1156x650+0+0")
    root.resizable(width=False, height=False)
    root.bg_icon_signin = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\loginimg.png")
    root.bg_icon_signup = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\signimg.png")
    root.bg_icon_main = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\main3.png")
    root.user_icon = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\img2.png")
    root.password_icon = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\img3.png")
    #root.login_icon = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\login.png")
    #root.email_icon = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\email.jpg")
    #root.camera = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\camera.png")
    root.history_icon = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\history.png")
    root.logout_icon = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\logout.png")
    root.playmain_icon = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\playmain.png")
    root.setting_icon = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\setting.png")
    root.bg_music = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\music.png")
    root.bg_music = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\music.png")
    root.bg_update = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\updatescreen.png")
    root.back_icon = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\back.png")
    #bg_lbl =Label(root,image=root.bg_icon_signin).pack()

    return root