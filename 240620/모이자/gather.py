n = int(input())
status = list(map(int, input().split()))

import sys
d = sys.maxsize

for i in range(n):
    a = 0
    for j in range(n):
        a += abs(i - j) * status[j]
    if d > a:
        d = a

print(d)