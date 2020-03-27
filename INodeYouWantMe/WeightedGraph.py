class WeightedGraph:
	class Node:
		def __init__(self, name):
			self.name = name
			self.neighbors = {}
	def __init__(self):
		self.nodes = []
	
	def addNode(self, nodeName):
		self.nodes.append(self.Node(nodeName))
	
	#This adds an undirected weighted edge between first and second (but not vice versa)
	def addDirectedEdge(self, first, second, weight):
		first.neighbors[second] = weight
	
	#This removes an undirected weighted edge between first and second (but not vice versa)
	def removeDirectedEdge(self, first, second):
		try:
			del first.neighbors[second]
		except:
			return
	
	#This returns all the nodes in the graph
	def getAllNodes(self):
		return self.nodes