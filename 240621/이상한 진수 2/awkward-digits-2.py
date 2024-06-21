n = input()

if '0' not in n:
    n = n[0:len(n) - 1]
    n += '0'
else:
    n = n.replace('0', '1', 1)

n = n[::-1]

cnt = 0
for i, c in enumerate(n, 0):
    if c == '1':
        cnt += 2**i

print(cnt)