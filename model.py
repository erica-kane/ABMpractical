import random
import operator
import matplotlib.pyplot

def distance_between(agents_row_a, agents_row_b):
    diff_y = (agents_row_a[0] - agents_row_b[0])
    diff_x = (agents_row_a[1] - agents_row_b[1])
    distance = (diff_y**2 + diff_x**2)**0.5
    return distance

# Creating a list for agents and variables
agents = []
num_of_agents = 10
num_of_it = 100

# Creating co-ordinates for the amount of agents we set (10)
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
print(agents)

# Randomly moving our 10 agents 100 times 
for _ in range(num_of_it):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
print(agents)

# Answer = pythaian distance between agents
distance_between(agents[0], agents[1])

# for loop for every agent 
for first_agent in agents:
    for second_agent in agents:
        distance = distance_between(first_agent, second_agent)
        print(first_agent, second_agent, distance)

# Plot agent locations 
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1], agents[i][0])
# m = max(agents, key=operator.itemgetter(1))
# matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()