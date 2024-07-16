t = int(input())
arr = list(map(int, input().split()))
biggest = max(arr)

cnt = 0
for i in range(t - 1):
    for j in range(i + 1, t):
        for k in range(2, biggest):
            if ((arr[i] + arr[j])) / 2 == k:
                cnt += 1

print(cnt)