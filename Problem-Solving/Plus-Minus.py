#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    #initialising the variables to store total and individual total
    tot = len(arr)
    pos = 0
    nos = 0
    zos = 0

    for num in arr:
        #looping through the array
        if(num > 0): #checks if number is positive
            pos +=1
        elif(num < 0): #checks if number is positive
            nos +=1
        else: #if both codition does not satisfy it is zero then
            zos +=1

    #printing  the proportions       
    print(pos/tot)
    print(nos/tot)
    print(zos/tot)
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
