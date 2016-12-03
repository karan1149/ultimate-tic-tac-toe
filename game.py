
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

def getGridWins(state): # returns tuple of (agentWins, oppWins)
    agentWins = 0
    oppWins = 0
    for row in state[0]: #state[0] = board
        if(state[0][row].status == 1):
            agentWins += 1
        if(state[0][row].status == 2):
            oppWins += 1
    return (agentWins, oppWins)

# get start state for game
def startState():
	board = []
	for row in range(9):
		board.append(Grid())
	printBoard(board)
	return (board, 1, None)


def printBoard(board):
	for row in board:
		print row

#get possible actions for a given state
def actions(state):
	actions = []
	board = state[0]
	lastPos = state[2]
	if(lastPos == None or board[lastPos].status != 0):
		for row in board:
			if(board[lastPos].status == 0):
				actions = findAvailablePos(board[lastPos], actions, lastPos)
	else:
		actions = findAvailablePos(board[lastPos], actions, lastPos)

## Helper method that finds all available positions in a grid and adds to possible actions
def findAvailablePos(grid, actions, gridNum):
	for row in grid:
		for col in grid[row]:
			if(col == 0):
				actions.append((gridNum, 3*row + col))
	return actions





#get successor state from a state given an action
def succ(state, action):
	board = state[0]
	grid = board[action[0]]
	grid[action[1]/3][action[1]%3] = state[1] + 1 ## indexes grid, then row, then col to get element
	updateGridStatus(grid) ## check if grid is won, lost, or tied
	nextPlayer = 0
	if(state[1] == 0):
		nextPlayer = 1
	return (board, nextPlayer, action[1])

def updateGridStatus(grid):

#check if a state is an end state
def isEnd(state):
	return


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
