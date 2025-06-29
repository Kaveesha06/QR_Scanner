import time
import cv2
from pyzbar.pyzbar import decode

cam = cv2.VideoCapture(0)
cam.set(5, 640) # Set width
cam.set(6, 480) # Set height

camera = True
while camera == True:
    sucess, frame = cam.read()

    for i in decode(frame):
        print(i.type)
        print(i.data.decode('utf-8'))
        time.sleep(6)

        cv2.imshow("QR Code Scanner", frame)
        cv2.waitKey(3)

