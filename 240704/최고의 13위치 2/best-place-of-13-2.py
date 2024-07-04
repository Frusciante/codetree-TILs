n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


maximum = 0
for i in range(n):
    for j in range(n - 2):
        for k in range(i, n):
            cnt1 = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            if i == k:
                for l in range(j + 3, n - 2):
                    cnt2 = arr[k][l] + arr[k][l+1] + arr[k][l+2]
                    maximum = max(cnt1 + cnt2, maximum)
            else:
                for l in range(n - 2):
                    cnt2 = arr[k][l] + arr[k][l+1] + arr[k][l+2]
                    maximum = max(cnt1 + cnt2, maximum)

print(maximum)