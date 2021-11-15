import sys
import cv2
import voiceRecognition 
import face_recognition
import cvzone
import os
import numpy as np


path = 'imagesFaces'
images = []
classNames = []
myList = os.listdir(path)


for cl in myList:
    curImg = cv2.imread('{}/{}'.format(path,cl))
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

def metricsFaces(images):
    metricsF_list = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        metrics = face_recognition.face_encodings(img)
        metricsF_list.append(metrics)

    return metricsF_list

metricsListknown = metricsFaces(images)

while True:
    word = str(voiceRecognition.voiceDetec())
    if word == 'close':
        sys.exit('program close by user!!')
        
    elif word == 'activate':

        cap = cv2.VideoCapture(0)
        detector = cvzone.HandDetector(maxHands=1, detectionCon=0.7)
        mySerial = cvzone.SerialObject('COM4', 9600, 1)
        
        while True:
             success, img = cap.read()
             k=cv2.waitKey(1)
             

             if k%256==32:
                cv2.destroyWindow('tes')
                img2 = cv2.imread('imagesDefault/listen2.png',1)
                cv2.imshow('say something',img2)
                cv2.waitKey(1)
                word = voiceRecognition.voiceDetec()

                if word == 'close':
                    sys.exit('close by user!!')

                
                if word == 'my hand':
                    print('working')
                    print(metricsListknown)
                    print(len(metricsListknown))
                    cv2.destroyWindow('say something')
                    while True:
                        ret, img3 = cap.read()
                        #k=cv2.waitKey(1)
                        #cv2.imshow('recognition',img3)
                        #print('logre')
                        imgS = cv2.resize(img3,(0,0),None,0.25,0.25)
                        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

                        facesCurTime = face_recognition.face_locations(imgS)[0]
                        metricsCurTime = face_recognition.face_encodings(imgS)[0]

                        #for metricFace, faceLoc in zip(metricsCurTime, facesCurTime):
                        matches = face_recognition.compare_faces([metricsListknown], metricsCurTime)
                        #faceDis = face_recognition.face_distance(metricsListknown, metricFace)
                            #matchIndex = np.argmin(faceDis)

                        if matches:
                            name = classNames[0].upper()
                            y1,x2,y2,x1 = facesCurTime
                            y1,x1,y2,x2 = y1*4,x1*4,y2*4,x2*4
                            cv2.rectangle(img3, (x1,y1),(x2,y2),(0,255,0),2)
                            cv2.rectangle(img3,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                            cv2.putText(img3,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                            img3 = detector.findHands(img3)
                            lmList, bbox = detector.findPosition(img3)
                            
                            if lmList:
                                fingers = detector.fingersUp()
                                print(fingers)
                                mySerial.sendData(fingers)
                            

                        else:
                            cv2.destroyWindow('recognition')
                            denegadoImg = cv2.imread('imagesDefault/denegado.png',1)
                            cv2.imshow('ACCESO DENEGADO', denegadoImg)
                            cv2.waitKey(2500)
                            break
                       
                        k = cv2.waitKey(1)     
                        if k%256==32:
                                   cv2.destroyWindow('recognition')
                                   cv2.imshow('say something',img2)
                                   cv2.waitKey(1)
                                   word = voiceRecognition.voiceDetec()

                                   if word == 'close':
                                       cv2.destroyWindow('say something')
                                       closeImg = cv2.imread('imagesDefault/close3.jpg',1)
                                       cv2.imshow('close program',closeImg)
                                       cv2.waitKey(2500)
                                       sys.exit(1)
                                       


                        cv2.imshow('recognition',img3)
                      

                    '''       
                    cv2.destroyWindow('say something')
                   
                    print(len(metricsListknown)
                    ''' 
             cv2.imshow('tes',img)
             
