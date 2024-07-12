x, y = tuple(map(int, input().split()))

maximum = 0
for i in range(x, y + 1):
    sum_x = sum(tuple(map(int, str(i))))
    maximum = max(maximum, sum_x)

print(maximum)