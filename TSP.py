import numpy as np
import random
import pandas as pd

class City:

    def __init__(self, x, y):
        self.x = x
        self.y =  y

    def getDis(self, dest):
        xDistance = abs(self.x - dest.x)
        yDistance = abs(self.y - dest.y)
        dis = np.sqrt((xDistance** 2) + (yDistance ** 2))
        return dis

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

class Fitness:
    def __init__(self, path):
        self.path = path
        self.dis = 0
        self.fit = 0.0

    def routeDistance(self):
        if self.dis == 0:
            routeDis = 0
            for i in range(0, len(self.path)):
                cityFrom = self.path[i]
                cityTo = None

                if i + 1 < len(self.path):
                    cityTo = self.path[i + 1]
                else:
                    cityTo = self.path[0]

                routeDis = routeDis + cityFrom.getDis(cityTo)
            self.dis = routeDis
        return self.dis

    def routeFit(self):
        if self.fit == 0:
            self.fit = 1 / float(self.routeDistance())
        return self.fit



def makePath(citiesList):
    path = random.sample(citiesList, len(citiesList))
    return path

def initialPopulation(popSize, citiesList):
    population = []

    for i in range(0, popSize):
        population.append(makePath(citiesList))
    return population


def FitnessPerCity(population):
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFit()
    return sorted(fitnessResults.items())


def selection(rankPop, size):
    selectPop = []
    df = pd.DataFrame(np.array(rankPop), columns=["Index", "Fitness"])
    #print(df)


    for i in range(0, size):
        selectPop.append(rankPop[i][0])
    for i in range(0, len(rankPop) - size):
        pick = 100 * random.random()
        for i in range(0, len(rankPop)):
            if pick <= df.iat[i, 3]:
                selectPop.append(rankPop[i][0])
                break
    return selectPop


def mating(population, selectPop):
    matingPool = []
    for i in range(0, len(selectPop)):
        index = selectPop[i]
        matingPool.append(population[index])
    return matingPool


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




def offSpring(matingPool, fitSize):
    children = []
    length = len(matingPool) - fitSize
    pool = random.sample(matingPool, len(matingPool))

    for i in range(0, fitSize):
        children.append(matingPool[i])

    for i in range(0, length):
        child = crossover(pool[i], pool[len(matingPool) - i - 1])
        children.append(child)
    return children


def mutate(individual, mutRate):
    for swapped in range(len(individual)):
        if (random.random() < mutRate):
            swapWith = int(random.random() * len(individual))

            city1 = individual[swapped]
            city2 = individual[swapWith]

            individual[swapped] = city2
            individual[swapWith] = city1
    return individual


def mutPopulation(population, mutRate):
    mutatedPop = []

    for index in range(0, len(population)):
        mutIndex = mutate(population[index], mutRate)
        mutatedPop.append(mutIndex)
    return mutatedPop


def nGeneration(currentGen, fitSize, mutRate):
    rankPop = FitnessPerCity(currentGen)
    selectPop = selection(rankPop, fitSize)
    matingPool = mating(currentGen, selectPop)
    children = offSpring(matingPool, fitSize)
    nGeneration = mutPopulation(children, mutRate)
    return nGeneration


def geneticAlgorithm(population, popSize, fitSize, mutRate, gens):
    newPop = initialPopulation(popSize, population)
    #print("Initial distance: " + str(1 / FitnessPerCity(newPop)[0][1]))

    for i in range(0, gens):
        newPop = nGeneration(newPop, fitSize, mutRate)


    print("Final distance: " + str(1 / FitnessPerCity(newPop)[0][1]))
    bestRouteIndex = FitnessPerCity(newPop)[0][0]
    bestRoute = newPop[bestRouteIndex]
    print("Best Route:")
    return bestRoute