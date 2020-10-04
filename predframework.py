import random


class Pred():
    def __init__(self, environment, preds, herd):
        self.y_max = len(environment) - 1
        self.x_max = len(environment[0]) - 1
        self.y = random.randint(0, self.y_max)
        self.x = random.randint(0, self.x_max)
        self.environment = environment
        self.store = 0
        self.preds = preds
        self.herd = herd

    # def distance_between(self, agent):
    #     return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5

    # def hunt(self):
