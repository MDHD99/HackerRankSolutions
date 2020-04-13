#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr1 = arr
    arr2 = arr
    max = 0
    minimax = 0

    arr1 = sorted(arr1)
    arr2 = sorted(arr2,reverse=True)


    for i in range(0, 4):
        minimax += arr1[i]
        print(arr[i])

    for i in range(0, 4):
        max += arr2[i]

    print(minimax, max)


if __name__ == '__main__':
    arr = [5 ,2 ,3, 4 ,5]

    miniMaxSum(arr)
