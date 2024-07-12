n, c, g, h = tuple(map(int, input().split()))

arr = []
maximum = 0
minimum = 1000
for i in range(n):
    t1, t2 = tuple(map(int, input().split()))
    maximum = max(t2, maximum)
    minimum = min(t1, minimum)
    arr.append((t1, t2))

best = 0
for i in range(minimum, maximum + 1):
    amount = 0
    for (t1, t2) in arr:
        if i < t1:
            amount += c
        elif i > t2:
            amount += h
        else:
            amount += g
    best = max(best, amount)

print(best)