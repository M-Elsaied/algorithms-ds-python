#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    for i in range(1,len(arr)):
        j = i
        while j >0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-=1
    # print(arr)
    min_dif = float('inf')
    min_list = []
    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i]
        if diff < min_dif:
            min_dif = diff
    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i]
        if diff == min_dif:
            min_list.append(arr[i])
            min_list.append(arr[i+1])
    # print(arr)
    # print(min_list)
    return min_list



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
