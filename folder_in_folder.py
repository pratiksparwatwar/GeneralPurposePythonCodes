import os
import cv2

img_dir = "/home/user/Documents/Project/KSH/false_positive/"
dest_dir = "/home/user/Documents/Project/KSH/test_folder/"

dir_list = os.listdir(img_dir)
dir_list.sort()
for directory in dir_list:
    img_list = os.listdir(img_dir+directory)
    img_list.sort()
    for img in img_list:
        print(img_dir+directory+"/"+img)
        im = cv2.imread(img_dir+directory+"/"+img)
        
        dest_path = dest_dir+directory
        if os.path.isdir(dest_path) is not True:
            os.makedirs(dest_path)
        cv2.imwrite(dest_path+"/"+img, im)
