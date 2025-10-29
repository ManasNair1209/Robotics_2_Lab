import cv2

# 1. Load and grayscale
gray_img = cv2.imread('indian-national-polyester-flag.jpeg', cv2.IMREAD_GRAYSCALE)

# 2. Get gradients
sobel_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3) # d_x = 1
sobel_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3) # d_y = 1

# 3. Combine
edges = cv2.magnitude(sobel_x, sobel_y)
edges = cv2.convertScaleAbs(edges) # Convert to uint8

# 4. Show
cv2.imshow('Edges', edges)
cv2.waitKey(0)