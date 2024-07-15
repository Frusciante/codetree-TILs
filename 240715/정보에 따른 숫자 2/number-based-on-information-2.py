t, a, b = tuple(map(int, input().split()))
line = [0] * (b + 1)

for _ in range(t):
    c, num = tuple(input().split())
    num = int(num)
    line[num] = c

cnt = 0
for i in range(a, b + 1):
    d1 = 0
    d2 = 0
    searching = ''
    for j in range(i, a - 1, -1):
        if line[j] in ('N', 'S'):
            searching = 'S' if line[j] == 'N' else 'N'
            if line[j] == 'S':
                d1 = i - j
            else:
                d2 = i - j
            break

    for k in range(i + 1, b + 1):
        if line[k] == searching:
            if searching == 'S':
                d1 = k - i
            else:
                d2 = k - i
            break

    if d1 <= d2:
        cnt += 1

print(cnt)