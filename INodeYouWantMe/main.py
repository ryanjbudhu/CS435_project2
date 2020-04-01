from WeightedGraph import WeightedGraph
from GridGraph import GridGraph
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

def createRandomGridGraph(n):
	g = GridGraph()
	cols = floor(sqrt(n)) # Pick how long each row is
	rowcount = colcount = 0
	idx = 1
	while idx <= n:
		if colcount == cols:
			colcount = 0
			rowcount += 1
		x = rowcount
		y = colcount
		g.addGridNode(x, y, createLabel(idx)) # Insert a node at (x,y)
		nodes = g.getAllNodes() # Get the updated node grid
		if colcount > 0: # If its not the leftmost node in grid
			g.addUndirectedEdge(nodes[x][y-1], nodes[x][y])
		if idx > cols: # If its not the first row
			g.addUndirectedEdge(nodes[x-1][y], nodes[x][y])
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
			
def printGrid(nodes, edges=False):
	for x in nodes:
		print([i.name for i in x])
	if edges:
		print()
		for x in nodes:
			for y in x:
				print(y.name)
				for edge in y.neighbors:
					print('\t',y.name, ':', edge.name)

def test():
	g = createRandomCompleteWeightedGraph(10)
	ts = TreadmillMazeSolver()
	#printGraph(g.getAllNodes())
	path,old = ts.dijkstras(g.getAllNodes()[0])
	print('old:',[{i.name:old[i]} for i in old])
	print('new:',[{i.name:path[i]} for i in path])
	#g = createLinkedList(10)

def testGrid():
	newg = createRandomGridGraph(90)
	printGrid(newg.getAllNodes(), edges=True)

'''
A	B	C
D	E	F
G	H	I
J	K	L
M	N
'''