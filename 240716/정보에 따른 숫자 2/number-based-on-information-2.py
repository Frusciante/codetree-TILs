t, a, b = tuple(map(int, input().split()))
line = [0] * (1001)

for _ in range(t):
    c, num = tuple(input().split())
    num = int(num)
    line[num] = c
cnt = 0
for i in range(a, b + 1):
    d1 = 0
    d2 = 0
    d1_found = False
    d2_found = False
    move = 0
    while (i - move >= 0) or (i + move <= 1000):
        if i - move >= 0 and line[i - move] != 0:
            if line[i - move] == 'S':
                if not d1_found:
                    d1 = move
                    d1_found = True
            if line[i - move] == 'N':
                if not d2_found:
                    d2 = move
                    d2_found = True
        if i + move <= 1000 and line[i + move] != 0:
            if line[i + move] == 'S':
                if not d1_found:
                    d1 = move
                    d1_found = True
            if line[i + move] == 'N':
                if not d2_found:
                    d2 = move
                    d2_found = True
        if d1_found and d2_found:
            break
        move += 1
    if d1 <= d2 and d1_found and d2_found:
        cnt += 1

print(cnt)