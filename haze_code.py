import cv2, math
import os
import numpy as np
import random
myPath = 'test_fog/'
outPath = 'haze/'
def processImage(filesource, destsource, name, imgtype):
    imgtype = 'jpeg' if imgtype == '.jpg' else 'png'
    img = cv2.imread(name)
    img_f = img / 255.0
    (row, col, chs) = img.shape
    A = 0.6
    beta = 0.03
    size = 40
    center = (row // 2, col // 2)
    for j in range(row):
        for l in range(col):
            d = -0.04 * math.sqrt((j - center[0]) ** 2 + (l - center[1]) ** 2) + size
            td = math.exp(-beta * d)
            img_f[j][l][:] = img_f[j][l][:] * td + A * (1 - td)
    cv2.imwrite(name, img_f*255) 
def run():
    os.chdir(myPath)
    for i in os.listdir(os.getcwd()):
        postfix = os.path.splitext(i)[1]
        print(postfix, i)
        if postfix == '.jpg' or postfix == '.png':
            processImage(myPath, outPath, i, postfix)
if __name__ == '__main__':
    run()
