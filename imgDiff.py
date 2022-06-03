import cv2 as cv
import numpy as np

# 2枚の画像の差分画像を書き出すプログラム

def writeDiffImg(img1, img2):
    if img1.shape == img2.shape:
        img_diff = img1.astype(int) - img2.astype(int)
        img_diff_abs = np.abs(img_diff)
        print(type(img1))
        print(type(img_diff_abs))
        # img_diff_abs_grey = cv.cvtColor(img_diff.asType(np.float32), cv.COLOR_BGR2GRAY)
        print("最大値" + str(img_diff_abs.max()))
        print("最小値" + str(img_diff_abs.min()))
        # print(type(img_diff_abs_grey))
        cv.imwrite("diff_image.png", img_diff_abs)
    
def getDiffImg(img1, img2):
    img_diff_abs = None
    if img1.shape == img2.shape:
        img_diff = img1.astype(int) - img2.astype(int)
        img_diff_abs = np.abs(img_diff)
        print(type(img1))
        print(type(img_diff_abs))
        # img_diff_abs_grey = cv.cvtColor(img_diff.asType(np.float32), cv.COLOR_BGR2GRAY)
        print("最大値" + str(img_diff_abs.max()))
        print("最小値" + str(img_diff_abs.min()))
        # print(type(img_diff_abs_grey))
    return img_diff
# img1 = cv.imread("./assets/assetImg1.png")
# img2 = cv.imread("./assets/assetImg1.png")

# if img1.shape == img2.shape:
#     img_diff = img1.astype(int) - img2.astype(int)
#     img_diff_abs = np.abs(img_diff)
#     print(type(img1))
#     print(type(img_diff_abs))
#     # img_diff_abs_grey = cv.cvtColor(img_diff.asType(np.float32), cv.COLOR_BGR2GRAY)
#     print("最大値" + str(img_diff_abs.max()))
#     print("最小値" + str(img_diff_abs.min()))
#     # print(type(img_diff_abs_grey))
#     cv.imwrite("diff_image.png", img_diff_abs)
    # エラーになる後で調べる
    # cv.imshow("diff_image", img_diff_abs)
# 2枚の画像の差分画像を書き出すプログラムここまで