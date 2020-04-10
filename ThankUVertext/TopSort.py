class TopSort:
	def __init__(self):
		pass
	
	def Kahns(self, graph):
		nodes = graph.getAllNodes()
		in_degree = dict(((i.name,0) for i in nodes))
		for i in nodes:
			for n in i.neighbors:
				in_degree[n.name] += 1
		queue = []
		# Create a list of nodes where their in degree is 0
		queue = list(filter(lambda i: in_degree[i.name]==0, nodes))
		output = []
		while queue:
			cur = queue.pop(0)
			output.append(cur)
			for i in cur.neighbors:
				in_degree[i.name] -= 1
				if in_degree[i.name] == 0:
					queue.append(i)
		return output
	
	def mDFS(self, graph):
		for i in graph.getAllNodes():
			path = self.DFS(i)
		return path
	
	def DFS(self, cur, path=[]):
		for i in cur.neighbors:
			if i not in path:
				self.DFS(i,path)
		if cur not in path:
			path.insert(0,cur)
		return path