'''
PROBLEM 1: Simple Array Sum:
---------------------------

Given an array of N integers, can you find the sum of its elements?

INPUT FORMAT:
------------
The first line contains an integer, N, denoting the size of the array. 

The second line contains N space-separated integers representing the array's
elements.

OUTPUT FORMAT:
-------------
    Print the sum of the array's elements as a single integer.

SAMPLE INPUT:
------------
6
1 2 3 4 10 11

SAMPLE OUTPUT:
-------------
31

EXPLANATION:
-----------
We print the sum of the array's elements, which is: 1 + 2 + 3 + 4 + 10 + 11 = 31
'''

import sys

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
print sum(arr)