import cv2 as cv
import numpy as np

# 画像の色を判定するプログラム

def detectValue(img):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h = imgHSV.T[0].flatten().mean()
    s = imgHSV.T[1].flatten().mean()
    v = imgHSV.T[2].flatten().mean()
    print(h)
    print(s)
    print(v)
    return v
# https://qiita.com/Zumwalt/items/4d9bc15608483fa77476
# print(img)
# 画像の色を判定するプログラムここまで