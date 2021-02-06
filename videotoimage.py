import cv2
import os
import numpy as np
import logging
import time
import math
import datetime

video_path = "Precision_pwil_pre_top_2020-10-18_15-12-51.avi"
folder_path = "output/"

def main(video_path):
    cap = cv2.VideoCapture(video_path)
    counter = 0
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        frame = frame[0:1020,450:670]
        PIC_DATE_TIME = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f')
        cv2.imwrite(folder_path+PIC_DATE_TIME+".jpg", frame)
        cv2.imshow('video',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        counter += 1

if __name__ == '__main__':
    main(video_path)