#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    def sort(array):
        
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

    #just any sorting function can work^^
    count=0
    med = d//2
    print('med', med)
    if len(expenditure)<=d:
        return
    for i in range(len(expenditure)):
        if i >d:
            start = i-(d+1)
            end = i-1
            print(start, end)
            tmp = sort(expenditure[start:end])
            print(tmp)
            tmp_sort = tmp[med]
            print('tmp', 2*tmp_sort, expenditure[i-1])
            if 2*tmp_sort >= expenditure[i-1]:
                count+=1
                print('count', count)

    return count
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
