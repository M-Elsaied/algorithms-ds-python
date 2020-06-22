def quickSort(array):
    
    helper(array,0, len(array)-1)
    return array
def helper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    rightIdx =  endIdx
    leftIdx = startIdx+1
    pivotIdx = startIdx
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx+=1
        if array[rightIdx]>= array[pivotIdx]:
            rightIdx-=1
    swap(rightIdx, pivotIdx, array)
    leftSubarrayIsSmaller = rightIdx-1-startIdx > endIdx - (rightIdx+1)
    if leftSubarrayIsSmaller:
        helper(array, startIdx, rightIdx-1)
        helper(array, rightIdx+1, endIdx)
    else:
        helper(array, rightIdx+1, endIdx)
        helper(array, startIdx, rightIdx-1)
def swap(i,j, array):
    array[i], array[j] = array[j], array[i]

arr=[8,5,2,9,6]
if __name__ == "__main__":
    
    quickSort(arr)
    print(arr)