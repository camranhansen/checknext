import cv2
import numpy as np



img = cv2.imread("pink_squares_matte.jpg")

img = cv2.GaussianBlur(img, (5, 5),5)

# convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# set lower and upper color limits (for pink)
lower_val = (131, 37, 200)
upper_val = (255, 161, 255)

mask = cv2.inRange(hsv, lower_val, upper_val)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

points = []
for cont in contours:
    points.append([cont[0][0][0], cont[0][0][1]])

cnt = np.array(points)

rect = cv2.minAreaRect(cnt)
# print(rect)
print(img.shape)

box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

# points = [[contours[0][0][0][0], contours[0][0][0][0]],
#           [contours[1][0][0][0], contours[1][0][0][0]],
#           [contours[2][0][0], contours[2][0][1]],
#           [contours[3][0][0], contours[3][0][1]]]
# note: can change this in the future to be more accurate

width = int(rect[1][0])
height = int(rect[1][1])

src_pts = box.astype("float32")

dst_pts = np.array([[0, height-1],
                    [0, 0],
                    [width-1, 0],
                    [width-1, height-1]], dtype="float32")

M = cv2.getPerspectiveTransform(src_pts, dst_pts)

warped = cv2.warpPerspective(img, M, (width, height))

cv2.waitKey(0)
res = cv2.resize(warped, (300,300))
# cv2.imshow("original",img)
cv2.imshow("test", res)

cv2.waitKey(0)



