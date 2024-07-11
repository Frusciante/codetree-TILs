import copy
n = int(input())

arr = [tuple(map(int, input().split())) for _ in range(n)]

end = max(arr, key = lambda x: x[1])[1]

line = [0] * (end + 1)
for item in arr:
    a, b = item
    for i in range(a, b + 1):
        line[i] += 1

cnt = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            copied_line = copy.deepcopy(line)
            for l in range(arr[i][0], arr[i][1] + 1):
                copied_line[l] -= 1
            for l in range(arr[j][0], arr[j][1] + 1):
                copied_line[l] -= 1
            for l in range(arr[k][0], arr[k][1] + 1):
                copied_line[l] -= 1
            if max(copied_line) <= 1:
                cnt += 1

print(cnt)