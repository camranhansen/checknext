<<<<<<< HEAD
# import cv2
# import numpy as np
#
# im = cv2.imread("pink_squares_matte.jpg")
# img = cv2.resize(im, (500, 400))
#
# # load image
#
# # add blur because of pixel artefacts
# img = cv2.GaussianBlur(img, (5, 5),5)
# # convert to HSV
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# # set lower and upper color limits
#
# lower_val = (131, 37, 200)
# upper_val = (255, 161, 255)
# # Threshold the HSV image to get only green colors
# mask = cv2.inRange(hsv, lower_val, upper_val)
# # apply mask to original image
# res = cv2.bitwise_and(img, img, mask= mask)
# #show imag
# # cv2.imshow("Result", res)
# # detect contours in image
# contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# # draw filled contour on result
# # for cnt in contours:
# #     print(cnt.min())
#
# #for contour 0
#
# for cnt in contours:
#     print(cnt[0])
# # detect edges in mask
# # edges = cv2.Canny(mask,100,100)
# # to save an image use cv2.imwrite('filename.png',img)
# #show images
# # cv2.imshow("Result_with_contours", res)
# # cv2.imshow("Mask", mask)
# # cv2.imshow("Edges", edges)
#
# cv2.rectangle(img, (contours[3][0][0], contours[3][0][1]), (contours[0][0][0], contours[0][0][1]),(0,255,0),3)
#
# # gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# # gray = cv2.GaussianBlur(gray, (5, 5), 0)
# # _, test_thing = cv2.threshold(gray, 120,255,1) # inverted threshold (light obj on dark bg)
# # test_thing = cv2.dilate(test_thing, None)  # fill some holes
# # test_thing = cv2.dilate(test_thing, None)
# # test_thing = cv2.erode(test_thing, None)   # dilate made our shape larger, revert that
# # test_thing = cv2.erode(test_thing, None)
# # contours, hierarchy = cv2.findContours(test_thing, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# #
# # rect = cv2.minAreaRect(contours[1])
# # box = cv2.boxPoints(rect)
# # box = np.int0(box)
# # cv2.drawContours(img,[box],0,(0,255,0),2)
# # cv2.imshow("test",img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
#
# cv2.waitKey(0)
#
=======
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

res = cv2.resize(warped, (800,800))


board = {}

for x in range(0, 801, 100):
    for y in range(0, 801, 100):
        board[(x,y)] = "E"

print(board)
board[(0,0)] = "B"
print(board)

for pos in board:
    cv2.circle(res,pos, 3, (0,255, 0), 3)


#
cv2.imshow("test", res)
# #
>>>>>>> parent of 1a2d82d... pretiffied into functoin
#
