a1, a2 = tuple(map(int, input().split()))
b1, b2 = tuple(map(int, input().split()))

if a2 < b1 or b2 < a1:
    print((a2 - a1) + (b2 - b1))
else:
    print(max(a2, b2) - min(a1, b1))