n, m = tuple(map(int, input().split()))
nums = tuple(map(int, input().split()))

maximum = 0
for i in range(n):
    ans = 0
    idx = nums[i]
    for _ in range(m):
        temp = nums[idx - 1]
        idx = temp
        ans += temp
    maximum = max(maximum, ans)

print(maximum)