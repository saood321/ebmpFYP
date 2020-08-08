from svmClasssifier import *
import math

"""
@requires: xlist containing x-cordinates and ylist containing y-cordinates of 68 landmarks. 
@functionality: This function calculate distance from each point to all other points.
@effect: Return mood of person from predict() to landmark()
"""
def distance(xlist,ylist):

    distance=[]

    for i in list(range(0, 68)):
        for j in list(range(0, 66)):
            if j >= i:
                distance.append(math.sqrt(((xlist[j + 1] - xlist[i]) ** 2) + ((ylist[j + 1] - ylist[i]) ** 2)))

    mood=predict(distance)
    return mood
