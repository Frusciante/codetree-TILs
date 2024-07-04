n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

cnt = 0
l = len(nums)
for i in range(n - l + 1):
    check = arr[i:i+l]
    for num in nums:
        if num in check:
            check.remove(num)
    if len(check) == 0:
        cnt += 1

print(cnt)