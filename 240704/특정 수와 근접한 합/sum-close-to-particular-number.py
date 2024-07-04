n, s = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

import sys

minimum = sys.maxsize

for i in range(n - 1):
    for j in range(i + 1, n):
        minimum = min(abs(s - (sum(arr) - (arr[i] + arr[j]))), minimum)

print(minimum)