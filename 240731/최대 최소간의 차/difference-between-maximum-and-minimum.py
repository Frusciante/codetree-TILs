n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
cost = [0] * n
maxnum = max(arr)
minnum = min(arr)

while maxnum - minnum > k:
    min_changed = False
    max_changed = False

    min_cnt = 0
    for i in range(n):
        if arr[i] + cost[i] == minnum:
            min_cnt += 1

    max_cnt = 0
    for i in range(n):
        if arr[i] - cost[i] == maxnum:
            max_cnt += 1

    for i in range(n):
        if arr[i] + cost[i] == minnum and min_cnt < max_cnt:
            cost[i] += 1
            min_changed = True
        elif arr[i] - cost[i] == maxnum and min_cnt >= max_cnt:
            cost[i] += 1
            max_changed = True
    if max_changed:
        maxnum -= 1
    elif min_changed:
        minnum += 1

print(sum(cost))