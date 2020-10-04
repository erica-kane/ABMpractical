import random

class Sheep():
    def __init__(self, environment, herd, preds):
        self.y_max = len(environment) - 1
        self.x_max = len(environment[0]) - 1
        self.y = random.randint(0, self.y_max)
        self.x = random.randint(0, self.x_max)
        self.environment = environment
        self.store = 0 
        self.herd = herd
        self.preds = preds

    def move (self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % self.y_max
        else:
            self.y = (self.y - 1) % self.y_max 

        if random.random() < 0.5:
            self.x = (self.x + 1) % self.x_max
        else:
            self.x = (self.x - 1) % self.x_max

    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] -= self.environment[self.y][self.x]
        
    
    
    def distance_between(self, sheep):
        return (((self.x - sheep.x)**2) + ((self.y - sheep.y)**2))**0.5

