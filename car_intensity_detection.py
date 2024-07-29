import cv2

import imutils  #To Resize


cascade_src = 'cars.xml'

car_cascade = cv2.CascadeClassifier(cascade_src) #Loading XML file

cam=cv2.VideoCapture(0)  #Initializing Camera id

while True:

    _,img=cam.read()   #Reading frame from camera
    
    img=imutils.resize(img,width=1000)  #Resizing the frame
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Converting bgr to gray
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)  #Getting Coordinates
    
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) #drawing a rectangle
        
    cv2.imshow("Frame", img)   #Display the frame
    
    b=str(len(cars))
    a= int(b)
    n=a
    print("------------------------------------------------")
    print ("North: %d "%(n))
    if n>=8:
        print ("North More Traffic, Please on the GREEN Signal")
    else:
        print ("no traffic")
    if cv2.waitKey(33) == 27:
        break

cam.release()
cv2.destroyAllWindows()
