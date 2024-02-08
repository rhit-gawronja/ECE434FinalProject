#!/usr/bin/env python3

import cv2
import time
#import imutils
  
# Initializing the HOG person
# detector
cv2.useOptimized()
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
  
# Reading the Image
camera = cv2.VideoCapture(0)

ret, frame = camera.read()

print("read image")
# Resizing the Image
#image = imutils.resize(image,
#                       width=min(400, image.shape[1]))

new_width = 450 #450 
new_height = 400 # 400
hog_time_start = time.time()
resized_image = cv2.resize(frame, (new_width, new_height))
# Detecting all the regions in the 
# Image that has a pedestrians inside it
(regions, _) = hog.detectMultiScale(resized_image, 
                                    winStride=(8,8),
                                    padding=(8, 8),
                                    scale=1.05)
print("hog scaled")
print(regions)
# Drawing the regions in the Image
for (x, y, w, h) in regions:
    cv2.rectangle(resized_image, (x, y), 
                  (x + w, y + h), 
                  (0, 0, 255), 2)
print("region drawn")
hog_time_end = time.time()

elapsed = hog_time_end-hog_time_start
print(elapsed)
# Showing the output Image
cv2.imwrite("newbox.png", resized_image)

camera.release()
