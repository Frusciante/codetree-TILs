n = int(input())
nums = list(map(int, input().split()))

noc = n ** 3

ans = 1
for item in nums:
    cnt = 0
    for j in range(1, n + 1):
        if abs(j - item) >= 3:
            cnt += 1
    ans *= cnt

print(noc - ans)