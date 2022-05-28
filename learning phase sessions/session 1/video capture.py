import cv2 
import numpy as np 
cap = cv2.VideoCapture(0) 
 
while True :
    check,frame = cap.read()
    cv2.imshow('window',frame)
    if cv2.waitKey(1)
          break
cap.release()
cv2.destroyAllWindows()
