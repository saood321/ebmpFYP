from tkinter import *
from pygame import mixer
import os
from mutagen.mp3 import MP3
import time
import threading
from tkinter.messagebox import *
global textMusicCurrent
global textMusicLength
playlist = []
global playlistBox
global statusBar
global btnMute
global imageVolume
global scaleVolume
global imageMute
global path
global music_selected
global myresult
import actual.DataBaseConnect
mydb, mycursor = actual.DataBaseConnect.database()
global path2

def select_music():
    global music_selected
    global path
    global paused
    global path2

    if paused:
        mixer.music.unpause()
        statusBar['text'] = "Playing - " + os.path.basename(path2)
        paused = FALSE
    else:
        try:
            music_selected = playlistBox.curselection()
            music_selected = int(music_selected[0])
            music_play_path = playlist[music_selected]
            mydb, mycursor = actual.DataBaseConnect.database()
            sql = ("""SELECT SongUrl FROM song WHERE SongName='%s' """ % (music_play_path))
            mycursor.execute(sql)
            url = mycursor.fetchall()
            path2 = url[0][0] + ".mp3"
            mixer.music.load(path2)
            time.sleep(1)
            mixer.music.play()
            statusBar['text'] = "Playing - " + os.path.basename(url[0][0])
            show_details(path2)
        except :
            showerror("EBMP","First Click on song")


global index
def ratingChange(myresult,oldrating1):
    global index
    music_selected = playlistBox.curselection()
    music_selected = int(music_selected[0])
    index = myresult[music_selected]
    try:
        length = len(oldrating1)

        mydb, mycursor = actual.DataBaseConnect.database()

        sql = ("""SELECT NoOfRating FROM Song WHERE SongId='%s' """ % (index[0]))
        mycursor.execute(sql)
        no_rating = mycursor.fetchall()
        no_rating = no_rating[0][0]

        sql = ("""SELECT TotalRating FROM Song WHERE SongId='%s' """ % (index[0]))
        mycursor.execute(sql)
        total_rating = mycursor.fetchall()
        total_rating = total_rating[0][0]

        val = float(value1)

        if(length==0):
            rating_update=((total_rating*no_rating)+val)/(no_rating+1)
            rating_update=round(rating_update,2)

            new_no_rating=no_rating+1

        else:
            new_no_rating=no_rating
            oldrating=oldrating1[0][1]
            rating_update = ((total_rating * no_rating) + (val-oldrating)) / (no_rating)
            rating_update = round(rating_update, 2)

        mycursor.execute("""UPDATE Song SET TotalRating='%s' WHERE SongId=%s""", (rating_update, index[0]))
        mydb.commit()
        updated = mycursor.rowcount

        mycursor.execute("""UPDATE Song SET NoOfRating='%s' WHERE SongId=%s""", (new_no_rating, index[0]))
        mydb.commit()
        updated1 = mycursor.rowcount

        if (updated == 1 and updated1 == 1):
            showinfo("EBMP", "updated")
    except:
        showerror("EBMP","Failed")

global val
def getname():
    sys.path.append(r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\EBMPgui")
    from Signin import Geek
    p = Geek()
    val = p.getVal()
    return val

def user_ratingChange(myresult,oldrating1):
    global val
    global index

    length = len(oldrating1)
    val = getname()
    mydb, mycursor = actual.DataBaseConnect.database()

    if(length==0):
        sql = "INSERT INTO History (UserID,SongId,Rating) VALUES (%s, %s,%s)"
        val1 = (val, index[0], value1)
        mycursor.execute(sql, val1)
        mydb.commit()
    else:

        val = float(value1)
        mycursor.execute("""UPDATE history SET Rating='%s' WHERE SongId=%s""", (val, index[0]))
        mydb.commit()

def two(myresult):
    try:
        mydb, mycursor = actual.DataBaseConnect.database()
        music_selected = playlistBox.curselection()
        music_selected = int(music_selected[0])
        index = myresult[music_selected]
        val=getname()

        sql = ("""SELECT SongId,Rating FROM history WHERE UserId='%s' and SongId='%s' """ % (val,index[0]))
        mycursor.execute(sql)
        url = mycursor.fetchall()
        ratingChange(myresult,url)
        user_ratingChange(myresult,url)
    except:
        showerror("EBMP","First Play the Song")


global value1
def report_change(name,value):
    global value1
    value1=value


def fill(myresult2,playlistBox,playlist):
    print(myresult2)
    k = 0

    length = len(myresult2)
    while k<length:
        playlistBox.insert(k, myresult2[k][1])
        playlist.insert(k, myresult2[k][1])
        k=k+1
    return playlistBox,playlist

def refresh_playlist(mood):
    import MusicSelection
    import CheckSongType
    playlistBox.delete(0,'end')
    songtype1 = CheckSongType.songtype(mood)
    songtype = songtype1[0][0]
    musiclist=MusicSelection.randomsong(songtype,10)
    musiclist1=idToSongName(musiclist)
    fill(musiclist1,playlistBox,playlist)

def idToSongName(myresult):
    myresult2 = []
    count=0
    for i in myresult:
        sql = ("""SELECT SongUrl,SongName FROM Song WHERE SongId='%s' """ % (myresult[count][0]))
        mycursor.execute(sql)
        myresult1 = mycursor.fetchall()
        count = count + 1
        myresult2.append(myresult1[0])
    return myresult2

def main(mood,calltype):
    from PIL import ImageTk
    win=Toplevel()
    win.bg_music = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\music.png")

    label=Label(win, image=win.bg_music)
    label.image = win.bg_music
    label.pack()
    global playlistBox
    playlistBox = Listbox(win, relief=RAISED, width=38, height=12)
    playlistBox.place(x=200, y=190)
    val=getname()

    if calltype=="History":
        import actual.MusicSelection

        myresult=actual.MusicSelection.historysongs(None,val,10)
        myresult2 = idToSongName(myresult)

        fill(myresult2, playlistBox, playlist)
    else:
        import MusicSelection
        myresult=MusicSelection.database(mood,val)
        myresult2 = idToSongName(myresult)
        fill(myresult2, playlistBox, playlist)
        Label(win, text=mood, font=("times new roman", 25, "bold")).place(x=510, y=140)


    global var
    var = DoubleVar()
    scale = Scale(win,command=lambda value, name=var: report_change(name, value),variable=var, orient=HORIZONTAL, sliderlength=40, width=20, length=200, from_=0, to=10)
    scale.place(x=710,y=270)
    button = Button(win, text="Rate Song",command=lambda:two(myresult))
    button.place(x=760,y=330)


    if calltype !="History":
        win.refresh_icon = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\refresh.png")
        button = Button(win, image=win.refresh_icon,command=lambda: refresh_playlist(mood))
        button.place(x=220, y=400)

    textWelcome = Label(win, text="Welcome to EBMP")
    textWelcome.place(x=470,y=200)

    global textMusicLength
    textMusicLength = Label(win, text="Total Length: --:--")
    textMusicLength.place(x=470,y=250)

    global textMusicCurrent
    textMusicCurrent = Label(win, text="Current Time: --:--", relief=GROOVE)
    textMusicCurrent.place(x=470,y=300)

    global statusBar
    statusBar = Label(win, text="Status", relief=SUNKEN, anchor=W)
    statusBar.place(x=470,y=330)




    win.playcircle_icon = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\playcircle.png")

    win.stop_icon = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\stop.png")
    btnStop = Button(win, image=win.stop_icon, command=music_stop)
    btnStop.place(x=630, y=400)

    win.pause_icon = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\pause.png")
    btnPause = Button(win, image=win.pause_icon, command=music_pause)
    btnPause.place(x=460,y=400)



    win.rewind_icon = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\rewind.png")
    btnRewind = Button(win, image=win.rewind_icon, command=select_music)
    btnRewind.place(x=500, y=470)



    select_button = Button(win,image=win.playcircle_icon, command= select_music)
    select_button.place(x=545, y=400)

    global btnMute
    win.mute_icon = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\volumeoff.png")
    win.volume_icon = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\volumeup.png")
    btnMute = Button(win, image=win.volume_icon, command=music_mute)
    btnMute.place(x=590, y=470)
    mixer.init()
    scaleVolume = Scale(win, from_=0, to=100, orient=HORIZONTAL, command=music_volume)
    scaleVolume.set(80)
    scaleVolume.place(x=650, y=470)

    win.protocol("WM_DELETE_WINDOW",lambda: on_exit(win))
    win.mainloop()


def start_counter(length):
    global paused
    count = 0

    while count <= length and mixer.music.get_busy():
        if paused:
            continue
        else:
            mins, secs = divmod(count, 60)
            mins = round(mins)
            secs = round(secs)

            formatCounter = '{:02d}:{:02d}'.format(mins, secs)
            textMusicCurrent['text'] = "Current Time - " + formatCounter

            time.sleep(1)
            count += 1


def show_details(filepath):
    splitFileName = os.path.splitext(filepath)

    if splitFileName[1] == '.mp3':
        totalLength = MP3(filepath).info.length
    elif splitFileName[1] == '.MP3':
        totalLength = MP3(filepath).info.length
    else:
        totalLength = mixer.Sound(filepath).get_length()

    mins, secs = divmod(totalLength, 60)
    mins = round(mins)
    secs = round(secs)

    formatLength = '{:02d}:{:02d}'.format(mins, secs)
    textMusicLength['text'] = "Total Length - " + formatLength

    threadCounter = threading.Thread(target=start_counter, args=(totalLength,))
    threadCounter.start()


def music_stop():
    try:
        global paused
        statusBar['text'] = "Stopped"
        paused = FALSE
    except:
        showerror("EBMP","Cannot stop")

paused = FALSE


def music_pause():
    try:
        global paused
        paused = TRUE
        mixer.music.pause()
        statusBar['text'] = "Paused"
    except:
        showerror("EBMP","Cannot pause")

muted = FALSE


def music_mute():
    global muted
    global btnMute
    try:
        if muted:
            mixer.music.set_volume(0.8)
            btnMute.configure(image=imageVolume)
            scaleVolume.set(80)
            muted = FALSE
        else:
            mixer.music.set_volume(0)
            btnMute.configure(image=imageMute)
            scaleVolume.set(0)
            muted = TRUE
    except:
        showerror("EBMP","Cannot Mute")

def music_volume(val):

    volume = int(val) / 100
    mixer.music.set_volume(volume)


def on_exit(win):
    music_stop()
    win.destroy()

def call(mood,calltype):
    main(mood,calltype)
