#== date : 20210506 ==#

import cv2
import os
import time

#for labelme
import codecs
import PIL
from PIL import Image
import io
import json

#for labelImg
import pandas as pd
import xml.etree.ElementTree as ET
import xml.dom.minidom as md

input_path = "/home/user/Documents/Practice/Practice_json/input/"
output_path = "/home/user/Documents/Practice/Practice_json/output/"

def encodeImageForJson(image):
    t_encode = int(time.time()*1000)

    img_pil = Image.fromarray(image, mode='RGB')
    f = io.BytesIO()
    img_pil.save(f, format='PNG')
    data = f.getvalue()
    encData = codecs.encode(data, 'base64').decode()
    encData = encData.replace('\n', '')

    print("time for encode : ", int(time.time()*1000) - t_encode)
    
    return encData

def labelme_rotate(imagedata, json_ip_path, json_op_path, width, height):
    t_json = int(time.time()*1000)
    with open(json_ip_path, 'r') as f1:
        d = json.load(f1)
        d['imageData'] = imagedata
        for i in d['shapes']:
            for points in i['points']:
                points[0] = width - points[0]
                points[1] = height - points[1]
    with open(json_op_path, 'w') as f2:
        json.dump(d, f2)

    print("time for json : ", int(time.time()*1000) - t_json)
    
def labelImg_rotate(xml_ip_path, xml_op_path, width, height, f):
    t_xml = int(time.time()*1000)
    file = md.parse(xml_ip_path)
    
    no_of_labels = file.getElementsByTagName("object")
    print("number of labels : ", len(no_of_labels))
    
    for i in range(len(no_of_labels)):
        #=========== for xmin =================#
        xmin = file.getElementsByTagName("xmin")
        xmin_new = str(width - int(xmin[i].firstChild.nodeValue))
        file.getElementsByTagName("xmin")[i].childNodes[0].nodeValue = xmin_new
        xmin = file.getElementsByTagName("xmin")
        #print(xmin[i].firstChild.nodeValue)    
        #=========== for xmax =================#
        xmax = file.getElementsByTagName("xmax")
        xmax_new = str(width - int(xmax[i].firstChild.nodeValue))
        file.getElementsByTagName("xmax")[i].childNodes[0].nodeValue = xmax_new
        xmax = file.getElementsByTagName("xmax")
        #print(xmax[i].firstChild.nodeValue)
        #=========== for ymin =================#
        ymin = file.getElementsByTagName("ymin")
        ymin_new = str(height - int(ymin[i].firstChild.nodeValue))
        file.getElementsByTagName("ymin")[i].childNodes[0].nodeValue = ymin_new
        ymin = file.getElementsByTagName("ymin")
        #print(ymin[i].firstChild.nodeValue)
        #=========== for ymax =================#
        ymax = file.getElementsByTagName("ymax")
        ymax_new = str(height - int(ymax[i].firstChild.nodeValue))
        file.getElementsByTagName("ymax")[i].childNodes[0].nodeValue = ymax_new
        ymax = file.getElementsByTagName("ymax")
        #print(ymax[i].firstChild.nodeValue)

    #=============changing folder =================#
    folder = file.getElementsByTagName("folder")
    folder_new = output_path.split("/")[-2]
    file.getElementsByTagName("folder")[0].childNodes[0].nodeValue = folder_new
    folder = file.getElementsByTagName("folder")
    #print(folder[0].firstChild.nodeValue)
    
    #=============changing path =================#
    path = file.getElementsByTagName("path")
    path_new = output_path+f[:-4]+".jpg"
    file.getElementsByTagName("path")[0].childNodes[0].nodeValue = path_new
    path = file.getElementsByTagName("path")
    #print(path[0].firstChild.nodeValue)
    
    with open(xml_op_path,"w") as fs:
        fs.write(file.toxml())
        fs.close()

    print("time for xml : ", int(time.time()*1000) - t_xml)

def main():
    dirlist = os.listdir(input_path)
    dirlist.sort()
    for f in dirlist:
        #================ Rotating jpg =================#
        if ".jpg" in f:
            img = cv2.imread(input_path+f)
            print(img.shape)
            height = img.shape[0]
            width = img.shape[1]
            img = cv2.rotate(img, cv2.ROTATE_180)
            cv2.imwrite(output_path+f, img)
        #================ Rotating json =================#
        if ".json" in f:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            imagedata = encodeImageForJson(img)
            json_ip_path = input_path+f
            json_op_path = output_path+f
            labelme_rotate(imagedata, json_ip_path, json_op_path, width, height)
        #================ Rotating xml =================#
        if ".xml" in f:
            xml_ip_path = input_path+f
            xml_op_path = output_path+f
            labelImg_rotate(xml_ip_path, xml_op_path, width, height, f)

if __name__ == '__main__':
    main()