import numpy

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

print(numpy.inner(A, B))
print(numpy.outer(A, B))