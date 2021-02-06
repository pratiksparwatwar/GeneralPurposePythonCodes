import cv2
import os

y1_crop,y2_crop,x1_crop,x2_crop = 250,750,250,950
x1_rect, x2_rect, y1_rect, y2_rect = 220,450, 150,400 

#imgrd = imgrd[y1_crop:y2_crop, x1_crop:x2_crop]
#cv2.rectangle(result, (x1_cam,0),(x2_cam,result.shape[0]),(0,0,0),-1)

img_loc="input/"
output_loc = "output/"

def main(img_loc):
    imgs=os.listdir(img_loc)
    for img in imgs:
        imgrd=cv2.imread(img_loc+img)
        x = imgrd.shape[1]
        y = imgrd.shape[0]
        print(x, y)

        imgrd = imgrd[y1_crop:y2_crop, x1_crop:x2_crop]
        print(imgrd.shape) 
        
        cv2.rectangle(imgrd, (x1_rect,y1_rect),(x2_rect,y2_rect),(0,0,0),-1)   
        cv2.imwrite(output_loc+img, imgrd)
        cv2.imshow("imgrd", imgrd)
        cv2.waitKey(0)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
            #break

if __name__ == '__main__':
    main(img_loc)