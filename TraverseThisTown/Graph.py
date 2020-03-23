class Graph:
	class Node:
		def __init__(self, name):
			self.name = name
			self.neighbors = []
	def __init__(self):
		self.nodes = []
	
	def addNode(self, nodeName):
		self.nodes.append(self.Node(nodeName))
	
	#This adds an undirected edge between first and second (and vice versa)
	def addUndirectedEdge(self, first, second):
		if first in second.neighbors or second in first.neighbors:
			return
		first.neighbors.append(second)
		second.neighbors.append(first)
	
	#This removes an undirected edge between first and second (and vice versa)
	def removeUndirectedEdge(self, first, second):
		try:
			first.neighbors.remove(second.name)
			second.neighbors.remove(first.name)
		except:
			return
	
	#This returns all the nodes in the graph
	def getAllNodes(self):
		return self.nodes