from simulate import *
from game import *
from agent import *

agent1 = ReflexAgent();
agent2 = RandomAgent();
simulator = TicTacToeSimulator(agent1, agent2);
print simulator.playGame();
