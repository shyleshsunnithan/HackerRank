#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    arr = []
    ares = 0 #to store Alice's points 
    bres = 0 #to store Bob's points
    
    for i in range(3): #running through the triplet
        #loop checks each condition and add points as per the condition

        if(a[i]>b[i]):
            ares +=1
        
        elif(a[i] < b[i]):
            bres +=1

        #we didn't added the equality condition since we don't add points 

    arr.append(ares) #appending the point of alice
    arr.append(bres) #appending the point of bob

    return arr #returning the resultant array



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
