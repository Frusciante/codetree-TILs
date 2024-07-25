import sys

n, k = tuple(map(int, input().split()))
nums = [int(input()) for _ in range(n)]
nums.sort()

max_cnt = 0
for i in range(n):
    cnt = 1
    for j in range(i + 1, n):
        if nums[j] - nums[i] <= k:
            cnt += 1
        else:
            break
    max_cnt = max(max_cnt, cnt)
    
print(max_cnt)