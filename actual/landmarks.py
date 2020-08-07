from getLandmarks import *
from distanceCalculation import *

"""
@requires: This function gets the resized facial-image of person for landmarks
@functionality: This function opens camera, draw rectangle around face and show mood of person around rectangle
@effect: Return mood of person
"""
def landmarks(resized):
    xlist, ylist = get_landmarks(resized)
    if not xlist:
        return 0
    else:
        return distance(xlist,ylist)