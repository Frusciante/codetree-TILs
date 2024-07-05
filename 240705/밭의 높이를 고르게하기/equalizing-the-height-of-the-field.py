n, h, t = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

import sys
min_cnt = sys.maxsize
for i in range(n - t + 1):
    cnt = 0
    for j in range(i, i + t):
        cnt += abs(arr[j] - h)
    min_cnt = min(cnt, min_cnt)

print(min_cnt)