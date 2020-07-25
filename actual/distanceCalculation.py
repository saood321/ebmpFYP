from svmClasssifier import *
import math

def distance(list1,list2):
    def createList(r1, r2):
        return list(range(r1, r2))
    def createList1(r3, r4):
        return list(range(r3, r4))

    r1, r2 = 0, 68
    mylist1 = createList(r1, r2)
    r3, r4 = 0, 66
    mylist2 = createList1(r3, r4)
    distance=[]
    row = 0
    for i in mylist1:
        for j in mylist2:
            if j >= i:
                row = row + 1
                distance.append(math.sqrt(((list1[j + 1] - list1[i]) ** 2) + ((list2[j + 1] - list2[i]) ** 2)))

    mood=predict(distance)
    return mood
