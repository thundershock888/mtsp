import matplotlib;
import time as timer

matplotlib.use("TkAgg")
from galogic import *
from route import *
import matplotlib.pyplot as plt
import progressbar


pbar = progressbar.ProgressBar()

startTime = timer.time()

# Add Dustbins

for i in range(numNodes):
    RouteManager.addDustbin(Dustbin())

xaxis = []  # Generation count
yaxis = []  # Fittest value (distance)
routeData = []  # Fittest value (distance)
random.seed(seedValue)
pop = Population(populationSize, True)
globalRoute = pop.getFittest()

print('Initial minimum distance: ' + str(globalRoute.getDistance()))

# Start evolving
for i in pbar(range(populationSize)):
    pop = GA.evolvePopulation(pop)
    localRoute = pop.getFittest()

    if(localRoute.getDistance() < globalRoute.getDistance()):
        globalRoute = localRoute
    routeData.append((globalRoute))
    xaxis.append(i)
    yaxis.append(localRoute.getDistance())




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

# Enumerates each agent's path, so we can plot it
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



