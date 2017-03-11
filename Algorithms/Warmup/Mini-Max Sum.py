import sys


a,b,c,d,e = input().strip().split(' ')
array = [int(a),int(b),int(c),int(d),int(e)]
ma = 0
mi = sum(array)
for i in range(0,5):
    last = array.copy()
    last.pop(i)
    s = sum(last)
    if s > ma:
        ma = s
    if s < mi:
        mi = s
print('{i} {a}'.format(i=mi, a=ma))