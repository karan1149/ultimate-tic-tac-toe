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
# print "percep vs random agent" # 0.6425 0.1189 0.2386 10,000 trials

# agent1 = ReflexAgent();
# agent2 = RandomAgent();
# simulator = UltimateTicTacToeSimulator(agent1, agent2);
# print simulator.playGames(1000);
# print "reflex vs random agent"; # 0.416 0.349 0.235 1000
#
# agent1 = PerceptronAgent();
# agent2 = ReflexAgent();
# simulator = UltimateTicTacToeSimulator(agent1, agent2);
# print simulator.playGames(1000);
# print "percep vs reflex agent" # 0.54 0.154 0.306 1000

# agent1 = PerceptronAgent();
# agent2 = PerceptronAgent();
# simulator = UltimateTicTacToeSimulator(agent1, agent2);
# print simulator.playGames(5000);
# print "percep vs percep agent" # 0.5588 0.0408 0.4004 5,000
#
# agent1 = ReflexAgent();
# agent2 = ReflexAgent();
# simulator = UltimateTicTacToeSimulator(agent1, agent2);
# print simulator.playGames(1000);
# print "reflex vs reflex agent" # 0.305 0.424 0.271 1000

# agent1 = AdvancedPerceptronAgent();
# agent2 = AdvancedPerceptronAgent();
# simulator = UltimateTicTacToeSimulator(agent1, agent2);
# print simulator.playGames(5000);
# print "adv percep vs adv percep agent" #
#
# agent1 = AdvancedPerceptronAgent();
# agent2 = PerceptronAgent();
# simulator = UltimateTicTacToeSimulator(agent1, agent2);
# print simulator.playGames(5000);
# print "adv percep v percep agent" #

agent1 = AdvancedPerceptronAgent();
agent2 = ReflexAgent();
simulator = UltimateTicTacToeSimulator(agent1, agent2);
print simulator.playGames(1000);
print "adv percep v reflex agent" #

agent1 = AdvancedPerceptronAgent();
agent2 = RandomAgent();
simulator = UltimateTicTacToeSimulator(agent1, agent2);
print simulator.playGames(5000);
print "advanced percep vs random agent" #


# agent1 = MinimaxPruningAgent(2);
# # agent1 = RandomAgent();
# agent2 = AdvancedPerceptronAgent();
# simulator = UltimateTicTacToeSimulator(agent1, agent2);
# print simulator.playGames(100);
# print "minimax prungin2 vs advanced perceptron agent"





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
