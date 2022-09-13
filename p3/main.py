import cv2;
import numpy as np

#图片的加法，溢出要和256余
img1 =np.random.randint(0,256,size=[3,3],dtype=np.uint8);
img2 =np.random.randint(0,256,size=[3,3],dtype=np.uint8);
img3 =img1+img2;
#print("img1=\n",img1);
#print("img2=\n",img2);
#print("img3=\n",img3);


#cv2.add() 超过回取最大值，并且支持数值和图像的重载函数。
a =cv2.imread("./1.jpg");
b =a;
res1 =a+b;
res2=cv2.add(a,b);
#cv2.imshow("res1",res1);
#这个更亮了
#cv2.imshow("res2",res2);
#cv2.imshow("res",a);

#3x4元素值都是100的二维数组
img1 =np.ones((3,4),dtype=np.uint8)*100;
img2 =np.ones((3,4),dtype=np.uint8)*10;

gamma=3;
#img3 =cv2.addWeighted(img2,0.6,img2,5,gamma);
#print(img3);
#结果=imgx0.6+img2x5+3

#水印了
imk2 =cv2.imread("./k2.jpg");
imk3 =cv2.imread("./k3.jpg");
imk4 = cv2.addWeighted(imk2,0.3,imk3,0.7,0);
#cv2.imshow("a",imk4);

#按位与运算，255二进制是8个1
cv2.waitKey();