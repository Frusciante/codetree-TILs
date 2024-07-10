n, b = tuple(map(int, input().split()))
arr = [int(input()) for _ in range(n)]

arr.sort()

cnt = 0
ans = 0
for i in range(n):
    if ans + arr[i] <= b:
        ans += arr[i]
        cnt += 1
    elif ans + (arr[i] // 2) <= b:
        ans += arr[i] // 2
        cnt += 1
        break
    else:
        break
print(cnt)