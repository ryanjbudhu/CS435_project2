from WeightedGraph import WeightedGraph

from Label import createLabel
from random import randint
from TreadmillMazeSolver import TreadmillMazeSolver
from math import sqrt,floor

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

def createRandomCompleteWeightedBoxGraph(n):
	g = WeightedGraph()
	for i in range(1,n+1):
		g.addNode(createLabel(i))
	nodes = g.getAllNodes()
	cols = floor(sqrt(len(nodes)))
	rowcount = colcount = idx = 0
	while idx < len(nodes):
		nodes[idx].x = rowcount
		nodes[idx].y = colcount
		randomWeight = randint(1, 15)
		if colcount == cols:
			colcount = 0
			rowcount += 1
		if colcount > 0:
			g.addDirectedEdge(nodes[idx-1], nodes[idx], randomWeight)
		if idx > cols - 1:
			g.addDirectedEdge(nodes[idx-cols], nodes[idx], randomWeight)
		
		colcount += 1
		idx += 1
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
	g = createRandomCompleteWeightedGraph(10)
	ts = TreadmillMazeSolver()
	#printGraph(g.getAllNodes())
	path,old = ts.dijkstras(g.getAllNodes()[0])
	print('old:',[{i.name:old[i]} for i in old])
	print('new:',[{i.name:path[i]} for i in path])
	#g = createLinkedList(10)

g = createRandomCompleteWeightedBoxGraph(25)
printGraph(g.getAllNodes())

'''
A	B	C
D	E	F
G	H	I
J	K	L
M	N
'''