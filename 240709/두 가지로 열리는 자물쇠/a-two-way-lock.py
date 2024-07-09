n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1 = [item - 1 for item in arr1] 
arr2 = [item - 1 for item in arr2]

bitmap = [list(0 for _ in range(n)) for _ in range(3)]

for i in range(3):
    bitmap[i][arr1[i]] += 1
    bitmap[i][arr2[i]] += 2
    for j in range(1, 3):
        a = (arr1[i] + j) % n
        bitmap[i][a] += 1
    for j in range(1, 3):
        a = (arr1[i] - j + n) % n
        bitmap[i][a] += 1
    for j in range(1, 3):
        a = (arr2[i] + j) % n
        bitmap[i][a] += 2
    for j in range(1, 3):
        a = (arr2[i] - j + n) % n
        bitmap[i][a] += 2

cnt = 0
for i in range(n):
    if bitmap[0][i]:
        for j in range(n):
            if bitmap[1][j]:
                for k in range(n):
                    if bitmap[2][k]:
                        check1 = False
                        if bitmap[0][i] % 2 == bitmap[1][j] % 2 == bitmap[2][k] % 2 == 1:
                            cnt += 1
                            check1 = True
                        check2 = False
                        if bitmap[0][i] >= 2 and bitmap[1][j] >= 2 and bitmap[2][k] >= 2:
                            cnt += 1
                            check2 = True
                        if check1 and check2:
                            cnt -= 1


print(cnt)