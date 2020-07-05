#why does this doesnt work?
def productSum(array):
	sum = 0
	depth = 1
	for i in range(len(array)):
		if type(array[i]) is int:
			sum += array[i]
		else:
			sum+=productSum(array[i])
			depth+=1
	return sum*depth
#this works
def productSum(array, depth=1):
	sum = 0
	for i in range(len(array)):
		if type(array[i]) is int:
			sum += array[i]
		else:
			sum+=productSum(array[i],depth+1)
	return sum*depth