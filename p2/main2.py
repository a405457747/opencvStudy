import cv2;
import numpy as np

#img =cv2.imread("./a1.jpg");

#打印全部显示
np.set_printoptions(threshold=np.inf)
#print(img);

#cv2.imshow("d",img);

#蓝色通道
blue=np.zeros((300,300,3),dtype=np.uint8);
blue[:,:,0]=255;
#cv2.imshow("blue",blue);

#绿色通道
green=np.zeros((300,300,3),dtype=np.uint8);
green[:,:,1]=255;
#cv2.imshow("green",green);

#切片操作https://www.cnblogs.com/Sinte-Beuve/p/6573246.html

cv2.waitKey();
cv2.destroyAllWindows();


