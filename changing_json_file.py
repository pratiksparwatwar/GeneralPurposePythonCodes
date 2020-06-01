import os
import json

image_path = "/home/user/Documents/Project/Bajaj_Engine_Project_UI/On_site_data/videos/images/K1BS6_IP/train/k1ip_lot4_labelled/"

img_list = os.listdir(image_path)
img_list.sort()
for f in img_list:
    if ".json" in str(f):
        with open(image_path + f, 'r') as f1:
            d = json.load(f1)
            #print(d.keys())
            for i,j in enumerate(d):
                if i < 4:
                    d['shapes'][i]['label'] = d['shapes'][i]['label'].replace("KIBS6", "K1BS6")
                    print(d['shapes'][i]['label'])        
                else:
                    continue
        with open(image_path + f, 'w') as f2:
            json.dump(d, f2)
