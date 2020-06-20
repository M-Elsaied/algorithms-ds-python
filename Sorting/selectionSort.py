def selectionSort(arr):
    currentIdx = 0
    while currentIdx < len(arr) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx, len(arr)):
            if arr[smallestIdx] > arr[i]:
                smallestIdx = i
        arr[currentIdx], arr[smallestIdx] = arr[smallestIdx], arr[currentIdx]
        currentIdx+=1
    return arr

arr=[8,5,2,9,6]
if __name__ == "__main__":
    
    selectionSort(arr)
    print(arr)