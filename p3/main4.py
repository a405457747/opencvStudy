import cv2;
import numpy as np

#3.5图像和数值的运算
#像这种加法，指的是所有都加起来。
np.set_printoptions(threshold=np.inf)
img1 =np.ones((4,4),dtype=np.uint8)+9;
img2 =cv2.add(img1,3);
#print("img2=\n",img2);
#3.6位平面分解
#建立二进制矩阵，按位与运算提取第n个位平面。位平面的思想就是二进制数越靠前比重越大，越和原图相似
lena =cv2.imread("./aa5.jpg",0);
#print(lena);
cv2.imshow("lena",lena);
r,c =lena.shape;
#这里8表示长度
x=np.zeros((r,c,8),dtype=np.uint8);

for i in range(8):
    x[:,:,i]=2**i;
#print(x);

r=np.zeros((r,c,8),dtype=np.uint8);
for i in range(8):
    tmp =cv2.bitwise_and(lena,x[:,:,i])

    r[:,:,i]=tmp;

    #如果大于0就弄成白点
    #这个会生成二维的逻辑矩阵
    mask =r[:,:,i]>0;



    if(i==0):
        print("temp\n",tmp);
        print("before R \n",r);
    #这样给三维矩阵的直接复制
    r[mask]=255;

    if(i==0):
        print("changed R \n",r);
        print("mask \n",mask);


    #cv2.imshow(str(i),r[:,:,i]);


x2=np.zeros((4,4,8),dtype=np.uint8);
#利用异或加密和解密

cv2.waitKey(0);
cv2.destroyAllWindows();