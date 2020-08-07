from svmClasssifier import *
import math

"""
@requires: xlist containing x-cordinates and ylist containing y-cordinates of 68 landmarks. 
@functionality: This function calculate distance from each point to all other points.
@effect: Return mood of person from predict() to landmark()
"""
def distance(xlist,ylist):
    def createList(r1, r2):
        return list(range(r1, r2))
    def createList1(r3, r4):
        return list(range(r3, r4))

    r1, r2 = 0, 68
    mylist1 = createList(r1, r2)
    r3, r4 = 0, 66
    mylist2 = createList1(r3, r4)
    distance=[]

    for i in mylist1:
        for j in mylist2:
            if j >= i:
                distance.append(math.sqrt(((xlist[j + 1] - xlist[i]) ** 2) + ((ylist[j + 1] - ylist[i]) ** 2)))

    mood=predict(distance)
    return mood
