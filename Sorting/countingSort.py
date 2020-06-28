def countingSort(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    countArray = [0] * (max+1)
    for num in arr:
        countArray[num] += 1
    i = 0
    # print(countArray)
    for count in range(len(countArray)):
        for idx in range(countArray[count]):
            arr[i] = count
            i+=1
    return arr
def countSortString(strr):
    countArray = [0] * 26
    for chr in strr:
        idx = ord(chr) - ord('a')
        countArray[idx] = countArray[idx]+1
    # print(countArray)
    i = 0
    for count in range(len(countArray)):
        for idx in range(countArray[count]):
            c = chr(ord('a') + count)
            strr[i] = c
            i+=1            

arr=[8,5,2,9,6]
strr='cba'
if __name__ == "__main__":
    
    countingSort(arr)
    print(arr)
    countSortString(strr)
    print(strr)