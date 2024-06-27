import sys

n = int(input())

arr = [tuple(map(int, input().split())) for _ in range(n)]
min_d = sys.maxsize

for i in range(1, n - 1):
    now = arr[0]
    path = [now]
    d = 0
    for j in range(1, n):
        if j == i:
            continue
        else:
            px, py = path[-1]
            now = arr[j]
            path.append(now)
            x, y = now
            d += abs(x - px) + abs(y - py)
    min_d = min(min_d, d)

print(min_d)