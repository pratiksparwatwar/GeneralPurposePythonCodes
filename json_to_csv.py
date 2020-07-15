import os
import json
import csv

image_path = "/home/ubuntu/Documents/Pratik/Bajaj/bajaj_data_frcnn/K3/K3BS6_VSVG/"
# fl = open('/home/ubuntu/Documents/Pratik/Bajaj/bajaj_data_frcnn/K3/K3.csv', 'a+')
# datavd = 'filename,width,height,class,xmin,ymin,xmax,ymax'
# fl.write(datavd)
# fl.write('\n')
# fl.flush()
# fl.close()

img_list = os.listdir(image_path)
img_list.sort()
for f in img_list:
    if ".json" in str(f):
        with open(image_path + f, 'r') as f1:
            d = json.load(f1)
            #print(d.keys())
            for i in d['shapes']:
                fl = open('/home/ubuntu/Documents/Pratik/Bajaj/bajaj_data_frcnn/K3/K3.csv', 'a+')
                datavd = str(d['imagePath'])+","+str(d['imageWidth'])+","+str(d['imageHeight'])+","+str(i['label'])+","+str(int(i['points'][0][0]))+","+str(int(i['points'][0][1]))+","+str(int(i['points'][1][0]))+","+str(int(i['points'][1][1]))
                # if "OUTER" in str(i['label']):
                #     datavd = str(d['imagePath'])+","+str(d['imageWidth'])+","+str(d['imageHeight'])+","+str(i['label'])+","+str(472)+","+str(111)+","+str(1299)+","+str(937)
                # if "VBIG" in str(i['label']):
                #     datavd = str(d['imagePath'])+","+str(d['imageWidth'])+","+str(d['imageHeight'])+","+str(i['label'])+","+str(537)+","+str(340)+","+str(895)+","+str(727)
                # if "VSMALL" in str(i['label']):
                #     datavd = str(d['imagePath'])+","+str(d['imageWidth'])+","+str(d['imageHeight'])+","+str(i['label'])+","+str(960)+","+str(357)+","+str(1213)+","+str(653)
                # if "THREAD" in str(i['label']):
                #     datavd = str(d['imagePath'])+","+str(d['imageWidth'])+","+str(d['imageHeight'])+","+str(i['label'])+","+str(799)+","+str(168)+","+str(1023)+","+str(443)

                fl.write(datavd)
                fl.write('\n')
                fl.flush()
                fl.close()

                #print(d['imagePath'],d['imageWidth'],d['imageHeight'],i['label'],int(i['points'][0][0]),int(i['points'][0][1]),int(i['points'][1][0]),int(i['points'][1][1]))
