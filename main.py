import os
from traceback import print_tb
from cv2 import imshow, imwrite
from matplotlib.pyplot import text
import numpy as np
import cv2 as cv
import imgDiff
import detectColor


def main():
    imageCount = 0
    frameCount = 0
    saveDir = "C:/Users/yuta/Desktop/autoEditpg/exported/"
    videoFPS = 30

    # 保存先のディレクトリが存在しなければ作成
    # この処理をしないとimwriteでエラーが出ないのに保存されないという状態になる
    if not os.path.exists(saveDir):
        os.mkdir(saveDir)

    cap = cv.VideoCapture('./video_test.mp4')
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    
    videoFPS = cap.get(cv.CAP_PROP_FPS)
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Display the resulting frame
        # cv.imshow('frame', gray)
        
        # 20秒ごとに写真を保存するかどうかを判定する
        if(frameCount > videoFPS * 10):
            imageArr = np.asarray(frame)
            if imageCount == 0:
                print("first image")
                # パスの区切りに//を使わないとエラーが出るものがあったがこれは/でも大丈夫みたい
                cv.imwrite(saveDir + "exportedImage" + str(imageCount) + ".png", imageArr)
                print("saveing image at " + saveDir + "exportedImage" + str(imageCount) + ".png")
                imageCount = imageCount + 1
            else:
                print("second image")
                baseImg = cv.imread(saveDir + "exportedImage" + str(imageCount - 1) + ".png", cv.IMREAD_COLOR)
                print(saveDir + "exportedImage" + str(imageCount) + ".png")
                # diffImg = imgDiff.getDiffImg(baseImg, baseImg)
                imgDiff.writeDiffImg(baseImg, frame)
                diffImg = cv.imread("./diff_image.png")
                if type(diffImg) == None:
                    print("diffImg is None")
                value = detectColor.detectValue(diffImg)
                print("value: {}".format(value))
                if value > 40:
                    cv.imwrite(saveDir + "exportedImage" + str(imageCount) + ".png", imageArr)
                    imageCount = imageCount + 1
            frameCount = 0
        else:
            frameCount = frameCount + 1
            # print("frameCount: " + str(frameCount))
        putFPSText(frame=frame, text="FPS" + str(videoFPS))
        imshow("frame", frame )
        if cv.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()
    
    
def putFPSText(frame, text):
    cv.putText(frame, text,(10,20), cv.FONT_HERSHEY_PLAIN, 1, (255,0,0), 2, cv.LINE_4)
    
if(__name__ == "__main__"):
    main()