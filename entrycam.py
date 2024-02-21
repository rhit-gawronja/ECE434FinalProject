#!/usr/bin/env python3

import cv2
import time
#import imutils
# initializing tensorflow interpreter
from imageProcessing import my_function,check_last_run,processFrame
from config import configureStreamKey, configureStreamPlatform
from queue import Queue
import subprocess
# Initializing the HOG person
# detector

RTMP_URL = configureStreamPlatform()
STREAM_KEY =  configureStreamKey()
# Reading the Image by grabbing the camera
camera = cv2.VideoCapture(0)

frame_width = 320
frame_height =180
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
BUFFER_SIZE = 20  # Number of frames to buffer
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

camera.release()
process.stdin.close()
process.wait()

cv2.destroyAllWindows()
