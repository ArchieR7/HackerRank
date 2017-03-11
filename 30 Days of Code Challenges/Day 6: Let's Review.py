ans = []
for _ in range(int(input())):
    s = input()
    odd = ''
    even = ''
    for i in range(0, len(s)):
        if (i + 1) % 2 == 1:
            odd += s[i]
        else :
            even += s[i]
    ans.append('{o} {e}'.format(o=odd, e=even))

for a in ans:
    print(a)
