import cv2
import numpy as np

# imagen 1 cuadrado
img1 = np.zeros((400,600), dtype=np.uint8)
img1[100:300, 200:400] = 255
# imagen 2 círculo
img2 = np.zeros((400, 600), dtype=np.uint8)
img2 = cv2.circle(img2, (300,200), 125, (255), -1)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
