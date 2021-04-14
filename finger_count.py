import cv2
import numpy as np
import math

cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    roi=frame[50:250,50:250]
    cv2.rectangle(frame,(50,50),(250,250),(0,255,0),2)
    blur=cv2.GaussianBlur(roi,(3,3),0)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    lb=np.array([0,20,50])
    ub=np.array([25,255,255])
    mask=cv2.inRange(hsv,lb,ub)
    kernel=np.ones((5,5))
    dilate=cv2.dilate(mask,kernel,iterations=3)
    erosion=cv2.erode(dilate,kernel,iterations=2)
    filteration=cv2.GaussianBlur(erosion,(3,3),0)
    ret,thresh=cv2.threshold(filteration,127,255,cv2.THRESH_BINARY)
    contours,hierarchy= cv2.findContours(filteration,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    try:
        cnt = max(contours, key = lambda x: cv2.contourArea(x))
        if len(cnt)==0:
            cnt = max(contours, key = lambda x: cv2.contourArea(x))
        epsilon = 0.0005*cv2.arcLength(cnt,True)
        approx= cv2.approxPolyDP(cnt,epsilon,True)
        hull = cv2.convexHull(cnt)
            
        #define area of hull and area of hand
        areahull = cv2.contourArea(hull)
        areacnt = cv2.contourArea(cnt)
        
        #find the percentage of area not covered by hand in convex hull
        arearatio=((areahull-areacnt)/areacnt)*100
        
        #find the defects in convex hull with respect to hand
        hull = cv2.convexHull(approx, returnPoints=False)
        defects = cv2.convexityDefects(approx, hull)

        l=0
            
        #code for finding no. of defects due to fingers
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])
            pt= (100,180)
            
            
            # find length of all sides of triangle
            a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
            s = (a+b+c)/2
            ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
            
            #distance between point and convex hull
            d=(2*ar)/a
            
            # apply cosine rule here
            angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
            
        
            # ignore angles > 90 and ignore points very close to convex hull(they generally come due to noise)
            if angle <= 90 and d>30:
                l += 1
                cv2.circle(roi, far, 3, [255,0,0], -1)
            
            #draw lines around hand
            cv2.line(roi,start, end, [0,255,0], 2)
            
            
        l+=1
        
        #print corresponding gestures which are in their ranges
        font = cv2.FONT_HERSHEY_SIMPLEX
        if l==1:
            if areacnt<2000:
                cv2.putText(frame,'Put hand in the box',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            else:
                if arearatio<12:
                    cv2.putText(frame,'0',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                #elif arearatio<17.5:
                    #cv2.putText(frame,'Best of luck',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                    
                else:
                    cv2.putText(frame,'1',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                    
        elif l==2:
            cv2.putText(frame,'2',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        elif l==3:
            
                #if arearatio<27:
            cv2.putText(frame,'3',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                #else:
                # cv2.putText(frame,'ok',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                    
        elif l==4:
            cv2.putText(frame,'4',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        elif l==5:
            cv2.putText(frame,'5',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        elif l==6:
            cv2.putText(frame,'reposition',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        else :
            cv2.putText(frame,'reposition',(10,50), font, 2, (0,0,255), 3, cv2.LINE_AA)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        k=cv2.waitKey(1)
        if k==27:
            break
    except:
        pass

cap.release()
cv2.destroyAllWindows()