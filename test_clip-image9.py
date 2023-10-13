# -*- coding: utf-8 -*-
'''
将一张图片填充为正方形后切为9张图
Author:
'''
import os

from PIL import Image
import sys


# 将图片填充为正方形
def fill_image(image):
    image = Image.open(image)
    width, height = image.size
    # 选取长和宽中较大值作为新图片的
    new_image_length = width if width > height else height
    # 生成新图片[白底]
    new_image = Image.new(image.mode, (new_image_length, new_image_length), color='white')
    # 将之前的图粘贴在新图上，居中
    if width > height:  # 原图宽大于高，则填充图片的竖直维度
        # (x,y)二元组表示粘贴上图相对下图的起始位置
        new_image.paste(image, (0, int((new_image_length - height) / 2)))
    else:
        new_image.paste(image, (int((new_image_length - width) / 2), 0))

    width, height = new_image.size
    item_width = int(width / 3)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0, 3):  # 两重循环，生成9张图片基于原图的位置
        for j in range(0, 3):
            # print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
            box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
            box_list.append(box)

    image_list = [new_image.crop(box) for box in box_list]

    index = 1
    for image in image_list:
        image.save('./output/' + str(index) + '.png', 'PNG')
        index += 1




#image.show()
def test_clip_image():
    file_path = "img/P0023_824_1848_824_1848.png"
    fill_image(file_path)
    imgs = len(os.listdir("./output"))
    assert imgs == 9

