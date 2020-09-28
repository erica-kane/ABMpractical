import random
import operator
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation 
from itertools import combinations
import time
import csv
import agentframework
import requests
import bs4

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

# # Getting dimensions of environment 
# y_len = len(environment)
# x_len = len(environment[0])

# Creating a list for agents and variables
agents = []
num_of_agents = 10
num_of_it = 100
neighbourhood = 20

# ax.set_autoscale_on(False)

# scraping x and y data 
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})


# Make the agents 
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))

# Prove the agents have access to the list of agents 
agents[1].x
agents[5].agents[1].x


# initialise the graph
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Move the agents 

def update(frame_number):
    
    fig.clear()  

    matplotlib.pyplot.imshow(environment)

    #for _ in range(num_of_it):
    #random.shuffle(agents)
    for agent in agents:
        agent.move()
        agent.eat()
        agent.share(neighbourhood)

    for agent in agents:
        matplotlib.pyplot.scatter(agent.x, agent.y)
  

# Add a funciton that will run the model 
# .draw was used instead of .show as .show is deprecated 
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_it, repeat=False)
    canvas.draw()

# animation = matplotlib.animation.FuncAnimation(fig, update, interval = 1, repeat = False, frames = num_of_it)
# matplotlib.pyplot.show()

# Building the main window 
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop()


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





# # Distance between any 2 given agents
# agents[0].distance_between(agents[6])

# # start = time.process_time()

# # for loop to find the distance between every agent combination
# # This loop uses combinations, a function which returns tuples with no repeated combinations 
# # This removes pairs repeating and distances between the same agent 

# distance_list = []

# for first_agent, second_agent in combinations(agents, 2):
#     distance = first_agent.distance_between(second_agent)
#     distance_list.append(distance)

# for dist in distance_list:
#     if dist <= neighbourhood:
#         print(dist)

# # end = time.process_time()
# # print(end - start)

# # Finding the minimum and maximum distances 
# # print(distance_list)
# # max(distance_list)
# # min(distance_list)

# # Graph for times when agents increase 
# # agent_numbers = [10, 100, 500, 1000, 2000, 3000]
# # times = [0.0005, 0.0088, 0.1924, 0.7024, 2.7459, 6.1976]
# # matplotlib.pyplot.plot(agent_numbers, times, marker = 'o', color = "r")
# # matplotlib.pyplot.xlabel('Number of agents')
# # matplotlib.pyplot.ylabel('Time (s)')