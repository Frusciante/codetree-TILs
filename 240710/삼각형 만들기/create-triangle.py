n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

max_w = 0
for i in range(n):
    for j in range(n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        if x1 == x2:
            for k in range(n):
                x3, y3 = points[k]
                w = abs((y1 - y2) * (x1 - x3))
                max_w = max(w, max_w)
        if y1 == y2:
            for k in range(n):
                x3, y3 = points[k]
                w = abs((x1 - x2) * (y1 - y3))
                max_w = max(w, max_w)

print(max_w)