import game as *
import random
import collections
import util as *

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
            score = dotProduct(simpleFeatureExtractor(succ(state, action)), self.weights);
            if score > bestActionScore:
                bestActionScore = score;
                bestAction = action;
        return action;

    def simpleFeatureExtractor(self, state):
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
        currentOppWins = getGridWins(state)[getOppIndex(player(state))];
        # check if making move might give a square to the opponent
        opponentState = succ(state, action);
        opponentActions = actions(opponentState);
        # assume a function returning (Player 1 tiles won, Player 2 tiles won) exists getGridWins(state)
        opponentSuccess = any([getGridWins(succ(opponentState, oppAction))[getOppIndex(player(state))] > currentOppWins for oppAction in opponentActions]);
        return not opponentSuccess;

def featureExtractor(state):
    features = collections.defaultdict(float);
    features["numWins"] = getGridWins(state)[getOppIndex(player(state))];
    # assumes helper countCenterMoves(state, player number 0 indexed)
    features["numCenterPieces"] = countCenterMoves(state, getOppIndex(player(state)));
    features["numCornerPieces"] = countCornerMoves(state, getOppIndex(player(state)));
    features["numAdjacentPieces"] = countAdjacentMoves(state, getOppIndex(player(state)));
    return features;

class MinimaxAgent:
    def __init__(self, d):
        self.depth = d;
        self.weights = collections.defaultdict(float);
    def getAction(self, state):
        def minimaxValue(state, depth, firstInTree, agent):
            actions = actions(state);
            if isEnd(state):
                return utility(state);
            elif depth == 0:
                return self.eval(state);
            newDepth = depth - 1 if agent != firstInTree else depth;
            if agent == 0:
                return max(minimaxValue(succ(state, action), newDepth, firstInTree, getOppIndex(agent)) for action in actions);
            elif agent == 1:
                return min(minimaxValue(succ(state, action), newDepth, firstInTree, getOppIndex(agent)) for action in actions);
        def monteCarloUpdate

        def TDLearning(state, action, reward, newState):

        return randomMax([(minimaxValue(succ(state, action), self.depth, getOppIndex(player(state)), getOppIndex(player(state))), action) \
            for action in actions]);
