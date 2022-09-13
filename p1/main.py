import cv2;

#读取图片，第二个参数是图片样式，返回的是numpy数组
im1 =cv2.imread("./1.jpg",cv2.IMREAD_GRAYSCALE);
print(im1);

#创建窗口，imshow默认也会创建
window1=cv2.namedWindow("default");

#显示图片，第一个窗口名，第二个图片数组
im2=cv2.imshow("default",im1);

#0表示等待键盘触发的时间为0ms，返回ascii码
retval=cv2.waitKey(0);

if(retval==ord('a')):
    #销毁窗口
    cv2.destroyWindow("default");
    print("closed");
#保存图片，传入的是数组
cv2.imwrite("./a1.jpg",im1);