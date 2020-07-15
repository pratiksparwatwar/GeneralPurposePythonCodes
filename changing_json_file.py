import os
import json

image_path = "/home/ubuntu/Documents/Vikram/AstaMRCNNLabelledIMG/AstaAllImages/"

img_list = os.listdir(image_path)
img_list.sort()
for f in img_list:
    if ".json" in str(f):
        with open(image_path + f, 'r') as f1:
            d = json.load(f1)
            for i,j in enumerate(d['shapes']):
                d['shapes'][i]['label'] = d['shapes'][i]['label'].replace("old", "new")
                print(d['shapes'][i]['label'])
        with open(image_path + f, 'w') as f2:
           json.dump(d, f2)
