
from TSP import City, geneticAlgorithm
from pandas import read_csv, DataFrame
import matplotlib.pyplot as plt

cities = []
cities1 = []
map_graph =  {}
map_graph2 =  {}
def addtoPopulation(x1,y1):

    cities.append(City(x = x1, y = y1))

def addtoPopulation2(x1,y1):

    cities2.append(City(x = x1, y = y1))


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

#Problem Domain 1

print("\nProblem domain 1 ")

route = (geneticAlgorithm(population= cities, popSize=20, fitSize=20, mutRate=0.05, gens=100))

print(route)



#map_graph = list(zip(route, route[1:] + route[:1]))

for v, w in zip(route[:-1], route[1:]):
    map_graph[v] = w


x = []
y = []

# Each Key and Value are edges, key are edges
#print(map_graph)
#print("\n\n")


for key,value in map_graph.items():
    p = str(key)



    i = p.split(",")
    q= i[0].split("(")

    x.append(int(q[1]))

    c = i[1].split(")")

    y.append(int(c[0]))




x.append(x[0])
y.append(y[0])






# Problem Domain 2
df = read_csv('Distances.csv', index_col=False)
cities2 = list(df.columns)[1:]
p1 = []
p2 = []
for v0 in range(0,len(cities2)):
        for v1 in range(v0+1, len(cities2)):
            p1.append(df[cities2[v0]][v1])
        if p1:
            a = (v0 , min(p1))
        else:
            a = (v0, 0)
        p2.append(a)
        p1.clear()


print("\nProblem domain 2 ")
#print(p2)


x2 = []
y2 = []

for e in p2:

    o = str(e)

    n = o.split(",")

    p = n[0].split("(")

    x2.append(int(p[1]))

    b = n[1].split(")")

    y2.append(int(b[0]))


for i in range(len(x2)):
    cities1.append(City(x2[i], y2[i]))


#print(cities1)
route2 = (geneticAlgorithm(population= cities1, popSize=8, fitSize=8, mutRate=0.5, gens= 50))

print(route2)


for c, z in zip(route2[:-1], route2[1:]):
    map_graph2[c] = z


x3 = []
y3 = []


for key,value in map_graph2.items():
    p = str(key)



    i = p.split(",")
    q= i[0].split("(")

    x3.append(int(q[1]))

    c = i[1].split(")")

    y3.append(int(c[0]))




x3.append(x3[0])
y3.append(y3[0])




f = plt.figure(1)
plt.plot(x, y, 'bo-')
plt.title('Travelling Salesmen Problem 1')
plt.ylabel('Y position')
plt.xlabel('X position')


g= plt.figure(2)
plt.plot(x3, y3, 'ro-')
plt.title('Travelling Salesmen Problem 2')
plt.ylabel('Y position')
plt.xlabel('X position')


plt.show()


