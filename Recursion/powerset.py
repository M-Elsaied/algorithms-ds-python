#iterative
def powerset(array):
    finalArray = []
    finalArray.append([])
    for i in range(len(array)):
        for j in range(len(finalArray)):
            finalArray.append(finalArray[j]+ [array[i]])
    return finalArray

#recursion
def powerset(array, idx=None):
    if idx is None:
        idx = len(array)-1
    if idx < 0:
        return [[]]
    element = array[idx]
    subsets = powerset(array, idx-1)
    for i in range(len(subsets)):
        current = subsets[i]
        subsets.append(current+[element])
    return subsets