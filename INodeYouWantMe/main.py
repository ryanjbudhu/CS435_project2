from WeightedGraph import WeightedGraph
from Label import createLabel
from random import randint
from TreadmillMazeSolver import TreadmillMazeSolver

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

def printGraph(nodes):
	for i in nodes:
		print(i.name)
		for j in i.neighbors:
			print('\t',j.name,':',i.neighbors[j])
			

def test():
	g = createRandomCompleteWeightedGraph(1000)
	ts = TreadmillMazeSolver()
	#printGraph(g.getAllNodes())
	path,old = ts.dijkstras(g.getAllNodes()[0])
#	print('old:',[{i.name:old[i]} for i in old])
	print('new:',[{i.name:path[i]} for i in path])
	print("Length:", len(path))
	#g = createLinkedList(10)
test()