import cv2
import matplotlib.pyplot as plt
import numpy as np 

from utils import *
from darknet import Darknet


# Set the location and name of the cfg file
cfg_file = './cfg/yolov3.cfg'

# Set the location and name of the pre-trained weights file
weight_file = './weights/yolov3.weights'

# Set the location and name of the COCO object classes file
namesfile = 'data/coco.names'

# Load the network architecture
m = Darknet(cfg_file)

# Load the pre-trained weights
m.load_weights(weight_file)

# Load the COCO object classes
class_names = load_class_names(namesfile)

# Set the NMS threshold
nms_thresh = 0.6

# Set the IOU threshold
iou_thresh = 0.4




cap = cv2.VideoCapture(0) #testing on labtop camera 
def Circle_ded(img,Centers,x,y): #cirlce detection
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # convert from colored to gray system 
    #blur = cv2.medianBlur(gray,5)
    blur = gray 
    circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,100, #cricle detection 
                                param1= 200,param2=50)
    if circles is not(None):

        circles = np.uint16(np.around(circles))
        
        for i in circles[0,:]:
            Centers.append([i[0],i[1]])
            cv2.circle(img,([i[0],i[1]]),3,[255,0,255],3)
            cv2.putText(original_image,'camera' ,(l,b),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
            cv2.imshow('gray',img)

    
    
            
 
cap = cv2.VideoCapture(0)


while True:
    check ,img= cap.read()
    # Convert the image to RGB
    #original_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    original_image = img

    # We resize the image to the input width and height of the first layer of the network.    
    resized_image = cv2.resize(original_image, (m.width, m.height))

    # Set the IOU threshold. Default value is 0.4
    iou_thresh = 0.4#0.1

    # Set the NMS threshold. Default value is 0.6
    nms_thresh = 0.6#0.3

    # Detect objects in the image
    boxes = detect_objects(m, resized_image, iou_thresh, nms_thresh)

    # Print the objects found and the confidence level
    #print_objects(boxes, class_names)

    #Plot the image with bounding boxes and corresponding object cla    ss labels
    dh, dw, _ = original_image.shape
    for dt in boxes:

        name_num = int(dt[-1])
        name = class_names[name_num]
        if name_num == 0:
            continue

        # Split string to float
        x, y, w, h = dt[0:4]


        l = int((x - w / 2) * dw)
        r = int((x + w / 2) * dw)
        t = int((y - h / 2) * dh)
        b = int((y + h / 2) * dh)

     
        
        if l < 0:
            l = 0
        if r > dw - 1:
            r = dw - 1
        if t < 0:
            t = 0
        if b > dh - 1:
            b = dh - 1
        box = original_image[t:b,l:r]
        center = Circle_ded(box,[],l,t)

            
        
        
     
    

        cv2.rectangle(original_image, (l, t), (r, b), (0, 0, 255), 1)
        
  
    cv2.imshow('camera',original_image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
          break
