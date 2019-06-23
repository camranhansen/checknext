#Main file
import cv2
import numpy
from contours import squarify
from circle import get_piece_colour

def make_board():
    board = {}

    for x in range(0, 800, 100):
        for y in range(0, 800, 100):
            board[(x,y)] = "E"

    return board

def display_grid(img, board):
    #mutating function for image
    for pos in board:
        cv2.circle(img,pos, 3, (0,255, 0), 3)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def move_piece(img, board):
    available = []
    for key in board:
        if board[key] == "B":
            available.append(key)

    highest = (0,0)
    for piece in available:
        if piece[1] > highest[1]:
            highest = piece


    #now we move piece

    if board[(highest[0]+100, highest[1]+100)] == "W":
        cv2.arrowedLine(img, (highest[0]+50, highest[1]+50),(highest[0]+150, highest[1]+150), (0,0, 255), 10)
    else:
        cv2.arrowedLine(img, (highest[0]+50, highest[1]+50),(highest[0]-50, highest[1]+150), (0,0, 255), 10)

    cv2.imshow('reccomended move', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




# board_img = squarify("final_1.jpg")
# # print(get_piece_colour((board_img), (0,0),(100,100)))
# board = make_board()


board_img = squarify("final_2.jpg")
# print(get_piece_colour((board_img), 600,600))
board = make_board()
for key in board:
    board[key] = get_piece_colour(board_img, key[0], key[1])
# display_grid(board_img, board)
move_piece(board_img, board)
# print(board)