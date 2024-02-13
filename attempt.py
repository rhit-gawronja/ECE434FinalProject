#!/usr/bin/env python3

import cv2
#import imutils


# initializing tensorflow interpreter
cv2.useOptimized()
# Initializing the HOG person
# detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
  
# Reading the Image
image = cv2.imread('joey.jpg')
print("read image")
# Resizing the Image
#image = imutils.resize(image,
#                       width=min(400, image.shape[1]))

new_width = 400 #450 
new_height = 500 # 400

resized_image = cv2.resize(image, (new_width, new_height))
# Detecting all the regions in the 
# Image that has a pedestrians inside it
(regions, _) = hog.detectMultiScale(resized_image, 
                                    winStride=(4,4),
                                    padding=(4, 4),
                                    scale=1.05)
print("hog scaled")
print(regions)
# Drawing the regions in the Image
for (x, y, w, h) in regions:
    cv2.rectangle(resized_image, (x, y), 
                  (x + w, y + h), 
                  (0, 0, 255), 2)
print("region drawn") 
# Showing the output Image
cv2.imwrite("newbox.png", resized_image)


