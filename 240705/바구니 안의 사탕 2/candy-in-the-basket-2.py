n, k = tuple(map(int, input().split()))

arr = [0] * 101

max_idx = 0
for _ in range(n):
    num, idx = tuple(map(int, input().split()))
    arr[idx-1] = num
    max_idx = max(max_idx, idx)

maximum = 0
for i in range(k, max_idx-k):
    maximum = max(sum(arr[i-k:i+k+1]), maximum)

print(maximum)