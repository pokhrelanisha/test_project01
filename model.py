import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
import cvzone

cap = cv2.VideoCapture('girl.mp4')
detector = FaceMeshDetector(maxFaces=1)
plotY = LivePlot(640,360,[20,50],invert=True)


idlist = [22 ,23, 24,26, 110, 157, 158,159,160,161,130,243]
ratiolist = []
blinkCounter = 0
counter = 0
color = (255,0,255)


while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)

    sucess, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw= False)

    if faces: 
        face = faces[0]
        for id in idlist:
            cv2.circle(img, face[id],5, color,cv2.FILLED )

        leftUp = face[159]
        leftDown = face[23]
        leftleft = face[130]
        leftright = face[243]
        lenghtVer,_ = detector.findDistance(leftUp,leftDown)
        lenghtHor,_ = detector.findDistance(leftleft,leftright)

        cv2.line(img,leftUp,leftDown,(0,255,0),3)
        cv2.line(img,leftleft,leftright,(0,255,0),3)

        ratio = int((lenghtVer/lenghtHor)*100)
        ratiolist.append(ratio)
        if len(ratiolist)>2:
            ratiolist.pop(0)
        ratioAvg = sum(ratiolist)/len(ratiolist)

        if ratioAvg <35 and counter ==0 :
            blinkCounter +=1
            color = (0,200,0)
            counter = 1 
        if counter != 0:
            counter += 1
            if counter >10:
                counter = 0
                color = (255,0,255)

        cvzone.putTextRect(img,f'Blink Count:{blinkCounter}',(50,100), colorR=color)

        imgPlot =plotY.update(ratioAvg,color)
        img = cv2.resize(img, (640,360))
        imgStack = cvzone.stackImages([img,imgPlot],2,1)
    else:
        img = cv2.resize(img, (640,360))
        imgStack = cvzone.stackImages([img,img],2,1)

    
    cv2.imshow('Image',imgStack)
    cv2.waitKey(25)