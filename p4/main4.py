
import cv2;
import numpy as np


#添加alpha通道

img =cv2.imread("./1.jpg");
bgra =cv2.cvtColor(img,cv2.COLOR_BGR2BGRA);
b,g,r,a =cv2.split(bgra);
a[:,:]=10;
bgra125=cv2.merge([b,g,r,a]);
cv2.imshow('a',bgra125);


cv2.waitKey();
cv2.destroyAllWindows();