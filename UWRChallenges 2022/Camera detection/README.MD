What distinguishes the camera object from the ot of the
objects is that the Camera is an isometric that has a circle inside while the other objects are
only isometric without anything inside. We used Hough Circle Transform to detect the circles.
The circle Hough Transform (CHT) is a basic feature extraction technique used in digital image
processing for detecting circles in imperfect images. The circle candidates are produced by
“voting” in the Hough parameter space and then selecting local maxima in an accumulator
matrix


![image](https://user-images.githubusercontent.com/61525054/170823231-ee899eef-d700-4b48-8f4a-e7ae991271be.png)

for detect the isometric we used yolov3 based on boxes database 
like of database : https://public.roboflow.com/object-detection/packages-dataset

![image](https://user-images.githubusercontent.com/61525054/170823236-e6a8c515-d52a-44db-8f68-91da6e446068.png)


![image](https://user-images.githubusercontent.com/61525054/170823249-08efe86f-7bcd-4439-8d89-b46f4093a34b.png)     ![image](https://user-images.githubusercontent.com/61525054/170823259-caa50869-961f-4f2f-8747-08ddf707566f.png)
       

