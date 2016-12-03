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
