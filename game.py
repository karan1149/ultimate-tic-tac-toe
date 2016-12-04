from util import *
import copy

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
	return (board, 0, None)


#get possible actions for a given state
def actions(state):
	actions = []
	board = state[0]
	lastPos = state[2]
	if(lastPos == None or board[lastPos].status != 0):
		for i in range(9):
			grid = board[i]
			if(grid.status == 0):
				actions.extend(findActionsInGrid(grid, i));
	else:
		actions = findActionsInGrid(board[lastPos], lastPos)
	return actions;

## Helper method that finds all available positions in a grid and adds to possible actions
def findActionsInGrid(grid, gridNum):
	actions = [];
	for rowNumber, row in enumerate(grid.grid):
		for colNumber, col in enumerate(row):
			if(col == 0):
				actions.append((gridNum, posFromRowCol(rowNumber, colNumber)))
	return actions;



#get successor state from a state given an action
def succ(state, action):
	board = copy.deepcopy(state[0])
	grid = board[action[0]]
	rowCol = rowColFromPos(action[1])
	grid.grid[rowCol[0]][rowCol[1]] = state[1] + 1 ## indexes grid, then row, then col to get element
	if(grid.status == 0):
		updateGridStatus(grid) ## check if grid is won, lost, or tied
	return (board, getOppIndex(state[1]), action[1]);

def updateGridStatus(grid):
	gridWithStatus = grid;
	grid = grid.grid;
	center = grid[1][1]
	if(center != 0):
		if((center == grid[1][0] and center == grid[1][2]) or (center == grid[0][1] and center == grid[2][1]) or (center == grid[0][0] and center == grid[2][2]) or (center == grid[0][2] and center == grid[2][0])):
			gridWithStatus.status = center
			return
	topMid = grid[0][1]
	if(topMid != 0):
		if(topMid == grid[0][0] and topMid == grid[0][2]):
			gridWithStatus.status = topMid
			return
	leftMid = grid[1][0]
	if(leftMid != 0):
		if(leftMid == grid[0][0] and leftMid == grid[2][0]):
			gridWithStatus.status = leftMid
			return
	rightMid = grid[1][2]
	if(rightMid != 0):
		if(rightMid == grid[0][2] and rightMid == grid[2][2]):
			gridWithStatus.status = rightMid
			return
	botMid = grid[2][1]
	if(botMid != 0):
		if(botMid == grid[2][0] and botMid == grid[2][2]):
			gridWithStatus.status = botMid
			return
	for row in grid:
		for col in row:
			if(col == 0):
				return
	gridWithStatus.status = 3 ## if all positions are filled and no winners, status = tied
	return


#check if a state is an end state
def isEnd(state):
	result = playerWins(state)
	return result[0]


def playerWins(state):
	board = state[0]
	cStat = board[4].status ## Status of center grid
	if(cStat != 0 and cStat != 3):
		if((cStat == board[3].status and cStat == board[5].status) or (cStat == board[1].status and cStat == board[7].status) or (cStat == board[0].status and cStat == board[8].status) or (cStat == board[2].status and cStat == board[6].status)):
			return (True, cStat)
	tmStat = board[1].status ## status of top middle grid
	if(tmStat != 0 and tmStat != 3):
		if(tmStat == board[0].status and tmStat == board[2].status):
			return (True, tmStat)
	lmStat = board[3].status ## status of left middle grid
	if(lmStat != 0 and lmStat != 3):
		if(lmStat == board[0].status and lmStat == board[6].status):
			return (True, lmStat)
	rmStat = board[5].status ## status of right middle grid
	if(rmStat != 0 and rmStat != 3):
		if(rmStat == board[2] and rmStat == board[8]):
			return (True, rmStat)
	bmStat = board[7].status ## status of bottom middle grid
	if(bmStat != 0 and bmStat != 3):
		if(bmStat == board[6].status and bmStat == board[8].status):
			return (True, bmStat)
	allFilled = 1
	for grid in board: ## Makes there exists a grid still in play, if not then game is a draw
		if(grid.status == 0):
			allFilled = 0
			break
	if(allFilled == 1):
		return (True, 3) ## tie game
	return (False, None)


# fix this to account for draws
# utility for state if it is an end state
def utility(state):
	result = playerWins(state)
	if(result[1] == 1):
		return 100
	elif(result[1] == 2):
		return -100
	return 0

#player that needs to move in a given state
def player(state):
	return state[1]
