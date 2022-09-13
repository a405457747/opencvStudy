import cv2;
import numpy as np

#numpy操作实战教学
img =cv2.imread("./a1.jpg");
#打印全部显示
np.set_printoptions(threshold=np.inf)
#print(img);
for i in range(0,20):
    for j in range(0,20):
        img[i,j]=[23,14,99];#这个133代替[133,133,133]
    

cv2.imshow("ff",img);

cv2.waitKey(0);
cv2.destroyAllWindows();


