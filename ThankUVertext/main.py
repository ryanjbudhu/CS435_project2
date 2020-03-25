from DirectedGraph import DirectedGraph
from TopSort import TopSort
from Label import createLabel
from random import sample,randrange,choice

def createRandomDAGIter(n):
	g = DirectedGraph()
	for i in range(1,n+1):
		g.addNode(createLabel(i))
	nodes = g.getAllNodes()
	weights = list(range(0,len(nodes),10))
	order =[]
	for i in nodes:
		neighs = randrange(1, n//2)
		x = nodes.index(i)
#		suggested = choices(nodes[:x]+nodes[x+1:],weights=weights[:x]+weights[x+1:],k=neighs)
		suggested = sample(nodes[:x]+nodes[x+1:],k=neighs)
		for j in suggested:
			if j == nodes[0]:
				g.addDirectedEdge(i, choice(nodes[1:nodes.index(i)]+nodes[nodes.index(i)+1:]))
				continue
			g.addDirectedEdge(i, j)
#	choice(nodes).neighbors = []
	return g


def test():
	g = createRandomDAGIter(5)
	ts = TopSort()
	print([{i.name:[j.name for j in i.neighbors]} for i in g.getAllNodes()])
	kahnsPath = ts.Kahns(g)
#	mDFSPath = ts.mDFS(g)
	print([i.name for i in kahnsPath])
#	print([i.name for i in mDFSPath])
test()