import numpy as np
import random
import pandas as pd

class City:

    def __init__(self, x, y):
        self.x = x
        self.y =  y

    def get_distance(self, dest):
        xDistance = abs(self.x - dest.x)
        yDistance = abs(self.y - dest.y)
        distance = np.sqrt((xDistance** 2) + (yDistance ** 2))
        return distance

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def routeDistance(self):
        if self.distance == 0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                fromCity = self.route[i]
                toCity = None

                if i + 1 < len(self.route):
                    toCity = self.route[i + 1]
                else:
                    toCity = self.route[0]

                pathDistance = pathDistance + fromCity.get_distance(toCity)
            self.distance = pathDistance
        return self.distance

    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness



def createRoute(cityList):
    route = random.sample(cityList, len(cityList))
    return route

def initialPopulation(popSize, cityList):
    population = []

    for i in range(0, popSize):
        population.append(createRoute(cityList))
    return population


def FitnessForEachCity(population):
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFitness()
    return sorted(fitnessResults.items())


def selection(popRanked, size):
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index", "Fitness"])
    #print(df)


    for i in range(0, size):
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - size):
        pick = 100 * random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i, 3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults


def mating(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool


def crossover(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []

    cityA = int(random.random() * len(parent1))
    cityB = int(random.random() * len(parent1))

    startCity = min(cityA, cityB)
    endCity = max(cityA, cityB)

    for i in range(startCity, endCity):
        childP1.append(parent1[i])

    for item in parent2:
        if item not in childP1:
            childP2.append(item)

    child = childP1 + childP2
    return child




def offSpring(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, eliteSize):
        children.append(matingpool[i])

    for i in range(0, length):
        child = crossover(pool[i], pool[len(matingpool) - i - 1])
        children.append(child)
    return children


def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if (random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))

            city1 = individual[swapped]
            city2 = individual[swapWith]

            individual[swapped] = city2
            individual[swapWith] = city1
    return individual


def mutatePopulation(population, mutationRate):
    mutatedPop = []

    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop


def nextGeneration(currentGen, eliteSize, mutationRate):
    popRanked = FitnessForEachCity(currentGen)
    selectionResults = selection(popRanked, eliteSize)
    matingpool = mating(currentGen, selectionResults)
    children = offSpring(matingpool, eliteSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration


def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
    pop = initialPopulation(popSize, population)
    #print("Initial distance: " + str(1 / FitnessForEachCity(pop)[0][1]))

    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)


    print("Final distance: " + str(1 / FitnessForEachCity(pop)[0][1]))
    bestRouteIndex = FitnessForEachCity(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    print("Best Route:")
    return bestRoute