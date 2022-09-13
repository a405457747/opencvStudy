import cv2;
import numpy as np
from sympy import im;
# 二值化只有黑白
# 灰度图颜色从0-255，越小越黑
# 色彩空间，表述三基色混合成的颜色的模式。比如从视觉角度（色调、饱和度、亮度）
# RGB是三个通道,每个通道范围[0,255]
# OpenCV中是BGR的顺序
# Numpy数组中，image[0,0]表示从左上角开始的几行几列

#创建一个元素值都是0的并且是8*4，数据类型为np.uint8的数组
img =np.zeros((300,150),dtype=np.uint8);
img[0,0]=0;
#print(img[0,2]);
print(img,img.size);

#range函数取不到8
for i in range(3,8):
    #print(i);
    pass

#双range感性的认识宽是59，高是49，左上角是(0,40)
for i in range(0,50):
    for j in range(40,100):
        img[i,j]=255;

cv2.imshow("d",img);
cv2.waitKey();
cv2.destroyAllWindows();


