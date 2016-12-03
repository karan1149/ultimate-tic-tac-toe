from game import *
import random
import collections
from util import *

class RandomAgent:
    def getAction(self, state):
        possibleActions = actions(state);
        numberActions = len(possibleActions);
        randomAction = possibleActions[random.randrange(numberActions)];
        return randomAction;

class PerceptronAgent:

    def __init__(self):
        self.weights = {"numWins" : 5, "numCenterPieces": .2, "numAdjacentPieces": .4, "numCornerPieces": .1};

    def getAction(self, state):
        possibleActions = actions(state);
        bestAction = None;
        bestActionScore = float("-inf");
        for action in possibleActions:
            score = dotProduct(self.simpleFeatureExtractor(succ(state, action)), self.weights);
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
        numberActions = len(possibleActions);

        modifiedActions = [action for action in possibleActions if self.actionFilter(state, action)];
        modifiedNumberActions = len(modifiedActions);

        if modifiedNumberActions != 0:
            randomAction = modifiedActions[random.randrange(modifiedNumberActions)];
        else:
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
        # optimize eta, decreasing function
        self.eta = .001;
        # can play with number of iterations
        self.monteCarloIterations = 25;
        self.eval = lambda state: dotProduct(state, self.weights);
    def monteCarloUpdate(self, state):
        for i in range(self.monteCarloIterations):
            # can play with exploration policy
            episode = [];
            currentState = state;
            while not isEnd(currentState):
                player = player(currentState);
                actions = actions(state);
                if player == 0:
                    bestNewState = None;
                    bestAction = None;
                    bestScore = float("-inf");
                    for action in actions:
                        successor = succ(state, action);
                        score = dotProduct(featureExtractor(successor), self.weights);
                        if score > bestScore:
                            bestAction = action;
                            bestNewState = successor;
                    reward = 0 if not isEnd(newState) else utility(newState);
                    episode.extend((currentState, bestAction, reward, bestNewState));
                    currentState = bestNewState;
                elif player == 1:
                    worstNewState = None;
                    worstAction = None;
                    worstScore = float("inf");
                    for action in actions:
                        successor = succ(state, action);
                        score = dotProduct(featureExtractor(successor), self.weights);
                        if score > worstScore:
                            worstAction = action;
                            worstNewState = successor;
                    reward = 0 if not isEnd(newState) else utility(newState);
                    episode.extend((currentState, worstAction, reward, worstNewState));
                    currentState = worstNewState;
            # possibly shuffle or reverse
            for resultTuple in episode:
                TDLearningUpdate(*resultTuple);
    def TDLearningUpdate(self, state, action, reward, newState):
        gradient = featureExtractor(state);
        residual = dotProduct(featureExtractor(state), self.weights) - reward - dotProduct(featureExtractor(newState), self.weights);
        multiplyVector(gradient, residual);
        incrementSparseVector(self.weights, -1 * self.eta, gradient);
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
        self.monteCarloUpdate(state);
        return randomMax([(minimaxValue(succ(state, action), self.depth, getOppIndex(player(state)), getOppIndex(player(state))), action) \
            for action in actions]);



class MinimaxPruningAgent:
    def __init__(self, d):
        self.depth = d;
        self.weights = collections.defaultdict(float);
        # optimize eta, decreasing function
        self.eta = .001;
        # can play with number of iterations
        self.monteCarloIterations = 25;
        self.eval = lambda state: dotProduct(featureExtractor(state), self.weights);
    def monteCarloUpdate(self, state):
        for i in range(self.monteCarloIterations):
            # can play with exploration policy
            episode = [];
            currentState = state;
            while not isEnd(currentState):
                currPlayer = player(currentState);
                currActions = actions(state);
                if currPlayer == 0:
                    bestNewState = None;
                    bestAction = None;
                    bestScore = float("-inf");
                    for action in currActions:
                        successor = succ(currentState, action);
                        score = dotProduct(featureExtractor(successor), self.weights);
                        if score > bestScore:
                            bestAction = action;
                            bestNewState = successor;
                    reward = 0 if not isEnd(bestNewState) else utility(bestNewState);
                    episode.append((currentState, bestAction, reward, bestNewState));
                    currentState = bestNewState;
                elif currPlayer == 1:
                    worstNewState = None;
                    worstAction = None;
                    worstScore = float("inf");
                    for action in currActions:
                        successor = succ(currentState, action);
                        score = dotProduct(featureExtractor(successor), self.weights);
                        if score < worstScore:
                            worstAction = action;
                            worstNewState = successor;
                    print worstNewState;
                    print printBoard(worstNewState[0]), worstNewState[1], worstNewState[2];
                    reward = 0 if not isEnd(worstNewState) else utility(worstNewState);
                    episode.append((currentState, worstAction, reward, worstNewState));
                    currentState = worstNewState;
            # possibly shuffle or reverse
            for resultTuple in episode:
                self.TDLearningUpdate(*resultTuple);
    def TDLearningUpdate(self, state, action, reward, newState):
        gradient = featureExtractor(state);
        residual = dotProduct(featureExtractor(state), self.weights) - reward - dotProduct(featureExtractor(newState), self.weights);
        multiplySparseVector(gradient, residual);
        incrementSparseVector(self.weights, -1 * self.eta, gradient);
    def getAction(self, state):
        def minimaxValue(state, depth, firstInTree, agent, alpha, beta):
            currActions = actions(state);
            if isEnd(state):
                return utility(state);
            elif depth == 0:
                return self.eval(state);
            newDepth = depth - 1 if agent != firstInTree else depth;
            if agent == 0:
                if alpha < beta:
                    for action in currActions:
                        if alpha < beta:
                            score = minimaxValue(succ(state, action), newDepth, firstInTree, getOppIndex(agent), alpha, beta);
                            if score > alpha:
                                alpha = score;
                        else:
                            return alpha;
                return alpha;
            elif agent == 1:
                if alpha < beta:
                    for action in currActions:
                        if alpha < beta:
                            score = minimaxValue(succ(state, action), newDepth, firstInTree, getOppIndex(agent), alpha, beta);
                            if score < beta:
                                beta = score;
                        else:
                            return beta;
        self.monteCarloUpdate(state);
        print actions(state);
        print state;
        print printBoard(state[0]), state[1], state[2];
        return randomMax([(minimaxValue(succ(state, action), self.depth, getOppIndex(player(state)), getOppIndex(player(state)), float("-inf"), float("inf")), action) \
            for action in actions(state)]);
