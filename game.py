import util as *

class Grid():
	def __init__(self):
		grid = []
		for row in range(3):
			grid.append([])
			for col in range(3):
				grid[row].append(0)
		self.grid = grid
		self.status = 0 # 0 = Inplay, 1 = agentWin, 2 = oppWin, 3 = tie(nobody)

	def __str__(self):
		return str(self.grid)


# get start state for game
def startState():
	board = []
	for row in range(9):
		board.append(Grid())
	printBoard(board)
	return (board, 0, None)

# fix printing here so it appears to be a proper grid and move to util.py
def printBoard(board):
	for row in board:
		print row

#get possible actions for a given state
def actions(state):
	actions = []
	board = state[0]
	lastPos = state[2]
	if(lastPos == None or board[lastPos].status != 0):
		for grid in board:
			if(grid.status == 0):
				actions.extend(findActionsInGrid(board[lastPos], actions, lastPos));
	else:
		actions = findActionsInGrid(board[lastPos], actions, lastPos)
    return actions;

## Helper method that finds all available positions in a grid and adds to possible actions
def findActionsInGrid(grid, gridNum):
    actions = [];
	for row in grid:
		for col in grid[row]:
			if(col == 0):
				actions.append((gridNum, posFromRowCol(row, col)))
	return actions;



#get successor state from a state given an action
def succ(state, action):
	board = state[0]
	grid = board[action[0]]
	rowCol = rowColFromPos(action[1])
	grid[rowCol[0]][rowCol[1]] = state[1] + 1 ## indexes grid, then row, then col to get element
	if(grid.status == 0):
		updateGridStatus(grid) ## check if grid is won, lost, or tied
	return (board, getOppIndex(state[1]), action[1])

def updateGridStatus(grid):
	center = grid[1][1]
	if(center != 0):
		if((center == grid[1][0] and center == grid[1][2]) or (center == grid[0][1] and center == grid[2][1]) or (center == grid[0][0] and center == grid[2][2]) or (center == grid[0][2] and center == grid[2][0])):
			grid.status = center
			return
	topMid = grid[0][1]
	if(topMid != 0):
		if(topMid == grid[0][0] and topMid == grid[0][2]):
			grid.status = topMid
			return
	leftMid = grid[1][0]
	if(leftMid != 0):
		if(leftMid == grid[0][0] and leftMid == grid[2][0]):
			grid.status = leftMid
			return
	rightMid = grid[1][2]
	if(rightMid != 0):
		if(rightMid == grid[0][2] and rightMid = grid[2][2]):
			grid.status = rightMid
			return
	botMid = grid[2][1]
	if(botMid != 0):
		if(botMid == grid[2][0] and botMid == grid[2][2]):
			grid.status = botMid
			return
	for row in grid:
		for col in grid[row]:
			if(col == 0):
				return
	grid.status = 3 ## if all positions are filled and no winners, status = tied
	return


#check if a state is an end state
def isEnd(state):
	board = state[0]
	centerStatus = board[4].status
	if(centerStatus != 0 or centerStatus != 3):
		if((centerStatus == board[3] and centerStatus == board[5]) or )


# fix this to account for draws
# utility for state if it is an end state
def utility(state):
	if(state[1] == 0):
		return 100
	else:
		return -100

#player that needs to move in a given state
def player(state):
	return state[1]

startState()
