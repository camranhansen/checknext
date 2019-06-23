import cv2
import numpy as np
import random


img = cv2.imread("small_1.jpg")

img = cv2.GaussianBlur(img, (5, 5),5)

# convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# set lower and upper color limits (for pink)
lower_val = (131, 37, 180)
upper_val = (255, 161, 255)

mask = cv2.inRange(hsv, lower_val, upper_val)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))
points = []

for i in range(len(contours)):
    totalx = 0
    totaly = 0
    for element in contours[i]:
        totalx += element[0][0]
        totaly += element[0][1]

    points.append([int(totalx/len(contours[i])), int(totaly/len(contours[i]))])


# for cont in contours:
    # x = random.randint(0, )
    # points.append([cont[0][0][0], cont[0][0][1]])
    # print([cont[0][0][0], cont[0][0][1]])

# cv2.drawContours(img, contours, -1, (0,255, 0), 100)
# res = cv2.resize(img, (600,600))
# print(res[0,0])
# cv2.imshow("contours", res)
# cv2.waitKey(0)
# print(points)
cnt = np.array(points)

rect = cv2.minAreaRect(cnt)
# print(rect)
print(img.shape)

box = cv2.boxPoints(rect)
box = np.int0(box)
# cv2.drawContours(img, [box], 0, (0, 0, 255), 2)


width = int(rect[1][0])
height = int(rect[1][1])

src_pts = box.astype("float32")

dst_pts = np.array([[0, height-1],
                    [0, 0],
                    [width-1, 0],
                    [width-1, height-1]], dtype="float32")

M = cv2.getPerspectiveTransform(src_pts, dst_pts)

warped = cv2.warpPerspective(img, M, (width, height))

res = cv2.resize(warped, (600,600))
cv2.imshow("original", (cv2.resize(img, (600, 600))))
cv2.imshow("test", res)

cv2.waitKey(0)



