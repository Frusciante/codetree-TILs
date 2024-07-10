n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

import sys
min_dis = sys.maxsize
for i in range(n - 1):
    for j in range(i + 1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        dis = (x1 - x2)**2 + (y1 - y2)**2
        min_dis = min(dis, min_dis)

print(min_dis)