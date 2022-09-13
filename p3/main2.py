import cv2;
import numpy as np

#利用按位与，掩膜图片
a=np.random.randint(0,255,(5,5),dtype=np.uint8);
b =np.zeros((5,5),dtype=np.uint8);
b[0:3,0:3]=255;
b[4,4]=255;
c =cv2.bitwise_and(a,b);
print("a=\n",a);
print("b=\n",b);
print("c=\n",c);
#彩色图片需要掩膜则需要转换成彩色图像。

im1 =cv2.imread("./1.jpg");
im2 =cv2.bitwise_not(im1);
#鬼图
#cv2.imshow("a",im2)

#3.4掩模
#如果有掩模，操作只会在淹模值为非空的像素点上执行，并将其他像素点置为0
# res=cv2.add(arg1,arg2,掩模)

#任何数值与自身进行按位与计算的结果，得到的仍是自身的值




cv2.waitKey();