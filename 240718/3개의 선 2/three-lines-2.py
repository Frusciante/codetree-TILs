n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

all_lines = set()
for point in points:
    x, y = point
    all_lines.add((0, x))
    all_lines.add((1, y))

all_lines_list = list(all_lines)
l = len(all_lines_list)

possible = 0
bitmap = [0] * n
for i in range(l - 2):
    for j in range(i + 1, l - 1):
        for k in range(j + 1, l):
            x_or_y1, line1 = all_lines_list[i]
            x_or_y2, line2 = all_lines_list[j]
            x_or_y3, line3 = all_lines_list[k]
            for m in range(n): 
                if points[m][x_or_y1] == line1 or points[m][x_or_y2] == line2 or points[m][x_or_y3] == line3:
                    bitmap[m] = 1
            if 0 not in bitmap:
                possible = 1
                break
            for z in range(n):
                bitmap[z] = 0

print(possible)