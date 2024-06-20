n = int(input())
mat = [list(map(int, input().split())) for _ in range(3)]

mx = 0
for i in range(n - 2):
    cnt = 0
    for j in range(i, i + 3):
        if mat[i][j] == 1:
            cnt += 1
    mx = max(mx, cnt)
print(cnt)