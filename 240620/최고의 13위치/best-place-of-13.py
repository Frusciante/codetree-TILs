n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

mx = 0
for i in range(n):
    for j in range(n - 2):
        cnt = 0
        for k in range(j, j + 3):
            print(i, k , cnt)
            if mat[i][k] == 1:
                cnt += 1
        mx = max(mx, cnt)
print(mx)