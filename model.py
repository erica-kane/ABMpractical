import random
import operator
import matplotlib.pyplot

# Creating a list for agents and variables
agents = []
num_of_agents = 10
num_of_it = 100

# Creating co-ordinates for the amount of agents we set (10)
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
print(agents)

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


# # Answer = pythaian distance between y0,x0 and y1,x1
# answer = (((agents[0][0] - agents[1][0])**2) + \
#     ((agents[0][1] - agents[1][1])**2))**0.5
# print(answer)

# # Which agent is furthest east? (highest x)
# print(max(agents))
# print(max(agents, key=operator.itemgetter(1)))

# Plot agent locations 
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1], agents[i][0])
# m = max(agents, key=operator.itemgetter(1))
# matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()