import cv2
import os 

path = 'E:\WhiteHatJr Projects\Video Creator\Images'
images = os.listdir(path)

images_array = []

for i in images :
    newimage = path + "\\" + i
    images_array.append(newimage)

firstimage = cv2.imread(images_array[0])
height,width,channels = firstimage.shape
size = (width,height)
newvideo = cv2.VideoWriter('sunrise.mp4',cv2.VideoWriter_fourcc(*'DIVX'),40,size)
for i in reversed(images_array) :
    frame = cv2.imread(i)
    newvideo.write(frame)
newvideo.release()
#print(images_array)

