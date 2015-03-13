import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/home/zarin/Documents/SoftDesSp15/haarcascade_frontalface_alt.xml')
kernel = np.ones((21,21),'uint8')


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
    for (x,y,w,h) in faces:
        frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
        # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.circle(frame,(350,150), 20, (0,0,0), -1)
        cv2.circle(frame,(450,150), 20, (0,0,0), -1)
        cv2.line(frame,(300,250),(500,250),(255,0,0),10)


    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


