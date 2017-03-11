import sys


n = int(input().strip())
a = []
s = 0
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
for i in range(len(a)):
    s += a[i][i] - a[i][len(a) - i - 1]
print(abs(s))