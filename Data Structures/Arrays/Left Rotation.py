import sys

(N, D) = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

for i in range(0,D):
	temp = nums[0]
	nums.pop(0)
	nums.append(temp)

print(' '.join(str(n) for n in nums))