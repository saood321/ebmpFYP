import DataBaseConnect

def songtype(mood):
    mydb,mycursor=DataBaseConnect.database()
    sql = ("""SELECT SongTypeId  FROM songtype WHERE Type='%s' """ % (mood))
    mycursor.execute(sql)
    songTypeId = mycursor.fetchall()
    return songTypeId