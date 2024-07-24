n, m = tuple(map(int, input().split()))
arr = []
for _ in range(m):
    nums = list(map(int, input().split()))
    nums.sort()
    arr.append(tuple(nums))

maximum = 0
for item in arr:
    maximum = max(maximum, arr.count(item))

print(maximum)