n, k = tuple(map(int, input().split()))

bombs = [int(input()) for i in range(n)]

biggest = -1
for i in range(n):
    for j in range(i - k, i + k + 1):
        if j < 0 or j >= n or j == i:
            continue
        if bombs[i] == bombs[j]:
            biggest = max(biggest, bombs[i])

print(biggest)