import sys
n = int(input())

arr = [tuple(map(int, input().split())) for _ in range(n)]

min_w = sys.maxsize
for i in range(n):
    min_x = sys.maxsize
    max_x = -sys.maxsize
    min_y = sys.maxsize
    max_y = -sys.maxsize
    for j in range(n):
        if j == i:
            continue
        x, y = arr[j]
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        min_y = min(y, min_y)
        max_y = max(y, max_y)
    min_w = min(min_w, (max_x - min_x) * (max_y - min_y))

print(min_w)