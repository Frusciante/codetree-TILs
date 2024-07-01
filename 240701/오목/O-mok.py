arr = [list(map(int, input().split())) for _ in range(19)]

winner = 0
loc = [-1, -1]

for i in range(19):
    for j in range(19):
        if arr[i][j] in (1, 2):
            if j < 15:
                if arr[i][j] == arr[i][j+1] == arr[i][j+2] == arr[i][j+3] == arr[i][j+4]:
                    loc = [i, j+2]
                    winner = arr[i][j]
                    break
                if i < 15:
                    if arr[i][j] == arr[i+1][j+1] == arr[i+2][j+2] == arr[i+3][j+3] == arr[i+4][j+4]:
                        loc = [i+2, j+2]
                        winner = arr[i][j]
                        break

            if i < 15:
                if arr[i][j] == arr[i+1][j] == arr[i+2][j] == arr[i+3][j] == arr[i+4][j]:
                    loc = [i+2, j]
                    winner = arr[i][j]
                    break
                if j > 3:
                    if arr[i][j] == arr[i+1][j-1] == arr[i+2][j-2] == arr[i+3][j-3] == arr[i+4][j-4]:
                        loc = [i+2, j-2]
                        winner = arr[i][j]
                        break

print(winner)
if loc != [-1, -1]:
    print(loc[0]+1, loc[1]+1)