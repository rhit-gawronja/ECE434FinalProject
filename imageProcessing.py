import cv2
from messaging import sendText
import time
last_run_time = None
def my_function():
    global last_run_time
    # Update the last run timestamp
    last_run_time = time.time()
    # Your function code goes here
    print("Function has been run.")

def check_last_run():
    global last_run_time
    if last_run_time is None:
        return False  # Function has never been run
    current_time = time.time()
    elapsed_time = current_time - last_run_time
    return elapsed_time <= 30  # 10 minutes = 600 seconds
def processFrame(frame):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    (regions, _) = hog.detectMultiScale(frame, 
                                    winStride=(4,4),
                                    padding=(4, 4),
                                    scale=1.05)
    print(regions)
# Drawing the regions in the Image
    num_pp=0
    for (x, y, w, h) in regions:
        cv2.rectangle(frame, (x, y), 
                  (x + w, y + h), 
                  (0, 0, 255), 2)
        num_pp+=1
        

# Showing the output Image
    cv2.imwrite("newbox.png", frame)
    if num_pp>=1 :
        sendText() 