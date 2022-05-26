
import cv2
import numpy as np

def ph(frame):
    global i 
    def click_event(event, x, y, flags, param): #clcik event fucntion 
        global count #giveing index for every picture to stitched it again
        #img = cv2.imread('33.png')
        img = frame
        img = cv2.resize(img,(1000,1000)) # resize the image 
        if event == cv2.EVENT_LBUTTONDOWN:
    
            #cv2.circle(img, (x, y), 3, (0, 0, 0), 1, cv2.FILLED)
            points.append((x, y)) # save every points we clicked on 
            if len(points) ==2 :
                cv2.rectangle(img, points[-1], points[-2], (19,69, 139), 2) # draw rectange we click tiwce
                # determine dimensions of rectangle 
                w1 = min(points[-1][0],points[-2][0])
                w2 = max(points[-1][0],points[-2][0])
                h1 = min(points[-1][1],points[-2][1])
                h2 = max(points[-1][1],points[-2][1])
                # dvide image into 2 pieces 
                p1 = img[h1:h2,w1:int((w2+w1)/2)]
                p2 = img[h1:h2,int((w2+w1)/2):w2]
                #save the images 
                cv2.imwrite("imgs/"+str(count)+'.jpg',p1)
                cv2.imwrite("imgs/"+str(count+1)+'.jpg',p2)
                count = count + 2
                points.clear()

            cv2.imshow('Image', img)
            #cv2.imwrite('33.png', img)
        elif event == cv2.EVENT_RBUTTONDOWN:
            img = frame
            #img = cv2.imread('33.png')
            img = cv2.resize(img,(1000,1000))
            
        



    #frame = cv2.imread('33.png')
    img = frame
    img = cv2.resize(img,(1000,1000))
    cv2.imshow('Image', img)
    #points = []
    cv2.setMouseCallback('Image', click_event)

    cv2.waitKey(30)
    #cv2.destroyAllWindows()
#frame = cv2.imread('Untitled.png')
cap = cv2.VideoCapture('4588.mp4')
points = []
count = 0
while True:
    check,frame = cap.read()
    ph(frame)