
"""
simplified version of project


INITIAL IMAGE PROCESSING
_______________________________________________________________
static image
load into opencv
crop based on mark
resize to square for later processing
_______________________________________________________________



CELL/FIELD-BASED PROCESSING
_______________________________________________________________
Mark edges (where color intersects) (mainapp/conf.cfg, splitpoints (?))
	they seem to hard-code pixels that are splitpoints?
	have some slight success with canny --> findcontours --> array of contours --> then can do cell detection
go cell-by-cell:
	use Hough circle detection for pieces (see searchforpawn)
	detect color
Load array into pre-specified data structure for storing gamestate
_______________________________________________________________


MOVE PLANNING
_______________________________________________________________

Input gamestate into checkers heuristic
Output optimal move/log to console
_______________________________________________________________




Avg COLORS (within certain tolerances)
_______________________________________________________________
Black square: rgb(112, 91, 85)
White square: rgb(197, 184, 171)

Black peice: rgb(52, 51, 51)
White piece: rgb(208, 214, 170)


Ranges for pink squares:
R: 208-255
G: 37-161
B: 131-255

"""
import cv2
import copy


img = cv2.imread('board_1.jpg')
res = cv2.resize(img, (500, 400))
res2 = copy.deepcopy(res)


cv2.imshow('image', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

lower = [131, 37, 208]
upper = [255, 161, 255]
