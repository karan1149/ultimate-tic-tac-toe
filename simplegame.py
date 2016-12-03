from util import *

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
	actions = []
	for rowNumber, row in enumerate(state[0]):
		for colNumber, col in enumerate(row):
			if(col == 0):
				actions.append(posFromRowCol(rowNumber, colNumer))
	return actions



## get successor state given a current state and an action
def succ(state, action):
	

## check if a state is an end state
def isEnd(state):

## utility of state, given that it is an end state
def utility(state):