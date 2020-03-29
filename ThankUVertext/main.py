from DirectedGraph import DirectedGraph
from TopSort import TopSort
from Label import createLabel
from random import sample,randrange,shuffle

def createRandomDAGIter(n):
	# Create new DirectedGraph and add n amount of nodes to it
	g = DirectedGraph()
	for i in range(1,n+1):
		g.addNode(createLabel(i))
		
	# Copy the list of the nodes from the graph
	# so we can pop from list
	nodes = g.getAllNodes().copy()
	
	# Shuffle the nodes so the graph doesn't
	# start with "A" every time
	shuffle(nodes)
	# While there are nodes in the list
	while len(nodes) > 0:
		cur = nodes.pop(0)
		if len(nodes)<=1:
			break
			
		# XXX Choose a random amount of children XXX
		# Make nodes have 2 children
		num = 2 # randrange(1,len(nodes))
		
		# Add a random sample of num length
		# the neighbor of the cur
		for i in sample(nodes,num): g.addDirectedEdge(cur, i)
		
		# For every neighbor of cur do the same
		for n in cur.neighbors:
			nodes.pop(nodes.index(n))
			if len(nodes) <= 1:
				break
			num = 2 # randrange(1,len(nodes))
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