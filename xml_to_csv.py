### xml to csv
import cv2
import os
import pandas as pd
import xml.etree.ElementTree as ET

#import cv2
import numpy as np
#import os
import json
#import pandas as pd
import base64


def xml2csv(xml_path):
    """Convert XML to CSV

    Args:
        xml_path (str): Location of annotated XML file
    Returns:
        pd.DataFrame: converted csv file

    """
    print("xml to csv {}".format(xml_path))
    xml_list = []
    xml_df=pd.DataFrame()
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     float(member[4][0].text),
                     float(member[4][1].text),
                     float(member[4][2].text),
                     float(member[4][3].text)
                     )
            xml_list.append(value)
            column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
            xml_df = pd.DataFrame(xml_list, columns=column_name)
    except Exception as e:
        print('xml conversion failed:{}'.format(e))
        return pd.DataFrame(columns=['filename,width,height','class','xmin','ymin','xmax','ymax'])
    return xml_df

def df2labelme(symbolDict,image_path,image):
    """ convert annotation in CSV format to labelme JSON

    Args:
        symbolDict (dataframe): annotations in dataframe
        image_path (str): path to image
        image (np.ndarray): image read as numpy array

    Returns:
        JSON: converted labelme JSON

    """
    try:
        symbolDict['1']= symbolDict[['xmin','ymin']].values.tolist()
        symbolDict['2']= symbolDict[['xmin','ymax']].values.tolist()
        symbolDict['3']= symbolDict[['xmax','ymax']].values.tolist()
        symbolDict['4']= symbolDict[['xmax','ymin']].values.tolist()
        symbolDict['points']= symbolDict[['1','2','3','4']].values.tolist()
        symbolDict['shape_type']='polygon'
        symbolDict['group_id']=None
        height,width,_=image.shape
        symbolDict['height']=height
        symbolDict['width']=width
        encoded = base64.b64encode(open(image_path, "rb").read())
        symbolDict.loc[:,'imageData'] = encoded
        symbolDict.rename(columns = {'class':'label','filename':'imagePath','height':'imageHeight','width':'imageWidth'},inplace=True)
        converted_json = (symbolDict.groupby(['imagePath','imageWidth','imageHeight','imageData'], as_index=False)
                     .apply(lambda x: x[['label','points','shape_type','group_id']].to_dict('r'))
                     .reset_index()
                     .rename(columns={0:'shapes'})
                     .to_json(orient='records'))
        converted_json = json.loads(converted_json)[0]
    except Exception as e:
        converted_json={}
        print('error in labelme conversion:{}'.format(e))
    return converted_json

folder_path = "/home/user/Documents/essencial_codes/xml_to_json/asta_sample_labelled_images/"
img_list = os.listdir(folder_path)
img_list.sort()
for f in img_list:
    if "xml" in f:
        xml_path = folder_path + f 
        xml_csv=xml2csv(xml_path)
        image_path = folder_path + f[:-4]+".jpg"
        image=cv2.imread(image_path)        
        csv_json=df2labelme(xml_csv,image_path,image)
        json_path = folder_path + f[:-4]+".json"
        with open(json_path, 'w') as f2:
            json.dump(csv_json, f2)
        
        
