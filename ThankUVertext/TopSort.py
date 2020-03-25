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
		queue = list(filter(lambda i: in_degree[i.name]==0, nodes))
		output = []
		print(in_degree)
		while queue:
			print([i.name for i in queue])
			print(in_degree)
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
			'''if path:
				print([i.name for i in path])
			else:
				print(path)'''
		return path
	
	def DFS(self, cur, path=[]):
		if cur in path:
			return path
		path.append(cur)
		for i in cur.neighbors:
			if i not in path:
				return self.DFS(i,path)