n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(1, n + 1):
    for j in range(n - i + 1):
        if (sum(arr[j:j+i]) / i) in arr[j:j+i]:
            cnt += 1

print(cnt)