class TreadmillMazeSolver:
	def __init__(self):
		pass
	
	def dijkstras(self, start):
		shortest = {start:0}
		for i in start.neighbors:
			shortest[i] = start.neighbors[i]
		notvisited = [i for i in shortest]
		notvisited.remove(start)
		print([i.name for i in notvisited])
		while notvisited:
			cur = min(notvisited,key=lambda x:shortest[x])
			print(cur.name)
			notvisited.remove(cur)
		
		return shortest