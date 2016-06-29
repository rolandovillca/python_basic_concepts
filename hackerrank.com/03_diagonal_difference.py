#!/bin/python

'''
PROBLEM: Diagonal Difference:
----------------------------
Given a square matrix of size N x N, calculate the absolute difference between
the sums of its diagonals.

INPUT FORMAT:
------------
The first line contains a single integer, N. The next N lines denote the
matrix's rows, with each line containing N space-separated integers describing
the columns.

OUTPUT FORMAT:
-------------
Print the absolute difference between the two sums of the matrix's diagonals as
a single integer.

SAMPLE INPUT:
------------
3
11 2   4
 4 5   6
10 8 -12

SAMPLE OUTPUT:
-------------
15

EXPLANATION:
-----------
The primary diagonal is: 
11
    5
        -12

Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:
        4
    5
10

Sum across the secondary diagonal: 4 + 5 + 10 = 19 
Difference: |4 - 19| = 15
'''

import sys

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

primary_diagonal = 0
secondary_diagonal = 0

for i, rows in enumerate(a):
    for j, row in enumerate(rows):
        if (i - j) == 0:
            primary_diagonal += row
        if (((n-1) - i) - ((n-1) - j)) == 0:
            secondary_diagonal += rows[(n-1) - i]

print abs(primary_diagonal - secondary_diagonal)