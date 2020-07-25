
import cv2
from cropImage import *
import time

def camera():
    mood=""
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 1024)
    cap.set(15, 0.1)
    previous = time.time()
    delta = 0
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
        delta += current - previous
        previous = current
        if delta > 5:
            mood1 = crop(frame)
            if (mood1 == 0):
                mood = ""
            else:
                mood = mood1[0]
            delta = 0

        cv2.imshow("result", frame)
        if(cv2.waitKey(1) & 0xFF == ord('n')):
            cap.release()
            cv2.destroyAllWindows()
            return mood

        if (cv2.waitKey(2) & 0xFF == ord('q')):
            cap.release()
            cv2.destroyAllWindows()
            return None

