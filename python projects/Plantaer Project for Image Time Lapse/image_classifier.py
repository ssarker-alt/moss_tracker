import numpy as np  # type: ignore
import cv2          # type: ignore


image = cv2.imread("moss.jpeg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


lower_green = np.array ([30, 40, 40])
upper_green = np.array ([90, 255, 255])

mask = cv2.inRange(hsv, lower_green, upper_green)
green_pixels = cv2.countNonZero(mask)
total_pixels = mask.size 
green_percent = (green_pixels/total_pixels) * 100 


print(f"Green Pixel Percentage: {green_percent:.2f}%")



