s = input()

l = len(s)
cnt = 0

for i in range(l - 4):
    if s[i] == '(' and s[i + 1] == '(':
        for j in range(i + 2, l - 1):
            if s[j] == ')' and s[j + 1] == ')':
                cnt += 1

print(cnt)