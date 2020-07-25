import os
import cv2
import dlib
import xlwt
from matplotlib import style
style.use("ggplot")
global i
i=1
def distance(list1,list2):
    k=0
    global i
    i=i+1
    import pandas as pd
    import math
    import xlwt
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('Sheet1')
    df = pd.read_excel("surprise1.xls", sheet_name=0)
    limit=len(list1)

    sheet1.write(0, i - 1, "Surprise")
    name = r"C:\Users\M.Saood Sarwar\Downloads\Compressed\try\surpriseDistance1.xls"
    book.save(name)

    def createList(r1, r2):
        return list(range(r1, r2))

    def createList1(r3, r4):
        return list(range(r3, r4))

    r1, r2 = 0, 68
    mylist1 = createList(r1, r2)
    r3, r4 = 0, 66
    mylist2 = createList1(r3, r4)


    for i in mylist1:
        for j in mylist2:
            if j >= i:
                distance = math.sqrt(((list1[j + 1] - list1[i]) ** 2) + ((list2[j + 1] - list2[i]) ** 2))
                sheet1.write(k, i, distance)
                k = k + 1

    name = r"C:\Users\M.Saood Sarwar\Downloads\Compressed\try\surpriseDistance1.xls"
    book.save(name)
    print('End')


directory = r'C:\Users\M.Saood Sarwar\Downloads\Compressed\try'
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')
j=0

xlist = []
ylist = []
count = 1
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".py"):
        images=os.path.join(directory, filename)
        image = cv2.imread(images)
        # Set up some required objects
        detector = dlib.get_frontal_face_detector()  # Face detector
        predictor = dlib.shape_predictor(
            "shape_predictor_68_face_landmarks.dat")  # Landmark identifier. Set the filename to whatever you named the downloaded file


        def get_landmarks(image):


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



        xlist,ylist=get_landmarks(image)

        distance(xlist,ylist)


    else:
        continue
print("End")

