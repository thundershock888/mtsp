import matplotlib;
import numpy as np
import time as timer

matplotlib.use("TkAgg")
from galogic import *
from route import *
import matplotlib.pyplot as plt
import progressbar
from matplotlib.animation import FuncAnimation

pbar = progressbar.ProgressBar()

startTime = timer.time()

# Add Dustbins
for i in range(numNodes):
    RouteManager.addDustbin(Dustbin())

random.seed(seedValue)
routeData = []  # Fittest value (distance)
yaxis = []  # Fittest value (distance)
xaxis = []  # Generation count

pop = Population(populationSize, True)
globalRoute = pop.getFittest()
print('Initial minimum distance: ' + str(globalRoute.getDistance()))

# Start evolving
for i in pbar(range(populationSize)):
    pop = GA.evolvePopulation(pop)
    localRoute = pop.getFittest()
    if globalRoute.getDistance() > localRoute.getDistance():
        globalRoute = localRoute
    routeData.append(globalRoute)
    yaxis.append(localRoute.getDistance())
    xaxis.append(i)



print('Global minimum distance: ' + str(globalRoute.getDistance()))
print('Final Route: ' + globalRoute.toString())
CPUTime = timer.time() - startTime
print("CPU time (s): {:.2f}".format(CPUTime))

fig = plt.figure()
plt.plot(xaxis, yaxis, 'r-')

# create the figure and axes objects
fig2, ax = plt.subplots()

# Graph final route paths
x = []
y = []

# Enumerates each agent's path
for salesman in range(numTrucks):
    for path in range(len(globalRoute.route[salesman])):
        x.append(globalRoute.getDustbin(salesman, path).getX())
        y.append(globalRoute.getDustbin(salesman, path).getY())
        ax.annotate(str(path), xy=(globalRoute.getDustbin(salesman, path).getX(),
                                   globalRoute.getDustbin(salesman, path).getY()))
    # Returns each agent to first position
    x.append(globalRoute.getDustbin(0, 0).getX())
    y.append(globalRoute.getDustbin(0, 0).getY())
    ax.annotate(str(0), xy=(globalRoute.getDustbin(0, 0).getX(),
                            globalRoute.getDustbin(0, 0).getY()))

    startingIndex = (len(x) - len(globalRoute.route[salesman])) - 1  # Starting index for each agent
    #print(startingIndex)
    if startingIndex == 0:
        ax.plot(x, y, label=salesman)   # Plot first agent route
    else:
        ax.plot(x[startingIndex:], y[startingIndex:], label=salesman)  # Plot rest of agent routes

ax.legend(loc='best')
ax.scatter(x, y)
plt.show()


# function that draws each frame of the animation
def update(i):
    x = []
    y = []
    for salesman in range(numTrucks):
        for path in range(routeData[i].routeLengths[salesman]):
            x.append(routeData[i].getDustbin(salesman, path).getX())
            y.append(routeData[i].getDustbin(salesman, path).getY())
            ax.annotate(str(path), xy=(routeData[i].getDustbin(salesman, path).getX(),
                                       routeData[i].getDustbin(salesman, path).getY()))

    ax.plot(x, y, label=salesman)

    ax.clear()
    ax.scatter(x, y, c="red")
    ax.legend(loc='best')

# ani = FuncAnimation(fig2, update, frames=populationSize, interval=500, repeat=True)
# plt.show()
