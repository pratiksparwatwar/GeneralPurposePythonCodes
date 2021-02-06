import cv2
import os
import numpy as np
import logging
import time
import math
import datetime

# import some common libraries
import matplotlib.pyplot as plt
import numpy as np
import cv2

from IPython.display import display
from PIL import Image

video_path = "brown_bare1.avi"
folder_path = "output/"

def main(video_path):
    cap = cv2.VideoCapture(video_path)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = int(cap.get(cv2.CAP_PROP_FPS))    
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(folder_path+"video.avi",fourcc, fps, (width,height))
    
    counter = 0
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        out.write(frame)
        frame = cv2.resize(frame, (int(frame.shape[1] * 70 / 100), int(frame.shape[0] * 70 / 100)))
        cv2.imshow('video',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        counter += 1
    out.release()        
    cap.release()
    cv2.destroyAllWindows()
    

if __name__ == '__main__':
    main(video_path)