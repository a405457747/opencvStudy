import cv2;
import numpy as np

#
img =cv2.imread("./1.jpg");
#通道拆分
bim =img[:,:,0];
gim=img[:,:,1];
rim=img[:,:,2];

print(bim);
#img[:,:,2]=0;
#cv2.imshow("b",img);
#cv2.imshow("g",gim);
#cv2.imshow("r",rim);

#拆分通道
b,g,r=cv2.split(img);
#cv2.imshow("b",b);
#cv2.imshow("g",g);
#cv2.imshow("r",r);

#通道合并
im2 =cv2.merge([g,b,r])
#cv2.imshow("d",im2);
#cv2.imshow("d2",img);

#返回行数和列数和维度
print(im2.shape)
#size返回行*列*通道数
print(im2.size);
#数据类型
print(im2.dtype);
cv2.waitKey();