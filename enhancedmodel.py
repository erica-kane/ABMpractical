# Import the necessary libraries and the classes from the framework 
import random
import operator
import matplotlib
import matplotlib.pyplot
import matplotlib.animation 
import csv
from enhancedframework import Sheep, Pred


# Read the CSV
environment = []
f = open('in.txt', newline = '')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)

environment = list(reader)

f.close()


# Getting dimensions of environment 
y_len = len(environment)
x_len = len(environment[0])


# Creating a list for all agents and initialising variables
herd = []
preds = []
num_of_sheep = 20
num_of_preds = 10
num_of_it = 100


# Make the sheep
for i in range(num_of_sheep):
    herd.append(Sheep(environment, herd, preds))


# Make the predators 
for i in range(num_of_preds):
    preds.append(Pred(environment, herd, preds))


# Initialise the graph
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# Move the agents
# Set the size of the point to be equal to the store, to show how the sheep grow as they eat, and the predators grow as they kill (eat) the sheep
# This also tests that the predators are eating the sheep correctly  

def update(frame_number):
    
    fig.clear()  

    matplotlib.pyplot.imshow(environment)

# The sheep's action is specified as it can do either exclusively of the other
    for sheep in herd:
        sheep.move()
        sheep.eat()

# The predator is simulated because all its actions are essential and defined within the sub class 
    for pred in preds:
        pred.simulate()

    for sheep in herd:
        matplotlib.pyplot.scatter(sheep.x, sheep.y, c = 'w', s = sheep.store)
    for pred in preds:
        matplotlib.pyplot.scatter(pred.x, pred.y, c = 'k', marker = 'v', s = pred.store + 50)
  

animation = matplotlib.animation.FuncAnimation(fig, update, interval = 1, repeat = False, frames = num_of_it)
matplotlib.pyplot.show()

