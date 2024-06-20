s = input()
le = len(s)
ans = 0
for i in range(le - 1):
    if s[i] == '(':
        for j in range(i + 1, le):
            if s[j] == ')':
                ans += 1
print(ans)