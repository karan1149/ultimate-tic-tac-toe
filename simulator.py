from simulate import *
from game import *
from agent import *

# agent1 = MinimaxPruningAgent(2);
# # agent1 = RandomAgent();
# agent2 = AdvancedPerceptronAgent();
# simulator = TicTacToeSimulator(agent1, agent2);
# print simulator.playGames(100);
# print "minimax prungin2 vs advanced perceptron agent"

agent1 = MinimaxPruningAgent(1);
# agent1 = RandomAgent();
agent2 = AdvancedPerceptronAgent();
simulator = TicTacToeSimulator(agent1, agent2);
print simulator.playGames(100);
print "minimax prungin2 vs reg perceptron agent"
