import cv2
import numpy as np
imgs = []
#wrap:
for i in range(8):
    imges = cv2.imread(str(i)+".jpg")
    imges = cv2.resize(imges,(500,500))
    # cv2.imshow('imges',imges)
    # cv2.waitKey(0)
    
    # detrmine the width and height affter wrap
    width,height = 350,450
    #detrmine the edges of the photo
    pts1 = np.float32([[411,72],[726,103],[363,523],[686,553]])
    #creat a matrix to fit the wrap on it
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    #ft the wrap
    mat =  cv2.getPerspectiveTransform(pts1,pts2)
    #creating output
    imgOut = cv2.warpPerspective(imges, mat, (width,height))

    imgs.append(imges)


# cv2.imshow("img",img)
# cv2.imshow("Output",imgOut)
# cv2.waitKey(0)

#joining images:


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
imgstack = stackImages(0.3,([imgs[6],imgs[7]],[imgs[4],imgs[5]],[imgs[2],imgs[3]],[imgs[0],imgs[1]]))
#imgstack = stackImages(0.5,([img,img,img],[img,img,img]))
# imghor = np.hstack((img,img1))
# imgver = np.vstack((img,img1))

# cv2.imshow("hrozontal img" , imghor)
# cv2.imshow("vertical img" , imgver)

cv2.imshow(" img stack " , imgstack)
                       
cv2.waitKey(0)