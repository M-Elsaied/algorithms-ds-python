def countingSort(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    countArray = [0] * (max+1)
    for num in arr:
        countArray[num] += 1
    i = 0
    print(countArray)
    for count in range(len(countArray)):
        for idx in range(countArray[count]):
            arr[i] = count
            i+=1
    return arr
arr=[8,5,2,9,6]
if __name__ == "__main__":
    
    countingSort(arr)
    print(arr)