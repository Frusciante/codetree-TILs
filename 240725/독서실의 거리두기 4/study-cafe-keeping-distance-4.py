n = int(input())
seats = list(map(int, input()))

maxmin_dis = 0
for i in range(n - 1):
    if seats[i] == 1:
        continue
    for j in range(i + 1, n):
        if seats[j] == 1:
            continue
        min_dis = n
        for k in range(n):
            if seats[k] == 1 or k in [i, j]:
                for l in range(k + 1, n):
                    if seats[l] == 1 or l in [i, j]:
                        min_dis = min(min_dis, l - k)
        maxmin_dis = max(maxmin_dis, min_dis)

print(maxmin_dis)