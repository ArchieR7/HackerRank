n = int(input().strip())
print(len(max(str(bin(n)).replace('0b', '').split('0'))))