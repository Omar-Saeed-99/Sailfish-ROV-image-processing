# In Inspecting an offshore aquaculture fish pen
we should follow the RED line that looks like the letter “Z” This means that we only have 3 types of movements, we set RIGHT move as Default, And when a vertical line appears, it changes the default from right to left This process is repeated until the task is completed, in Identifying and counting damaged net areas We converted the image to a binary mode(black & white), which appears in green as black and the rest of the colors in white, and when a white square appears with an area larger than the adjacent areas, this means that there is a gap in the network and it is recognized As shown in the picture below
![image](https://user-images.githubusercontent.com/61525054/170714702-a0fd077f-eaec-4cd9-b9d3-64c5d6fb2116.png)

# To differentiate between “morts” from live fish 
a Yolov4 model was used to detect fish in real-time then we released the mort fish The mort fish seems brighter due to reflecting the light as it lies on its side. As shown in the picture.

![image](https://user-images.githubusercontent.com/61525054/170715066-78c5580a-4ea2-4084-90ac-f756ce37fc49.png)

# In the Measure fish size Task, 
The PVC tube on which the fish is hung has a known length. We will draw a line on the tube to find out its length in pixels and divide it by its true length to find out the ratio between the real length and the length in pixels in the image and then draw a line on
the fish we want to be measured and calculate its length in pixels and then multiply it by the ratio that we calculated before and find the real length


# In mapping task 
A picture of 8 squares representing  locusts will appear. The co-pilot will click on the picture, the beginning and end of the ship, and after selecting it, the ship will appear in front of him, drawn in the pictur
