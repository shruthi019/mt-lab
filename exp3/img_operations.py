import cv2

img_color = cv2.imread('igdtuw_logo.jpg', 1)
img_grayscale = cv2.imread('igdtuw_logo.jpg', 0)

img_color_dimensions = img_color.shape
img_grayscale_dimensions = img_grayscale.shape

print('Colored logo dimensions: ', img_color_dimensions)
print('Grayscale logo dimensions: ', img_grayscale_dimensions)

cv2.imshow('Colored logo', img_color)
cv2.waitKey(0)
cv2.imshow('Grayscale logo', img_grayscale)
cv2.waitKey(0)

down_width = 100
down_height = 93
down_factor = (down_width, down_height)
resized_down_img = cv2.resize(img_color, down_factor, interpolation=cv2.INTER_LINEAR)
img_color_downsized_dimension = resized_down_img.shape
print('Resized (down) color logo dimensions: ', img_color_downsized_dimension)

cv2.imshow('Resized down color logo', resized_down_img)
cv2.waitKey(0)

up_width = 400
up_height = 372
up_factor = (up_width, up_height)
resized_up_img = cv2.resize(img_color, up_factor, interpolation=cv2.INTER_LINEAR)
img_color_upsized_dimension = resized_up_img.shape
print('Resized (up) color logo dimensions: ', img_color_upsized_dimension)

cv2.imshow('Resized up color logo', resized_up_img)
cv2.waitKey(0)