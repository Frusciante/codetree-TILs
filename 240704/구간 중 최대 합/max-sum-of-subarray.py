n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

maximum = 0

for i in range(n - 2):
    maximum = max(maximum, arr[i] + arr[i+1] + arr[i+2])

print(maximum)