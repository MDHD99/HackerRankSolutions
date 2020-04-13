#!/bin/python3

import os
import sys


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time = s.split(':')

    seconds,stamp = time[2][:len(time[2])//2],time[2][len(time[2])//2:]
    time[2] = seconds
    if (stamp == 'PM' and (int(time[0])) != 12):
        time[0] = str(int(time[0]) + 12)

    if (stamp == 'AM' and int(time[0])) == 12 :
        time[0] = '00'
        
    if (stamp == 'PM' and int(time[0])) == 12 :
        time[0] = '12'  

    separator = ':'
    time = separator.join(time)

    return(time)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
