
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




COLORS (within certain tolerances)
_______________________________________________________________
Black square: rgb(112, 91, 85)
White square: rgb(197, 184, 171)

Black peice: rgb(52, 51, 51)
White piece: rgb(208, 214, 170)
"""
print("test")