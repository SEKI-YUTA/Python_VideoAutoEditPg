import os
from cv2 import imshow, imwrite
from matplotlib.pyplot import text
import numpy as np
import cv2 as cv

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
        if(frameCount > videoFPS * 20):
            imageArr = np.asarray(frame)
            # パスの区切りに//を使わないとエラーが出るものがあったがこれは/でも大丈夫みたい
            cv.imwrite(saveDir + "exportedImage" + str(imageCount) + ".png", imageArr)
            print("saveing image at " + saveDir + "exportedImage" + str(imageCount) + ".png")
            imageCount = imageCount + 1
            frameCount = 0
        else:
            frameCount = frameCount + 1
            print("frameCount: " + str(frameCount))
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