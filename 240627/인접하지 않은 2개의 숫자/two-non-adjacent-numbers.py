n = int(input())
arr = list(map(int, input().split()))

import sys
max_val = -1


for i in range(n - 2):
    for j in range(i + 2, n):
        max_val = max(max_val, arr[i] + arr[j])
        
print(max_val)