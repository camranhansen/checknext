#Main file
import cv2
import numpy
from contours import squarify
# from circle import

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
