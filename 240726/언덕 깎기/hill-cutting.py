n = int(input())
arr = [int(input()) for _ in range(n)]

def update(arr):
    maxval = max(arr)
    minval = min(arr)
    maxidx = arr.index(maxval)
    minidx = arr.index(minval)
    return maxval, minval, maxidx, minidx

maxval, minval, maxidx, minidx = update(arr)
add_cnt = 0
minus_cnt = 0
while maxval - minval > 17:
    arr[minidx] += 1
    add_cnt += 1
    if maxval - minval <= 17:
        break
    arr[maxidx] -= 1
    minus_cnt += 1
    maxval, minval, maxidx, minidx = update(arr)

print(minus_cnt ** 2 + add_cnt ** 2)