n = int(input())
arr = [int(input()) for _ in range(n)]

import sys
min_d = sys.maxsize

for i in range(n):
    d = 0
    now = i
    cnt = 0
    for j in range(i, i + n):
        d += arr[j % n] * cnt
        cnt += 1
    min_d = min(d, min_d)

print(min_d)