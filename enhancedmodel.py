import random
import operator
import matplotlib
import matplotlib.pyplot
import matplotlib.animation 
import csv
import sheepframework
import predframework


# Read the CSV
environment = []
f = open('in.txt', newline = '')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)

environment = list(reader)

f.close()


# # Getting dimensions of environment 
y_len = len(environment)
x_len = len(environment[0])


# Creating a list for agents and variables
herd = []
preds = []
num_of_sheep = 20
num_of_preds = 10
num_of_it = 100


# Make the agents 
for i in range(num_of_sheep):
    herd.append(sheepframework.Sheep(environment, herd, preds))


# Make the predators 
for i in range(num_of_preds):
    preds.append(predframework.Pred(environment, preds, herd))


# initialise the graph
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Move the agents 

def update(frame_number):
    
    fig.clear()  

    matplotlib.pyplot.imshow(environment)

    #random.shuffle(agents)
    for sheep in herd:
        sheep.move()
        sheep.eat()

    for sheep in herd:
        matplotlib.pyplot.scatter(sheep.x, sheep.y, c = 'w')
    for pred in preds:
        matplotlib.pyplot.scatter(pred.x, pred.y, c = 'k', marker = 'v')
  

animation = matplotlib.animation.FuncAnimation(fig, update, interval = 1, repeat = False, frames = num_of_it)
matplotlib.pyplot.show()

