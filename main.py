import cv2

# read image
img = cv2.imread('image.jpg')

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply Gaussian blur
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# get edges
edges = cv2.Canny(gray, 50, 150)

# invert colors
edges = cv2.bitwise_not(edges)

# save sketch
cv2.imwrite('sketch.jpg', edges)


# To use