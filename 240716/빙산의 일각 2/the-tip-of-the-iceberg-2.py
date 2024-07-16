n = int(input())
icebergs = [int(input()) for _ in range(n)]
icebergs.append(0)
biggest = max(icebergs)

max_cnt = 0
for i in range(biggest):
    cnt = 0
    for j in range(0, n):
        if (icebergs[j] > i and icebergs[j + 1] <= i):
            cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)