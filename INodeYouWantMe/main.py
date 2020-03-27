from WeightedGraph import WeightedGraph
from Label import createLabel
from random import randint

def createRandomCompleteWeightedGraph(n):
	g = WeightedGraph()
	for i in range(1,n+1):
		g.addNode(createLabel(i))
	nodes = g.getAllNodes()
	for i in nodes:
		x = nodes.index(i)
		suggested = nodes[:x]+nodes[x+1:]
		for j in suggested:
			randomWeight = randint(1, 15)
			g.addDirectedEdge(i, j, randomWeight)
	return g

def createLinkedList(n):
	g = WeightedGraph()
	for i in range(1, n+1):
		g.addNode(createLabel(i))
	nodes = g.getAllNodes()
	for i in range(len(nodes)-1):
		nodes[i].neighbors[nodes[i+1]] = 1
	return g

#g = createRandomCompleteWeightedGraph(10)
g = createLinkedList(10)
nodes = g.getAllNodes()
#exit()
for i in nodes:
	print(i.name)
	for j in i.neighbors:
		print('\t',j.name,':',i.neighbors[j])