# import cv2
# import warnings
# warnings.filterwarnings("ignore")

# face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")

# first_read = True
# cap = cv2.VideoCapture(0)
# while True:
#     _,img=cap.read()

#     grays=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     gray = cv2.bilateralFilter(grays, 5, 1, 1)
#     faces= face_cascade.detectMultiScale(gray,1.05,11)

#     if len(faces) > 0:
#         for(x,y,w,h) in faces:
#             cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0), 2)
#             cv2.putText(img, "Face", (x,y-5), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,255), 1)
#             imgGreyFace= gray[y:(y+h),x:(x+w)]
#             imgColorFace= img[y:(y+h),x:(x+w)]
        
#             eyes= eye_cascade.detectMultiScale(imgGreyFace,2.6,10)
#             if len(eyes) >= 2:
#                 for(x_eye,y_eye,w_eye,h_eye) in eyes:
#                     cv2.rectangle(imgColorFace,(x_eye,y_eye), (x_eye+w_eye,y_eye+h_eye), (0,0,255), 3)
#                     if first_read:
#                         cv2.putText(img, "Eye's detected", (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
#                                 1, (0, 255, 0), 2)
#             else:
#                 if first_read:
#                     cv2.putText(img, "No Eye's detected", (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
#                                 1, (255, 255, 255), 2)
#                 else:
#                     cv2.putText(img, "Blink Detected.....!!!!", (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
#                                 1, (0, 255, 0), 2)   
#                     cv2.imshow('image',img)
#                     cv2.waitKey(1)
#                     print("Blink Detected.....!!!!")
   
       
#         cv2.imshow("Output",img)
#     a = cv2.waitKey(1)
#     if a == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()


