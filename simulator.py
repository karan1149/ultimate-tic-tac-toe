from simulate import *
from game import *
from agent import *

# agent1 = RandomAgent();
# agent2 = RandomAgent();
# simulator = UltimateTicTacToeSimulator(agent1, agent2);
# print simulator.playGames(10000);
# print "random v random"; # 0.39 0.27 0.34 10,000

# agent1 = PerceptronAgent();
# agent2 = RandomAgent();
# simulator = UltimateTicTacToeSimulator(agent1, agent2);
# print simulator.playGames(10000);
# print "percep vs random agent"
#
# agent1 = ReflexAgent();
# agent2 = RandomAgent();
# simulator = UltimateTicTacToeSimulator(agent1, agent2);
# print simulator.playGames(1000);
# print "reflex vs random agent";

agent1 = PerceptronAgent();
agent2 = ReflexAgent();
simulator = UltimateTicTacToeSimulator(agent1, agent2);
print simulator.playGames(10000);
print "percep vs reflex agent"


# agent1 = MinimaxPruningAgent(2);
# # agent1 = RandomAgent();
# agent2 = AdvancedPerceptronAgent();
# simulator = UltimateTicTacToeSimulator(agent1, agent2);
# print simulator.playGames(100);
# print "minimax prungin2 vs advanced perceptron agent"

# agent1 = ExpectimaxAgent(1);
# # agent1 = RandomAgent();
# agent2 = PerceptronAgent();
# simulator = UltimateTicTacToeSimulator(agent1, agent2);
# print simulator.playGames(100);
# print "^ expectimax1 vs reg perceptron agent"

#
# simple agent code
#

# agent1 = SimplePerceptronAgent();
# agent2 = SimpleRandomAgent();
# simulator = TicTacToeSimulator(agent1, agent2);
# print simulator.playGames(10000);
# print "^ simple perceptron against simple random"; #.92, 0, .08 10,000 trials

# agent2 = SimplePerceptronAgent();
# agent1 = SimpleRandomAgent();
# simulator = TicTacToeSimulator(agent1, agent2);
# print simulator.playGames(10000);
# print "^ simple random against simple perceptron, reversed order"; # 0.29 0.0 0.71 10,000 trials

# agent1 = SimpleRandomAgent();
# agent2 = SimpleRandomAgent();
# simulator = TicTacToeSimulator(agent1, agent2);
# print simulator.playGames(10000);
# print "^ simple random against simple random"; #.58, .13, .29 10,000 trials

#
# /simple agent code
#
