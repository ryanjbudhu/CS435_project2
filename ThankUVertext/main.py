from DirectedGraph import DirectedGraph
from TopSort import TopSort
from Label import createLabel
from random import sample,randrange,choice,shuffle

def createRandomDAGIter(n):
	g = DirectedGraph()
	for i in range(1,n+1):
		g.addNode(createLabel(i))
	nodes = g.getAllNodes().copy()
	shuffle(nodes)
	total = len(nodes)
	while len(nodes) > 0:
		cur = nodes.pop(0)
		if len(nodes)<=1:
			break
		num = randrange(1,len(nodes))
		for i in sample(nodes,num): g.addDirectedEdge(cur, i)
		for n in cur.neighbors:
			nodes.pop(nodes.index(n))
			if len(nodes) <= 1:
				break
			num = randrange(1,len(nodes))
			for i in sample(nodes,num): g.addDirectedEdge(n, i)
	return g


def test():
	g = createRandomDAGIter(15)
	ts = TopSort()
	print([{i.name:[j.name for j in i.neighbors]} for i in g.getAllNodes()])
	print()
	kahnsPath = ts.Kahns(g)
	mDFSPath = ts.mDFS(g)
	print("Kahn's Algorithm:")
	print([i.name for i in kahnsPath])
	print("mDFS Algorithm:")
	print([i.name for i in mDFSPath])
test()