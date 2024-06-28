n = int(input())
s = input()

cnt = 0
for i in range(n - 2):
    if s[i] == 'C':
        for j in range(i + 1, n - 1):
            if s[j] == 'O':
                for k in range(j + 1, n):
                    if s[k] == 'W':
                        cnt += 1

print(cnt)