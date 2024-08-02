n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mov = [a1 - b1 for a1, b1 in zip(a,b)]

cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if mov[i] * mov[j] < 0:
            if abs(mov[i]) >= abs(mov[j]):
                cnt += abs(mov[j] * (j - i))
                mov[i] += mov[j]
                mov[j] = 0
            else:
                cnt += abs(mov[i] * (j - i))
                mov[j] += mov[i]
                mov[i] = 0

print(cnt)