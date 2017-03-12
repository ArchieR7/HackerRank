import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

# 橫的執行 4 次、直的執行 4 次
max = -9 * 7
for i in range(0,4):
	for j in range(0,4):
		s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
		if s > max:
			max = s

print(max)