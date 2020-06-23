def mergeSort(array):
	if len(array) == 1:
		return array
	middleIdx = len(array) // 2
	leftHalf = array[:middleIdx]
	rightHalf = array[middleIdx:]
	return mergeSortedArrays(mergeSort(leftHalf),mergeSort(rightHalf))
def mergeSortedArrays(leftHalf, rightHalf):
	sortedArray = [None] * (len(leftHalf) + len(rightHalf))
	k = i = j = 0 #k for sorted, i for left, j for right
	while i < len(leftHalf) and j < len(rightHalf):
		if leftHalf[i] <= rightHalf[j]:
			sortedArray[k] = leftHalf[i]
			i+=1
		else:
			sortedArray[k] = rightHalf[j]
			j+=1		
		k+=1
	while i < len(leftHalf):
		sortedArray[k] = leftHalf[i]
		i+=1
		k+=1
	while j < len(rightHalf):
		sortedArray[k] = rightHalf[j]
		j+=1
		k+=1
	return sortedArray
arr=[8,5,2,9,6]
if __name__ == "__main__":
    
    mergeSort(arr)
    print(arr)