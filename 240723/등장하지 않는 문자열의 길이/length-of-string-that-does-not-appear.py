n = int(input())
s = input()
check = [0] * (n + 1)

m = 100
# 문자열 길이 i
reapeted = False
for i in range(1, n + 1):
    for j in range(n - i + 1):
        comp = s[j:j+i]
        cnt = 0
        for k in range(n - i + 1):
            if s[k:k+i] == comp:
                cnt += 1
            if cnt > 1:
                reapeted = True
                cnt = 0
                break
    if not reapeted:
        m = i
        break
    reapeted = False

print(m)