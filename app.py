# -*- coding : UTF-8 -*-
# coding=utf-8
# coding=UTF-8

from PIL import Image
from multiprocessing import Process
import histogram as htg
import requests as req
from io import BytesIO

if __name__ == '__main__':

    # read image files
    # img1 = Image.open('img1.jpg')
    # img2 = Image.open('img2.jpg')
    # img1.show()
    # img2.show()
    ig1 = 'http://qitoujia-dev.oss-cn-hangzhou.aliyuncs.com/alotImgs/1538212037755-poster.jpg'
    ig2 = 'http://qitoujia-dev.oss-cn-hangzhou.aliyuncs.com/alotImgs/1538212037755-poster.jpg'
    response1 = req.get(ig1)
    response2 = req.get(ig2)
    img1 = Image.open(BytesIO(response1.content))
    img2 = Image.open(BytesIO(response2.content))

    # Histogram Similarity Calculation
    # regularize the images
    img1_htg = htg.regularizeImage(img1)
    img2_htg = htg.regularizeImage(img2)

    hg1 = img1_htg.histogram()
    # print(img1.histogram())
    hg2 = img2_htg.histogram()
    # print(img2.histogram())

    # draw the histogram in a no-blocking way
    sub_thread = Process(target=htg.drawHistogram, args=(hg1, hg2,))
    sub_thread.start()

    # print the histogram similarity
    print('依据图片直方图距离计算相似度：{}'.format(htg.calMultipleHistogramSimilarity(img1_htg, img2_htg)))
