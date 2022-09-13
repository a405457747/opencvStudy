
import cv2;
import numpy as np


img =np.random.randint(0,256,size=[5,5],dtype=np.uint8);

min =100;
max=200;
mask =cv2.inRange(img,min,max);
#print("img=\n",img);
#print("mask=\n",mask);

img =np.ones([5,5],dtype=np.uint8)*9;
mask =np.zeros([5,5],dtype=np.uint8);
mask[0:3,0]=1;
mask[2:5,2:4]=1;
roi=cv2.bitwise_and(img,img,mask=mask);
#print("img=\n",img);
#print("mask=\n",mask);
#print("roi=\n",roi);

#ps的提取颜色教程。hsv色调取范围+-10，s和v取[100,255]，否则色调都变了

opencv =cv2.imread("./aa4.jpg");
hsv =cv2.cvtColor(opencv,cv2.COLOR_BGR2HSV);
cv2.imshow("opencv",opencv);

#蓝色
minBlue =np.array([110,50,50]);
maxBlue =np.array([130,255,255]);

#确定蓝色区域
mask =cv2.inRange(hsv,minBlue,maxBlue);
#锁定蓝色区域
blue =cv2.bitwise_and(opencv,opencv,mask=mask);
cv2.imshow("blue",blue);

cv2.waitKey();
cv2.destroyAllWindows();