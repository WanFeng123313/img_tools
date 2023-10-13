import os
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
from lxml.etree import Element, SubElement, tostring, ElementTree

import xml.etree.ElementTree as ET
import pickle
import os
import numpy as np
import cv2
import csv
from tqdm import tqdm
# classes = ["0", "1", "2", "3"]  # 类别

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def convert_annotation(xmls_path, csv_path, xml_name,number):
    xml_path = os.path.join(xmls_path, xml_name)
    in_file = open(xml_path, encoding="UTF-8")


    # in_file = open('./label_xml\%s.xml' % (image_id), encoding='UTF-8')
    #
    # out_file = open('./label_txt\%s.txt' % (image_id), 'w')  # 生成txt格式文件
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)
    if width == 0 or height == 0:
        print("%s文件中width和height为0" % xml_name)
    for objnumber, obj in enumerate(root.iter('object')):
        cls = obj.find('name').text
        # print(cls)
        # if cls not in classes:
        #     continue
        # cls_id = classes.index(cls)
        cls_id = 0
        xmlbox = obj.find('bndbox')
        b = ((int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text)),
             (int(xmlbox.find('xmax').text),int(xmlbox.find('ymax').text))
             )
        poly = (np.array(b))
        # # 四点坐标归一化
        # poly[:, 0] = poly[:, 0] / width
        # poly[:, 1] = poly[:, 1] / height

        xmin = b[0][0]
        ymin = b[0][1]

        w = b[1][0] - b[0][0]
        h = b[1][1] - b[0][1]
        img_name = xml_name.replace("xml", "jpg")
        with open(csv_path, 'a', encoding="UTF-8",newline="") as out_file:
            writer = csv.writer(out_file)
            if number == 0 and objnumber == 0:
                writer.writerow(
                    ['label_name', 'bbox_x', 'bbox_y', 'bbox_width', 'bbox_height', 'image_name', 'image_width',
                     'image_height'])
            writer.writerow([cls, xmin, ymin, w, h, img_name, width, height])
            # out_file.write('%s %s %s %s %s %s\n' % (cls_id, c_x, c_y, w, h, the))


# xml_path = os.path.join(CURRENT_DIR, './label_xml/')
def test_convert():
    xmls_path = r"E:\code-dmx\data\MAR20\dino\Annotations_dino"
    csv_path = r"E:\code-dmx\data\MAR20\dino\annotation.csv"

    # xml list
    img_xmls = os.listdir(xmls_path)

    for number, img_xml in tqdm(enumerate(img_xmls)):
        #label_name = img_xml.split('.')[0]
        #print(label_name)
        convert_annotation(xmls_path, csv_path, img_xml, number)
    assert os.path.exists(csv_path)


