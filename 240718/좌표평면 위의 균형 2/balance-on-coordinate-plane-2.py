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

minx = minx - 1 if minx % 2 == 1 else minx
maxx = maxx + 1 if maxx % 2 == 1 else maxx
miny = miny - 1 if miny % 2 == 1 else miny
maxy = maxy + 1 if maxy % 2 == 1 else maxy

minm = n
for i in range(minx, maxx + 1, 2):
    for j in range(miny, maxy + 1, 2):
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

        for k in range(4):
            cnts[k] = 0

print(minm)