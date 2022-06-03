import sys
import cv2 as cv
import numpy as np

# 画像表示プログラム
# img = cv.imread("C://Users//yuta//Desktop//autoEditpg//test.jpg")

# if img is None:
#     sys.exit()
    
# cv.imshow("image", img)
# k = cv.waitKey(0)
# 画像表示プログラムここまで


# webカメラのフレームレートを取得するプログラム
# cap = cv.VideoCapture(0)
# print(cap.get(cv.CAP_PROP_FPS))
# while cap.isOpened():
#     ret, frame = cap.read()
#     imshow("frame", frame)
    
#     if(cv.waitKey(1) == ord("q")):
#         break
    
# cap.release()
# cv.destroyAllWindows()
# webカメラのフレームレートを取得するプログラムここまで


# 動画ファイルのフレームレートを取得するプログラム
# cap = cv.VideoCapture("./video_test.mp4")
# print(cap.get(cv.CAP_PROP_FPS))

# while cap.isOpened():
#     ret, frame = cap.read()
#     imshow("frame", frame)
#     if(cv.waitKey(1) == ord("q")):
#         break
    
# cap.release()
# cv.destroyAllWindows()
# 動画ファイルのフレームレートを取得するプログラムここまで


# 画像を横に並べて表示させるプログラム
# img1 = cv.imread("./assets/assetImg1.png")
# img2 = cv.imread("./assets/assetImg2.png")

# mergedImg = np.hstack((img1, img2))
# print(type(mergedImg))
# print(type(img1))
# cv.imshow("img", mergedImg)
# cv.waitKey(0)
# cv.destroyAllWindows()
# 画像を横に並べて表示させるプログラムここまで


# 画像を完全一致か判定するプログラム
# img1 = cv.imread("./assets/assetImg1.png")
# img2 = cv.imread("./assets/assetImg2.png")

# print("画像が一致しています" if np.array_equal(img1, img2) else "画像が一致しません")
# 画像を完全一致か判定するプログラムここまで

# # 2枚の画像の差分画像を書き出すプログラム
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
#     # cv.imshow("diff_image", img_diff_abs)
# # 2枚の画像の差分画像を書き出すプログラムここまで


# 画像の色を判定するプログラム
# img = cv.imread("./diff_image.png")
# imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# h = img.T[0].flatten().mean()
# s = img.T[1].flatten().mean()
# v = img.T[2].flatten().mean()
# print(h)
# print(s)
# print(v)
# https://qiita.com/Zumwalt/items/4d9bc15608483fa77476
# print(img)
# 画像の色を判定するプログラムここまで


img = cv.imread("C:\\Users\\yuta\\Desktop\\autoEditpg\\exported\\exportedImage0.png")
cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()