import sys

n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

for i in range(10000):
    sec = 1
    cnt = 0
    possible = True

    for j in range(n):
        if i < arr[j]:
            possible = False
            break
        
        if i < cnt + arr[j]:
            cnt = 0
            sec += 1

        cnt += arr[j]

    if possible and m == sec:
        print(i)
        break