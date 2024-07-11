k, n = tuple(map(int, input().split()))
games = [list(map(int, input().split())) for _ in range(k)]
all_noc = [[] for _ in range(k)]

for i in range(k):
    for j in range(n):
        for l in range(j + 1, n):
            all_noc[i].append((games[i][j], games[i][l]))

cnt = 0
for item in all_noc[0]:
    check = True
    for j in range(k):
        if item not in all_noc[j]:
            check = False
            break
    if check:
        cnt += 1

print(cnt)