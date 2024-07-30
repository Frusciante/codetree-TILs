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
    
    # 합의 상한 정했고, 넘으면 섹션 추가했으므로 섹션 수는 m보다 작을 수 있음.
    # 나눌 수 있는 부분 아무렇게나 나누면 됨.
    if possible and m >= sec:
        print(i)
        break