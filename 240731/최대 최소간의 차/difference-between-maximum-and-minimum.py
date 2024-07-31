n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
cost = [0] * n
maxnum = max(arr)
minnum = min(arr)

while maxnum - minnum > k:
    min_changed = False
    max_changed = False
    for i in range(n):
        if arr[i] + cost[i] == minnum:
            cost[i] += 1
            min_changed = True
        elif arr[i] - cost[i] == maxnum:
            cost[i] += 1
            max_changed = True
    if max_changed:
        maxnum -= 1
    if min_changed:
        minnum += 1

print(sum(cost))