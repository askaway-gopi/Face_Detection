import cv2

#path = "C:/Users/Gopinath/Desktop/download.jpg"
#img = cv2.imread(path)
capture = cv2.VideoCapture(0)
fd = cv2.CascadeClassifier("C:/Python/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

while True:
    cap,frame = capture.read()
    faces = fd.detectMultiScale(frame, 1.32, 5)

    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,255,0),3)

    cv2.imshow("Detected Img",frame)
    key = cv2.waitKey(1)
    if(key == ord('q')):
        break
capture.release()
cv2.destroyAllWindows()
