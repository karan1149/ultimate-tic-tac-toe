from simulate import *
from game import *
from agent import *

agent1 = PerceptronAgent();
agent2 = RandomAgent();
simulator = TicTacToeSimulator(agent1, agent2);
print simulator.playGames(100);
