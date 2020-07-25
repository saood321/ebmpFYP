import cv2
import dlib
import xlwt
import matplotlib.pyplot as plt
m=0
def crop(image,m):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )

    print("[INFO] Found {0} Faces.".format(len(faces)))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_color = image[y:y + h, x:x + w]
        print("[INFO] Object found. Saving locally.")
        cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color)
        img=str(w)+str(h)+'_faces.jpg'

    img = cv2.imread(img)
    status = cv2.imwrite('faces_detected.jpg', image)
    print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('sheet1')


    width = 350
    height = 350
    dim = (width, height)

    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    print('Resized Dimensions : ', resized.shape)
    cv2.imshow("Resized image", resized)
    cv2.imwrite('resizeface{}.jpg'.format(m), resized)



#capture from camera at location 0
cap = cv2.VideoCapture(0)
#set the width and height, and UNSUCCESSFULLY set the exposure time
cap.set(3,1280)
cap.set(4,1024)
cap.set(15, 0.1)

while True:
    ret, img = cap.read()
    frame = cv2.flip(img, 1)
    window_name = 'Image'
    center_coordinates = (680, 350)
    axesLength = (150, 200)
    angle = 0
    startAngle = 0
    endAngle = 360
    color = (55, 55, 255)
    thickness = 7
    image = cv2.ellipse(frame, center_coordinates, axesLength,angle, startAngle, endAngle, color, thickness)

    cv2.imshow('Image',image)
    if (cv2.waitKey(1) & 0xFF == ord('n')):
        m = m + 1
        crop(frame,m)
    elif (cv2.waitKey(2) & 0xFF == ord('e')):
        break
cap.release()
cv2.destroyAllWindows()
