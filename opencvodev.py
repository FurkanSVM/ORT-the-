import cv2 as cv 
import numpy as np 
vid=cv.VideoCapture("reddetection.mp4")
while True:
    blank = np.zeros((500,500,3), dtype="uint8")
    isTrue, frame=vid.read()
    hsv_frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower_red = np.array([0, 80, 80])
    upper_red = np.array([10, 255, 255])
    mask1 = cv.inRange(hsv_frame, lower_red, upper_red)
    lower_red = np.array([140, 80, 50])
    upper_red = np.array([180, 255, 255])
    mask2 = cv.inRange(hsv_frame, lower_red, upper_red)
    mask = cv.bitwise_or(mask1, mask2)
    red = cv.bitwise_and(frame, frame, mask=mask)
    contours, hierarchies = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        contour = max(contours, key=cv.contourArea)
        ((x, y), radius) = cv.minEnclosingCircle(contour)
    centerx = cv.minEnclosingCircle(contour)[0][0] 
    centery = cv.minEnclosingCircle(contour)[0][1]
    cv.putText(frame,"Distance= {:.2f}".format(((centerx-320)**2+(centery-176)**2)**(1/2)),(0,30),cv.FONT_HERSHEY_PLAIN,1,(255,255,255),1)
    cv.circle(frame,(int(centerx),int(centery)),5,1,3,-1)
    cv.imshow("video",frame)
    if cv.waitKey(1) & 0xFF==ord("d"):
        break
vid.release()
cv.destroyAllWindows()

#320,176