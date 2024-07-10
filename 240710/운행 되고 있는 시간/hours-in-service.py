n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

o_arr = [0] * 1001

for i, (a, b) in enumerate(arr):
    for j in range(a, b + 1):
        o_arr[j] += 1

max_val = 0
for i, (a, b) in enumerate(arr):
    copied = o_arr
    for j in range(a, b + 1):
        copied[j] -= 1
    cnt = 0
    for j in range(1001):
        if copied[j] is not 0:
            cnt += 1
    max_val = max(max_val, cnt)

print(max_val)