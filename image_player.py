import glob
import cv2

for png_file in sorted(glob.glob('C:\Temp\shadows\*.png')):
    frame = cv2.imread(png_file, cv2.IMREAD_UNCHANGED)
    cv2.imshow("xxx", frame)
    cv2.waitKey(100)
