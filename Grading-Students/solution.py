    #!/bin/python3

import math
import os
import random
import re
import sys

    #
    #
    # The function is expected to return an INTEGER_ARRAY.
    # The function accepts INTEGER_ARRAY grades as parameter.
    #

def gradingStudents(grades):
    length = len(grades)
    rgrades = []
    for grade in range(0,length):
        if(grades[grade]>=38):
            nearestFive = 5*round(grades[grade]/5)
            if((nearestFive-grades[grade]<3) and (nearestFive-grades[grade]>=0)):
                rgrades.append(nearestFive)
            else:
                rgrades.append(grades[grade])

        else:
            rgrades.append(grades[grade])



    return rgrades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
