import sys

n = int(input().strip())
for i in range(1,11):
        print('{n} x {i} = {a}'.format(n=n, i=i, a=n * i))
