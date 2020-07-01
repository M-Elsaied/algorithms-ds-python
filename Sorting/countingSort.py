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
    for char in strr:
        idx = ord(char) - ord('a')
        countArray[idx] = countArray[idx]+1
    # print(countArray)
    strr_list = list(strr)
    i = 0
    for count in range(len(countArray)):
        for idx in range(countArray[count]):
            c = chr(ord('a') + count)
            strr_list[i] = c
            i+=1    
    print("".join(strr_list))
    return "".join(strr_list) 
arr=[8,5,2,9,6]
strr='cba'
if __name__ == "__main__":
    
    countingSort(arr)
    print(arr)
    x = countSortString(strr)
    print(x)