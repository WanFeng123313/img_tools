from PIL import Image

img = Image.open('E:\gxy\code-gxy\P0023_824_1848_824_1848_instance_color_RGB.png')

# 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
Img = img.convert('L')
Img.save("test1.jpg")

# 自定义灰度界限，大于这个值为白色，小于这个值为黑色
threshold = 100

table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

# 图片二值化
photo = Img.point(table, '1')
photo.save("test2.jpg")