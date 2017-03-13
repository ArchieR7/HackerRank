#!/bin/python3

import sys

n,t = input().strip().split()
n,t = [int(n), int(t)]
c = list(map(int, input().strip().split()))

bobot = 0
current = n
c.pop()
for i in c:
    if current - i >= 5:
        current -= i
    else :
        current -= i
        bobot += n - current
        current = n

print(bobot)