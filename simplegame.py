from util import *
import copy

# get start state for game
def startState():
	board = []
	for i in range(3):
		board.append([])
		for j in range(3):
			board[i].append(0)
	return (board, 0) ## tuple of board and player's turn

## get possible actions from current state = positions open on board
def actions(state):
	actions = [] ## possible positions the player can play in
	for rowNumber, row in enumerate(state[0]):
		for colNumber, col in enumerate(row):
			if(col == 0):
				actions.append(posFromRowCol(rowNumber, colNumber))
	return actions



## get successor state given a current state and an action
def succ(state, action):
	board = copy.deepcopy(state[0])
	rowCol = rowColFromPos(action)
	board[rowCol[0]][rowCol[1]] = state[1] + 1
	return (board, getOppIndex(state[1]))

def isEnd(state):
	result = playerWins(state)
	return result[0]

## Returns a tuple of a boolean of whether the game is over, and who won e.g (True, 1) or (False, None)
def playerWins(state):
	grid = state[0]
	center = grid[1][1]
	if(center != 0):
		if((center == grid[1][0] and center == grid[1][2]) or (center == grid[0][1] and center == grid[2][1]) or (center == grid[0][0] and center == grid[2][2]) or (center == grid[0][2] and center == grid[2][0])):
			return (True, center)
	topMid = grid[0][1]
	if(topMid != 0):
		if(topMid == grid[0][0] and topMid == grid[0][2]):
			return (True, topMid)
	leftMid = grid[1][0]
	if(leftMid != 0):
		if(leftMid == grid[0][0] and leftMid == grid[2][0]):
			return (True, leftMid)
	rightMid = grid[1][2]
	if(rightMid != 0):
		if(rightMid == grid[0][2] and rightMid == grid[2][2]):
			return (True, rightMid)
	botMid = grid[2][1]
	if(botMid != 0):
		if(botMid == grid[2][0] and botMid == grid[2][2]):
			return(True, botMid)
	for row in grid:
		for col in row:
			if(col == 0):
				return (False, None)
	return (True, 3)

## utility of state, given that it is an end state
def utility(state):
	result = playerWins(state)
	if(result[1] == 1):
		return 100
	elif(result[1] == 2):
		return -100
	return 0
## gets which player's turn it is
def player(state):
	return state[1]
