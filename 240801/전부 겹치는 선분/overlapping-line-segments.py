n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(1, 101):
    satisfied = True
    for (x, y) in arr:
        if i < x or y < i:
            satisfied = False
            break
    if satisfied:
        print("Yes")
        break
else:
    print("No")