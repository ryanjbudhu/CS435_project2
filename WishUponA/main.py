from random import randint
from math import sqrt,floor
from GridGraph import GridGraph
from Label import createLabel

def createRandomGridGraph(n):
	g = GridGraph()
	cols = n # floor(sqrt(n)) # Pick how long each row is
	rowcount = colcount = 0
	idx = 1
	while idx <= n**2:
		if colcount == cols:
			colcount = 0
			rowcount += 1
		x = rowcount
		y = colcount
		g.addGridNode(x, y, createLabel(idx)) # Insert a node at (x,y)
		nodes = g.getAllNodes() # Get the updated node grid
		if colcount > 0: # If its not the leftmost node in grid
			if randint(0, 1):
				g.addUndirectedEdge(nodes[x][y-1], nodes[x][y])
		if idx > cols: # If its not the first row
			if randint(0, 1):
				g.addUndirectedEdge(nodes[x-1][y], nodes[x][y])
		colcount += 1
		idx += 1
	return g


def astar(start):
	openList = {start:0}
	closedList = []
	
	while openList:
		q = min(openList, key=lambda x: openList[x])
		cur = openList[q]
		del openList[q]
		print(q,':',cur)
		closedList.append(q)
	return closedList


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

def testGrid(showN=False):
	n = 10
	g = createRandomGridGraph(n)
	nodes = g.getAllNodes()
	sourceNode = nodes[0][0]
	destNode = nodes[n-1][n-1]
	printGrid(nodes,showN)
testGrid(False)

'''
A	B	C
D	E	F
G	H	I
J	K	L
M	N
'''