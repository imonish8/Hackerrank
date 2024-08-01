# https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

# Reading input
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Computing the Cartesian product
result = product(A, B)

# Printing the result
print(' '.join(map(str, result)))
