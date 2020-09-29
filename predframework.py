import random

class Pred():
    def __init__(self, environment, preds, agents):
        self.y_max = len(environment) - 1
        self.x_max = len(environment[0]) - 1
        self.y = random.randint(0, self.y_max)
        self.x = random.randint(0, self.x_max)
        self.environment = environment
        self.preds = preds
        self.agents = agents