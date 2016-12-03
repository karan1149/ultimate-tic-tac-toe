def dotProduct(v1, v2):
    sum = 0;
    for x in v1:
        sum += v1[x] * v2[x]
    return sum;

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
