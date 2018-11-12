# coding=utf-8


from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
import math
import requests as req
from io import BytesIO

# 正则化图像
def regularizeImage(img, size = (9, 8)):
    return img.resize(size).convert('L')

# 计算hash值
def getHashCode(img, size = (9, 8)):

    result = []
    for i in range(size[0] - 1):
        for j in range(size[1]):
            current_val = img.getpixel((i, j))
            next_val = img.getpixel((i + 1, j))
            if current_val > next_val:
                result.append(1)
            else:
                result.append(0)

    return result

# 比较hash值
def compHashCode(hc1, hc2):
    cnt = 0
    for i, j in zip(hc1, hc2):
        if i == j:
            cnt += 1
    print('cnt======',cnt)
    return cnt

# 计算差异哈希算法相似度
def caldHashSimilarity(img1, img2):
    img1 = regularizeImage(img1)
    img2 = regularizeImage(img2)
    hc1 = getHashCode(img1)
    hc2 = getHashCode(img2)
    return compHashCode(hc1, hc2)

def main():
    # im1=io.imread('http://jihepai-pro.oss-cn-hangzhou.aliyuncs.com/static/img/ac-main-default.jpg')
    # print(im1)
    img1 = 'http://s15.sinaimg.cn/mw690/0002LEyMzy6LSizlI5M5e&690'
    img2 = 'https://img-blog.csdn.net/20140311015106328?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbGl5Z2NoZW5n/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center'
    response1 = req.get(img1)
    response2 = req.get(img2)
    image1 = Image.open(BytesIO(response1.content))
    image2 = Image.open(BytesIO(response2.content))

    caldHashSimilarity(image1, image2)
    # image1 = io.imread(img1)
    # image2 = io.imread(img2)
    # pic1 = stringToHash('1.jpg')
    # pic2 = stringToHash('2.jpg')
    # print("this two picture is " + str((8 * 8 - calculateHammingDistance(pic1,pic2)) / (8 * 8) * 100) + "% similarity")
if __name__ == "__main__":
    main()
