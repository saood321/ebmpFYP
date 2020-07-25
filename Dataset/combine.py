import os
import cv2
import dlib
import xlwt
from matplotlib import style
style.use("ggplot")

directory = r'C:\Users\M.Saood Sarwar\Downloads\Compressed\images\images\train\normal1'
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')
j=0
k=0
xlist = []
ylist = []
count = 1
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".py"):
        k = k + 1
        images=os.path.join(directory, filename)
        print(images)
        image = cv2.imread(images)
        # Set up some required objects
        detector = dlib.get_frontal_face_detector()  # Face detector
        predictor = dlib.shape_predictor(
            "shape_predictor_68_face_landmarks.dat")  # Landmark identifier. Set the filename to whatever you named the downloaded file


        def get_landmarks(image, k):

            header1='NX{}'.format(k)
            header2 = 'NY{}'.format(k)
            xlist = [header1]
            ylist = [header2]
            detections = detector(image, 1)
            for k, d in enumerate(detections):  # For all detected face instances individually
                shape = predictor(image, d)  # Draw Facial Landmarks with the predictor class

                for i in range(1, 68):  # Store X and Y coordinates in two lists
                    xlist.append(float(shape.part(i).x))
                    ylist.append(float(shape.part(i).y))


            if len(detections) > 0:
                return xlist,ylist

            else:  # If no faces are detected, return error message to other function to handle
                landmarks = "error"
                return landmarks



        xlist,ylist=get_landmarks(image,k)

        for i, e in enumerate(xlist):
            sheet1.write(i, j, e)
        name = "normal1.xls"
        book.save(name)
        j = j + 1
        for i, e in enumerate(ylist):
            sheet1.write(i, j, e)

        name = "normal1.xls"
        book.save(name)
        j = j + 1
        print("Wait...",count)
        count=count+1


    else:
        continue
print("End")