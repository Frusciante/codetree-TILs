import sys
n = int(input())
seats = list(map(int, input()))

maximum = 0
for i in range(n):
    if seats[i] == 1:
        continue
    closest = n
    for j in range(n):
        dis = 0
        if i == j or seats[j] == 1:
            for k in range(j + 1, n):
                if seats[k] == 1 or k == i:
                    dis = k - j
                    closest = min(closest, dis)
                    break
    maximum = max(closest, maximum)
print(maximum)