import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    for xml_file in glob.glob(path + '/*.xml'):
        with open(xml_file, encoding='latin-1') as f:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            for member in root.findall('object'):
                member[0].text = member[0].text.replace("TENSE","Tense")
        tree.write(xml_file, encoding='latin-1')
def main():
    image_path = './xml/'
    xml_df = xml_to_csv(image_path)

main()
