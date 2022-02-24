# Import packages
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./igdtuw_logo.jpg')
print(img.shape) # Print image shape
cv2.imshow("original", img)

# Cropping an image
cropped_image = img[80:280, 150:330]

# Display cropped image
cv2.imshow("cropped", cropped_image)

# Save the cropped image
cv2.imwrite("Cropped Image.jpg", cropped_image)

cv2.waitKey(0)
# cv2.destroyAllWindows()

# path
path = r'./igdtuw_logo.jpg'
  
# Reading an image in default mode
src = cv2.imread(path)
  
# Window name in which image is displayed
window_name = 'Rotated Image'
  
# Using cv2.rotate() method
# Using cv2.ROTATE_90_CLOCKWISE rotate
# by 90 degrees clockwise
image = cv2.rotate(src, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
  
# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)

# load an image in grayscale mode
img = cv2.imread(path,0)
  
# calculate frequency of pixels in range 0-255
histg = cv2.calcHist([img],[0],None,[256],[0,256]) 

plt.plot(histg)
plt.show()

src = cv2.imread(path)
  
# Window name in which image is displayed
window_name = 'Transposed Image'
  
# Using cv2.transpose() method
image = cv2.transpose(src)
  
# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)

b,g,r = cv2.split(src)
# print(b, g, r)

cv2.destroyAllWindows()