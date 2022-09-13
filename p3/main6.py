import cv2;
import numpy as np

#数字水印
#原理在最低有效位信息替换
#步骤先与运算，再或运算

lena =cv2.imread("./1.jpg",0);
#水印图片
watermark =cv2.imread("./water1.jpg",0);
#将水印图片内的255处理为1，方便嵌入
w=watermark[:,:]>0
watermark[w]=1;
r,c =lena.shape
#生成元素值都是254的数组
t254=np.ones((r,c),dtype=np.uint8)*254;
#获取lena高七位
lenaH7 =cv2.bitwise_and(lena,t254);
#将watermark嵌入lenaH7内
e=cv2.bitwise_or(lenaH7,watermark);
#生成元素值都是1的数组
t1 =np.ones((r,c),dtype=np.uint8);
wm =cv2.bitwise_and(e,t1);
#将水印图片内的1处理为255，方便显示
w=wm[:,:]>0;
wm[w]=255;
cv2.imshow("e",e);
cv2.imshow("wm",wm);


cv2.imshow("a",lena);

cv2.waitKey(0);
cv2.destroyAllWindows();
