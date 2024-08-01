a1, a2 = tuple(map(int, input().split()))
b1, b2 = tuple(map(int, input().split()))
start = min(a1, b1)
end = max(a2, b2)
areas = [0] * (end + 1)

for i in range(start, end):
    if (a1 <= i and i < a2) or (b1 <= i and i < b2):
        areas[i] = 1

print(sum(areas))