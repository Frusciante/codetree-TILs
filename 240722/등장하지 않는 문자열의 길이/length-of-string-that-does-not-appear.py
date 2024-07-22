n = int(input())
s = input()
check = [0] * (n + 1)

for i in range(n):
    new_s = ""
    for j in range(i, n):
        new_s += s[j]
        if s.count(new_s) == 1:
            check[len(new_s)] += 1

m = max(check)

print(check.index(m))