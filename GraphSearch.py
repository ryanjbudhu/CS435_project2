from Graph import Graph

class GraphSearch:
	def __init__(self):
		pass
	
	def DFSRec(self,start, end):
		if start == end:
			return [end]
		path = self.DFSRecHelper(start, end)
		return path
		
	def DFSRecHelper(self,cur, end, path=[]):
		path.append(cur)
		if cur == end:
			return path
		for i in cur.neighbors:
			if i not in path:
				return self.DFSRecHelper(i,end,path)
	
	def DFSIter(self, start, end):
		stack = [start]
		visited = [start.name]
		while stack:
			cur = stack.pop()
			for j in cur.neighbors:
				if j.name not in visited:
					visited.append(j.name)
					stack.append(j)
				if j == end:
					return [start] + stack
		return None
		
	def BFTRec(self, g):
		path = []
		for i in g.getAllNodes():
			if i not in path:
				path = self.BFTRecHelper(i, path)
		return path
		
	def BFTRecHelper(self, cur, path):
		for i in cur.neighbors:
			if i not in path:
				path.append(i)
				path = self.BFTRecHelper(i, path)
		return path
	
	def BFTIter(self, g):
		queue = []
		visited = []
		for i in g.getAllNodes():
			if i not in visited:
				visited.append(i)
				queue.append(i)
			while queue:
				cur = queue.pop(0)
				for j in cur.neighbors:
					if j not in visited:
						queue.append(j)
						visited.append(j)
		return visited