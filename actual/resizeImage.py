import cv2
from imageEnhancement import *
"""
@requires: Image that we want to resize
@functionality: This function resize the image according to our need
@effect: Return mood of person from imageEnhance() to crop()
"""
def resize(img):
    width = 48
    height = 48
    dimension = (width, height)

    resized = cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)
    return imageEnhance(resized)