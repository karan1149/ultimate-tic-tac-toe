from simulate import *
from game import *
from agent import *


# simple agent code
# agent1 = SimplePerceptronAgent();
# agent2 = SimpleRandomAgent();
# simulator = TicTacToeSimulator(agent1, agent2);
# print simulator.playGames(10000);
# print "^ simple perceptron against simple random"; #.92, 0, .08

# agent1 = SimpleRandomAgent();
# agent2 = SimpleRandomAgent();
# simulator = TicTacToeSimulator(agent1, agent2);
# print simulator.playGames(10000);
# print "^ simple random against simple random"; #.58, .13, .29

agent1 = MinimaxPruningAgent(2);
# agent1 = RandomAgent();
agent2 = AdvancedPerceptronAgent();
simulator = UltimateTicTacToeSimulator(agent1, agent2);
print simulator.playGames(100);
print "minimax prungin2 vs advanced perceptron agent"

# agent1 = AdvancedPerceptronAgent();
# agent2 = RandomAgent();
# simulator = UltimateTicTacToeSimulator(agent1, agent2);
# print simulator.playGames(300);
# print "percep v random";

# agent1 = ExpectimaxAgent(1);
# # agent1 = RandomAgent();
# agent2 = PerceptronAgent();
# simulator = UltimateTicTacToeSimulator(agent1, agent2);
# print simulator.playGames(100);
# print "^ expectimax1 vs reg perceptron agent"
