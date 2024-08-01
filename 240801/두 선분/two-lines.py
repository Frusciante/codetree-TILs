x1, x2, x3, x4 = tuple(map(int, input().split()))

if (x3 < x1 and x1 < x4) or (x3 < x2 and x2 < x4):
    print('intersecting')
else:
    print('nonintersecting')