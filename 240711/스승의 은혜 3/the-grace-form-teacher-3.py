n, b = tuple(map(int, input().split()))
arr = [tuple(map(int, input().split())) for _ in range(n)]

arr.sort(key = lambda x: (x[0] + x[1], x[0]))

cnt = 0
ans = 0
for (price, shipping) in arr:
    if ans + price + shipping <= b:
        ans += price + shipping
        cnt += 1
    elif ans + (price // 2) + shipping <= b:
        ans += (price // 2) + shipping
        cnt += 1
    else:
        break
print(cnt)