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
11 2 4
4 5 6
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