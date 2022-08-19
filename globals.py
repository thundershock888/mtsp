import random
import math
'''
All Globals needed listed below
'''

xMax = 200
yMax = 200
seedValue = 1
numNodes = 20
numGenerations = 14
# size of population
populationSize = 20
mutationRate = 0.02
tournamentSize = 10
elitism = True
numTrucks = 4

def random_range(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""

    #below is code that name a random list whose n-1 elements sum to total
    sample = random.sample(range(1, total), n - 1)
    #sort list
    dividers = sorted(sample)
    #joins the two following lists: dividers + [total], [0] + dividers into list
    zipped = zip(dividers + [total], [0] + dividers)
    #returns random object a - b from zipped
    return [a - b for a, b in zipped]

# Randomly distribute number of dustbins to subroutes
# Maximum and minimum values are maintained to reach optimal result

def route_lengths():

    upper = (numNodes + numTrucks - 1)
    fa = upper/numTrucks*1.6 # max route length
    fb = upper/numTrucks*0.6 # min route length
    a = random_range(numTrucks, upper)
    while 1:
        if all( i < fa and i > fb  for i in a):
                break
        else:
                a = random_range(numTrucks, upper)
    return a
