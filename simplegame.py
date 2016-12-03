from util import *
import copy

# get start state for game
def startState():
	board = []
	for i in range(3):
		board.append([])
		for j in range(3):
			board[i].append(0)
	return (board, 0)

## get possible actions from current state
def actions(state):
	actions = [] ## possible positions the player can play in
	for rowNumber, row in enumerate(state[0]):
		for colNumber, col in enumerate(row):
			if(col == 0):
				actions.append(posFromRowCol(rowNumber, colNumer))
	return actions



## get successor state given a current state and an action
def succ(state, action):
	board = copy.deepcopy(state[0])
	rowCol = rowColFromPos(action)
	board[rowCol[0]][rowCol[1]] = state[1] + 1
	return (board, getOppIndex(state[1]))



## check if a state is an end state
def isEnd(state):

## utility of state, given that it is an end state
def utility(state):
	