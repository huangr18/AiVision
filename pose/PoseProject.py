import cv2
import time
import PoseModule as pm


cap = cv2.VideoCapture('PoseVideos/v1.mp4')
#cap = cv2.VideoCapture(0)
pTime = 0
detector = pm.poseDetector()
while True:
    sucess, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw = False)
    if len(lmList) != 0:
        print(lmList[14])
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 5, (255, 100, 20), cv2.FILLED)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 100), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)