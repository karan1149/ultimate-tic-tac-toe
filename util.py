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
        for row in grid:
            for col in row:
                return


