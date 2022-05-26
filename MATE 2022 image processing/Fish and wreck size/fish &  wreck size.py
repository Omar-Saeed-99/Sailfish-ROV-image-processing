import cv2
import math as m
def lenght(frame):
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    def click_event(event, x, y, flags, param):
        wr = 30 #rernce real lenght  30 for fish 70 for shipe wrick
        img = frame
        img = cv2.resize(img,(1000,1000)) # reszie the image
        if event == cv2.EVENT_LBUTTONDOWN:
    
            cv2.circle(img, (x, y), 3, (0, 0, 0), 1, cv2.FILLED) # draw circle when click on screen
            points.append((x, y)) # save every point clicked 
            if len(points) % 2 == 0:
                cv2.line(img, points[-1], points[-2], (0, 0, 255), 1, cv2.LINE_AA) #draw line connecting 2 circles 
                if len(points)==2: #for refernce 
                    r = m.sqrt(m.pow(abs(points[-1][0]-points[-2][0]),2)+m.pow(abs(points[-1][1]-points[-2][1]),2)) # using Pythagoras theroy to detrmine the length 
                    ro.append(r)
                    v = r/wr
                    vo.append(v)
                if len(points) == 4:# for fish or shipe wrick 
                    r = (m.sqrt(m.pow(abs(points[-1][0]-points[-2][0]),2)+m.pow(abs(points[-1][1]-points[-2][1]),2)))/vo[-1]
                    cv2.putText(img,'x = '+str(r),(50+70,50+70),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,255),1) # display the length in CM 
                    points.clear()
            cv2.putText(img,'points = '+str(len(points)),(50,50),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,255),1) # display how many points you had clicked 


            cv2.imshow('Image', img)
        elif event == cv2.EVENT_RBUTTONDOWN:
            img = frame
            img = cv2.resize(img,(1000,1000))
            
            



    img = frame
    img = cv2.resize(img,(1000,1000))
    cv2.imshow('Image', img)
    points = []
    ro = []
    vo = []
    cv2.setMouseCallback('Image', click_event)

    cv2.waitKey(0) # for freezing the streaming and capture one image only 
    cv2.destroyAllWindows()
