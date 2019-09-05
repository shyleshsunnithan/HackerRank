#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    #we run a loop to print the pattern
    for i in range(1,n+1):
        print((n-i)*' ',end = '') #prints the spaces
        print(i*'#') #prints the '#' character



if __name__ == '__main__':
    n = int(input())

    staircase(n)
