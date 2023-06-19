import cv2
import numpy as np
import time
import PoseModule as pm


#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("PoseVideos/v7.mp4")
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
color = (225, 0 ,225)
bar = 0
per = 0

while True:
    success, img = cap.read()
    #success, src = cap.read()
    #img = cv2.flip(src, 180)
    img = cv2.resize(img, (720, 720))
    # img = cv2.imread("PoseImage/jumping_Jacks.jpg")
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        # Right Arm
        rArmAngle = detector.findAngle(img, 12, 14, 16)
        # Left Arm
        lArmAngle = detector.findAngle(img, 11, 13, 15)
        # Right Leg
        rLegAngle = detector.findAngle(img, 28, 24, 23)
        # Left Leg
        lLegAngle = detector.findAngle(img, 24, 23, 27)
        
        raper = np.interp(rArmAngle,(195, 220), (0, 100))
        laper = np.interp(lArmAngle,(125, 165), (100, 0))
        rlper = np.interp(rLegAngle,(250, 270), (100, 0))
        llper = np.interp(lLegAngle,(250, 270), (100, 0))
        per = (raper + laper + rlper + llper) / 4
        print(rArmAngle, raper)
        #print(raper)

        rabar = np.interp(rArmAngle,(195, 220), (630, 50))
        labar = np.interp(lArmAngle,(125, 165), (50, 630))
        rlbar = np.interp(rLegAngle,(250, 270), (50, 630))
        llbar = np.interp(rLegAngle,(250, 270), (50, 630))
        bar = (rabar + labar + rlbar + llbar) / 4
        #print(bar)

        # check jumping jacks
        color = (255, 0 ,255)
        if raper == laper == rlper == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if raper == laper == rlper == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0

    #print(count)

    # Bar x+75
    cv2.rectangle(img, (630, 50), (705, 630), color, 3)
    cv2.rectangle(img, (630, int(bar)), (705, 630), color, cv2.FILLED)
    #print(bar)
    cv2.putText(img, f'{int(per)} %', (500, 75), cv2.FONT_HERSHEY_PLAIN, 4, color, 4)

    #cv2.rectangle(img, (0,450), (250, 720), (0, 255, 0), cv2.FILLED)
    #cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15, (255, 0, 0), 25)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(count), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)



    cv2.imshow("Image", img)
    cv2.waitKey(1)
