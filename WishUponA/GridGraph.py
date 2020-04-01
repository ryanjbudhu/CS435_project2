class GridGraph:
	class Node:
		def __init__(self, name, x=0, y=0):
			self.name = name
			self.x = x
			self.y = y
			self.neighbors = []
	def __init__(self):
		self.nodes = []
	
	def addGridNode(self, x, y, nodeName):
		# Edge cases to update the grid to be able to insert a new val at (x,y)
		if len(self.nodes) < x+1:
			for i in range(x+1 - len(self.nodes)): self.nodes.append([])
		if len(self.nodes[x]) < y+1:
			for i in range(y+1 - len(self.nodes[x])): self.nodes[x].append(None)
		
		self.nodes[x][y] = self.Node(nodeName, x, y)
	
	# This adds an undirected edge between first and second (but not vice versa)
	def addUndirectedEdge(self, first, second):
		if first in second.neighbors or second in first.neighbors:
			return
		first.neighbors.append(second)
		second.neighbors.append(first)
		
	
	# This removes an undirected edge between first and second (but not vice versa)
	def removeUndirectedEdge(self, first, second):
		try:
			first.neighbors.remove(second)
			second.neighbors.remove(first)
		except:
			return
	
	# This returns all the nodes in the graph
	def getAllNodes(self):
		return self.nodes