n, h, t = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort(key = lambda x: abs(h - x))

cost = 0
for i in range(t):
    cost += abs(h - arr[i])

print(cost)