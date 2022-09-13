import cv2;
import numpy as np


# 颜色空间的转换


img =np.random.randint(0,256,size=[2,4,3],dtype=np.uint8);
rst =cv2.cvtColor(img,cv2.COLOR_HSV2BGR);
#print("img=\n",img);
#print("rst=\n",rst);

im1=cv2.imread("./1.jpg");
rgb =cv2.cvtColor(im1,cv2.COLOR_BGR2RGB);
#cv2.imshow('a',rgb);

#hsv重点研究

#灰度颜色指RGB成分相等，饱和度为0
#作为灰度图像显示时，较亮区域对应的颜色具有较高的饱和度。
#如果颜色饱和度低，那么所得色调不可靠

imgRed=np.zeros([1,1,3],dtype=np.uint8);
imgRed[0,0,2]=255;
Red =imgRed;
RedHsv =cv2.cvtColor(Red,cv2.COLOR_BGR2HSV);
#print("red=\n",Red);
#print("redhsv=\n",RedHsv);


#inRange函数锁定特定值
# 判断图像内像素点的像素值是否在指定的范围内
# dst返回大小和src一致，如过在区间内，dst对应值255，否则是0



cv2.waitKey();
cv2.destroyAllWindows();