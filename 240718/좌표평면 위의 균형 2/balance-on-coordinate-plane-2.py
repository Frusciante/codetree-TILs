import sys

n = int(input())

minx = sys.maxsize
maxx = -minx
miny = minx
maxy = maxx

points = []
for i in range(n):
    x, y = tuple(map(int, input().split()))
    minx = min(minx, x)
    miny = min(miny, y)
    maxx = max(maxx, x)
    maxy = max(maxy, y)
    points.append((x, y))

minm = n
for i in range(minx, maxx + 1):
    for j in range(miny, maxy + 1):
        cnts = [0] * 4
        for x, y in points:
            if x > i and y > j:
                cnts[0] += 1
            elif x < i and y > j:
                cnts[1] += 1
            elif x < i and y < j:
                cnts[2] += 1
            else:
                cnts[3] += 1
        
        minm = min(max(cnts), minm)

print(minm)