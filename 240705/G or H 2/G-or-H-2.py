n = int(input())

arr = []
for _ in range(n):
    pos, alpha = input().split()
    pos = int(pos)
    arr.append((pos, alpha))
arr.sort()

max_all = 0
for i in range(n-1):
    max_part = 0
    cnt_g = 0
    cnt_h = 0
    if arr[i][1] == 'G':
        cnt_g += 1
    else:
        cnt_h += 1
    for j in range(i+1, n):
        if arr[j][1] == 'G':
            cnt_g += 1
        else:
            cnt_h += 1
        if cnt_g == cnt_h:
            max_part = arr[j][0] - arr[i][0]
    if not (cnt_g and cnt_h):
        max_part = arr[len(arr)-1][0] - arr[0][0]
    max_all = max(max_all, max_part)

print(max_all)