from tkinter import *
from pygame import mixer
import os
from mutagen.mp3 import MP3
import time
import threading
from tkinter.messagebox import *
global textMusicCurrent
global textMusicLength
global playlistBox
global statusBar
global btnMute
global imageVolume
global scaleVolume
global imageMute
global music_selected
global songListWithIds
import actual.DataBaseConnect
global songPath
mydb, mycursor = actual.DataBaseConnect.database()
playlist = []
"""
@requires: None
@functionality: This function plays the selected song
@effect: None
"""
def select_music():
    global music_selected
    global paused
    global songPath

    if paused:
        mixer.music.unpause()
        statusBar['text'] = "Playing - " + os.path.basename(songPath)
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
            songPath = url[0][0] + ".mp3"
            mixer.music.load(songPath)
            time.sleep(1)
            mixer.music.play()
            statusBar['text'] = "Playing - " + os.path.basename(url[0][0])
            show_details(songPath)
        except :
            showerror("EBMP","First Click on song")

"""
@requires: songListWithIds contain song ids and oldrating1 contains songId and their respective old ratings
@functionality: This function changes the rating of that specific song when user rates
@effect: None
"""
global index
def ratingChange(songListWithIds,oldrating1):
    global index
    music_selected = playlistBox.curselection()
    music_selected = int(music_selected[0])
    index = songListWithIds[music_selected]
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

        newRating = float(rating)

        if(length==0):
            rating_update=((total_rating*no_rating)+newRating)/(no_rating+1)
            rating_update=round(rating_update,2)

            new_no_rating=no_rating+1

        else:
            new_no_rating=no_rating
            oldrating=oldrating1[0][1]
            rating_update = ((total_rating * no_rating) + (newRating-oldrating)) / (no_rating)
            rating_update = round(rating_update, 2)

        mycursor.execute("""UPDATE Song SET TotalRating='%s' WHERE SongId=%s""", (rating_update, index[0]))
        mydb.commit()
        updated = mycursor.rowcount

        mycursor.execute("""UPDATE Song SET NoOfRating='%s' WHERE SongId=%s""", (new_no_rating, index[0]))
        mydb.commit()
        updated1 = mycursor.rowcount

        if (updated == 1 and updated1 == 1):
            showinfo("EBMP", "Updated")
    except:
        showerror("EBMP","Failed")

"""
@requires: None
@functionality: This function gets the username of that user who is currently login
@effect: Return username of user
"""
global val
def getname():
    sys.path.append(r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\EBMPgui")
    from Signin import Geek
    p = Geek()
    username = p.getVal()
    return username

"""
@requires: oldrating1 contains songId and their respective old ratings of that specific user
@functionality: This function changes the rating of song in history
@effect: none
"""
def user_ratingChange(oldrating1):
    global rating
    global index

    length = len(oldrating1)
    username = getname()
    mydb, mycursor = actual.DataBaseConnect.database()

    if(length==0):
        sql = "INSERT INTO History (UserID,SongId,Rating) VALUES (%s, %s,%s)"
        values = (username, index[0], rating)
        mycursor.execute(sql, values)
        mydb.commit()
    else:

        rating = float(rating)
        mycursor.execute("""UPDATE history SET Rating='%s' WHERE SongId=%s""", (rating, index[0]))
        mydb.commit()

"""
@requires: songListWithIds contain list of song_ids
@functionality: This function calls the two function that changes overall rating and user rating individually
@effect: None
"""
def two(songListWithIds):
    try:
        mydb, mycursor = actual.DataBaseConnect.database()
        music_selected = playlistBox.curselection()
        music_selected = int(music_selected[0])
        index = songListWithIds[music_selected]
        username=getname()

        sql = ("""SELECT SongId,Rating FROM history WHERE UserId='%s' and SongId='%s' """ % (username,index[0]))
        mycursor.execute(sql)
        oldRating= mycursor.fetchall()
        ratingChange(songListWithIds,oldRating)
        user_ratingChange(oldRating)
    except:
        showerror("EBMP","First Play the Song")


"""
@requires: value
@functionality: This function opens camera, draw rectangle around face and show mood of person around rectangle
@effect: Return mood of person
"""
global rating
def report_change(value):
    global rating
    rating=value


"""
@requires: None
@functionality: This function opens camera, draw rectangle around face and show mood of person around rectangle
@effect: Return mood of person
"""
def fill(songList,playlistBox,playlist):
    print(songList)
    k = 0

    length = len(songList)
    while k<length:
        playlistBox.insert(k, songList[k][1])
        playlist.insert(k, songList[k][1])
        k=k+1
    return playlistBox,playlist

"""
@requires: None
@functionality: This function opens camera, draw rectangle around face and show mood of person around rectangle
@effect: Return mood of person
"""
def refresh_playlist(mood):
    import MusicSelection
    import CheckSongType
    playlistBox.delete(0,'end')
    songtype1 = CheckSongType.songtype(mood)
    songtype = songtype1[0][0]
    musiclist=MusicSelection.randomsong(songtype,10)
    musiclist1=idToSongName(musiclist)
    fill(musiclist1,playlistBox,playlist)


"""
@requires: None
@functionality: This function opens camera, draw rectangle around face and show mood of person around rectangle
@effect: Return mood of person
"""
def idToSongName(songListWithIds):
    songList = []
    count=0
    for i in songListWithIds:
        sql = ("""SELECT SongUrl,SongName FROM Song WHERE SongId='%s' """ % (songListWithIds[count][0]))
        mycursor.execute(sql)
        tempList = mycursor.fetchall()
        count = count + 1
        songList.append(tempList[0])
    return songList

"""
@requires: None
@functionality: This function opens camera, draw rectangle around face and show mood of person around rectangle
@effect: Return mood of person
"""
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
    username=getname()

    if calltype=="History":
        import actual.MusicSelection

        songListWithIds=actual.MusicSelection.historysongs(None,username,10)
        songList = idToSongName(songListWithIds)

        fill(songList, playlistBox, playlist)
    else:
        import MusicSelection
        songListWithIds=MusicSelection.database(mood,username)
        songList = idToSongName(songListWithIds)
        fill(songList, playlistBox, playlist)
        Label(win, text=mood, font=("times new roman", 25, "bold")).place(x=510, y=140)


    global var
    var = DoubleVar()
    scale = Scale(win,command=lambda value, name=var: report_change(value),variable=var, orient=HORIZONTAL, sliderlength=40, width=20, length=200, from_=0, to=10)
    scale.place(x=710,y=270)
    button = Button(win, text="Rate Song",command=lambda:two(songListWithIds))
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


"""
@requires: None
@functionality: This function opens camera, draw rectangle around face and show mood of person around rectangle
@effect: Return mood of person
"""
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


"""
@requires: None
@functionality: This function opens camera, draw rectangle around face and show mood of person around rectangle
@effect: Return mood of person
"""
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


"""
@requires: None
@functionality: This function opens camera, draw rectangle around face and show mood of person around rectangle
@effect: Return mood of person
"""
def music_stop():
    try:
        global paused
        statusBar['text'] = "Stopped"
        paused = FALSE
    except:
        showerror("EBMP","Cannot stop")

paused = FALSE


"""
@requires: None
@functionality: This function opens camera, draw rectangle around face and show mood of person around rectangle
@effect: Return mood of person
"""
def music_pause():
    try:
        global paused
        paused = TRUE
        mixer.music.pause()
        statusBar['text'] = "Paused"
    except:
        showerror("EBMP","Cannot pause")

muted = FALSE


"""
@requires: None
@functionality: This function opens camera, draw rectangle around face and show mood of person around rectangle
@effect: Return mood of person
"""
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

"""
@requires: None
@functionality: This function opens camera, draw rectangle around face and show mood of person around rectangle
@effect: Return mood of person
"""
def music_volume(val):

    volume = int(val) / 100
    mixer.music.set_volume(volume)

"""
@requires: None
@functionality: This function opens camera, draw rectangle around face and show mood of person around rectangle
@effect: Return mood of person
"""
def on_exit(win):
    music_stop()
    win.destroy()

"""
@requires: None
@functionality: This function opens camera, draw rectangle around face and show mood of person around rectangle
@effect: Return mood of person
"""
def call(mood,calltype):
    main(mood,calltype)
