import cv2
from Segmentation import *
import time

"""
@requires: None
@functionality: This function opens camera, draw rectangle around face and show mood of person around rectangle
@effect: Return mood of person
"""
def camera():
    mood=""
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 1024)
    cap.set(15, 0.1)
    previous = time.time()
    counter = 0
    while True:
        ret, img = cap.read()
        frame = cv2.flip(img, 1)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, mood, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        current = time.time()
        counter += current - previous
        previous = current
        if counter > 5:
            mood = crop(frame)
            if (mood == 0):
                mood = ""
            else:
                mood=mood[0]
            counter = 0

        cv2.imshow("result", frame)
        if(cv2.waitKey(1) & 0xFF == ord('n')):
            cap.release()
            cv2.destroyAllWindows()
            return mood

        if (cv2.waitKey(2) & 0xFF == ord('q')):
            cap.release()
            cv2.destroyAllWindows()
            return None

