#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    altitude = 0
    newaltitude = 0
    valies = 0
    for step in range(n):
        altitude = newaltitude
        if(s[step] == 'U'):
            newaltitude+=1
        else:
            newaltitude-=1
        
        if(altitude == 0 and newaltitude<0):
            valies+=1
    
    return valies        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
