n, k = tuple(map(int, input().split()))

arr = [0] * 1000

max_idx = 0
for _ in range(n):
    num, idx = tuple(map(int, input().split()))
    arr[idx] = num
    max_idx = max(max_idx, idx)

maximum = 0
for i in range(k, max_idx-k+1):
    maximum = max(sum(arr[i-k:i+k+1]), maximum)

print(maximum)