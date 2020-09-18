import random

class Agent():
    def __init__(self, environment):
        self.y_len = len(environment)
        self.x_len = len(environment[0])
        self.y = random.randint(0, self.y_len)
        self.x = random.randint(0, self.x_len)
        self.environment = environment
        self.store = 0 

    def move (self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % self.y_len
        else:
            self.y = (self.y - 1) % self.y_len

        if random.random() < 0.5:
            self.x = (self.x + 1) % self.x_len
        else:
            self.x = (self.x - 1) % self.x_len

    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] -= self.environment[self.y][self.x]

    def sick(self):
        if self.store > 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0 

    def __str__(self):
        return 'Agent: ' + 'x = ' + str(self.x) + ', y = ' + str(self.y) + ', store = ' + str(self.store)

