import cv2;
import numpy as np

#10是最小，99娶不到最大是98
img=np.random.randint(10,99,size=[5,5],dtype=np.uint8);
print("img=\n",img);
#读取值
print(img.item(3,2));
#设置值
img.itemset((3,2),211);
print("img=\n",img);

img =np.random.randint(0,256,size=[256,256,3],dtype=np.uint8);
img.itemset((3,2,1),255);

#RCO刚兴趣的地方,赋值就相当于复制了
img =cv2.imread("./1.jpg");
img2=np.random.randint(0,256,size=[256,256,3],dtype=np.uint8);
face =img2[220:230,230:240]
img[220:230,230:240]=face;
cv2.imshow("demo",img);
cv2.waitKey();