import actual.DataBaseConnect
mydb,mycursor=actual.DataBaseConnect.database()

"""
@requires: songType means happy,sad etc username of user and limit represents how many songs we want to fetch
@functionality: This function select 3 top rated songs from user history
@effect: returns limit of history song
"""
def historysongs(songtype,username,limit):
    if songtype==None:
        sql = ("""SELECT history.SongId FROM history INNER JOIN song ON history.SongId = song.SongId WHERE  history.UserId='%s' ORDER BY Rating DESC LIMIT %s""" % (username, limit))
    else:
        sql = ( """SELECT history.SongId FROM history INNER JOIN song ON history.SongId = song.SongId WHERE song.SongTypeId='%s' and history.UserId='%s' ORDER BY Rating DESC LIMIT %s""" % (songtype,username,limit))
    mycursor.execute(sql)
    history = mycursor.fetchall()
    print(history)
    return history

"""
@requires: songtype represents mood happy,sad etc
@functionality: This function selects 3 top overall highly rated song 
@effect: List of songs
"""
def ratedsong(songtype):
    sql = ("""SELECT SongId FROM song  WHERE SongTypeId='%s' ORDER BY TotalRating DESC LIMIT 3 """ % (songtype))
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

"""
@requires: songtype represents mood of user and random_no represents how many songs that we want to get randomly
@functionality: This function selects random songs from song list
@effect: return list of random songs
"""
def randomsong(songtype,random_no):
    sql = ("""SELECT SongId FROM song WHERE SongTypeId='%s' ORDER BY RAND() LIMIT %s """ % (songtype, random_no))
    mycursor.execute(sql)
    randomlist = mycursor.fetchall()
    return randomlist

"""
@requires: combine_list represents old list in which we will append new_list
@functionality: This function appends two list and there is no repeation
@effect: combine_list contains oldlist and newlist
"""
def appending(combine_list,new_list):
    count=0
    for i in new_list:
        r=0
        for j in combine_list:
            if i==j:
                r=2
        if(r==0):
            combine_list.append(i)
            count = count + 1
    return combine_list

"""
@requires: mood and username of current user
@functionality: This function controls the whole process by ensuring there should be no repetation and list contain 10 songs
@effect: return combine_list contains 10 songs 
"""
def database(mood,username):
    global myresult
    import CheckSongType
    songtype1=CheckSongType.songtype(mood)
    songtype=songtype1[0][0]
    history=historysongs(songtype,username,3)
    myresult=ratedsong(songtype)
    random_no = 10 - 3 - len(history)
    randomlist=randomsong(songtype,random_no)
    combine_list=[]
    combine_list=appending(combine_list,myresult)
    combine_list=appending(combine_list,history)
    combine_list=appending(combine_list,randomlist)
    less=len(combine_list)
    less=10-less

    while less>0:
        a = randomsong(songtype, (less))
        combine_list=appending(combine_list,a)
        less = len(combine_list)
        less = 10 - less


    return combine_list





