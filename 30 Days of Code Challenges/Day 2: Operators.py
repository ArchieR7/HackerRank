import sys

a = input()
b = input()
c = input()

a = float(a)
b = float(b)
c = float(c)

s = a * b / 100 + a * c / 100 + a
s = round(s)
print('The total meal cost is {s} dollars.'.format(s=s))
