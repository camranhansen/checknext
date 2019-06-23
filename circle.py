import cv2
import numpy as np

# save a copy and convert image to b&w
img = cv2.imread("setup_board.jpg")
cimg = img
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# input coordinates for cropping
# (x0, y0) is upper left and (x1, y1) is lower right
x0 = 300
y0 = 44
x1 = 20
y1 = 400

# crop image
x = x1
y = y0
h = x0 - x1
w = y1-y0

crop_img = img[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)

# apply blur to b&w image
img = cv2.medianBlur(img,5)
img = cv2.GaussianBlur(img,(5,5), cv2.BORDER_DEFAULT)

# find circles using HoughCircles
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,60,param1=50,param2=30,minRadius=0,maxRadius=100)
circles = np.uint16(np.around(circles))

# draw circles
for i in circles[0, :]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    zerop=(0,0,0)
    zero=np.array(zerop)
    lowerp=(150, 150, 180)
    lower = np.array(lowerp)
    p_in_range=[]
    p_not_in_range = []

    cimg= cv2.medianBlur(cimg,5)

    height, width = img.shape[:2]
    range_1= i[0]-i[2] if 0 > i[0]-i[2] > width else 0
    range_2= i[0]+i[2] if 0 > i[0]+i[2] > width else width
    range_3= i[1]-i[2] if 0 > i[1]-i[2] > height else 0
    range_4 =  i[1]+i[2] if 0 > i[1]+i[2] > height else height
    for i in range(range_1, range_2):
        for j in range(range_3, range_4):
            if 0 <= cimg[j, i][0] <= lower[0] and 0 <= cimg[j, i][1] <= lower[1] and 0 <= cimg[j, i][2] <= lower[2]:
                p_in_range.append((i, j))
            else:
                p_not_in_range.append((i,j))

    mask = cv2.inRange(cimg, zero, lower)
    cv2.imshow('image', mask)

    print(len(p_in_range))
    print(len(p_not_in_range))
    colour_of_piece="white" if len(p_not_in_range) > len(p_in_range) else "black"
    print(colour_of_piece)

cv2.imshow('piece_detected', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()