#!/bin/python

'''
PROBLEM 4: Plus Minus:
---------------------
Given an array of integers, calculate which fraction of its elements are
positive, which fraction of its elements are negative, and which fraction of its
elements are zeroes, respectively. Print the decimal value of each fraction on a
new line.

Note: This challenge introduces precision problems. The test cases are scaled to
six decimal places, though answers with absolute error of up to 10^-4 are
acceptable.

INPUT FORMAT:
------------
The first line contains an integer, N, denoting the size of the array. 
The second line contains N space-separated integers describing an array of
numbers (a0, a1, a2, ... an-1).

OUTPUT FORMAT:
-------------
You must print the following 3 lines:

1. A decimal representing of the fraction of positive numbers in the array.
2. A decimal representing of the fraction of negative numbers in the array.
3. A decimal representing of the fraction of zeroes in the array.

SAMPLE INPUT:
------------
6
-4 3 -9 0 4 1         

SAMPLE OUTPUT:
-------------
0.500000
0.333333
0.166667

EXPLANATION:
-----------
There are 3 positive numbers, 2 negative numbers, and 1 zero in the array. 
The respective fractions of positive numbers, negative numbers and zeroes are
3/6 = 0.500000, 2/6 = 0.333333 and 1/6 = 0.166667, respectively.
'''

from __future__ import division
import sys

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

count_positive_nums = 0
count_negative_nums = 0
count_zero_nums = 0

for i in arr:
    if i > 0:
        count_positive_nums += 1
    elif i < 0:
        count_negative_nums += 1
    else:
        count_zero_nums += 1

print count_positive_nums/n
print count_negative_nums/n
print count_zero_nums/n