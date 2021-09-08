import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = [[] for i in range(m)]

for _ in range(n):
    matrix_item = input()
    for i in range(m):
        matrix[i].append(matrix_item[i])

norstring = "" 

for cols in matrix:
    for item in cols:
        norstring+=item

#print(norstring)

#norstring = "This$#is% Matrix#  %!"
regexs = """(?<=\w)(\W+)(?=\w)"""

print(re.sub(regexs, ' ', norstring))