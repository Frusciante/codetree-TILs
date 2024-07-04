n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

maximum = 0

for i in range(n - 2):
    maximum = max(maximum, sum(arr[i:i+k]))

print(maximum)