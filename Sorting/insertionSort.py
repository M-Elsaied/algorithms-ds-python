def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-=1
    return arr
arr=[8,5,2,9,6]
if __name__ == "__main__":
    
    insertionSort(arr)
    print(arr)