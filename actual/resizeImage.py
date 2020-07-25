import cv2
from imageEnhancement import *
def resize(img):
    width = 48
    height = 48
    dim = (width, height)

    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    #cv2.imwrite('resizeface.jpg', resized)
    return imageEnhance(resized)