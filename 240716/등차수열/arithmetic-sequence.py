t = int(input())
arr = list(map(int, input().split()))
biggest = max(arr)

max_cnt = 0
for k in range(2, biggest):
    cnt = 0
    for i in range(t - 1):
        for j in range(i + 1, t):
            if (arr[i] + arr[j]) == 2 * k:
                cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)