import sys
n = int(input())
arr = [tuple(map(int, input().split()))]

for i in range(n):
    mini = sys.maxsize
    maxi = -sys.maxsize

    for j, (x1, x2) in enumerate(arr):
        if i == j:
            continue
        mini = min(x1, mini)
        maxi = max(x2, maxi)

    if mini >= maxi:
        print('Yes')
        break
else:
    print('No')