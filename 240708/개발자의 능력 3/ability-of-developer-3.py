arr = list(map(int, input().split()))
l = len(arr)
s = sum(arr)

import sys
min_val = sys.maxsize

for i in range(l):
    for j in range(i + 1, l):
        for k in range(j + 1, l):
            cnt1 = arr[i] + arr[j] + arr[k]
            cnt2 = s - cnt1

            min_val = min(min_val, abs(cnt1 - cnt2))

print(min_val)