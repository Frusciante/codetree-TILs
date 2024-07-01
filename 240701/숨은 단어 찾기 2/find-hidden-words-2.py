n, m = tuple(map(int, input().split()))

arr = [input() for _ in range(n)]

cnt = 0
dys = [0, 1, 1, 1, 0, -1, -1, -1]
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
d = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            while d != 8:
                x = i
                y = j
                nx = x + dxs[d] * 2
                ny = y + dys[d] * 2
                if (nx < n and ny < m and nx >= 0 and ny >= 0):
                    x += dxs[d] * 2
                    y += dys[d] * 2
                    if arr[x][y] == arr[x-dxs[d]][y-dys[d]] == 'E':
                        cnt += 1
                d += 1
            d = 0


print(cnt)