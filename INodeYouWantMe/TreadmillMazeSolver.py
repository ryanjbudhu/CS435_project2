class TreadmillMazeSolver:
	def __init__(self):
		pass
	
	def dijkstras(self, start):
		shortest = {start:0}
		for i in start.neighbors:
			shortest[i] = start.neighbors[i]
		old = shortest.copy()
		notvisited = [i for i in shortest]
		notvisited.remove(start)
		while notvisited:
			cur = min(notvisited,key=lambda x:shortest[x])
			notvisited.remove(cur)
			for i in cur.neighbors:
				suggested = shortest[cur] + cur.neighbors[i]
				if shortest[i] > suggested:
					shortest[i] = suggested
		
		return shortest,old