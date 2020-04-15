from random import randint,shuffle
from math import sqrt,floor
from GridGraph import GridGraph
from Label import createLabel

def createRandomGridGraph(n):
	g = GridGraph()
	cols = n # floor(sqrt(n)) # Pick how long each row is
	rowcount = colcount = 0
	randomNums = list(range(1,n**2+1)) # randomize range list 1..n^2
	shuffle(randomNums)
	for idx in randomNums:
		if colcount == cols:
			colcount = 0
			rowcount += 1
		x = rowcount
		y = colcount
		g.addGridNode(x, y, createLabel(idx)) # Insert a node at (x,y)
		nodes = g.getAllNodes() # Get the updated node grid
		if colcount > 0: # If its not the leftmost node in grid
			if randint(0, 2): # 2/3 chance of creating a node, 50% was too little
				g.addUndirectedEdge(nodes[x][y-1], nodes[x][y])
		if idx > cols: # If its not the first row
			if randint(0, 2): # 2/3 chance of creating a node, 50% was too little
				g.addUndirectedEdge(nodes[x-1][y], nodes[x][y])
		colcount += 1
	return g


def astar(start, end):
	start.g = start.h = start.value = 0
	openList = [start] # Queue of nodes yet to finalize
	closedList = [] # Nodes its seen, "finalized"
	while openList:
		cur = min(openList, key=lambda x: x.value) # Pick node with lowest f
		openList.remove(cur) # Remove it from the open list
		closedList.append(cur) # finalize current
		if cur == end: # If the current node is the target node
			path = []
			current = cur
			while current is not None:
				path.insert(0,current)
				current = current.parent
			return path,len(closedList)
		for child in cur.neighbors: # add the neighbors to open if not finalized
			if child in closedList:
				continue
			child.g = cur.g+1
			child.h = abs(child.x - end.x) + abs(child.y - end.y)
			child.value = child.g + child.h
			child.parent = cur
			for node in openList:
				if child == node and child.g > node.g:
					continue
			openList.append(child)
	return [],len(closedList) # if end isn't found


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
	n = 15
	g = createRandomGridGraph(n)
	nodes = g.getAllNodes()
	sourceNode = nodes[0][0]
	destNode = nodes[n-1][n-1]
#	printGrid(nodes,showN)
	path,visited = astar(sourceNode, destNode)
	print([i.name for i in path])
	print()
	print("Nodes visited:",visited)
	
testGrid(False)