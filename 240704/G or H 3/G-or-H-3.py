n, k = tuple(map(int, input().split()))
arr = []
for _ in range(n):
    num, ch = input().split()
    num = int(num)
    arr.append((num, ch))
arr.sort()

def get_score(c):
    if c == 'G':
        return 1
    return 2

maximum = 0
for i in range(n):
    cnt = 0
    num, ch = arr[i]
    cnt += get_score(ch)

    for j in range(i+1, n):
        next_num, next_ch = arr[j]
        if next_num - num > k:
            break
        cnt += get_score(next_ch)

    maximum = max(cnt, maximum)

print(maximum)