class DirectedGraph:
	class Node:
		def __init__(self, name):
			self.name = name
			self.neighbors = []
	def __init__(self):
		self.nodes = []
	
	def addNode(self, nodeName):
		self.nodes.append(self.Node(nodeName))
	
	#This adds an undirected edge between first and second (but not vice versa)
	def addDirectedEdge(self, first, second):
		if first in second.neighbors:
			return
		first.neighbors.append(second)
	
	#This removes an undirected edge between first and second (but not vice versa)
	def removeDirectedEdge(self, first, second):
		try:
			first.neighbors.remove(second.name)
		except:
			return
	
	#This returns all the nodes in the graph
	def getAllNodes(self):
		return self.nodes