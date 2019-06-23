#Main file
import cv2
import numpy
from contours import squarify
from circle import get_piece_colour

def make_board():
    board = {}

    for x in range(0, 801, 100):
        for y in range(0, 801, 100):
            board[(x,y)] = "E"

    return board

def display_grid(img, board):
    #mutating function for image
    for pos in board:
        cv2.circle(img,pos, 3, (0,255, 0), 3)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#
# board_img = squarify("small_1.jpg")
# # print(get_piece_colour((board_img), (0,0),(100,100)))
# board = make_board()
# display_grid(board_img, board)



board_img = squarify("final_1.jpg")
print(get_piece_colour((board_img), 400,400))
