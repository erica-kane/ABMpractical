import random
import operator
import matplotlib.pyplot
from itertools import combinations
import time
import csv
import agentframework

# Read the CSV
environment = []
f = open('in.txt', newline = '')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)

# This code could be written like this:
# environment = list(reader)
# But a loop was used for practice 

for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)

f.close()

# Getting dimensions of environment 
y_len = len(environment)
x_len = len(environment[0])

# Make an single agent object
a = agentframework.Agent(environment)
print(a)
print(a.x, a.y)
a.move()
print(a.x, a.y)

# Function to find the distance between 2 agents 
def distance_between(agent_a, agent_b):
    diff_y = (agent_a.x - agent_b.x)
    diff_x = (agent_a.y - agent_b.y)
    distance = (diff_y**2 + diff_x**2)**0.5
    return distance

# Creating a list for agents and variables
agents = []
num_of_agents = 10 
num_of_it = 100

# Make the agents 
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))
print(agents)

# Drawning an initial plot to compare 
matplotlib.pyplot.ylim(0, y_len)
matplotlib.pyplot.xlim(0, x_len)
matplotlib.pyplot.imshow(environment)
for agent in agents:
    matplotlib.pyplot.scatter(agent.x, agent.y)
# m = max(agents, key=operator.itemgetter(1))
# matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()

# Move the agents 
for _ in range(num_of_it):
    for agent in agents:
        agent.move()
        agent.eat()
        agent.sick()

# Plot agent locations 
matplotlib.pyplot.ylim(0, y_len)
matplotlib.pyplot.xlim(0, x_len)
matplotlib.pyplot.imshow(environment)
for agent in agents:
    matplotlib.pyplot.scatter(agent.x, agent.y)
# m = max(agents, key=operator.itemgetter(1))
# matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()

# Writing out environment as a csv file 
envifile = open('envifile.txt', 'w', newline = '')
writer = csv.writer(envifile)
writer.writerows(environment)
envifile.close()

# Write out total amount stored by all agents 
totalstore = 0
for agent in agents:
     totalstore = agent.store + totalstore
storefile = open('storefile.txt', 'a')
storefile.write('Total agent store: ' + str(totalstore) + '\n')
storefile.close()


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