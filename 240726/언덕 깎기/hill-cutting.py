n = int(input())
arr = [int(input()) for _ in range(n)]
cnt_arr = [0] * n

def update(arr):
    maxval = max(arr)
    minval = min(arr)
    maxidx = arr.index(maxval)
    minidx = arr.index(minval)
    return maxval, minval, maxidx, minidx

maxval, minval, maxidx, minidx = update(arr)
while maxval - minval > 17:
    arr[minidx] += 1
    cnt_arr[minidx] += 1
    if maxval - minval <= 17:
        break
    arr[maxidx] -= 1
    cnt_arr[minidx] += 1

    maxval, minval, maxidx, minidx = update(arr)

print(maxval, minval, maxidx, minidx, arr)
print(cnt_arr)