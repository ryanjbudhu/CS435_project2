# Function to create a node name given a number:
# 1=A, 26=Z, 27=AA, 703=AAA
def createLabel(num):
	powr,mod = divmod(num, 26)
	if mod:
		out = chr(64 + mod)
	else:
		powr -= 1
		out = 'Z'
	if powr:
		return createLabel(powr) + out
	return out