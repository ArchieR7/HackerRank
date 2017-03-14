#!/bin/python3

import sys


def findMinimum(left, right):
    return 'min({left}, {right})'.format(left=left, right=right)

n = int(input().strip())

s = 'int'

for i in range(1,n):
    s = findMinimum('int', s)
    
print(s)

