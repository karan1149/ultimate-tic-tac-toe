from game import *
from agent import *

class TicTacToeSimulator:
    def __init__(self, agent1, agent2):
        self.agent1 = agent1;
        self.agent2 = agent2;

    # play a single game and return the winner agent number or 3 if it is a tie
    def playGame(self):
        state = startState();
        while not isEnd(state):
            # printBoard(state[0]);
            # print state[1], state[2];

            assert(player(state) >= 0 and player(state) <= 1);
            if player(state) == 0:
                action = self.agent1.getAction(state);
            else:
                action = self.agent2.getAction(state);
            # print action;
            # print;
            state = succ(state, action);
        util = utility(state);
        return 1 if util > 0 else (3 if util == 0 else 2);

    # play n games and return the percentage of times agent1 won, tied
    def playGames(self, n):
        won = 0.0;
        tied = 0.0;
        for i in range(n):
            gameResult = self.playGame();
            won += 1 if gameResult == 1 else 0;
            tied += 1 if gameResult == 3 else 0;
            print "won/tied so far", won, tied, "out of", i + 1;
        print won / n, tied / n, 1 - won / n - tied / n;
