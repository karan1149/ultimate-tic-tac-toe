import game as *;
import random;
import collections;

def dotProduct(v1, v2):
    sum = 0;
    for x in v1:
        sum += v1[x] * v2[x]
    return sum;

def getOppIndex(playerIndex):
    return abs(playerIndex - 1);

class RandomAgent:
    def getAction(self, state):
        possibleActions = actions(state);
        numberActions = len(possibleActions);
        randomAction = possibleActions[random.randrange(numberActions)];
        return randomAction;

class PerceptronAgent:

    def __init__(self):
        self.weights = {"numWins" : 1, "numCenterPieces": .2, "numAdjacentPieces": .4, "numCornerPieces": .1};

    def getAction(self, state):
        possibleActions = actions(state);
        bestAction = None;
        bestActionScore = float("-inf");
        for action in possibleActions:
            score = dotProduct(extractFeatures(succ(state, action)), self.weights);
            if score > bestActionScore:
                bestActionScore = score;
                bestAction = action;
        return action;

    def extractFeatures(self, state):
        features = collections.defaultdict(float);
        features["numWins"] = getGridWins(state)[getOppIndex(player(state))];
        # assumes helper countCenterMoves(state, player number 0 indexed)
        features["numCenterPieces"] = countCenterMoves(state, getOppIndex(player(state)));
        features["numCornerPieces"] = countCornerMoves(state, getOppIndex(player(state)));
        features["numAdjacentPieces"] = countAdjacentMoves(state, getOppIndex(player(state)));
        return features;

class ReflexAgent:
    def getAction(self, state):
        possibleActions = actions(state);
        modifiedActions = [action for action in possibleActions if actionFilter(action)];
        numberActions = len(modifiedActions);
        if numberActions != 0:
            randomAction = modifiedActions[random.randrange(numberActions)];
        else:
            numberActions = len(possibleActions);
            randomAction = possibleActions[random.randrange(numberActions)];
        return randomAction;

    def actionFilter(self, state, action):
        currentOppWins = getGridWins(state)[1];
        # check if making move might give a square to the opponent
        opponentState = succ(state, action);
        opponentActions = actions(opponentState);
        # assume a function returning (Player 1 tiles won, Player 2 tiles won) exists getGridWins(state)
        opponentSuccess = any([getGridWins(succ(opponentState, oppAction))[1] > currentOppWins for oppAction in opponentActions]);
        return not opponentSuccess;

