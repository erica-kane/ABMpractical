import random
import operator
import matplotlib.pyplot
from itertools import combinations
import time

# Function to find the distance between 2 agents 
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

# Plot agent locations 
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1], agents[i][0])
# m = max(agents, key=operator.itemgetter(1))
# matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()

# Distance between any 2 agents (any number between 0 and 9 can be given)
distance_between_2 = distance_between(agents[0], agents[1])
print(distance_between_2)

# Creating an empty list for the distances to append to
# We can append distance values to this in the for loop, to later find the max and min
distance_list = []

start = time.process_time()

# for loop to find the distance between every agent combination
# This loop uses combinations, a function which returns tuples with no repeated combinations 
# This removes pairs repeating and distances between the same agent 

for first_agent, second_agent in combinations(agents, 2):
    distance = distance_between(first_agent, second_agent)
    distance_list.append(distance)
print(distance_list)

end = time.process_time()
print(end - start)

# Finding the minimum and maximum distances 
print(distance_list)
max(distance_list)
min(distance_list)

# Graph for times when agents increase 
agent_numbers = [10, 100, 500, 1000, 2000, 3000]
times = [0.0005, 0.0088, 0.1924, 0.7024, 2.7459, 6.1976]
matplotlib.pyplot.plot(agent_numbers, times, marker = 'o', color = "r")
matplotlib.pyplot.xlabel('Number of agents')
matplotlib.pyplot.ylabel('Time (s)')