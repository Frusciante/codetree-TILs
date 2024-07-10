n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

last = max(arr, key = lambda x: x[1])[1]


max_val = 0
for i in range(n):
    oper_list = [0] * (last + 1)
    for j in range(n):
        if j == i:
            continue
        a, b = arr[j]
        for k in range(a, b):
            oper_list[k] = 1
    max_val = max(max_val, oper_list.count(1))

print(max_val)