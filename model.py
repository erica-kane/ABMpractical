import random
import operator
import matplotlib.pyplot

# Creating a list for agents 
agents = []

# Set y0 and x0 to a random value
#y0 = random.randint(0,99)
#x0 = random.randint(0,99)
#print(y0, x0)
agents.append([random.randint(0,99),random.randint(0,99)])
print(agents)

# Move y0 randomly
if random.random() < 0.5:
    agents[0][0] = agents[0][0] + 1
else:
    agents[0][0] = agents[0][0] - 1

# Move x0 randomly
if random.random() < 0.5:
    agents[0][1] = agents[0][1] + 1
else:
    agents[0][1] = agents[0][1] - 1
print(agents[0][0], agents[0][1])

# Set y1 and x1 to a random value 
#y1 = random.randint(0,99)
#x1 = random.randint(0,99)
#print(y1, x1)
agents.append([random.randint(0,99),random.randint(0,99)])
print(agents)

# Move y1 randomly
if random.random() < 0.5:
    agents[1][0] = agents[1][0] + 1
else:
    agents[1][0] = agents[1][0] - 1

# Move x1 randomly 
if random.random() < 0.5:
    agents[1][1] = agents[1][1] + 1
else:
    agents[1][1] = agents[1][1] - 1
print(agents[1][0], agents[1][1])

print(agents)
# Answer = pythaian distance between y0,x0 and y1,x1
answer = (((agents[0][0] - agents[1][0])**2) + \
    ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)

# Which agent is furthest east? (highest x)
print(max(agents))
print(max(agents, key=operator.itemgetter(1)))

# Plot agent locations 
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()