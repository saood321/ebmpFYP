import cv2
from landmarks import *
from hogFeatures import *

"""
@requires: Image of person that we want to enhance and improve the quality
@functionality: This function enhance the quality of image using Histogram Equalization
@effect: Return mood of person to resize() from hog() / landmarks()
"""
def imageEnhance(img):

    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray_img_eqhist=cv2.equalizeHist(gray_img)
    # if we want to use landmark algorithm
    return landmarks(gray_img_eqhist)
    #return hog(gray_img_eqhist)

