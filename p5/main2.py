from turtle import shape
import cv2
from cv2 import rotate;
import numpy as np
from sympy import im

#图像旋转矩阵
img =cv2.imread("./1.jpg");
h,w =img.shape[:2]
M =cv2.getRotationMatrix2D((w/2,h/2),45,0.6);
rotate =cv2.warpAffine(img,M,(w,h));

print("rotate",rotate);


cv2.waitKey();
cv2.destroyAllWindows();