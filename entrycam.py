#!/usr/bin/env python3

import cv2
import time
#import imutils
# initializing tensorflow interpreter
from imageProcessing import my_function,check_last_run,processFrame
from queue import Queue
import subprocess
# Initializing the HOG person
# detector

RTMP_URL = "rtmp://live.twitch.tv/app/"
STREAM_KEY = "live_1039350101_wNFlNT8Z6nSe42VAXDAAkxOzjd0r06"  
# Reading the Image by grabbing the camera
camera = cv2.VideoCapture(0)

frame_width = 320
frame_height = 180
camera.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
# Define the command to stream video using ffmpeg
command = ['ffmpeg',
           '-f', 'rawvideo',
           '-vcodec', 'rawvideo',
           '-pix_fmt', 'bgr24',
           '-s', f'{frame_width}x{frame_height}',
           '-r', '19',
           '-i', '-',
           '-c:v', 'libx264',
           '-b:v', '2M',
           '-preset', 'ultrafast',
           '-f', 'flv',
           f'{RTMP_URL}/{STREAM_KEY}']
process = subprocess.Popen(command, stdin=subprocess.PIPE)
BUFFER_SIZE = 30  # Number of frames to buffer
frame_buffer = Queue(maxsize=BUFFER_SIZE)
i=0
while True:
    ret, frame = camera.read()

# Resizing the Image
#image = imutils.resize(image,
#                       width=min(400, image.shape[1]))
    
    if i==0:
        my_function()
        i+=1 
    if frame_buffer.full() and check_last_run():
        print('buf full')
        frame_buffer.get()  # Remove oldest frame if buffer is full
    frame_buffer.put(frame)
    if not check_last_run():
        frameDup=frame
        processFrame(frameDup)
        my_function()

    # If buffer is full, start streaming frames
    if frame_buffer.full():
        for _ in range(BUFFER_SIZE):
            frame_to_stream = frame_buffer.get()
            process.stdin.write(frame_to_stream.tobytes())
            process.stdin.flush()
#     new_width = 800 #450 
#     new_height = 750 # 400
#     hog_time_start = time.time()
#     resized_image = cv2.resize(frame, (new_width, new_height))
# # Detecting all the regions in the 
# # Image that has a pedestrians inside it
#     (regions, _) = hog.detectMultiScale(resized_image, 
#                                     winStride=(4,4),
#                                     padding=(4, 4),
#                                     scale=1.05)
#     print("hog scaled")
#     print(regions)
# # Drawing the regions in the Image
#     num_pp=0
#     for (x, y, w, h) in regions:
#         if w*h >4000:
#             cv2.rectangle(resized_image, (x, y), 
#                   (x + w, y + h), 
#                   (0, 0, 255), 2)
#             num_pp+=1
        
#     print("region drawn")
#     hog_time_end = time.time()

#     elapsed = hog_time_end-hog_time_start
#     print(elapsed)
# # Showing the output Image
#     cv2.imwrite("newbox.png", resized_image)
#     if num_pp>=1 and not(check_last_run()):
#         my_function()
#         sendText()
camera.release()
process.stdin.close()
process.wait()

cv2.destroyAllWindows()
