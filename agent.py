from game import *
import random
import collections
from util import *
import simplegame

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
        scoredActions = [];
        for action in possibleActions:
            successor = succ(state, action);
            scoredActions.append((dotProduct(self.simpleFeatureExtractor(successor), self.weights), action));
        return randomMax(scoredActions);

    def simpleFeatureExtractor(self, state):
        features = collections.defaultdict(float);
        features["numWins"] = getGridWins(state)[getOppIndex(player(state))];
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
        opponentSuccess = any([getGridWins(succ(opponentState, oppAction))[getOppIndex(player(state))] > currentOppWins for oppAction in opponentActions]);

        return not opponentSuccess;

# class MinimaxAgent:
#     def __init__(self, d):
#         self.depth = d;
#         self.weights = collections.defaultdict(float);
#         # optimize eta, decreasing function
#         self.eta = .0001;
#         # can play with number of iterations
#         self.monteCarloIterations = 25;
#         self.eval = lambda state: dotProduct(state, self.weights);
#     def monteCarloUpdate(self, state):
#         for i in range(self.monteCarloIterations):
#             # can play with exploration policy
#             episode = [];
#             currentState = state;
#             while not isEnd(currentState):
#                 player = player(currentState);
#                 actions = actions(state);
#                 if player == 0:
#                     bestNewState = None;
#                     bestAction = None;
#                     bestScore = float("-inf");
#                     for action in actions:
#                         successor = succ(state, action);
#                         score = dotProduct(featureExtractor(successor), self.weights);
#                         if score > bestScore:
#                             bestAction = action;
#                             bestNewState = successor;
#                     reward = 0 if not isEnd(newState) else utility(newState);
#                     episode.extend((currentState, bestAction, reward, bestNewState));
#                     currentState = bestNewState;
#                 elif player == 1:
#                     worstNewState = None;
#                     worstAction = None;
#                     worstScore = float("inf");
#                     for action in actions:
#                         successor = succ(state, action);
#                         score = dotProduct(featureExtractor(successor), self.weights);
#                         if score > worstScore:
#                             worstAction = action;
#                             worstNewState = successor;
#                     reward = 0 if not isEnd(newState) else utility(newState);
#                     episode.extend((currentState, worstAction, reward, worstNewState));
#                     currentState = worstNewState;
#             # possibly shuffle or reverse
#             for resultTuple in episode:
#                 TDLearningUpdate(*resultTuple);
#     def TDLearningUpdate(self, state, action, reward, newState):
#         gradient = featureExtractor(state);
#         residual = dotProduct(featureExtractor(state), self.weights) - reward - dotProduct(featureExtractor(newState), self.weights);
#         multiplyVector(gradient, residual);
#         incrementSparseVector(self.weights, -1 * self.eta, gradient);
#     def getAction(self, state):
#         def minimaxValue(state, depth, firstInTree, agent):
#             actions = actions(state);
#             if isEnd(state):
#                 return utility(state);
#             elif depth == 0:
#                 return self.eval(state);
#             newDepth = depth - 1 if agent != firstInTree else depth;
#             if agent == 0:
#                 return max(minimaxValue(succ(state, action), newDepth, firstInTree, getOppIndex(agent)) for action in actions);
#             elif agent == 1:
#                 return min(minimaxValue(succ(state, action), newDepth, firstInTree, getOppIndex(agent)) for action in actions);
#         self.monteCarloUpdate(state);
#         return randomMax([(minimaxValue(succ(state, action), self.depth, getOppIndex(player(state)), getOppIndex(player(state))), action) \
#             for action in actions]);

def featureExtractor(state):
    features = collections.defaultdict(float);
    wins = getGridWins(state)
    features["numWins"] = wins[0];
    features["relativeWins"] = wins[0] - wins[1];
    features["otherWins"] = wins[1];

    # features["numAdjacentWins"] = getGridWinsAdjacent()
    features["numCenterPieces"] = countCenterMoves(state, 0);
    features["numCornerPieces"] = countCornerMoves(state, 0);
    features["numAdjacentPieces"] = countAdjacentMoves(state, 0);
    features["numOtherCenterPieces"] = countCenterMoves(state, 1);
    features["numOtherCornerPieces"] = countCornerMoves(state, 1);
    features["numOtherAdjacentPieces"] = countAdjacentMoves(state, 1);

    # adjacent won grids
    grids = countAdjacentGrids(state);
    features["numAdjacentWonGrids"] = grids[0];
    features["numOtherAdjacentWonGrids"] = grids[1];
    features["gridsDifference"] = grids[0] - grids[1];
    # effect of limiting next move:
    if state[2] is not None:
        # advantage of making move from the forced grid, if the next player is the first player
        features["advantageOfNextGrid"] = gridAdjacentMoves(state[0][state[2]], 0);
        if state[1] == 1:
            features["advantageOfNextGrid"] *= -1;
    return features;

class AdvancedPerceptronAgent:
    def __init__(self):
        self.weights = {'numCornerPieces': 0.811020200948285, 'numOtherCenterPieces': 0.0809559760347321, 'relativeWins': 1.0153244869861855, 'numAdjacentWonGrids': 0.969296961952278, 'numOtherAdjacentWonGrids': -0.6814807021505367, 'advantageOfNextGrid': 0.5395673542865317, 'numOtherCornerPieces': 0.7058793287408335, 'gridsDifference': 1.6507776641028122, 'numAdjacentPieces': 0.7130969880480094, 'numWins': 0.5323490704404454, 'numCenterPieces': 0.021778991208712777, 'otherWins': -0.48297541654574627, 'numOtherAdjacentPieces': -1.2963960051123138};

    def getAction(self, state):
        possibleActions = actions(state);
        scoredActions = [];
        for action in possibleActions:
            successor = succ(state, action);
            scoredActions.append((dotProduct(featureExtractor(successor), self.weights), action));
        return randomMax(scoredActions);

class MinimaxPruningAgent:
    def __init__(self, d):
        self.depth = d;
        # maybe try randomizng weights
        # self.weights = collections.defaultdict(float);
        self.weights = {'numCornerPieces': 0.811020200948285, 'numOtherCenterPieces': 0.0809559760347321, 'relativeWins': 1.0153244869861855, 'numAdjacentWonGrids': 0.969296961952278, 'numOtherAdjacentWonGrids': -0.6814807021505367, 'advantageOfNextGrid': 0.5395673542865317, 'numOtherCornerPieces': 0.7058793287408335, 'gridsDifference': 1.6507776641028122, 'numAdjacentPieces': 0.7130969880480094, 'numWins': 0.5323490704404454, 'numCenterPieces': 0.021778991208712777, 'otherWins': -0.48297541654574627, 'numOtherAdjacentPieces': -1.2963960051123138};
        # optimize eta, decreasing function
        self.eta = .00001;
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
                currActions = actions(currentState);
                if currPlayer == 0:
                    bestNewState = None;
                    bestAction = None;
                    if random.random() > .25:
                        bestScore = float("-inf");
                        for action in currActions:
                            successor = succ(currentState, action);
                            score = dotProduct(featureExtractor(successor), self.weights);
                            if score > bestScore:
                                bestAction = action;
                                bestNewState = successor;
                    else:
                        bestAction = currActions[random.randrange(len(currActions))];
                        bestNewState = succ(currentState, bestAction);
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
                    reward = 0 if not isEnd(worstNewState) else utility(worstNewState);
                    episode.append((currentState, worstAction, reward, worstNewState));
                    currentState = worstNewState;
                    # numberActions = len(currActions);
                    # randomAction = currActions[random.randrange(numberActions)];
                    # successor = succ(currentState, randomAction);
                    # reward = 0 if not isEnd(successor) else utility(successor);
                    # episode.append((currentState, randomAction, reward, successor));
                    # currentState = successor;
            # possibly shuffle or reverse
            for resultTuple in reversed(episode):
                # print resultTuple[1], resultTuple[2];
                self.TDLearningUpdate(*resultTuple);
        print self.weights;
    def TDLearningUpdate(self, state, action, reward, newState):
        gradient = featureExtractor(state);
        if isEnd(newState):
            residual = dotProduct(featureExtractor(state), self.weights) - reward;
        else:
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
            # print agent;
            if agent == 0:
                currActions.sort(key=lambda x: self.eval(succ(state, x)), reverse=True);
                currActions = currActions[:3];
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
                currActions.sort(key=lambda x: self.eval(succ(state, x)));
                currActions = currActions[:3];
                if alpha < beta:
                    for action in currActions:
                        if alpha < beta:
                            score = minimaxValue(succ(state, action), newDepth, firstInTree, getOppIndex(agent), alpha, beta);
                            if score < beta:
                                beta = score;
                        else:
                            return beta;

        # self.monteCarloUpdate(state);
        return randomMax([(minimaxValue(succ(state, action), self.depth, getOppIndex(player(state)), getOppIndex(player(state)), float("-inf"), float("inf")), action) \
            for action in actions(state)]);

class ExpectimaxAgent:
    def __init__(self, d):
        self.depth = d;
        # maybe try randomizng weights
        # self.weights = collections.defaultdict(float);
        self.weights = {'numCornerPieces': 0.811020200948285, 'numOtherCenterPieces': 0.0809559760347321, 'relativeWins': 1.0153244869861855, 'numAdjacentWonGrids': 0.969296961952278, 'numOtherAdjacentWonGrids': -0.6814807021505367, 'advantageOfNextGrid': 0.5395673542865317, 'numOtherCornerPieces': 0.7058793287408335, 'gridsDifference': 1.6507776641028122, 'numAdjacentPieces': 0.7130969880480094, 'numWins': 0.5323490704404454, 'numCenterPieces': 0.021778991208712777, 'otherWins': -0.48297541654574627, 'numOtherAdjacentPieces': -1.2963960051123138};
        self.eval = lambda state: dotProduct(featureExtractor(state), self.weights);
    def getAction(self, state):
        def minimaxValue(state, depth, firstInTree, agent):
            currActions = actions(state);
            if isEnd(state):
                return utility(state);
            elif depth == 0:
                return self.eval(state);
            newDepth = depth - 1 if agent != firstInTree else depth;
            if agent == 0:
                currActions.sort(key=lambda x: self.eval(succ(state, x)), reverse=True);
                currActions = currActions[:3];
                maxScore = float("-inf");
                for action in currActions:
                    score = minimaxValue(succ(state, action), newDepth, firstInTree, getOppIndex(agent));
                    if score > maxScore:
                        maxScore = score;
                return maxScore;
            elif agent == 1:
                scoreSum = 0.0;
                for action in currActions:
                    score = minimaxValue(succ(state, action), newDepth, firstInTree, getOppIndex(agent));
                    scoreSum += score;
                return scoreSum / len(currActions);


        # self.monteCarloUpdate(state);
        return randomMax([(minimaxValue(succ(state, action), self.depth, getOppIndex(player(state)), getOppIndex(player(state))), action) \
            for action in actions(state)]);

class SimpleRandomAgent:
    def getAction(self, state):
        possibleActions = simplegame.actions(state);
        numberActions = len(possibleActions);
        randomAction = possibleActions[random.randrange(numberActions)];
        return randomAction;

class SimplePerceptronAgent:

    def __init__(self):
        self.weights = {"numWins" : 5, "numCenterPieces": .2, "numAdjacentPieces": .4, "numCornerPieces": .1};

    def getAction(self, state):
        possibleActions = simplegame.actions(state);
        scoredActions = [];
        for action in possibleActions:
            successor = simplegame.succ(state, action);
            scoredActions.append((dotProduct(self.simpleFeatureExtractor(successor), self.weights), action));
        return randomMax(scoredActions);

    def simpleFeatureExtractor(self, state):
        features = collections.defaultdict(float);
        otherPlayer = getOppIndex(player(state));
        features["numWins"] = 1 if simplegame.playerWins(state)[1] == otherPlayer + 1 else 0;
        features["numCenterPieces"] = 1 if state[0][1][1] == otherPlayer else 0;
        features["numCornerPieces"] = simpleCountCornerMoves(state, otherPlayer);
        features["numAdjacentPieces"] = simpleAdjacentMoves(state, otherPlayer);
        return features;
