#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countInversions(arr):
    # Write your code here
    n = len(arr)
    if n == 1:
        return 0
    m1 = n // 2
    m2 = n - m1
    array1 = arr[:m1]
    array2 = arr[m1:]
    result = countInversions(array1) + countInversions(array2)
    
    i1,j = 0,0
    for i in range(n):
        if i1 < m1 and ( j >= m2 or array1[i1] <= array2[j]):
            arr[i] = array1[i1]
            result +=j
            i1 +=1
        elif j < m2:
            arr[i] = array2[j]
            j +=1
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
