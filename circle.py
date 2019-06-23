import cv2
import numpy as np


def get_piece_colour(img, x, y):
# save a copy and convert image to b&w
    cimg = img
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # input coordinates for cropping
    # (x0, y0) is upper left and (x1, y1) is lower right


    h = 100
    w = 100

    cimg = cimg[y:y+h, x:x+w]
    img = img[y:y+h, x:x+w]
    cv2.imshow('piece_detected', img)
    cv2.waitKey(0)
    # apply blur to b&w image
    img = cv2.medianBlur(img,5)
    img = cv2.GaussianBlur(img,(5,5), cv2.BORDER_DEFAULT)

    # find circles using HoughCircles
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,60,param1=50,param2=30,minRadius=0,maxRadius=100)
    if circles is None:
        return "E"

    # draw circles
    else:
        for i in circles[0, :]:
            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            zerop=(0,0,0)
            zero=np.array(zerop)
            lowerp=(150, 150, 150)
            lower = np.array(lowerp)
            p_in_range=[]
            p_not_in_range = []

            cimg = cv2.medianBlur(cimg,5)

            height, width = cimg.shape[:2]
            range_1= i[0]-i[2] if 0 < i[0]-i[2] < width else 0
            range_2= i[0]+i[2] if 0 < i[0]+i[2] < width else width
            range_3= i[1]-i[2] if 0 < i[1]-i[2] < height else 0
            range_4 = i[1]+i[2] if 0 < i[1]+i[2] < height else height
            for i in range(int(range_1), int(range_2)):
                for j in range(int(range_3), int(range_4)):
                    if 0 <= cimg[j, i][0] <= lower[0] and 0 <= cimg[j, i][1] <= lower[1] and 0 <= cimg[j, i][2] <= lower[2]:
                        p_in_range.append((i, j))
                    else:
                        p_not_in_range.append((i,j))

            # mask = cv2.inRange(cimg, zero, lower)
            # cv2.imshow('image', mask)

            print(len(p_in_range))
            print(len(p_not_in_range))
            colour_of_piece = "W" if len(p_not_in_range) > len(p_in_range) else "B"
            cv2.imshow('piece_detected', cimg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return colour_of_piece
