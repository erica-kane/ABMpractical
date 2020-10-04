import random

# Initialising the class, ensuring that the agents have access to the environment and each other
# Agents must be provided with x's and y's to be initialised (scraped data in the model)
# Providing the agent with a y.max and x.max to link the maximum coordinate to the length of the environment when moving
class Agent():
    def __init__(self, environment, agents, y, x):
        self.y_max = len(environment) - 1
        self.x_max = len(environment[0]) - 1
        self.y = y
        self.x = x
        self.environment = environment
        self.store = 0 
        self.agents = agents


# Creating the movement function
# Agents move randomly, on their x and y axis by 1 (if they go over the environment boundary they wrap round the other side)
    def move (self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % self.y_max
        else:
            self.y = (self.y - 1) % self.y_max 

        if random.random() < 0.5:
            self.x = (self.x + 1) % self.x_max
        else:
            self.x = (self.x - 1) % self.x_max


# Creating eat function 
# Agents eat from the environment if the value is over 10 (taking 10 from the environment and adding 10 to their store)
# If the environment is less than 10, they add the specific amount remaining to their store and it is taken from the environment
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] -= self.environment[self.y][self.x]

# Agents are sick if they eat too much
# Whent the stores go above 100, the contents of their store is put back into the environment and the store is reset to 0
        if self.store > 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0 


# Creating share function 
# To make the agents share you must initialise them with a neighbouhood value 
# For each agent, distance is calculated, and if the distance is less than the neighbourhood value, their stores are set to the average of both
# This does not happen for agents with themselves
# A print statement is made after every share, stating the distance they were apart to check it was under 20, and the average the store was set to
    def share(self, neighbourhood):
        for agent in self.agents:
            if agent != self:
                distance = self.distance_between(agent)
                if distance <= neighbourhood:
                    sum = self.store + agent.store
                    average = sum/2
                    self.store = average 
                    agent.store = average 
                    print("sharing " + str(distance) + " " + str(average))
    

# Creating distance funcion 
# This is used in the sharing process above, and must be initialised with an agent to calculate the distance with 
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5


# String representation
    def __str__(self):
        return 'Agent: ' + 'x = ' + str(self.x) + ', y = ' + str(self.y) + ', store = ' + str(self.store)

