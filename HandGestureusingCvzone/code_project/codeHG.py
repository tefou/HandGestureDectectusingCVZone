import cv2
from cvzone.HandTrackingModule import HandDetector
import os
import uuid

detection = HandDetector(detectionCon=0.8, maxHands= 2)
video = cv2.VideoCapture(0)

while True:
    ret,frame = video.read()
    hands,img = detection.findHands(frame)
    cv2.rectangle(img,(0,480),(300,425),(50,50,255),-2)
    cv2.rectangle(img,(640,480),(400,425),(50,50,255),-2)
    if hands:
        lmlist = hands[0]
        figerUp= detection.fingersUp(lmlist)
        print(figerUp)
        
        #We hypothesize that finger-based cheating may be occurring in this exam setting, whereby students signal their chosen multiple-choice answer (A, B, C, or D) using their fingers.
        if figerUp==[0,0,0,0,0]:
            cv2.putText(frame,'Frame Count = 0',(20,460),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame, 'Warning', (440, 460), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1,cv2.LINE_AA)
        if figerUp==[0,1,0,0,0] or figerUp==[1,0,0,0,0] or figerUp==[0,0,1,0,0] or figerUp==[0,0,0,1,0] or figerUp==[0,0,0,0,1]:
            cv2.putText(frame,'Frame Count = 1',(20,460),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame, 'Cheating Answer A', (440, 460), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1,cv2.LINE_AA)
        if figerUp==[0,1,1,0,0] or figerUp==[1,1,0,0,0] or figerUp==[0,0,1,1,0] or figerUp==[0,0,0,1,1] or figerUp==[1,0,0,0,1]:
            cv2.putText(frame,'Frame Count = 2',(20,460),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame, 'Cheating Answer B', (440, 460), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1,cv2.LINE_AA)
        if figerUp==[0,1,1,1,0] or figerUp==[1,1,1,0,0] or figerUp==[0,0,1,1,1] or figerUp==[1,1,0,0,1]:
            cv2.putText(frame,'Frame Count = 3',(20,460),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame,'Cheating Answer C',(440,460),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
        if figerUp==[0,1,1,1,1] or figerUp==[1,1,1,1,0] or figerUp==[1,1,1,0,1]or figerUp==[1,1,1,1,0]:
            cv2.putText(frame,'Frame Count = 4',(20,460),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame, 'Cheating Answer D', (440, 460), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1,cv2.LINE_AA)
        if figerUp==[1,1,1,1,1]:
            cv2.putText(frame,'Frame Count = 5',(20,460),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame, 'Cheating Answer E', (440, 460), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1,cv2.LINE_AA)
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    
    if k==ord('q'):
        
        break




video.release()
cv2.destroyAllWindows()
