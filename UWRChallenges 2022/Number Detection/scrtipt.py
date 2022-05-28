import numpy as np 
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
cong = r'--oem 3 --psm 6 outputbase digits'




#numbers = ['9','10','70']





def build_grade(size):
  grade  = np.ones((size*100 ,size*100,3)).astype(np.uint8)*255 
  y = 0
  pos = []
  for i in range(size):
    x = 0 
    for i in range(size):
      cv2.rectangle(grade,(x,y+100),(x+100,y-100),[255,0,0],3)
      pos.append((x+50,y+50))
      x = x+100
    y = y+100
  return grade,pos


img = cv2.imread('Untitled52.png')



numbers = list(map(str,input().split()))


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gray = cv2.bitwise_not(gray)
ret, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
thresh = cv2.bitwise_not(thresh)
#contours,_ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(img,contours,-1,[0,0,0],-1)

#img = cv2.Canny(img,0,255)


#print(img.shape[:2])
(hi,wi) = img.shape[:2]
#print(pytesseract.image_to_string(thresh))
boxes =pytesseract.image_to_data(thresh,config = cong)
#print(boxes)
list = []
i = 0
for x,b in enumerate(boxes.splitlines()):
    if x!= 0:
        b = b.split()
        if len(b)==12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            #if b[11]in numbers:
            
            #cv2.putText(img,b[11],(x,y-30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            list.append(b[11])
            if b[11]in numbers:
                cv2.rectangle(img,(x,y),(w+x,y+h),[0,0,255],1)
list = np.array(list)
grade,pos = build_grade(6)
print(len(pos))
for i in numbers:
    try:
        nums = np.where(list ==i)[0]
    except:
        None
    for i in nums:
        i = int(i)
        cv2.circle(grade,pos[i],20,[123,200,25],-1)
    



           
        #print(b[0])
cv2.imshow('Detected text', grade)
cv2.imshow('grade', img)
cv2.waitKey(0)
