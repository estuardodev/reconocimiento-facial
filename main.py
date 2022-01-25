import cv2

haar_file = 'haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)

while True:
    (_, im) =  webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(gray)
    for (x,y,w, h) in faces:
        cv2.rectangle(im, (x,y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('OpenCV', im)
    kay = cv2.waitKey(10)
    if kay == 27:
        break
