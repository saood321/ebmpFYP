from getLandmarks import *
from distanceCalculation import *
def landmarks(resized):
    xlist, ylist = get_landmarks(resized)

    if not xlist:
        return 0
    else:
        return distance(xlist,ylist)