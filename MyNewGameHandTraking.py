import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
captura = cv2.VideoCapture(0)
detector = htm.handDetector(4)

while True:
    sucesso, img = captura.read()
    img = detector.findHands(img,  draw=False)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(10)