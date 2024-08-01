xy = tuple(map(int, input().split()))
ab = tuple(map(int, input().split()))

def check_overlap(xy, ab):
    x1, y1, x2, y2 = xy
    a1, b1, a2, b2 = ab
    if (min(x1, x2) > max(a1, a2) or min(y1, y2) > max(b1, b2)):
        return False
    return True

if check_overlap(xy, ab) and check_overlap(ab, xy):
    print('overlapping')
else:
    print('nonoverlapping')