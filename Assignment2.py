
from CSCI_4610_Assignment_2.TSP import City, geneticAlgorithm

cities = []
def addtoPopulation(x1,y1):

    cities.append(City(x = x1, y = y1))



addtoPopulation(20,20)
addtoPopulation(20,40)
addtoPopulation(20,160)
addtoPopulation(40, 120)
addtoPopulation(60,20)
addtoPopulation(60,80)
addtoPopulation(60,200)
addtoPopulation(80,180)
addtoPopulation(100,40)
addtoPopulation(100, 120)
addtoPopulation(100,160)
addtoPopulation(120,80)
addtoPopulation(140, 140)
addtoPopulation(140,180)
addtoPopulation(160,80)
addtoPopulation(180, 60)
addtoPopulation(180,100)
addtoPopulation(180,200)
addtoPopulation(200,40)
addtoPopulation(200,160)


print(geneticAlgorithm(population= cities, popSize=20, eliteSize=20, mutationRate=0.01, generations=100))

