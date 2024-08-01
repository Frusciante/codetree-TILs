import sys
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    min_x2 = sys.maxsize
    max_x1 = -sys.maxsize
    overlapped = True
    for j, (x1, x2) in enumerate(arr):
        if i == j:
            continue
        max_x1 = max(x1, max_x1)
        min_x2 = min(x2, min_x2)
    if max_x1 > min_x2:
        overlapped = False
    if overlapped:
        print('Yes')
        break
else:
    print('No')