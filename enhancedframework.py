import random

# Create a main class that initialises (as both initialise in the same way)
# It also contains the distance function, as this could be useful for the sheep to know if they were to run from the nearest wolf 
# Finally, it contains a check for boundaries which makes the agents bounce off the environment perimeter 
# This is useful for 2 reasons:
    # Comparing the environment to real life, it is more likley that the animals are in a field and when faced with a wall they will bounce off 
    # When chasing a sheep, if the environment is torus, the predator will stop chasing it as it will no longer be the closest by coordinates 
# Both sheep and predators need to do this boundary check, so it is stored in the main class (also results in shorter code)
class Agent():
    def __init__(self, environment, herd, preds):
        self.y_max = len(environment) - 1
        self.x_max = len(environment[0]) - 1
        self.y = random.randint(0, self.y_max)
        self.x = random.randint(0, self.x_max)
        self.environment = environment
        self.store = 0
        self.herd = herd
        self.preds = preds

    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
    def check_boundaries(self):
        if self.y < 0:
            self.y = 0
        elif self.y > self.y_max:
            self.y = self.y_max
        
        if self.x < 0:
            self.x = 0
        elif self.x > self.x_max:
            self.x = self.x_max


# Initialising sheep sub class happens by default when you call the main class 
# It will eat like before, but is no longer sick. Instead, it stops eating when it is full (store 200)
class Sheep(Agent):
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] -= self.environment[self.y][self.x]

        if self.store > 200:
            self.store = 200

# The sheep moves like before, but the boundary check is called upon after 
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1)
        else:
            self.y = (self.y - 1)

        if random.random() < 0.5:
            self.x = (self.x + 1)
        else:
            self.x = (self.x - 1)

        self.check_boundaries()

# Dying is a characteristic of the sheep, rather than the predator, so is created in the sheep sub class 
    def die(self):
        self.herd.remove(self)


# Initialising the predator sub class in the same way 
class Pred(Agent):
# The first action is must take is finding a target (closest sheep)
# The distance and closest sheep are saved so the comparasion is always made to the last sheep observed with the closest distance 
    def find_target(self):
        min_dist = 999999999
        closest_sheep = None
        for sheep in self.herd:
            distance = self.distance_between(sheep)
            if distance < min_dist:
                closest_sheep = sheep
                min_dist = distance
        return closest_sheep

# The predator then hunts, moving towards the closest sheep, now called the target
# It does this by checking the target's coordinates, and moving in the appropriate direction to get closer to it
    def hunt(self):
        target = self.find_target()

        diff_x = target.x - self.x
        # Target to the right
        if diff_x > 0:
            self.x += 1
        # Target to the left
        elif diff_x < 0:
            self.x -= 1
        # On target
        else:
            pass

        diff_y = target.y - self.y
        # Target to the bottom
        if diff_y > 0:
            self.y += 1
        # Target to the top
        elif diff_y < 0:
            self.y -= 1
        # On target
        else:
            pass

# A boundary check is also made to stop the predator moving off the perimeter of the environment
        self.check_boundaries()
    
# The final stage of the hunt is to kill the target when you land on it 
# If both the x and y coordinates are equal, the predator first 'eats' the sheep's store, then kills the target (calling the die function created in the sheep sub class)
        if self.y == target.y and self.x == target.x:
            self.store += target.store
            target.store = 0
            target.die()
    
# The predator will always hunt, so a simulate function is created to be used in the model    
    def simulate(self):
        self.hunt()