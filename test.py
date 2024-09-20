import cv2
img = cv2.imread('PaddleDetection/dataset/data/JPEGImages/2022-12-28_120649.png') # 可切换多张图片进行测试
h,w,c = img.shape
print(h)
print(w)
print(c)