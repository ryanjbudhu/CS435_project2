from Graph import Graph
from GraphSearch import GraphSearch
from Label import createLabel
import random

def createRandomUnweightedGraphIter(n):
	g = Graph()
	for i in range(1,n+1):
		g.addNode(createLabel(i))
	neighs = random.randrange(1,n//3)
	nodes = g.getAllNodes()
	for i in nodes:
		x = nodes.index(i)
		suggested = random.sample(nodes[:x]+nodes[x+1:],neighs)
		for j in suggested:
			g.addUndirectedEdge(i, j)
	return g

def createLinkedList(n):
	g = Graph()
	for i in range(1,n+1):
		g.addNode(createLabel(i))
	nodes = g.getAllNodes()
	for i in range(len(nodes)-1):
		nodes[i].neighbors.append(nodes[i+1])
	return g

def BFTRecLinkedList(graph):
	pass

def BFTIterLinkedList(graph):
	pass

g = createRandomUnweightedGraphIter(20)
#g = createLinkedList(1000)
gs = GraphSearch()
allNodes = g.getAllNodes()
#path = gs.DFSRec(allNodes[0], allNodes[1])
#path = gs.DFSIter(allNodes[0], allNodes[1])
#path = gs.BFTRec(g)
#path = gs.BFTIter(g)
if path:
	for p in path:
		print(p.name)
else:
	print("No path")