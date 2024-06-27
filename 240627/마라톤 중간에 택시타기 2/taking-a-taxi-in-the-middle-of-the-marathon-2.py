n = int(input())

arr = [tuple(map(int, input().split())) for _ in range(n)]
now = arr[0]
path = [now]
max_d = 0

for i in range(1, n - 1):
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
    max_d = max(max_d, d)

print(max_d)