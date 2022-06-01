import os
from cv2 import imshow, imwrite
import numpy as np
import cv2 as cv

def main():
    imageCount = 0
    frameCount = 0
    saveDir = "C:/Users/yuta/Desktop/autoEditpg/exported/"

    # 保存先のディレクトリが存在しなければ作成
    # この処理をしないとimwriteでエラーが出ないのに保存されないという状態になる
    if not os.path.exists(saveDir):
        os.mkdir(saveDir)

    cap = cv.VideoCapture('./video_test.mp4')
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
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
        if(frameCount > 300):
            imageArr = np.asarray(frame)
            # パスの区切りに//を使わないとエラーが出るものがあったがこれは/でも大丈夫みたい
            cv.imwrite(saveDir + "exportedImage" + str(imageCount) + ".png", imageArr)
            print("saveing image at " + saveDir + "exportedImage" + str(imageCount) + ".png")
            imshow("frame", frame)
            imageCount = imageCount + 1
            frameCount = 0
        else:
            frameCount = frameCount + 1
            print("frameCount: " + str(frameCount))
        if cv.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()
    
    
if(__name__ == "__main__"):
    main()