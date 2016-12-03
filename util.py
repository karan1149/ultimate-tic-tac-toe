import random

def dotProduct(v1, v2):
    sum = 0;
    for x in v1:
        sum += v1[x] * v2[x]
    return sum;

def incrementSparseVector(v1, scale, v2):
    for x in v2:
        v1[x] += v2[x] * scale;

def multiplySparseVector(v1, scale):
    for x in v1:
        v1[x] *= scale;

def getOppIndex(playerIndex):
    return abs(playerIndex - 1);

def printBoard(board):
    for i in range(3):
        curGrid1 = board[i*3].grid
        curGrid2 = board[i*3 + 1].grid
        curGrid3 = board[i*3 + 2].grid
        for k in range(3):
            for j in range(3):
                print curGrid1[k][j],
            for j in range(3):
                print curGrid2[k][j],
            for j in range(3):
                print curGrid3[k][j],
            print

def printBoardStatuses(board):
    for i in range(3):
        printString = "";
        for q in range(3):
            printString += str(board[i * 3 + q].status);
        print printString;
    print;

def getGridWins(state): # returns tuple of (agentWins, oppWins)
    agentWins = 0
    oppWins = 0
    for grid in state[0]: #state[0] = board
        if(grid.status == 1):
            agentWins += 1
        if(grid.status == 2):
            oppWins += 1
    return (agentWins, oppWins)

def posFromRowCol(row, col):
    return 3*row + col

def rowColFromPos(pos):
    row = pos/3
    col = pos % 3
    return (row, col)

def randomMax(successors):
    maximumValue = max(successors)[0];
    possibleSuccessors = [successor for successor in successors if successor[0] == maximumValue];
    return random.choice(possibleSuccessors)[1];

def countCenterMoves(state, player):
    centerMoves = 0
    board = state[0]
    for grid in board:
        if(grid.grid[1][1] == player + 1):
            centerMoves += 1
    return centerMoves

def countCornerMoves(state, player):
    cornerMoves = 0
    board = state[0]
    for grid in board:
        if(grid.grid[0][0] == player + 1):
            cornerMoves += 1
        if(grid.grid[0][2] == player + 1):
            cornerMoves += 1
        if(grid.grid[2][0] == player + 1):
            cornerMoves += 1
        if(grid.grid[2][2] == player + 1):
            cornerMoves += 1
    return cornerMoves

def countAdjacentMoves(state, player):
    adjMoves = 0
    board = state[0]
    for grid in board:
        adjMoves += gridAdjacentMoves(grid, player)
    return adjMoves;

def gridAdjacentMoves(grid, player):
    adjMoves = 0
    grid = grid.grid
    for x in range(3):
        for y in range(3):
            if(grid[x][y] == player + 1):
                adjMoves += adjacentToSpace(grid, x, y)
    return adjMoves

def adjacentToSpace(grid,x, y):
    adjMoves = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if((x + dx > -1 and x + dx < 3) and (y + dy > -1 and y + dy < 3)): ## in bounds
                if(grid[x][y] == grid[x+dx][y+dy] and (not (dx == 0 and dy == 0))):
                    adjMoves += 1
    return adjMoves
