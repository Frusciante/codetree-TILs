x1, x2, x3, x4 = tuple(map(int, input().split()))

if (x3 <= x1 and x1 <= x4) or (x3 <= x2 and x2 <= x4) or (x1 <= x3 and x3 <= x2) or (x1 <= x4 and x4 <= x2):
    print('intersecting')
else:
    print('nonintersecting')