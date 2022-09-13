
import cv2;
import numpy as np



img =cv2.imread("./aa4.jpg");
hsv =cv2.cvtColor(img,cv2.COLOR_BGR2HSV);
h,s,v =cv2.split(hsv);
v[:,:]=255;
newHsv =cv2.merge([h,s,v]);
art =cv2.cvtColor(newHsv,cv2.COLOR_HSV2BGR);

cv2.imshow("art",art);
cv2.imshow("newHsv",newHsv);



cv2.waitKey();
cv2.destroyAllWindows();