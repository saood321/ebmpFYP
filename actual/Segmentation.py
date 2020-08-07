import cv2
from resizeImage import *

"""
@requires: Image that we want to crop
@functionality: This function crops the image and segment-out face from background
@effect: Return mood of person to camera() from resize()
"""
def crop(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )
    print("Found {0} Face(s).".format(len(faces)))
    if len(faces)>=1:

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            img = image[y:y + h, x:x + w]
        return resize(img)

    else:
        return 0




