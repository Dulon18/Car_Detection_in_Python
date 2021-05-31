#pip install opencv-python
import cv2
#capture frames from a video
cap=cv2.VideoCapture('car.mp4')

#object we want to detect
car_cascade=cv2.CascadeClassifier('cars.xml')

while True:
    ret,frames=cap.read()
    gray=cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
    cars=car_cascade.detectMultiScale(gray,1.1,2)

    # draw rectangle for each car
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(255,0,255),2)
       # display frame
        cv2.imshow('Car Detection By Python',frames)

       #Wait for Esc key to stop
        if cv2.waitKey(33) == 27:
            break
cv2.destroyAllwindows()
