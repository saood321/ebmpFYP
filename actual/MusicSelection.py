import actual.DataBaseConnect
mydb,mycursor=actual.DataBaseConnect.database()

def historysongs(songtype,val,limit):
    if songtype==None:
        sql = ("""SELECT history.SongId FROM history INNER JOIN song ON history.SongId = song.SongId WHERE  history.UserId='%s' ORDER BY Rating DESC LIMIT %s""" % (val, limit))
    else:
        sql = ( """SELECT history.SongId FROM history INNER JOIN song ON history.SongId = song.SongId WHERE song.SongTypeId='%s' and history.UserId='%s' ORDER BY Rating DESC LIMIT %s""" % (songtype,val,limit))
    mycursor.execute(sql)
    history = mycursor.fetchall()
    print(history)
    return history

def ratedsong(songtype):
    sql = ("""SELECT SongId FROM song  WHERE SongTypeId='%s' ORDER BY TotalRating DESC LIMIT 3 """ % (songtype))
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

def randomsong(songtype,random_no):
    sql = ("""SELECT SongId FROM song WHERE SongTypeId='%s' ORDER BY RAND() LIMIT %s """ % (songtype, random_no))
    mycursor.execute(sql)
    randomlist = mycursor.fetchall()
    return randomlist


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

def database(mood,val):
    global myresult

    import CheckSongType
    songtype1=CheckSongType.songtype(mood)
    songtype=songtype1[0][0]
    history=historysongs(songtype,val,3)
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





