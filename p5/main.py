import cv2;
import numpy as np
from sympy import im

#图像变化
img =cv2.imread("./1.jpg");
rows,cols =img.shape[:2]
size =(int(cols*0.9),int(rows*0.5));
rst =cv2.resize(img,size);

rst2=cv2.resize(img,None,fx=2,fy=0.5);
#cv2.imshow("a",rst);
#cv2.imshow("a2",rst2);


#翻转0是绕x翻转
#cv2.imshow("a", cv2.flip(img,0))

#仿射
#平移

img =cv2.imread("./1.jpg");
height,width =img.shape[:2];
x=100
y=200
M =np.float32([[1,0,x],[0,1,y]])
move =cv2.warpAffine(img,M,(width,hasattr))

cv2.imshow("move",move);
cv2.waitKey();
cv2.destroyAllWindows();