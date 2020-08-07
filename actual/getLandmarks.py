import dlib
"""
@requires: Get resized image of face for extracting landmarks of face
@functionality: This function extract landmarks from face containing x-cordinates and y-cordinates
@effect: Return two lists containing x and y-cordinates of 68 landmarks
"""
def get_landmarks(resized):
    detector = dlib.get_frontal_face_detector()  # Face detector+
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    img =resized

    xlist = []
    ylist = []
    detections = detector(img, 1)
    for face in detections:
        shape = predictor(img, face)  # Draw Facial Landmarks with the predictor class
    for i in range(1, 68):  # Store X and Y coordinates in two lists
        xlist.append(float(shape.part(i).x))
        ylist.append(float(shape.part(i).y))

    if len(detections) == 1:
        return xlist, ylist

    else:
        print("No face Detected")
        return xlist,ylist

