import math
import os
import random
import re
import sys

def minimumSwaps(arr):
    swap=0
    visited=[False]*len(arr)
    for i in range(len(arr)):
        if visited[i]==False:
            a=i
            b=arr[i]-1
            l=1
            visited[i]=True
            while b!=i:
                visited[b]=True
                a=b
                b=arr[b]-1
                l+=1
            swap+=l-1
    return swap           
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
