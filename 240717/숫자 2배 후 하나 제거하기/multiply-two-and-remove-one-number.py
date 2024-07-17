import sys

n = int(input())
nums = list(map(int, input().split()))

min_ans = sys.maxsize
for i in range(n):
    new_nums = nums[0:i]
    new_nums.extend(nums[i+1:])
    for k in range(n - 1):
        ans = 0
        new_nums[k] *= 2
        for j in range(n - 2):
            ans += abs(new_nums[j] - new_nums[j+1])
        min_ans = min(min_ans, ans)
        new_nums[k] //= 2



print(min_ans)