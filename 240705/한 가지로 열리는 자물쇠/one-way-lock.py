n = int(input())
nums = list(map(int, input().split()))

noc = n ** 3

ans = 1
for item in nums:
    ans *= (n - (item + 2))

print(noc - ans)