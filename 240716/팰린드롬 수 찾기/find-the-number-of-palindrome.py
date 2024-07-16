x, y = tuple(map(int, input().split()))

cnt = 0
for i in range(x, y + 1):
    i = str(i)
    if i == i[::-1]:
        cnt += 1

print(cnt)