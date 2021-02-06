import cv2
import os
import numpy as np
import logging
import time
import math
import datetime

img_loc="input/"
output_loc = "output/"

def main(img_loc):
    imgs=os.listdir(img_loc)
    for img in imgs:
        imgrd=cv2.imread(img_loc+img)
        cv2.imwrite(output_loc+img, imgrd)
        cv2.imshow("imgrd", imgrd)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    main(img_loc)