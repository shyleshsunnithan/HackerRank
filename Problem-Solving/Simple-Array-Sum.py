#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    
    sum=0 #initialising sum since we are adding something to it

    for i in ar:
        sum+=i #adding the sum of each element one-by-one on each iteration
    
    return sum
    #return sum(ar) <- this code does all the stuff we need but we can also do as above
    

    
#don't run this locally as some of the code below are optimised or done for communicating with their stuff
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
