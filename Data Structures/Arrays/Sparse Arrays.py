
N = int(input())
ns = []
for i in range(0,N):
	ns.append(input())

D = int(input())
ds = []
for i in range(0,D):
	d = input()
	ds.append(sum(1 for x in ns if x == d))

for a in ds:
	print(str(a))