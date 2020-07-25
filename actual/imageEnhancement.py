import cv2
from landmarks import *
from hogFeatures import *
def imageEnhance(img):

    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray_img_eqhist=cv2.equalizeHist(gray_img)
    #return landmarks(gray_img_eqhist) if we want to use landmark algorithm
    return hog(gray_img_eqhist)

