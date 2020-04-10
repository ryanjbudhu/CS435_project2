class Graph:
	class Node:
		def __init__(self, name):
			self.name = name
			self.neighbors = set()
	def __init__(self):
		self.nodes = []
	
	def addNode(self, nodeName):
		self.nodes.append(self.Node(nodeName))
	
	#This adds an undirected edge between first and second (and vice versa)
	def addUndirectedEdge(self, first, second):
		first.neighbors.add(second)
		second.neighbors.add(first)
	
	#This removes an undirected edge between first and second (and vice versa)
	def removeUndirectedEdge(self, first, second):
		first.neighbors.discard(second)
		second.neighbors.discard(first)
	
	#This returns all the nodes in the graph
	def getAllNodes(self):
		return self.nodes