import sys

t, a, b = tuple(map(int, input().split()))
line = [0] * (1001)

data = []
for _ in range(t):
    c, num = tuple(input().split())
    num = int(num)
    data.append((c, num))

cnt = 0
for i in range(a, b + 1):
    d1 = sys.maxsize
    d2 = sys.maxsize
    for item in data:
        c, num = item
        if c == 'S':
            d1 = min(d1, abs(i - num))
        else:
            d2 = min(d2, abs(i - num))
    if d1 <= d2:
        cnt += 1
print(cnt)